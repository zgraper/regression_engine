# **Linear & Logistic Regression GUI Tool**

This is a Python application with a graphical user interface (GUI) built using `tkinter`. It allows users to run linear or logistic regression models on data from `.csv` or `.xlsx` files. Users can interactively define the roles of each column (categorical, numerical, or excluded), choose the target column, and select the type of regression model.

---

## 🚀 **Features**

* 📂 Load .csv or .xlsx data files

* 👁️ Preview your dataset directly in the GUI

* 🔧 Define column types using dropdowns (categorical, numerical, exclude)

* 🎯 Select your target variable

* 📊 Choose between Linear Regression or Logistic Regression

* 🧠 Automatically performs:

   * Missing data cleanup

   * One-hot encoding for categorical variables

   * Label encoding for categorical target in logistic regression

* 📈 Displays model intercept and coefficients in the output window

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

* `matplotlib` (optional for future visualization features)

---

## 📂 **File Structure**

```
├── main.py                 # Entry point for the GUI
├── gui.py                  # Contains all tkinter GUI code
├── regression_engine.py   # Performs linear and logistic regression
├── utils.py                # Handles file loading and helper functions
├── requirements.txt        # Dependencies list
└── README.md               # This file
```

---

## 📌 **Future Features**

* Add performance metrics like R² and accuracy

* Show predicted vs. actual plots with `matplotlib`

* Save models or predictions to file

---
**
## 🧪 **Sample Usage**

1. Run the app:

```
python main.py
```

2. Select a data file

3. Preview the data

4. Assign column types and target

5. Choose regression type

6. Click "**Run Regression**"

---

## 👤 **Author**

Created by Zane Graper — feel free to fork or contribute!