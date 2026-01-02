import pandas as pd
import os
from student import Student
from analysis import *
from visualization import *

def main():
    print("STUDENT PERFORMANCE ANALYZER")
    filepath = os.path.join("data", "studenti.csv")
    df = pd.read_csv(filepath)
    studenti = [Student(row['Nume'], row['Nota'], row['Categorie']) for _, row in df.iterrows()]
    
    print("LISTA STUDENTILOR:")
    for s in studenti:
        print(f"  {s}")
    print("STATISTICI GENERALE:")
    stats = statistici_generale(df)
    print(f"Media generala: {stats['media']:.2f}")
    print(f"Mediana: {stats['mediana']:.2f}")
    print(f"Nota minima: {stats['min']}")
    print(f"Nota maxima: {stats['max']}")
    print(f"Procent promovati: {procent_promovati(df):.1f}%")
    
    print("TOP 3 STUDENTI:")
    top = top_studenti(df, n=3)
    for idx, (_, row) in enumerate(top.iterrows(), 1):
        print(f"{row['Nume']}: {row['Nota']} puncte ({row['Categorie']})")
    
    print("RESTANTIERI (Nota < 5):")
    rest = restantieri(df)
    if len(rest) > 0:
        for _, row in rest.iterrows():
            print(f"{row['Nume']}: {row['Nota']} puncte")
    else:
        print("Nu exista restantieri")
    
    print("MEDII PE CATEGORII:")
    medii = medii_pe_categorie(df)
    for categorie, medie in medii.items():
        print(f"{categorie}: {medie:.2f}")

    print("DISTRIBUTIA STUDENTILOR:")
    distributie = distributie_categorii(df)
    for categorie, numar in distributie.items():
        procent = (numar / len(df)) * 100
        print(f"{categorie}: {numar} studenți ({procent:.1f}%)")

    grafic_note(df)
    grafic_medii_categorii(df)
    grafic_complet(df)
if __name__ == "__main__":
    main()