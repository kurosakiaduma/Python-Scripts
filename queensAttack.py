def resetShifter():
    shifter = 0
    return shifter

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    possibles = []
    init = [r_q, c_q]
    
    shifter = resetShifter()
    
    while (init[0]+shifter) <= n or (init[0]-shifter) >= 1:
        shifter += 1
        
        v_ups = [init[0]+shifter, init[1]]
        v_downs = [init[0]-shifter, init[1]]
        
        if v_ups[0] <= n and v_ups != init:
            possibles.append(v_ups)
            
        if v_downs[0] >= 1 and v_downs != init:
            possibles.append(v_downs)

    shifter = resetShifter()
    
    while (init[1]+shifter) <= n or (init[1]-shifter) >= 1:
        shifter += 1
        
        l_lefts = [init[0], init[1]-shifter]
        l_rights = [init[0], init[1]+shifter]
                    
        if l_lefts[1] >= 1 and l_lefts != init:
            possibles.append(l_lefts)

        if l_rights[1] <= n and l_rights != init:
            possibles.append(l_rights)
    shifter = resetShifter()
    
    while (init[0]+shifter <= n and init[1]-shifter >= 1) or (init[0]-shifter >= 1 and init[1]-shifter >= 1):
        shifter+=1
        lu_ds = [init[0]+shifter, init[1]-shifter]
        ld_ds = [init[0]-shifter, init[1]-shifter]
        
        if lu_ds[0] <= n and lu_ds[1] >= 1:
            possibles.append(lu_ds)

        if ld_ds[0] >= 1 and lu_ds[1] >= 1:
            possibles.append(ld_ds)
    
    shifter = resetShifter()
    while (init[0]+shifter <= n and init[1]+shifter <= n) or (init[0]-shifter >= 1 and init[1]+shifter >= n):
        shifter+=1
        ru_ds = [init[0]+shifter, init[1]+shifter]
        rd_ds = [init[0]-shifter, init[1]+shifter]
        
        if ru_ds[0] <= n and ru_ds[1] <= n:
            possibles.append(ru_ds)

        if rd_ds[0] >= 1 and ru_ds[1] <= n:
            possibles.append(rd_ds)
             
        
    print(possibles)
