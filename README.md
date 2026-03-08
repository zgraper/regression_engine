# **Linear & Logistic Regression Tool**

This is a Python application with a web-based interface built using `Streamlit`. It allows users to run linear or logistic regression models on data from `.csv` or `.xlsx` files. Users can interactively define the roles of each column (categorical, numerical, or excluded), choose the target column, and select the type of regression model.

---

## 🚀 **Features**

* 📂 Upload .csv or .xlsx data files

* 👁️ Preview your dataset directly in the browser

* 🔧 Define column types using dropdowns (categorical, numerical, exclude)

* 🎯 Select your target variable

* 📊 Choose between Linear Regression or Logistic Regression

* 🧠 Automatically performs:

   * Missing data cleanup

   * One-hot encoding for categorical variables

   * Label encoding for categorical target in logistic regression

* 📈 Displays model intercept, coefficients, and performance metrics

* 📉 Plots Actual vs. Predicted values

---

## 🛠️ **Requirements**

Install dependencies with:

```
pip install -r requirements.txt
```

**Dependencies include:**

* `pandas`

* `scikit-learn`

* `openpyxl` (for Excel file support)

* `matplotlib` (for visualization)

* `streamlit` (for the web interface)

---

## 📂 **File Structure**

```
├── main.py                 # Entry point — launches the Streamlit app
├── app.py                  # Streamlit web interface
├── regression_engine.py   # Performs linear and logistic regression
├── utils.py                # Handles file loading and helper functions
├── requirements.txt        # Dependencies list
└── README.md               # This file
```

---

## 📌 **Usage**

Run the app using either:

```bash
python main.py
```

or directly with Streamlit:

```bash
streamlit run app.py
```

Then open your browser to the displayed local URL (typically http://localhost:8501).

---

## 🧪 **Sample Workflow**

1. Run the app
2. Upload a `.csv` or `.xlsx` data file
3. Preview the loaded data
4. Assign roles (categorical / numerical / exclude) to each column
5. Select your target column
6. Choose a regression type (Linear or Logistic)
7. Click **Run Regression** to see results and a plot

---

## 👤 **Author**

Created by Zane Graper — feel free to fork or contribute!

