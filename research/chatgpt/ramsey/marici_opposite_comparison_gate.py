#!/usr/bin/env python3
"""Exact conditional chiral comparison/reflection audit for the Marici 4-node seed.

Original directed occurrences are kept distinct. The 12 triangular 2-cells
are a CONDITIONAL admission policy, not a theorem of NativeTableRules.agda.
This script checks the group and chain presentations and a pointed-permutation
countermodel to automatic seam contraction.
"""
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.free_groups import free_group
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

V='ABCD'
s={'A':'B','B':'A','C':'D','D':'C'}
def par(p):
    nums=[V.index(z) for z in p]
    return sum(nums[i]>nums[j] for i in range(4) for j in range(i+1,4))%2
A4=[dict(zip(V,p)) for p in itertools.permutations(V) if par(p)==0]
chiral=sorted({tuple(g[v] for v in 'ABC') for g in A4})
assert len(chiral)==12 and tuple('ADB') in chiral
opp=[t for t in itertools.permutations(V,3) if t not in chiral]
assert set(chiral)|set(opp)==set(itertools.permutations(V,3))

arcs=tuple((u,v) for u in V for v in V if u!=v)
def refl(t):return tuple(s[v] for v in t)
def orb(t):return min(t,refl(t))
q_arcs=sorted({orb(e) for e in arcs})
q_faces=sorted({orb(f) for f in chiral})
assert len(q_arcs)==6 and len(q_faces)==6
assert all(refl(f)!=f for f in chiral)
assert all(refl(e)!=e for e in arcs)


def boundaries(vtypes,edges,faces,q=False):
    d1=sp.zeros(len(vtypes),len(edges))
    for i,(u,v) in enumerate(edges):
        if q:
            u,v=('X' if a in 'AB' else 'Y' for a in (u,v))
        d1[vtypes.index(u),i]-=1
        d1[vtypes.index(v),i]+=1
    d2=sp.zeros(len(edges),len(faces))
    for j,(u,v,w) in enumerate(faces):
        for e,c in (((u,v),1),((v,w),1),((u,w),-1)):
            d2[edges.index(orb(e) if q else e),j]+=c
    assert d1*d2 == sp.zeros(len(vtypes),len(faces))
    d=smith_normal_form(d2,domain=ZZ)
    snf=[abs(int(d[i,i])) for i in range(min(d.rows,d.cols)) if d[i,i]]
    r1=d1.rank(); r2=len(snf)
    return {
        'vertices':len(vtypes),'directed_edges':len(edges),'comparison_faces':len(faces),
        'rank_d1':int(r1),'rank_d2':r2,
        'snf_d2':snf,
        'H1_free_rank':len(edges)-r1-r2,
        'H1_torsion':[n for n in snf if n>1],
        'H2_free_rank':len(faces)-r2,
    }

# A reflection-equivariant opposite face orbit consists of CAD and DBC.
alpha=('C','A','D')
assert alpha in opp and refl(alpha)==('D','B','C')
up_before=boundaries(tuple(V),arcs,chiral)
up_after=boundaries(tuple(V),arcs,chiral+[alpha,refl(alpha)])
q_before=boundaries(('X','Y'),q_arcs,q_faces,True)
q_after=boundaries(('X','Y'),q_arcs,q_faces+[orb(alpha)],True)
assert (up_before['H1_torsion'],up_before['H2_free_rank'])==([2],3)
assert (q_before['H1_torsion'],q_before['H2_free_rank'])==([4],1)
assert (up_after['H1_torsion'],up_after['H2_free_rank'])==([],5)
assert (q_after['H1_torsion'],q_after['H2_free_rank'])==([2],2)

# Independent nonabelian fundamental-group check via finite presentations.
def group_order(edges,faces,edge_key,tree):
    tree=set(tree)
    gens=[e for e in edges if e not in tree]
    F,*x=free_group(','.join('x'+''.join(e) for e in gens))
    pick=dict(zip(gens,x))
    def edge(u,v):return pick.get(edge_key((u,v)),F.identity)
    rels=[edge(u,v)*edge(v,w)*edge(u,w)**-1 for u,v,w in faces]
    return FpGroup(F,rels).order()
up_order=group_order(arcs,chiral,lambda e:e,{('A','B'),('A','C'),('A','D')})
q_order=group_order(q_arcs,q_faces,orb,{('A','C')})
q_order_after=group_order(q_arcs,q_faces+[orb(alpha)],orb,{('A','C')})
up_order_after=group_order(arcs,chiral+[alpha,refl(alpha)],lambda e:e,{('A','B'),('A','C'),('A','D')})
assert [up_order,q_order,up_order_after,q_order_after]==[2,4,1,2]

