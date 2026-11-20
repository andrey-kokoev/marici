"""Find every valid cyclic order for Delta at p=991, without an order bound as input.
Stop at an interval obstruction: if its span <= floor(n/2), it persists for all larger n.
"""
from itertools import combinations, count
from ramsey_45_modular_rule_trial import eta_product


def obstruction(n, red, cyclic=True):
    for k, color in [(4, True), (5, False)]:
        for rest in combinations(range(1,n),k-1):
            vs=(0,)+rest
            if all(((min(j-i,n-j+i) if cyclic else j-i) in red)==color for i,j in combinations(vs,2)):
                return k,vs


def main(p=991):
    good=[]
    for n in count(1):
        m=n//2;a=eta_product([(1,24)],m) if m else [0]
        red={d for d in range(1,m+1) if pow(a[d],(p-1)//2,p)==1}
        block=obstruction(m+1,red,False)
        if block:
            print('permanent obstruction from',n,block);break
        bad=obstruction(n,red)
        if not bad:good.append(n)
        print(n,'valid' if bad is None else bad)
    print('all valid orders',good)
if __name__=='__main__':main()
