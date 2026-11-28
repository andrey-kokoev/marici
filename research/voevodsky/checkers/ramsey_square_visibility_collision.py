"""Matched address-only control. Permit arbitrary omissions from the successful contact transport, not just whole-class assignment. Compare up to external relabeling and square symmetries."""
from ramsey_excel_corner_predecessor_readout import squares,CAT,D,decode,check
from itertools import combinations,product
import json

def family(a,c):
    n=len(a);C=sum(1<<i for i in c);cls=[a[i]&~C for i in c];I=[0]
    for i,g in enumerate(a):I.extend([s|1<<i for s in I if not s&g]);
    qs={k:[q for q in I if q.bit_count()==k] for k in range(4,7)};cert={};full=set();smalls=[]
    def shape(sizes):return min(tuple(sizes[(b+d*j)%4] for j in range(4)) for b in range(4) for d in (1,-1))
    for off in (2,3):
        rows=[(1<<v)|(1<<c[(j+1)%4])|cls[(j+off)%4] for j,v in enumerate(c)];opts=[];mark=shape([(s&~C).bit_count() for s in rows]);full.add(mark)
        for j,s in enumerate(rows):
            ext=s&~C;ls=[];sub=ext
            while True:
                t=(s&C)|sub
                if all(any((u if h!=j else t)&q for h,u in enumerate(rows) if h in ix) for k in (6,5,4) for ix in combinations(range(4),8-k) for q in qs[k]):ls.append(t)
                if not sub:break
                sub=(sub-1)&ext
            opts.append(ls)
        for rs in product(*opts):
            key=shape([(s&~C).bit_count() for s in rs]);
            if key in cert:continue
            g=a[:]+[0]*5
            for i,s in enumerate(rs,n):
                g[i]=s|1<<(n+4);g[-1]|=1<<i
                for j in range(n):g[j]|=(s>>j&1)<<i
            if check(g,(1<<(n+5))-1,3,8):cert[key]=rs
        smalls.append(list(map(len,opts)))
    return full,cert,smalls

def audit():
    lines=(CAT/'r37_22.g6').read_text().splitlines();matched={}
    for idx,l in enumerate(lines,1):
        a=decode(l)
        for c in squares(a):
            sizes=tuple(sorted((a[v]&~sum(1<<j for j in c)).bit_count() for v in c));matched.setdefault(sizes,(idx,a,c))
    assert len(matched)==2;reports=[];common=None
    for key,(idx,a,c) in sorted(matched.items()):
        full,cert,opts=family(a,c);common=set(cert) if common is None else common&cert.keys();reports.append(dict(record_one_based=idx,c=c,sorted_class_sizes=key,whole_shapes=sorted(full),legal_subshapes=[dict(shape=k,rows=rs) for k,rs in sorted(cert.items())],single_row_options=opts))
    out=dict(reports=reports,shared=sorted(common));print([(r['record_one_based'],r['c'],r['whole_shapes'],len(r['legal_subshapes'])) for r in reports],sorted(common));(D.parent/'ramsey_square_visibility_collision.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
