from bot import BinanceClient

print("+---------+")
print("| TRADBOT |")
print("+---------+")
print("Thank you for using TradBot")
print("Enter your trades in the format <symbol> <side> <order> <quantity> <price>")

client = BinanceClient(API, SECRET)

while True:
    trade = input().split()
    result = client.create_order(trade[0], trade[1], trade[2], float(trade[3]))
    print(result)

    while True:
        choice = input("Continue?(Y/ N) ").lower().strip()
        
        if choice in ("y", "n"):
            break

        print("Choice should be either 'y' or 'n'")

    if choice == "n":
        break
                       
