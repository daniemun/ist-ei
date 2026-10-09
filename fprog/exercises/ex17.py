#!/usr/bin/env python3

cents_per_euro = 100

def e(c: float) -> int:
    return round(c / cents_per_euro)
    
def c(e: float) -> int:
    return round(e * cents_per_euro)

money_change_list:dict[int, int] = {
    c(0.01) : 0,
    c(0.02) : 0,
    c(0.05) : 0,
    c(0.10) : 0,
    c(0.20) : 0,
    c(0.50) : 0,
    c(1.00) : 0,
    c(2.00) : 0,
    c(5.00) : 0,
    c(10.00) : 0,
    c(20.00) : 0,
    c(50.00) : 0,
    c(100.00) : 0,
    c(200.00) : 0,
    c(500.00) : 0,
}
money_change_list_len = len(money_change_list)

def money_amount_to_string(money: int) -> str:
    if money >= cents_per_euro:
        return f"{(money / cents_per_euro):.0f}€"
    else:
        return f"{money}¢"
        
def get_immediately_smaller_money(money: int) -> int:
    old_key = 0
    for key in money_change_list.keys():
        if key > money:
            return old_key
            
        old_key = key
        
    return list(money_change_list)[-1] # Biggest number

def get_input() -> int:
    n = 0.0
    while True:
        try:
            n = float(input("Money amount (€): "))
            if n > 0:
                break
        except ValueError:
            print("Invalid money amount")
            
    return c(n)

def main() -> None:
    money = get_input()
    
    while money > 0:
        change = get_immediately_smaller_money(money)
        money -= change
        money_change_list[change] += 1
                
    for key, amount in money_change_list.items():
        if amount > 0:
            print(f"{money_amount_to_string(key)}: {amount}")
    
if __name__ == "__main__":
    main()