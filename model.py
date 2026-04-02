import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    data = {
    "age": [18,20,22,24,26,28,19,21,23,25,17,18],
    "study_hours": [2,3,4,5,6,7,2,3,4,5,1,1],
    "note": [8,10,12,14,16,18,9,11,13,15,2,4],
    "success": [0,0,1,1,1,1,0,0,1,1,0,0]
}

    df = pd.DataFrame(data)

    X = df[["age", "study_hours", "note"]]
    y = df["success"]

    model = LogisticRegression()
    model.fit(X, y)

    return model