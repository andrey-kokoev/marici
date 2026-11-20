"""Keep witness IDs in A-to-W-to-B joins on the target-only double seed."""
from ramsey_blind_start_formulas import seed,check

if __name__=='__main__':
    rows, offsets, _ = seed(7,'double'); assert check(rows,7)
    names=['a1','a2','a3']+[f'b{i}' for i in range(1,8)]
    W=((1<<10)-1)<<10
    def names_w(mask):return tuple(name+'w' for t,name in enumerate(names,10) if mask>>t&1)
    print('offsets',offsets)
    count=0
    for i in range(3):
        row=[]
        for j in range(3,10):
            ids=names_w(rows[i]&rows[j]&W);row.append(ids);count+=bool(ids)
        print(names[i],row)
    print('pairs with a common indexed witness',count,'of 21')
