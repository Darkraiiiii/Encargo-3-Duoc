class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, Animal):
        if Animal.numero not in self.carrito.keys():
            self.carrito[Animal.numero]={
                "animal_id":Animal.numero, 
                "animal": Animal.animal,
                "categoria": Animal.categoria,
                "precio": str (Animal.precio),
                "cantidad": 1,
                "total": Animal.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==Animal.numero:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = Animal.precio
                    value["total"]= value["total"] + Animal.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, Animal):
        id = Animal.numero
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,Animal):
        for key, value in self.carrito.items():
            if key == Animal.numero:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- Animal.precio
                if value["cantidad"] < 1:   
                    self.eliminar(Animal)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
