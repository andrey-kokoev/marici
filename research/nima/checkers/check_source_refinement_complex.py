"""Source-valence refinement complex versus Feynman evaluation."""
import runpy,json
from pathlib import Path
from sympy import Matrix,zeros,prod,factor,simplify
z=runpy.run_path('research/nima/checkers/check_quartic_contact_source.py')
T,D,faces,s,g,h=(z[k] for k in ('T','D','faces','s','g','h'))
E=sorted([d for d in D if sum(len(f)==4 for f in faces(d))==1],key=lambda d:sorted(d))
ends=[sorted(i for i,t in enumerate(T) if d<=t) for d in E]
assert len(E)==21 and all(len(x)==2 for x in ends)
d1=zeros(14,21)
for j,(a,b) in enumerate(ends):d1[a,j]=-1;d1[b,j]=1
squares=sorted([d for d in D if sum(len(f)==4 for f in faces(d))==2],key=lambda d:sorted(d))
def boundary(d):
    es=[j for j,e in enumerate(E) if d<=e];vs=sorted({v for j in es for v in ends[j]})
    out=zeros(21,1);v=vs[0];used=set()
    while len(used)<len(es):
        j=next(j for j in es if j not in used and v in ends[j]);a,b=ends[j]
        out[j]=1 if v==a else -1;v=b if v==a else a;used.add(j)
    assert v==vs[0];assert d1*out==zeros(14,1)
    return out
d2=Matrix.hstack(*(boundary(d) for d in squares));assert d2.shape==(21,3)
assert d1*d2==zeros(14,3)
pentagons=[frozenset([e]) for e in s if sorted(len(f) for f in faces(frozenset([e])))==[3,5]]
P=Matrix.hstack(*(boundary(d) for d in pentagons));assert P.shape==(21,6)
full=d2.row_join(P)
assert (d1.rank(),d2.rank(),full.rank())==(13,3,8)
# Source amplitude does not annihilate even a single ordinary edge boundary.
a,b=ends[0];ev=[g**4/prod(s[e] for e in t) for t in T]
ordinary=factor(ev[b]-ev[a]);assert ordinary!=0
x=next(iter(T[a]-E[0]));y=next(iter(T[b]-E[0]))
assert simplify(s[y]*ev[b]-s[x]*ev[a])==0
# Matching this common value to the quartic graph requires lambda/g^2.
contact=g**2*h/prod(s[e] for e in E[0])
assert simplify(contact-h/g**2*s[x]*ev[a])==0
out={'status':'passed','chain_dimensions':[14,21,3],'boundary_ranks':[13,3],'H1_dimension_over_Q':5,'pentagon_cells_not_in_source_valence':6,'rank_with_pentagons':8,'ordinary_edge_evaluation_defect':str(ordinary),'weighted_edge_cancellation':True,'quartic_matching_factor':'lambda/g^2 (requires g nonzero)','scope':'Combinatorial source-valence complex is not an admitted BRST/BV differential. Pentagon filling tests a declared enlargement, not a derived quintic interaction or a homotopy for the weight quadric.'}
Path('research/nima/results/source_refinement_complex.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
