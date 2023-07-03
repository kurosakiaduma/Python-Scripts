def bonAppetit(bill, k, b):
    # Write your code here
    bill.remove(bill[k])
    split = sum(bill)/2
    if split == b:
        print('Bon Appetit')
    else:
        print(int(b-split))
