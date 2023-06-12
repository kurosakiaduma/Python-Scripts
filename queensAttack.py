def resetShifter():
    shifter = 0
    return shifter

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    possibles = []
    init = [r_q, c_q]
    
    shifter = resetShifter()
    while (init[0]+shifter) <= n:
        shifter += 1
        v_ups = [init[0]+shifter, init[1]]
        if v_ups[0] <= n and v_ups != init:
            if v_ups in obstacles:
                break
            possibles.append(v_ups)
            
        
    shifter = resetShifter()
    while (init[0]-shifter) >= 1:
        shifter+=1
        v_downs = [init[0]-shifter, init[1]]
        if v_downs[0] >= 1 and v_downs != init:
            if v_downs in obstacles:
                break
            possibles.append(v_downs)
    
    
    shifter = resetShifter()
    while (init[1]-shifter) >= 1:
        shifter += 1
        l_lefts = [init[0], init[1]-shifter]            
        if l_lefts[1] >= 1 and l_lefts != init:
            if l_lefts in obstacles:
                break
            possibles.append(l_lefts)

        
    shifter = resetShifter()
    while (init[1]+shifter) <= n:
        shifter+=1
        l_rights = [init[0], init[1]+shifter]
        if l_rights[1] <= n and l_rights != init:
            if l_rights in obstacles:
                break
            possibles.append(l_rights)


    shifter = resetShifter()    
    while (init[0]+shifter <= n and init[1]-shifter >= 1):
        shifter+=1
        lu_ds = [init[0]+shifter, init[1]-shifter]        
        if lu_ds[0] <= n and lu_ds[1] >= 1:
            if lu_ds in obstacles:
                break
            possibles.append(lu_ds)


    shifter = resetShifter()
    while (init[0]-shifter >= 1 and init[1]-shifter >= 1):
        shifter+=1
        ld_ds = [init[0]-shifter, init[1]-shifter]
        if ld_ds[0] >= 1 and ld_ds[1] >= 1:
            if ld_ds in obstacles:
                break
            possibles.append(ld_ds)

        
    shifter = resetShifter()
    while (init[0]+shifter <= n and init[1]+shifter <= n):
        shifter+=1
        ru_ds = [init[0]+shifter, init[1]+shifter]
        if ru_ds[0] <= n and ru_ds[1] <= n:
            if ru_ds in obstacles:
                break
            possibles.append(ru_ds)

             
    shifter = resetShifter()
    while (init[0]-shifter >= 1 and init[1]+shifter <= n):
        shifter+=1
        rd_ds = [init[0]-shifter, init[1]+shifter]
        if rd_ds[0] >= 1 and rd_ds[1] <= n:
            if rd_ds in obstacles:
                break
            possibles.append(rd_ds)
        
        
    print(possibles,"\n",len(possibles))
    return len(possibles)