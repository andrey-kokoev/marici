"""Exhaustive restricted triangle-lattice certificates at six points."""
import json
from pathlib import Path
from itertools import combinations
from collections import Counter
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
p=json.loads(Path('research/nima/results/zero_support.json').read_text())
assert p['status']=='passed'
T=[set(tuple(e) for e in t) for t in p['triangulations']]
boundary={tuple(sorted((i,(i+1)%6))) for i in range(6)}
Q=list(combinations(range(6),3))
features=[{j for j,q in enumerate(Q) if all(e in t|boundary for e in combinations(q,2))} for t in T]
rect=p['rectangles']
def factors(M):
    d=smith_normal_form(M,domain=ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]
counts=Counter();defects=[];total=0
for mask in range(1<<14):
    bit=lambda i:(mask>>i)&1
    if not all(bit(a)*bit(b)==bit(c)*bit(d) for a,b,c,d in rect):continue
    total+=1
    ids=[i for i in range(14) if bit(i)]
    allowed=set().union(*(features[i] for i in ids))
    assert [i for i,f in enumerate(features) if f<=allowed]==ids
    B=Matrix([[int(j in features[i]) for j in sorted(allowed)] for i in ids]) if ids else Matrix.zeros(0,0)
    rows=[]
    for a,b,c,d in rect:
        if all(bit(i) for i in [a,b,c,d]):
            rows.append([int(i==a)+int(i==b)-int(i==c)-int(i==d) for i in ids])
    R=Matrix(rows) if rows else Matrix.zeros(0,len(ids))
    assert R*B==Matrix.zeros(len(rows),len(allowed))
    bf=factors(B);rf=factors(R)
    if len(bf)+len(rf)!=len(ids) or any(x!=1 for x in rf):defects.append(mask)
    counts[(len(ids),len(bf),len(rf),all(x==1 for x in bf))]+=1
assert total==4000 and not defects
# Nonprimitive replacement preserves rank but must fail the saturation criterion.
assert factors(Matrix([[2,-2]]))==[2]
result={'status':'passed','supports_checked':total,'relation_defects':defects,'strata':[{'support_size':k[0],'image_rank':k[1],'local_rank':k[2],'image_smith_all_one':k[3],'count':v} for k,v in sorted(counts.items())],'nonprimitive_control_rejected':True,'scope':'Six-point strata only; local row saturation and rank equality certify full relation lattice, not merely rational equality.'}
Path('research/nima/results/supported_coefficients.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','supports_checked':total,'relation_defects':len(defects),'all_image_smith_one':all(k[3] for k in counts),'stratum_types':len(counts)}))
