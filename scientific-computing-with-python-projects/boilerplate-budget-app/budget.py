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
            amount = obj["amount"]
            amount = f"{amount:>7.2f}"
            res.append(f"{desc}{amount}")
        res.append(f"Total: {self.get_balance():.02f}")

        return "\n".join(res)







def create_spend_chart(categories):
    
    chart = ["Percentage spent by category"]
    
    withdrawals = []
    categories = sorted(categories, key=lambda category: sum(obj["amount"] for obj in 
                                                             category.ledger if obj["amount"] < 0)    )
    for category in categories:
        money_spent = sum(obj["amount"] for obj in category.ledger if obj["amount"] < 0)
        withdrawals.append(money_spent)
    total = sum(withdrawals)

    for percentage in range(100, -1, -10):
        line = f"{percentage:3}| "
        for withdrawal in withdrawals:
            bar = "o" if withdrawal <= (percentage / 100 * total) else " "
            line += f"{bar:<3}"
        chart.append(line)

    chart.append("    -" + "---" * len(categories))

    max_name_length = max(len(category.name) for category in categories)

    for i in range(max_name_length):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += f"{category.name[i]}  "
            else:
                line += "   "
        chart.append(line)

    return "\n".join(chart)


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
    print(clothing)

    print(create_spend_chart([food, clothing, auto]))