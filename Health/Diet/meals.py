import csv
from Wealth.budget import budget
from diet import my_diet,family_diet

filename = 'meals.csv'




#                              MEAL

class Meal:
    categories = ['italian','chinese','indian','mexican','greek','african',
                  'soul food','pizza','healthy','cheesy','tacos','bbq','burgers','seafood','breakfast',
                  'subs','sandwhich']
    def __init__(self,name,foods,cost,cals,p,c,f,v):
        self.name = name
        self.foods = foods
        self.cost = cost
        self.cals = cals
        self.protein = p
        self.carbs = c
        self.fat = f
        self.vitamins = v
        self.from_restaraunt = False
        self.distance = 0
        self.wait_time = 0

    def save_meal(self):
        with open(filename) as f:
            pass
        
#                             MEAL




#                               MEAL PREP


class MealManager:
     def weekly_prep(self):
          pass #Use budget and selection parameters along with calorie and macro goals considered

     def pick_a_meal(self):
          pass #Use budget and mood and distance as the main priority in this scenario


#                               MEAL PREP



#                               Recipe

class Recipe:
     def __init__(self,ingredients,cost,instructions,prep_time):
          self.ingredients = ingredients
          self.cost = cost
          self.instructions = instructions
          self.prep_time = prep_time


def terminal_input(name,foods,cost,cals,p,c,f,v):
        name = input('name')
        foods = input('foods')
        cost = input('cost')
        cals = input('cals')
        protein = input('p')
        carbs = input('c')
        fat = input('f')
        vitamins = input('v')

        m = Meal(name,foods,cost,cals,protein,carbs,fat,vitamins)
        m.save_meal()