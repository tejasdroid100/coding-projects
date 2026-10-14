
house_price=int(1000000)
credit= int(input("write your credit score: "))
if credit>=670:
    adj_price= (10/100*1000000)
    print(f'House Down Payment: {adj_price}')
else:
    print(f'House Down Payment: {20/100*1000000}')
