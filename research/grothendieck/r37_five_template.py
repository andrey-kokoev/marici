"""Pick the least-gap five-root example to challenge a fixed-incidence theorem."""
from pathlib import Path

def hardest(m=5):
    record=100000; count=0
    for idx,line in enumerate((Path(__file__).resolve().parents[1]/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6').read_text().splitlines()):
        n=ord(line[0])-63; assert n==22
        bits=''.join(f'{ord(c)-63:06b}' for c in line[1:]); a=[0]*n
        for z,(j,i) in zip(bits,((j,i) for j in range(n) for i in range(j))):
            if z=='1':a[i]|=1<<j;a[j]|=1<<i
        def ind(p,s):
            yield s
            while p:
                b=p&-p;p^=b;yield from ind(p&~a[b.bit_length()-1],s|b)
        sets=list(ind((1<<n)-1,0));six=[s for s in sets if s.bit_count()==6]
        for s in sets:
            if s.bit_count()!=m or any(not(s>>v&1 or a[v]&s) for v in range(n)):continue
            count+=1;miss=sum(not(s&t) for t in six)
            if miss<record:
                record=miss; roots=[v for v in range(n) if s>>v&1]; winner=(idx,roots,sorted(sum((a[v]>>r&1)<<j for j,r in enumerate(roots)) for v in range(n) if not s>>v&1))
    print('rooted selections',count,'minimum',record,'first minimizing template',winner);return winner[2]
if __name__=='__main__':
    import sys
    hardest(*map(int,sys.argv[1:]))
