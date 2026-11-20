"""Erase only the direct A-B block. Enumerate all its admissible completions."""
from itertools import product
from ramsey_blind_start_formulas import seed, check


def main():
    original, _, _ = seed(7,'double')
    ab=list(product(range(3), range(3,10))); witnesses=((1<<10)-1)<<10
    base=original.copy()
    for i,j in ab:
        base[i] &= ~(1<<j); base[j] &= ~(1<<i)
    free=[(i,j) for i,j in ab if not (base[i]&base[j]&witnesses)]
    valid=[]
    for mask in range(1<<len(free)):
        rows=base.copy()
        for bit,(i,j) in enumerate(free):
            if mask>>bit&1:rows[i]|=1<<j; rows[j]|=1<<i
        if check(rows,7):valid.append(mask)
    original_mask=sum((original[i]>>j&1)<<b for b,(i,j) in enumerate(free));assert original_mask in valid
    print('candidates',1<<len(free),'valid',len(valid))
    for b,(i,j) in enumerate(free):print(f'a{i+1} b{j-2}',sorted({m>>b&1 for m in valid}))
    print('positive pair lists:', [[(i+1,j-2) for b,(i,j) in enumerate(free) if m>>b&1] for m in valid][:10]);return valid

if __name__=='__main__':main()
