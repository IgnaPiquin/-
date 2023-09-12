def create_spend_chart():
    numbers = []
    for i in range(100, -10, -10):
        numbers.append(f"{i:>{3}}|")
        print(numbers)
    
create_spend_chart()

print(((105*100/200) // 10) * 10)