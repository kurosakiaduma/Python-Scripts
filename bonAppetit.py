def bonAppetit(bill, k, b):
    # Write your code here
    bill.remove(bill[k])
    if (split := sum(bill)/2) == b:
        print('Bon Appetit')
    else:
        print(int(b-split))
