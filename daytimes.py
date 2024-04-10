def timeInWords(h, m):
    num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty'}
    try:
        assert((h in num2words.keys()) and 0<= m < 60)
        if m == 0:
            return f"{num2words.get(h)} o' clock"
        elif m == 1:
            return f'{num2words.get(m)} minutes past {num2words.get(h)}'
        elif m <= 30:
            if m == 15:
                return f'quarter past {num2words.get(h)}'
            elif 19 < m <= 30:
                if m == 30:
                    return f'half past {num2words.get(h)}'
                
                m = str(m)
                
                m1 = int(m[0]) * 10
                m2 = int(m[1])
                
                if m2 == 0:
                    return f'{num2words.get(m1)} minutes past {num2words.get(h)}'
                else:
                    return f'{num2words.get(m1)} {num2words.get(m2)} minutes past {num2words.get(h)}' 
                
        elif m > 30:
            if h < 12:
                h = h+1
            else:
                h = 1
            if m == 45:
                return f'quarter to {num2words.get(h)}'
            else:
                m = 60 - m
                
                if m < 20 and m != 10:
                    return f'{num2words.get(m)} minutes to {num2words.get(h)}'
                m = str(m)
                m1 = int(m[0]) * 10
                m2 = int(m[1])
                
                if m2 == 0:
                    return f'{num2words.get(m1)} minutes to {num2words.get(h)}'
                elif m2 > 0:
                    return f'{num2words.get(m1)} {num2words.get(m2)} minutes to {num2words.get(h)}'
    except:
        return "Invalid input"


timeInWords(5, 35)