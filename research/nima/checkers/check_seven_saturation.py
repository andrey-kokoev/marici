"""Coordinate saturation via homogeneous grevlex bases, last variable varied."""
import json
from pathlib import Path
from itertools import combinations
p=json.loads(Path('research/nima/results/seven_groebner.json').read_text());assert p['status']=='complete'
base=[tuple(map(tuple,g)) for g in p['basis']]
records=[]
class Cap(Exception):pass
for last in range(42):
    order=[i for i in range(42) if i!=last]+[last]
    def key(m):return (sum(m),tuple(-m[i] for i in reversed(order)))
    def orient(a,b):return (a,b) if key(a)>key(b) else (b,a)
    G=[orient(a,b) for a,b in base];steps=[0]
    def nf(m):
        while True:
            for a,b in G:
                if all(x>=y for x,y in zip(m,a)):
                    m=tuple(x-y+z for x,y,z in zip(m,a,b));steps[0]+=1
                    if steps[0]>10000:raise Cap()
                    break
            else:return m
    pairs=list(combinations(range(len(G)),2));cursor=0;complete=False
    try:
        while cursor<len(pairs):
            if len(G)>=200 or cursor>=20000:raise Cap()
            i,j=pairs[cursor];cursor+=1;a,b=G[i];c,d=G[j]
            if not any(x and y for x,y in zip(a,c)):continue
            l=tuple(max(x,y) for x,y in zip(a,c))
            v=nf(tuple(x-y+z for x,y,z in zip(l,a,b)))
            w=nf(tuple(x-y+z for x,y,z in zip(l,c,d)))
            if v!=w:
                k=len(G);G.append(orient(v,w));pairs.extend((i,k) for i in range(k))
        complete=True
    except Cap:pass
    # If no leading term involves the last variable, it is regular modulo I.
    regular=complete and all(a[last]==0 for a,b in G)
    records.append({'last_variable':last,'complete':complete,'basis_size':len(G),'pairs':cursor,'steps':steps[0],'regular_certificate':regular})
    if not regular:break
result={'status':'passed' if len(records)==42 and all(r['regular_certificate'] for r in records) else 'partial','records':records,'scope':'Grevlex bases homogeneous; leading terms omit the last variable, certifying I:x_i=I. No assertion for an unfinished order.'}
Path('research/nima/results/seven_saturation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'orders_checked':len(records),'max_basis':max(r['basis_size'] for r in records),'last_record':records[-1]}))