# Use quotient 1-cell gauge with AC a spanning tree. The edges carry powers
# of U=(1 2 3 4) in a 5-element fiber. The distinguished mark 0 is fixed.
exps={
    ('A','B'):1, ('A','C'):0, ('A','D'):-1,
    ('C','A'):2, ('C','B'):-1, ('C','D'):-1,
}
def exp(u,v):return exps[orb((u,v))]%4
assert all((exp(u,v)+exp(v,w)-exp(u,w))%4==0 for u,v,w in chiral)
assert all(exp(*refl((u,v)))==exp(u,v) for u,v in arcs)
assert (exp('C','A')+exp('A','D'))%4==1
assert (sum(exp(x,y) for x,y in [('C','A'),('A','B'),('B','A'),('A','D')]))%4==3
assert (exp('A','B')+exp('B','A'))%4==2
assert (exp('C','A')+exp('A','D')-exp('C','D'))%4==2
assert (exp('D','B')+exp('B','C')-exp('D','C'))%4==2

U=(0,2,3,4,1)
def compose(a,b):return tuple(a[b[i]] for i in range(5))
def power(u,n):
    out=tuple(range(5))
    for _ in range(n%4):out=compose(u,out)
    return out
assert power(U,4)==tuple(range(5)) and power(U,2)!=tuple(range(5))
all_maps={e:power(U,exp(*e)) for e in arcs}
assert all(f[0]==0 for f in all_maps.values())
for u,v,w in chiral:
    assert compose(all_maps[(v,w)],all_maps[(u,v)])==all_maps[(u,w)]

def composite(word):
    cur=tuple(range(5))
    for edge in word:
        cur=compose(all_maps[edge],cur)
    return cur
p0=[('C','A'),('A','D')]
p1=[('C','A'),('A','B'),('B','A'),('A','D')]
h=[('A','B'),('B','A')]
assert composite(p0)==power(U,1)
assert composite(p1)==power(U,3)
assert composite(h)==power(U,2)
assert composite(p0)[0]==composite(p1)[0]==0
assert composite(p0)!=composite(p1)
# Compare with the all-identity model; the same chiral identities still hold.
trivial={e:tuple(range(5)) for e in arcs}
assert all(compose(trivial[(v,w)],trivial[(u,v)])==trivial[(u,w)] for u,v,w in chiral)

out={
    'status':'passed',
    'scope':'Conditional orientation-preserving comparison CW complex; native admission NOT proved',
    'seed_reflection':'(A B)(C D)',
    'quotient_edges':[''.join(e) for e in q_arcs],
    'quotient_faces':[''.join(t) for t in q_faces],
    'before_opposite_comparison':{
        'chiral_cover':up_before,'reflection_quotient':q_before,
        'fundamental_group_orders':{'chiral_cover':int(up_order),'reflection_quotient':int(q_order)},
        'fundamental_groups':{'chiral_cover':'C2','reflection_quotient':'C4'},
        'generator_lift':'quotient AB squared lifts to AB BA',
    },
    'after_reflection_orbit_of_opposite_comparison':{
        'opposite_faces':[''.join(alpha),''.join(refl(alpha))],
        'chiral_cover':up_after,'reflection_quotient':q_after,
        'fundamental_group_orders':{'cover':int(up_order_after),'quotient':int(q_order_after)},
        'fundamental_groups':{'cover':'trivial','quotient':'C2'},
    },
    'pointed_countermodel':{
        'carrier_size':5,'marked_value':0,
        'common_permutation_generator':'U=(1 2 3 4) with 0 fixed',
        'edge_exponents_mod4':{''.join(e):exp(*e) for e in arcs},
        'seed_oriented_comparison_faces_satisfied_as_full_maps':len(chiral),
        'reflection_equivariant':True,
        'p0_action':'U', 'p1_action':'U^3','seam_action':'U^2',
        'p0_and_p1_agree_on_mark':True,
        'p0_and_p1_differ_as_maps':True,
        'opposite_comparison_requires_extra_full_map_equality':True,
        'all_identity_model_also_satisfies_seed_oriented_comparisons':True,
    },
    'not_established':['native generation of the 12 chiral comparison 2-cells',
                       'equivalence of native pointed fillers with homotopies of path histories',
                       'Ramsey admissibility derived from composition'],
}
path=Path('/mnt/data/marici_opposite_comparison_gate_results.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
