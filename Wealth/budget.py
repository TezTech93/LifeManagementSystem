import csv

budget_csv = 'my_budget.csv'
expenses_csv = 'my_expenses.csv'
savings_csv = 'my_savings.csv'
investments_csv = 'my_investments.csv'

class Budget:
    def __init__(self,income=[],expenses=[],savings=[],investments=[]):
        self.income = income
        self.expenses = expenses
        self.savings = savings
        self.investments = investments

    def calculate_income(self):
        total = 0
        for i in self.income:
            total += i.amt
        return total
    
    def calculate_expenses(self):
        total = 0
        for e in self.expenses:
            total += e.amt
        return total

    def create_standard_budget(self,percentages=[40,30,30]):
        #base off percent i.e 40,30,30
        total_income = self.calculate_income()
        expense_allocation = total_income * percentages[0] / 100
        savings_allocation = total_income * percentages[1] / 100
        investments_allocation = total_income * percentages[2] / 100
        monthly_budget = {
            'expenses': expense_allocation,
            'savings': savings_allocation,
            'investments': investments_allocation,
            'expenses_percent': percentages[0],
            'savings_percent': percentages[1],
            'investments_percent': percentages[2]
        }
        return monthly_budget

    def create_custom_budget(self,e,s,i):
        total_income = self.calculate_income()
        expense_allocation = total_income * e / 100
        savings_allocation = total_income * s / 100
        investments_allocation = total_income * i / 100
        monthly_budget = {
            'expenses': expense_allocation,
            'savings': savings_allocation,
            'investments': investments_allocation,
            'expenses_percent': e,
            'savings_percent': s,
            'investments_percent': i
        }
        return monthly_budget

    def save_as_csv(self):
        with open(budget_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['source', 'amt', 'freq'])
            for income in self.income:
                writer.writerow([income.source, income.amt, income.freq])
        with open(expenses_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'amt', 'freq'])
            for expense in self.expenses:
                writer.writerow([expense.name, expense.amt, expense.freq])
        with open(savings_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['cur_amt', 'goal_amt'])
            for saving in self.savings:
                writer.writerow([saving.cur_amt, saving.goal_amt])
        with open(investments_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['cur_amt', 'goal_amt'])
            for investment in self.investments:
                writer.writerow([investment.cur_amt, investment.goal_amt])

class Income:
    def __init__(self,source,amt,freq):
        self.source = source
        self.amt = amt
        self.freq = freq

    def alter(self,field,ctx):
        if field == 'source':
            self.source = ctx
        elif field == 'amt':
            self.amt = ctx
        elif field == 'freq':
            self.freq = ctx

class Expense:
    def __init__(self,name,amt,freq):
        self.name = name
        self.amt = amt
        self.freq = freq

    def alter(self,field,ctx):
        if field == 'name':
            self.name = ctx
        elif field == 'amt':
            self.amt = ctx
        elif field == 'freq':
            self.freq = ctx

class Savings:
    def __init__(self,cur_amt,goal_amt):
        self.cur_amt = cur_amt
        self.goal_amt = goal_amt

    def increase(self,amt):
        self.cur_amt += amt
        return self.cur_amt

    def decrease(self,amt):
        self.cur_amt -= amt
        return self.cur_amt

class Investment:
    def __init__(self,cur_amt,goal_amt):
        self.cur_amt = cur_amt
        self.goal_amt = goal_amt

    def increase(self,amt):
        self.cur_amt += amt
        return self.cur_amt

    def decrease(self,amt):
        self.cur_amt -= amt
        return self.cur_amt