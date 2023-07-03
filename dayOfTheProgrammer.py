#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    months = [30 if i % 2 == 0 else 31 for i in range(1,13)]
    if (year <= 1917 and (year % 4 == 0)) or (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        months[1] = 29
        months[7] = 31
    else:
        months[1] = 28
        months[7] = 31

    count = i = 0
    print(f'MONTHS {months}')

    while True:
        if (count+months[i]) > 256:
            break
        count+=months[i]
        i+=1
    
    if year == 1918:
        count-=13
    
    return f'{str(0)+str(256-count) if len(str(256-count)) < 2 else (256-count)}.{str(0) + str(i+1) if len(str(i+1)) < 2 else i+1}.{year}'