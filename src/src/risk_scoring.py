import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_sample.csv")

# Define scoring logic
def score_row(row):
    risk_score = 0

    # pH outside normal range
    if row['ph'] < 6.5 or row['ph'] > 8.5:
        risk_score += 2
    
    # temperature above 30°C could indicate bacterial growth
    if row['temp'] > 30:
        risk_score += 1
    
    # electrical conductivity too high means high contamination
    if row['ec'] > 500:
        risk_score += 1

    return risk_score

# Apply risk scoring
df['risk_score'] = df.apply(score_row, axis=1)

# Define risk level based on score
df['risk_level'] = df['risk_score'].map({
    0: "Low",
    1: "Moderate",
    2: "High",
    3: "High",
    4: "Critical"
})

# Show results
print("✅ Risk Scoring Complete\n")
print(df[['ph', 'temp', 'ec', 'risk_score', 'risk_level']])

# Save output
df.to_csv("../data/risk_scored.csv", index=False)
print("\n📁 Results saved to: data/risk_scored.csv")
