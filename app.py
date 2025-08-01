# app.py

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns

st.title("🎓 Student Performance Prediction")

@st.cache_data
def load_data():
    return pd.read_csv("student_mat.csv")

df = load_data()

# Prepare data
df['average'] = df[['G1', 'G2', 'G3']].mean(axis=1)
df['pass'] = df['average'].apply(lambda x: 1 if x >= 10 else 0)

X = df[['G1', 'G2', 'G3']]
y = df['pass']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)
acc = accuracy_score(y_test, model.predict(X_test))

st.success(f"Model Accuracy: {acc:.2f}")

st.subheader("Predict Student Result")
g1 = st.slider("G1", 0, 20, 10)
g2 = st.slider("G2", 0, 20, 10)
g3 = st.slider("G3", 0, 20, 10)

if st.button("Predict"):
    result = model.predict([[g1, g2, g3]])
    st.write("✅ Student will Pass" if result[0] == 1 else "❌ Student will Fail")

st.subheader("📊 Heatmap")
sns_plot = sns.heatmap(df[['G1', 'G2', 'G3', 'average', 'pass']].corr(), annot=True)
st.pyplot(sns_plot.figure)
