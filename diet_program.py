import pickle
 

class Products:
    def __init__(self,name,protein,carbo,fat) -> None:
        self.name=name
        self.protein=protein
        self.carbo=carbo
        self.fat=fat
        
        
    def count_cal(self):
        calories=self.protein*4+self.carbo*4+self.fat*9
        return calories
        
    def count_weight(self,weight):
        self.protein=self.protein*weight/100
        self.carbo=self.carbo*weight/100
        self.fat=self.fat*weight/100

print("ssaas")      
class Diary:
    def __init__(self) -> None:
        self.lista=[]
    
    def add_component(self,element):
        self.lista.append(element)
    
    def delete_component(self,element):
        self.lista.remove(element)
    
    def sum_components_calories(self):
        total_protein=0
        total_carbo=0
        total_fat=0
        total_calories=0
        
        for element in self.lista:
            total_protein+=element.protein
            total_carbo+=element.carbo
            total_fat+=element.fat
            total_calories+=element.count_cal()
        print(f"Total calories: {total_calories}, Total Protein: {total_protein}, Total Carbo: {total_carbo}, Total Fat: {total_fat}")

    def sort_components_by_calories(self):
        self.lista.sort(key=lambda x:x.count_cal())
        
    def search_by_name(self,name):
        found_products = [product for product in self.lista if product.name==name]
        return found_products
        
    def display(self):
        for i in self.lista:
            print(f"{i.name.capitalize()} calories: {i.count_cal()} protein: {i.protein} carbo: {i.carbo} fat: {i.fat}")
    
    #save products to file my_diary.pkl       
    def save_to_file(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(self.lista, f)
    
    #load products to file my_diary.pkl 
    def load_from_file(self, file_path):
        with open(file_path, "rb") as f:
            self.lista = pickle.load(f)

 
    
milk=Products("milk",4,4,9)
egg=Products("egg",10,2,3)
chicken_breast=Products("chicken_breast",20,2,2)
chicken_breast.count_weight(200)



my_diary=Diary()

my_diary.add_component(milk)
my_diary.add_component(egg)
my_diary.add_component(chicken_breast)

my_diary.display()
my_diary.sum_components_calories()
print("before-----------------sorting")
my_diary.sort_components_by_calories()
print("after-----------------sorting")
my_diary.display()
 
result=my_diary.search_by_name("egg")
print("---finded products---")
for product in result:
    print(f"{product.name}")


 


# my_diary.save_to_file("my_diary.pkl")

 
# my_diary_loaded = Diary()
# my_diary_loaded.load_from_file("my_diary.pkl")

 
  
 
 

