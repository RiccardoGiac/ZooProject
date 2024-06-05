import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):

#Riccardo: Questo test controlla se l'animale viene rimosso dalla fence

    def test_animal_remove(self):
        zookeeper_1: ZooKeeper = ZooKeeper(name="Luigi",
                                            surname="Mario",
                                            id=421)
        fence_1: Fence = Fence(area=200,temperature=20,habitat="Sea")
        animal_1: Animal = Animal(name="Jeff",species="Orca",age=4,
                                  height=6,width=10,preferred_habitat="Sea")
        zookeeper_1.add_animal(animal_1,fence_1)
        zookeeper_1.remove_animal(animal_1,fence_1)
        result: int = len(fence_1.animals_inside) 
        message: str = f"Error: remove_animal doesn't work properly"

        self.assertEqual(result,0,message)

#Riccardo: Questo test controlla se l'habitat dell'animale è uguale a quello della fence

    def test_animal_add_habitat(self):
        zookeeper_1: ZooKeeper = ZooKeeper(name="Marco",
                                           surname="Rossi",
                                            id=32)
        fence_1: Fence = Fence(area=200,temperature=10,
                               habitat="Sea")
        animal_1: Animal = Animal(name="Ciro",species="Lion",age=4,
                                  height=5,width=10,preferred_habitat="Savana")
        
        zookeeper_1.add_animal(animal_1,fence_1)
        result: int = len(fence_1.animals_inside)
        message: str = f"Error: add_animal doesn't work properly."

        self.assertEqual(result,0,message)


 #Riccardo: Questo test controlla se l'animale può essere feedato

    def test_feed(self):
        zookeeper_1: ZooKeeper = ZooKeeper(name="Marco",
                                           surname="Rossi",
                                            id=32)
        fence_1: Fence = Fence(area=1,temperature=10,
                               habitat="Savana")
        animal_1: Animal = Animal(name="Ciro",species="Lion",age=4,
                                  height=1,width=1,preferred_habitat="Savana")
        zookeeper_1.add_animal(animal_1,fence_1)
        zookeeper_1.feed(animal_1)


if __name__ == "__main__":
    unittest.main()



#python -m unittest -v