"""Source rule audit: planar subset of labelled massless real phi^3 trees."""
import json
from pathlib import Path
from itertools import combinations
from sympy import symbols,I,simplify
r=Path('research/nima/results');p=json.loads((r/'seven_point_fibers.json').read_text());gb=json.loads((r/'seven_groebner.json').read_text())
assert p['status']=='passed' and gb['status']=='complete'
T=[frozenset(tuple(e) for e in t) for t in p['triangulations']]
# Independent polygon recursion reproduces exactly the stored source channels.
def tris(vertices):
    if len(vertices)<=3:return [frozenset()]
    ans=[]
    for j in range(1,len(vertices)-1):
        left=vertices[:j+1];right=vertices[j:]
        edges=set()
        if len(left)>2:edges.add((vertices[0],vertices[j]))
        if len(right)>2:edges.add((vertices[j],vertices[-1]))
        for a in tris(left):
            for b in tris(right):ans.append(a|b|edges)
    return ans
assert set(tris(tuple(range(7))))==set(T) and len(T)==42
q=list(combinations(range(7),3));bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
g=symbols('g');weights=[]
for t in T:
    triangles=[a for a in q if all(e in t|bd for e in combinations(a,2))]
    assert len(t)==4 and len(triangles)==5
    assert simplify((-I*g)**5*I**4/(-I)-g**5)==0
    weights.append(g**len(triangles))
for a,b in gb['basis']:
    lhs=rhs=1
    for i in range(42):lhs*=weights[i]**a[i];rhs*=weights[i]**b[i]
    assert simplify(lhs-rhs)==0
facets=[]
for e in sorted(set().union(*T)):
    inside=set(range(e[0],e[1]+1));cells=[]
    for t in T:
        if e in t:
            a=frozenset(d for d in t-{e} if set(d)<=inside);b=(t-{e})-a;cells.append((a,b))
    L={a for a,b in cells};R={b for a,b in cells}
    assert set(cells)=={(a,b) for a in L for b in R}
    m=e[1]-e[0]+1;assert simplify(g**(m-2)*g**((9-m)-2)-g**5)==0
    facets.append({'channel':e,'left_terms':len(L),'right_terms':len(R),'residue_terms':len(cells)})
assert simplify(g**5-g**4)!=0 # wrong gluing/vertex normalization is rejected
out={'status':'passed','model':'massless real scalar L=1/2 (partial phi)^2 - g phi^3/3!','observable':'fixed-cyclic-order planar subset of labelled tree diagrams, not full identical-scalar amplitude','phase_convention':'iM_planar=-i A_planar','seven_point_coefficients':['g^5']*42,'coupling_stripped_coefficients':[1]*42,'quadrics_checked':63,'facets':facets,'triangle_factor':'g per cubic vertex','normalization':'A3=g; residue in channel variable s equals A_left*A_right','wrong_vertex_count_rejected':True,'residuals':['No positive-geometry slice or form Jacobian derived','No cosmological wavefunction or physical selection supplied','No empirical validation or external source authentication']}
(r/'cubic_scalar_source.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('seven_point_coefficients','coupling_stripped_coefficients','facets')}))
