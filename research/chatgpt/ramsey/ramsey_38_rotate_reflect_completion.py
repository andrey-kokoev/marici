"""Complete the signed outer block of 1499, not a bare table of address names.
Read target center links only after enumeration. R=half-turn within each ring,
F=exchange top and bottom layers. Require FR, not R and F separately."""
from itertools import combinations,product
from ramsey_38_cube_inversion import sign

ring=(0,1,2,5,8,7,6,3)
out=[9*z+j for z in range(3) for j in ring];centers=(4,13,22)
perm=[8*(2-z)+(i+4)%8 for z in range(3) for i in range(8)]

def invert(p):return sum((p>>i&1)<<j for i,j in enumerate(perm))

def main():
    I=[0]
    for j in range(24):
        a=sum(1<<i for i in range(j) if sign(out[i],out[j]));I += [p|1<<j for p in I if not p&a]
    fam={k:[s for s in I if s.bit_count()==k] for k in (5,6,7)}
    opts=[p for p in I if all(p&s for s in fam[7])];fixed=[p for p in opts if invert(p)==p];solutions=[]
    def pair(p,q,b):return not(p&q) if b else all(s&(p|q) for s in fam[6])
    for p,q in product(opts,fixed):
        r=invert(p);assert r in opts
        for b,c in product(range(2),repeat=2):
            if not (pair(p,q,b) and pair(q,r,b) and pair(p,r,c)):continue
            if b and c:continue
            if not(b or c) and any(not s&(p|q|r) for s in fam[5]):continue
            solutions.append((p,q,r,b,c))
    p,q,r=[sum(1<<i for i,v in enumerate(out) if sign(v,u)) for u in centers];answer=(p,q,r,int(sign(4,13)),int(sign(4,22)));assert answer in solutions
    assert set(solutions)=={answer,(r,q,p,answer[3],answer[4])} and p!=r
    print('legal individual columns, fixed columns, labelled completions:',len(opts),len(fixed),len(solutions))
    from ramsey_border_order import key,graph
    classes=set()
    for p,q,r,b,c in solutions:
        cols=[sum(1<<i for i in range(j) if sign(out[i],out[j])) for j in range(24)]+[p,q|(b<<24),r|(c<<24)|(b<<25)]
        classes.add(key(graph(27,sum(m<<(j*(j-1)//2) for j,m in enumerate(cols)))))
    print('unlabelled completions:',len(classes))
if __name__=='__main__':main()
