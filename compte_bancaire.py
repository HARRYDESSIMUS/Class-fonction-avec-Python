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
            print(f"{montant} € retirés.nouveau solde:{self.solde} €")
        else: 
            print(f"Fond insuffisant")
    
    def afficher_solde(self):
        print(f"solde de {self.titulaire}:{self.solde}")

compte1= CompteBancaire("Jean")
compte1.afficher_solde()
compte1.deposer(100)
compte1.retirer(50)
compte1.retirer(100)    


