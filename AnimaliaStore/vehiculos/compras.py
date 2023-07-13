class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito
    
    def agregar(self, animal):
        animal_data = {
            "animal_id": animal["numero"],
            "animal": animal["animal"],
            "categoria": animal["categoria_id"],
            "precio": str(animal["precio"]),
            "cantidad": 1,
            "total": animal["precio"],
        }
        if animal["numero"] not in self.carrito.keys():
            self.carrito[animal["numero"]] = animal_data
        else:
            for key, value in self.carrito.items():
                if key == animal["numero"]:
                    value["cantidad"] += 1
                    value["precio"] = animal["precio"]
                    value["total"] += animal["precio"]
                    break
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, animal):
        id = animal["numero"]
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, animal):
        for key, value in self.carrito.items():
            if key == animal["numero"]:
                value["cantidad"] -= 1
                value["total"] -= animal["precio"]
                if value["cantidad"] < 1:
                    self.eliminar(animal)
                break
        self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
