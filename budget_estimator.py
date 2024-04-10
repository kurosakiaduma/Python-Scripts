from icecream import ic
class Solution():
    def __init__(self, b, k:list, d: list):
        self.b = b
        self.k = k
        self.d = d
        
    def choose_arrays(self, k, d):
        b = self.b
        
        # Check if either list is empty
        if not k or not d:
            ic(-1)
            return []
        
        select_items = []
        k = sorted(k, reverse=True)
        d = sorted(d, reverse=True)
        
        val = max(k[0],d[0])
        
        if val in k and val not in d:
            # Use if statement instead of assert
            if max(d) <= (b-val):
                select_items.append(val)
                select_items.append(max(d))
                ic( select_items)
                return select_items
            else:
                if (min(d) > (b - val)):
                    k.remove(max(k))
                else:
                    d.remove(max(d))
            
                return self.choose_arrays(k,d)
                
        elif val in d and val not in k:
            # Use if statement instead of assert
            if max(k) <= (b-val):
                select_items.append(val)
                select_items.append(max(k))
                ic( select_items)
                return select_items
            else:
                if (min(k) > (b - val)):
                    d.remove(max(d))
                else:
                    k.remove(max(k))
                
                self.choose_arrays(k,d)
                        
        elif val in k and val in d:
        # unfortunately needed in situations where both keyboards
        # and drives have the same max price
            # Use if statement instead of assert
            if (val+min(k) > b) and (val+min(d)>b):
                k.remove(max(k))
                d.remove(max(d))
                return self.choose_arrays(k,d)        
            elif 2* val <= b:
                select_items.append(val)
                select_items.append(val)
                ic( select_items)
                return select_items
            else:
                while True:
                    try:
                        if (k[1] > d[1] and k[1] <= (b -val)):
                            select_items.append(val)
                            select_items.append(k[1])
                            ic( select_items)
                            return select_items
                        elif (d[1] > k[1] and d[1] <= (b -val)):
                            select_items.append(val)
                            select_items.append(d[1])
                            ic( select_items)
                            return select_items
                        elif d[1] == k [1] and d[1] <=b:
                            select_items.append(val)
                            select_items.append(d[1])
                            ic( select_items)
                            return select_items
                        else:
                            d.remove(d[1])
                            k.remove(k[1])
                    except IndexError:
                        ic( -1)
                        break


if __name__ == "__main__":
    a = Solution(k=[10, 9, 8], d=[10, 9, 8], b=19)
    a.choose_arrays(k=a.k,d=a.d)
