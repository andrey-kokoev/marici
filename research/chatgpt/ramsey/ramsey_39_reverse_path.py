"""Delete addresses 35..28 in catalogue order. Rank their reverse borders."""
from ramsey_39_fixed_seed_exact import B, I

def audit(n):
    mask=(1<<n)-1
    ind=[s for s in I if s<=mask];eight=[s for s in ind if s.bit_count()==8]
    opts=[p for p in ind if all(p&s for s in eight)]
    t=B[n]&mask;assert t in opts
    # Inverted index of candidates touching each old address.
    inc=[sum(1<<j for j,p in enumerate(opts) if p>>i&1) for i in range(n)]
    def touch(p):
        v=0
        while p:
            b=p&-p;v|=inc[b.bit_length()-1];p^=b
        return v
    missed=[(s,~touch(s)) for s in ind if s.bit_count()==7];scores=[]
    for p in opts:
        bad=0
        for s,m in missed:
            if not s&p:bad|=m
        scores.append(len(opts)-(touch(p)&bad).bit_count())
    a=scores[opts.index(t)];print(n,len(opts),a,max(scores),sum(b>a for b in scores),[i+1 for i in range(n) if t>>i&1])
if __name__=='__main__':
    for n in range(27,35):audit(n)
