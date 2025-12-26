import pandas as pd

def df_to_dict(_pd: pd.DataFrame) -> dict:
    df = pd.DataFrame()

    return df

id_filter = [1, 3, 5]
t = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Markus", "Tobbe", "Ted", "Anki", "Sameena"],
    "Age": [27, 25, 61, 51, 28]
})

print(t)

under_30 = t.loc[(t["Age"] < 30) & (t["ID"].isin(id_filter))]
print(under_30)

t_age = t.loc[(t["Name"].str.startswith("T")) & (t["Age"] >= 25)]
print(t_age)
