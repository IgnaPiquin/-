class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    # Method for cheking if there are enough funds to spend in the amount inputed
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    # Method for adding a withdraw, adding a dictionary like deposit but with the amount in negative notation
    def withdraw(self, amount, description=""):
         # cheking if there is enough funds to withdraw
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        # running through all the transactions in the ledger and getting the value of amounts from the dictionary
        for i in self.ledger:
            balance = balance + i["amount"]
        return balance
    
    # method to transfer funds form one object to another
    def transfer (self, amount, category):
        description = f"Transfer to {category.name}"
        # cheking if there is enough funds to transfer
        if self.check_funds(amount):
            self.withdraw(amount, description)
            description = f"Transfer from {self.name}"
            category.deposit(amount, description)
            return True
        else:
            return False
    def __str__(self):
        # Calculate the number of asterisk characters on both sides of the name
        asterisk_count = (30 - len(self.name)) // 2
        
        # Create the title line
        title_line = '*' * asterisk_count + self.name + '*' * asterisk_count

        # If the total_length is not even, add an extra asterisk on the right side
        if len(title_line) < 30:
            title_line += '*'
        
        lines = ""
        for i in self.ledger:
            
            #cheking if the description is too large
            if len(i['description']) > 23:
                #shortening the description and asingning a distance
                description = i['description'][:23]
                distance = 30 - len(description)
            else:
                #working out the distance and asingning the description
                distance = 30 - len(i['description'])
                description = i['description']
            
            #converting the amount to a string with two decimal places
            amount = f"{i['amount']:.2f}"
            #shortening the amount if the number has more than 7 characters
            if len(amount) > 7:
                amount = amount[:7]
            
            # creating the lines with the description and amount cleaned up
            lines += f"{description}{amount:>{distance}}\n"
        #Getting the total balance and saving it in the last line
        last_line = f"Total: {self.get_balance()}"
        
        return (title_line + "\n" + lines + last_line)
            
        

def create_spend_chart(categories):
    # making a list with all the posible percetages and | to use for the final print
    lines = []
    for i in range(100, -10, -10):
        lines.append(f"{i:>{3}}|")
    
    # creating a list with the spents of each category
    spent = []
    for category in categories:
        s = 0
        # Runing through all the ledgers and appending all the negative numbers
        for i in category.ledger:
            if i["amount"] <= 0:
                s += i["amount"]
        spent.append(s)
    
    #Creating a list with the names of all the categories
    names = []
    for category in categories:
        names.append(category.name)
    
    # Storaging the total amount spent for all the categories
    total_spent = 0
    for i in spent:
        total_spent += i
    
    # Creating a list with the percentages of the total spent for all the categories
    percentages = []
    for i in spent:
        percentages.append(((i*100/total_spent)// 10) * 10)
    
    
    # Running through all the psoible percentages (variable called numbers)
    for n in range(len(lines)):
        #running through the percentage of each category 
        for percentage in percentages:
            # If the percetage of the category is greater than or equal to the posible percentage then cocatenate " o " to the line
            if percentage >= float(lines[n][:3]):
                lines[n] += " o "
            else: # Else concatenete "  "
                lines[n] += "   "
        lines[n] += " "
    # Creating a separator between the percentages of the categories and the names of the categories and appending it to the lines list
    separator = "-" * (len(categories) * 3 + 1)
    separator = f"    {separator}"
    lines.append(separator)
    
    # Getting the size of the larger name of the categories
    larger_name = 0
    for name in names:
        if len(name) > larger_name:
            larger_name = len(name)
    
    # Adding the necessary starter space for the names of the categories
    for i in range(larger_name):
        lines.append("    ")

    # Looping through all the lines below the separator line (----)
    for i in range(len(lines)-larger_name, len(lines), 1) :
        #looping through all the names of the categories
        for name in names:
            # cp for character position
            cp =  i-(len(lines)-larger_name)
            if name[cp:cp+1]:
                lines[i] += f" {name[cp:cp+1]} "
            else:
                lines[i] += f"   "
        lines[i] += f" "
    
    graph = ""
    # Concatenating all the variables in the list into a string
    for i in range(len(lines)):
        if i == 0:
            graph += f"{lines[i]}"
        else:
            graph += f"\n{lines[i]}"
    
    return (f"Percentage spent by category\n" + graph)
            
        
        
    
    




testing = Category("Ignacio")
test2 = Category("Santiago")


testing.deposit(800, "Dolares")
testing.transfer(200,  test2)
testing.withdraw(10, "Testing the how to handle large strings")
test2.withdraw(100, "Testing the how to handle large strings")
print(testing.ledger)
print(testing.get_balance())
print(test2.ledger)
print(test2.get_balance())
print(testing)

print(create_spend_chart([testing, test2]))