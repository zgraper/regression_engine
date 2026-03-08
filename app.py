import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from regression_engine import run_linear_regression, run_logistic_regression

st.title("Regression Engine")
st.write("Upload a CSV or Excel file, configure your columns, and run linear or logistic regression.")

# File upload
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file, engine="openpyxl")
    except Exception as e:
        st.error(f"Failed to load file: {e}")
        st.stop()

    st.subheader("Data Preview")
    st.dataframe(data.head())

    # Regression type
    regression_type = st.radio("Regression Type", ["linear", "logistic"])

    # Column role assignment
    st.subheader("Column Roles")
    st.write("Assign a role to each column:")
    column_roles = {}
    for col in data.columns:
        role = st.selectbox(
            col,
            ["exclude", "categorical", "numerical"],
            key=f"role_{col}",
        )
        column_roles[col] = role

    # Target column
    target_col = st.selectbox("Target Column", data.columns)

    # Run regression
    if st.button("Run Regression"):
        cat_cols = [
            col for col, role in column_roles.items()
            if role == "categorical" and col != target_col
        ]
        num_cols = [
            col for col, role in column_roles.items()
            if role == "numerical" and col != target_col
        ]

        try:
            if regression_type == "linear":
                result, y_true, y_pred = run_linear_regression(
                    data, target_col, cat_cols, num_cols
                )
            else:
                result, y_true, y_pred = run_logistic_regression(
                    data, target_col, cat_cols, num_cols
                )

            st.subheader("Results")
            st.text(result)

            # Actual vs. Predicted plot
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.scatter(range(len(y_true)), y_true, label="Actual", alpha=0.7)
            ax.scatter(range(len(y_pred)), y_pred, label="Predicted", alpha=0.7)
            ax.set_title("Actual vs. Predicted")
            ax.set_xlabel("Sample Index")
            ax.set_ylabel("Value")
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error running regression: {e}")
