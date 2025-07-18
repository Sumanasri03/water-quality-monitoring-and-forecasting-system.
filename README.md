# Water Quality Risk Analyzer 🚰

A Python-based project to analyze water quality data and assign risk levels based on pH, temperature, and electrical conductivity — using only Python, no deep learning.

---

##  Features
- Load and clean sensor data
- Visualize indicators
- Apply simple rule-based risk scoring
- Export results to CSV

---

##  Folder Structure

##  How to Run Locally

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run preprocessing
python src/preprocess.py

# Step 3: Run risk scoring
python src/risk_scoring.py

# Step 4: Open notebook
jupyter notebook notebooks/example.ipynb

---

##  Algorithm Description

This project uses a simple, rule-based scoring algorithm to analyze water quality data without relying on complex machine learning models. The logic is implemented in pure Python, making it efficient and easy to understand.

### 1. Data Preprocessing Algorithm (`src/preprocess.py`)
- Loads raw water quality sensor data (e.g., pH, temperature, EC).
- Cleans missing or invalid entries.
- Normalizes and prepares the data for scoring.

### 2. Rule-Based Risk Scoring Algorithm (`src/risk_scoring.py`)
This scoring logic classifies water quality into 4 levels of risk:

| Risk Level | Description                   | Score |
|------------|-------------------------------|-------|
| 0          | Safe for use (all values OK)  | 0     |
| 1          | Low risk (1 parameter off)    | 1     |
| 2          | Moderate risk (2 parameters)  | 2     |
| 3          | High risk (3 or more)         | 3     |

#### Conditions Used:
- **pH**: Should be between `6.5` and `8.5`
- **Temperature**: Should be between `5°C` and `45°C`
- **Electrical Conductivity (EC)**: Should be under `2000 µS/cm`

If any of these parameters fall outside the safe range, a risk score is assigned.

### 3. Visualization & Analysis (`notebooks/example.ipynb`)
- Uses `pandas`, `matplotlib`, and `seaborn` to:
  - Load and preview cleaned data
  - Visualize trends (e.g., line plots of pH/EC over time)
  - Highlight data points by risk score

