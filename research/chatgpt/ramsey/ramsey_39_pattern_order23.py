"""For each legal first border of the 23-prefix, decide reachability of 28."""
from collections import Counter
from random import Random
from ramsey_39_pattern_three_choices import add,options

def run():
    rng=Random(39);pairs=[];ind=[0]
    for n in range(23):
        p=rng.choice(options(n,pairs,ind));pairs,ind=add(n,p,pairs,ind)
    opts=options(23,pairs,ind);orig=rng.choice(opts);mask=(1<<23)-1
    def seek(n,choices,fam):
        if not choices:return None
        if n==27:return [choices[0]]
        for p in choices:
            # Remaining new vertices can be ordered by their original 23-bit columns.
            miss=[s for s in fam[7] if not s&p];child=[]
            for q in choices:
                if q&mask < p&mask:continue
                if not p&q:child.append(q|1<<n)
                if all(q&s for s in miss):child.append(q)
            if child:
                nxt=[fam[0]]+[fam[k]+[s|1<<n for s in fam[k-1] if not s&p] for k in range(1,8)]
                path=seek(n+1,child,nxt)
                if path is not None:return [p]+path
        return None
    winners=[]
    for p in opts:
        pairs2,i2=add(23,p,pairs,ind);child=options(24,pairs2,i2)
        tail=seek(24,child,[[s for s in i2 if s.bit_count()==k] for k in range(8)])
        if tail is not None:winners.append([p]+tail)
    print('reach 28:',len(winners),'of',len(opts),'original succeeds:',any(w[0]==orig for w in winners))
    if winners:
        for n,p in enumerate(winners[0],23):
            assert p in options(n,pairs,ind);pairs,ind=add(n,p,pairs,ind);print(n+1,[i+1 for i in range(n) if p>>i&1])
if __name__=='__main__':run()
