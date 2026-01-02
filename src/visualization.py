import matplotlib.pyplot as plt
import seaborn as sns

def grafic_note(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df["Nota"], bins=10, color='skyblue', edgecolor='black')
    plt.title("Distributia Notelor", fontsize=16, fontweight='bold')
    plt.xlabel("Nota", fontsize=12)
    plt.ylabel("Frecventa", fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig("grafic_note.png", dpi=300)
    plt.show()

def grafic_medii_categorii(df):
    medii = df.groupby("Categorie")["Nota"].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    colors = ['#2ecc71', '#f39c12', '#e74c3c']
    bars = plt.bar(medii.index, medii.values, color=colors, edgecolor='black')
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title("Media Notelor pe Categorii", fontsize=16, fontweight='bold')
    plt.xlabel("Categorie", fontsize=12)
    plt.ylabel("Medie", fontsize=12)
    plt.ylim(0, 10.5)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig("grafic_categorii.png", dpi=300)
    plt.show()

def grafic_complet(df):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes[0, 0].hist(df["Nota"], bins=10, color='skyblue', edgecolor='black')
    axes[0, 0].set_title("Distributia Notelor", fontweight='bold')
    axes[0, 0].set_xlabel("Nota")
    axes[0, 0].set_ylabel("Frecventa")
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    medii = df.groupby("Categorie")["Nota"].mean().sort_values(ascending=False)
    axes[0, 1].bar(medii.index, medii.values, color=['#2ecc71', '#f39c12', '#e74c3c'], edgecolor='black')
    axes[0, 1].set_title("Media pe Categorii", fontweight='bold')
    axes[0, 1].set_xlabel("Categorie")
    axes[0, 1].set_ylabel("Medie")
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    sns.boxplot(data=df, x="Categorie", y="Nota", ax=axes[1, 0], hue="Categorie", palette="Set2", legend=False)
    axes[1, 0].set_title("Boxplot Note pe Categorii", fontweight='bold')
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    colors_map = {'excelent': 'green', 'bun': 'orange', 'slab': 'red'}
    for categorie in df['Categorie'].unique():
        subset = df[df['Categorie'] == categorie]
        axes[1, 1].scatter(subset['Varsta'], subset['Nota'], 
                          label=categorie, s=100, alpha=0.6, 
                          color=colors_map.get(categorie, 'blue'))
    axes[1, 1].set_title("Nota vs Varsta", fontweight='bold')
    axes[1, 1].set_xlabel("Varsta")
    axes[1, 1].set_ylabel("Nota")
    axes[1, 1].legend()
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("dashboard_complet.png", dpi=300)
    plt.show()