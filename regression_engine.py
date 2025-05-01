import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, accuracy_score


def run_linear_regression(data, target_col, cat_cols, num_cols):
    # Drop rows with missing data
    data = data.dropna(subset=[target_col] + cat_cols + num_cols)

    # One-hot encode categorical variables
    data_encoded = pd.get_dummies(data[cat_cols], drop_first=True)

    # Combine numerical and encoded categorical features
    X = pd.concat([data[num_cols], data_encoded], axis=1)
    y = data[target_col]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    # Create output summary
    coef_summary = "\n".join([f"{col}: {coef:.4f}" for col, coef in zip(X.columns, model.coef_)])
    output = (
        f"Linear Regression\n"
        f"Intercept: {model.intercept_:.4f}\n"
        f"R² Score: {r2:.4f}\n\n"
        f"Coefficients:\n{coef_summary}"
    )
    return output, y_test.tolist(), y_pred.tolist()


def run_logistic_regression(data, target_col, cat_cols, num_cols):
    # Drop rows with missing data
    data = data.dropna(subset=[target_col] + cat_cols + num_cols)

    # Encode target variable
    le = LabelEncoder()
    y = le.fit_transform(data[target_col])

    # One-hot encode categorical variables
    data_encoded = pd.get_dummies(data[cat_cols], drop_first=True)

    # Combine numerical and encoded categorical features
    X = pd.concat([data[num_cols], data_encoded], axis=1)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Create output summary
    coef_summary = "\n".join([f"{col}: {coef:.4f}" for col, coef in zip(X.columns, model.coef_[0])])
    output = (
        f"Logistic Regression\n"
        f"Intercept: {model.intercept_[0]:.4f}\n"
        f"Accuracy: {acc:.4f}\n\n"
        f"Coefficients:\n{coef_summary}"
    )
    return output, y_test.tolist(), y_pred.tolist()