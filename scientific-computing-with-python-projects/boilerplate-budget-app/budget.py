class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger = []


    def deposit(self, amount: float | int, description: str=""):
        self.ledger.append(dict(amount=amount, description=description))

    def get_balance(self) -> float:
        res = 0
        for obj in self.ledger:
            res += obj["amount"]
        return res
    
    def withdraw(self, amount: float | int, description: str="") -> bool:
        if not self.check_funds(amount): return False
        
        self.ledger.append(dict(amount=-amount, description=description))
        return True
    
    def transfer(self, amount: float, other_category) -> bool:
        if not self.check_funds(amount): return False

        self.withdraw(amount, description=f"Transfer to {other_category.name}")
        other_category.deposit(amount, description=f"Transfer from {self.name}")
        return True
    
    def check_funds(self, amount) -> bool:
        return amount <= self.get_balance()
    
    def __str__(self) -> str:
        headline = f"{self.name:*^30}"
        res = [headline]

        for obj in self.ledger:
            desc = obj["description"][:23]
            desc = f"{desc: <23}"
            amount = "{:>7.2f}".format(obj["amount"]) 
            res.append(f"{desc}{amount}")

        res.append(f"Total: {self.get_balance():.2f}")

        return "\n".join(res)

    
    def get_deposits(self) -> float:
        res = 0
        for obj in self.ledger:
            if (y := obj["amount"]) > 0:
                res += y
        return res
    def get_withdrawals(self) -> float:
        res = 0
        for obj in self.ledger:
            if (y := obj["amount"]) < 0:
                res += y
        return res

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [category.get_withdrawals() for category in categories]
    total_spent = sum(spendings)
    percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spendings]
    #print(f"{percentages = }")

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o" if percentage >= i else " "
            chart += "  "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            chart += category.name[i] if i < len(category.name) else " "
            chart += "  "
        if i < max_name_length - 1:
            chart += "\n"

    with open("chart.txt", "w") as f:
        f.write(chart)
    return chart


    
    


if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print()
    print(clothing)
    print()

    print(create_spend_chart([food, clothing, auto]))