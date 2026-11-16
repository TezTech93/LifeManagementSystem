import csv

class Diet:
    def __init__(self,cals,p,c,f,target_vitamins=[]):
        self.cals = cals
        self.protein = p     #grams
        self.carbs = c     #grams
        self.fat = f     #grams
        self.target_vitamins = target_vitamins

my_diet = Diet()
family_diet = Diet()

my_diet_fn = 'my_diet.csv'
family_diet_fn = 'family_diet.csv'