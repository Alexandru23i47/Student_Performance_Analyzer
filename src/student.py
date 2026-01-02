class Student:    
    def __init__(self, nume, nota, categorie):
        self.nume = nume
        self.nota = nota
        self.categorie = categorie

    def promovat(self):
        return self.nota >= 5
    
    def __str__(self):
        status = "Promovat" if self.promovat() else "Nepromovat"
        return f"{self.nume} | Nota: {self.nota} | {status} | {self.categorie}"