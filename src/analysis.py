def statistici_generale(df):
    return {
        "media": df["Nota"].mean(),
        "mediana": df["Nota"].median(),
        "min": df["Nota"].min(),
        "max": df["Nota"].max()
    }

def top_studenti(df, n=3):
    return df.sort_values("Nota", ascending=False).head(n)

def restantieri(df):
    return df[df["Nota"] < 5]

def medii_pe_categorie(df):
    return df.groupby("Categorie")["Nota"].mean()

def distributie_categorii(df):
    return df["Categorie"].value_counts()

def procent_promovati(df):
    promovati = len(df[df["Nota"] >= 5])
    total = len(df)
    return (promovati / total) * 100 if total > 0 else 0