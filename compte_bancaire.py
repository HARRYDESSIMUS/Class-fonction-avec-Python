class CompteBancaire:
    def __init__(self,titulaire,solde=0):
        self.titulaire=titulaire
        self.solde=solde
    

    def deposer(self,montant):
        self.solde += montant
        print(f"{montant}€ deposé . Nouveau solde : {self.solde}€")
    def retirer(self,montant):
        if montant<=self.solde:
            self.solde -= montant
            print(f"{montant} €")
