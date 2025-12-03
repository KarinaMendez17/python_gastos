# 🧾 **Daily Expense Tracker**

A simple and organized command-line application for managing daily expenses.  
Track your spending, filter by category/date, and generate useful reports.  
Yeah, basically a glorified spreadsheet but with Python and less suffering.  

---

## ✨ Features

### 🔸 **1. Register Expenses**
- Add expenses with:
  - Category (predefined or custom)
  - Amount
  - Optional description
  - Automatic date (`YYYY-MM-DD`)
- Input validation to avoid user-induced disasters
- Prevents duplicate predefined categories

---

### 🔸 **2. List Expenses**
- 📋 View **all** expenses  
- 🔍 Filter by:
  - **Category**
  - **Date range** (YYYY-MM-DD → YYYY-MM-DD)

---

### 🔸 **3. Reports**
Generate totals for:

- 🗓️ **Daily** expenses  
- 📅 **Weekly** expenses (Monday → Sunday)  
- 📆 **Monthly** expenses (YYYY-MM)

---

### 🔸 **4. JSON Storage**

Data is saved in:
- data/gastos.json


Automatically created if missing.  
Stored cleanly, without your greasy human fingerprint interfering.

---

## 📂 Project Structure

```
python_gastos/
│
├── data/
│   └── gastos.json
│
├── modules/
│   ├── registrar.py
│   ├── listar.py
│   ├── total.py
│   ├── reporte.py
│
├── services/
│   ├── sRegistrar.py
│   ├── sListar.py
│   ├── sTotal.py
│   ├── sReporte.py
│   └── utilities.py
│
└── main.py
```
---


## 🚀 How to Run

1. Clone the repository:

```bash
git clone <https://github.com/KarinaMendez17/python_gastos.git>
```
2. Enter the project folder:
```
cd python_gastos
```
3. Run the application:
```
python main.py
```

## 🛠️ Requirements

Python 3.10+

No external libraries required
(standard library only: json, datetime, os, time, etc.)

---

## 🧠 Notes

All expense data persists inside a JSON file.

Handles invalid input without exploding.

Modular structure for easy maintenance and extensions.

---

## 🌐 Developer

💀 Karina Méndez