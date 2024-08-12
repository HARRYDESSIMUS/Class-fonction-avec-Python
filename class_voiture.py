class voiture :
    def __init__(self,marque,vitesse,prix) :
        self.marque=marque
        self.vitesse=vitesse
        self.prix=prix

    @classmethod
    def toyata(cls):
        return cls(marque="toyota",vitesse="300",prix="20000")
    
    @classmethod
    def volvo(cls):
        return cls(marque="volvo",vitesse="238",prix="12000")
    
    @classmethod
    def ford (cls):
        return cls (marque="ford",vitesse="250",prix="15000")
toyo=voiture.toyata()
fordita=voiture.ford()
vol=voiture.volvo()