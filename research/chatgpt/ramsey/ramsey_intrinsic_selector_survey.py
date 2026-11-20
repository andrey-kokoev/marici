"""Audit the unchanged maximum-disjointness selector on maximum Ramsey graphs.
Columns: selected types = all open neighborhoods? selected types = just maximum-size neighborhoods?
"""
from collections import Counter
from urllib.request import urlopen
from ramsey_35_intrinsic_type_selector import select


def decode(s):
    n=s[0]-63;bits=''.join(f'{v-63:06b}' for v in s[1:]);rows=[0]*n
    for j in range(n):
        for i in range(j):
            if bits[j*(j-1)//2+i]=='1':rows[j]|=1<<i;rows[i]|=1<<j
    return rows

def audit(rows):
    hist,chosen=select(rows);alpha=next(iter(chosen)).bit_count();N=set(rows);large={s for s in N if s.bit_count()==alpha}
    return (chosen==N,chosen==large,len(chosen),len(chosen&N),len(large),max(hist))

if __name__=='__main__':
    for k,n in ((3,5),(4,8),(5,13),(6,17),(7,22),(9,35)):
        if k in (3,4,5,9):
            D={3:[1,-1],4:[1,-1,4],5:[1,-1,5,-5],9:[1,-1,7,-7,11,-11,16,-16]}[k]; graphs=[[sum(1<<((v+d)%n) for d in D) for v in range(n)]]
        else:graphs=list(map(decode,urlopen(f'https://users.cecs.anu.edu.au/~bdm/data/r3{k}_{n}.g6',timeout=20).read().splitlines()))
        results=[audit(g) for g in graphs];print(k,len(results),'full',sum(x[0] for x in results),'max only',sum(x[1] for x in results),'none genuine',sum(x[3]==0 for x in results),'first',results[0],flush=True)
