"""Predecessor only. Do not require a bijection: each side independently chooses a contact class."""
from ramsey_excel_corner_predecessor_readout import squares,CAT,decode,D
from itertools import product
from collections import Counter
import json


def audit():
    stats=Counter();at=Counter();force=Counter();ex=None
    for idx,line in enumerate((CAT/'r37_22.g6').read_text().splitlines(),1):
        a=decode(line);n=len(a);qs=[0]
        for i,g in enumerate(a):qs.extend([q|1<<i for q in qs if not q&g])
        qs=sorted((q for q in qs if q.bit_count()>=4),key=lambda q:(-q.bit_count(),q));assert qs[0].bit_count()==6
        for c in squares(a):
            cm=sum(1<<v for v in c);cl=[a[v]&~cm for v in c];base=[(1<<v)|(1<<c[(i+1)%4]) for i,v in enumerate(c)];sups=[[base[i]|cl[j] for j in range(4)] for i in range(4)]
            def independent(s):return all(not (a[v]&s) for v in range(n) if s>>v&1)
            opts=[[j for j,s in enumerate(row) if independent(s)] for row in sups];choices=list(product(*opts));assert len(choices)==16;stats['squares']+=1;stats['triangle_safe']+=len(choices)
            bad={h:set() for h in choices};one={}
            for q in qs:
                size=q.bit_count();hits={h for h in choices if size+sum(not(q&sups[i][j]) for i,j in enumerate(h))>7}
                for h in hits:bad[h].add(size)
                for j in range(4):
                    if j not in one and {h for h in choices if j not in h}<=hits:one[j]=q
            win=[h for h in choices if not bad[h]];assert set(win)=={tuple((i+k)%4 for i in range(4)) for k in (2,3)}
            for h,f in bad.items():at[max(f,default=0)]+=1
            for j in range(4):
                force[one[j].bit_count() if j in one else 0]+=1
                # Four private sites from the class and vertices with no corner contact.
                outside=((1<<n)-1)&~(cm|cl[0]|cl[1]|cl[2]|cl[3]);w=cl[j]
                if w.bit_count()==3:
                    w=one[j];assert w&~(cl[j]|outside)==0
                assert w.bit_count()==4 and independent(w) and all(not(w&sups[i][k]) for i in range(4) for k in range(4) if k!=j)
            if ex is None:ex=dict(record=idx,corners=c,classes=[[v for v in range(n) if m>>v&1] for m in cl],witness_for_omitted_class={j:[v for v in range(n) if q>>v&1] for j,q in one.items()},solutions=win)
    out=dict(scope='One whole contact class per side, reuse permitted, zero-based vertex labels. Largest old blue set witnessing each rejection; zero denotes no rejection.',stats=stats,by_largest_witness=at,one_uniform_witness_per_omitted_class=force,example=ex);print(out);(D.parent/'ramsey_square_coverage_assignment.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
