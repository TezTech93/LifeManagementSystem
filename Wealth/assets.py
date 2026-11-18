import csv

file = 'my_assets.csv'
assets = []

class Asset:
    def __init__(self,name,tp,value,desc):
        self.name = name
        self.type = tp
        self.value = value
        self.desc = desc
        assets.append(self)

    def alter(self,field,ctx):
        if field == 'name':
            self.name = ctx
        elif field == 'type':
            self.type = ctx
        elif field == 'value':
            self.value = ctx
        elif field == 'desc':
            self.desc = ctx
        print(f'Changed {field} to {ctx}')

def save_assets():
    vals = []
    for a in assets:
        row = {'name':a.name,'type':a.type,'value':a.value,'description':a.desc}
        vals.append(row)
    with open(file,'w') as f:
        pass