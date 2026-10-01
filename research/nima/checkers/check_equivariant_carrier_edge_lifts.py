"""Exhaustive S4-equivariant lifts of ordered carrier edges to permutations.

Conditional source semantics: a lift transports i to j, and relabelling acts
by conjugation. These requirements are not inferred from arrow labels alone.
"""
from itertools import permutations, product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/equivariant-carrier-edge-lifts.json'
out.unlink(missing_ok=True)
V=tuple(range(4)); G=tuple(permutations(V)); identity=V
edges=tuple((i,j) for i in V for j in V if i!=j)

def compose(b,a): return tuple(b[a[i]] for i in V)
def inverse(a): return tuple(a.index(i) for i in V)
def conjugate(p,a): return compose(compose(p,a),inverse(p))
def swap(i,j): return tuple(j if k==i else i if k==j else k for k in V)

base=(0,1)
H=tuple(p for p in G if (p[0],p[1])==base)
assert len(H)==2
transporter=tuple(g for g in G if g[0]==1)
assert len(transporter)==6
seeds=tuple(g for g in transporter if all(conjugate(h,g)==g for h in H))
assert len(seeds)==2
single=swap(0,1); double=compose(single,swap(2,3))
assert set(seeds)=={single,double}

profiles={}
for name,seed in (('endpoint_swap',single),('double_swap',double)):
    lift={}
    for i,j in edges:
        choices={conjugate(p,seed) for p in G if (p[0],p[1])==(i,j)}
        assert len(choices)==1
        lift[i,j]=choices.pop()
    for (i,j),g in lift.items():
        assert g[i]==j and lift[j,i]==inverse(g)
        for p in G:
            assert lift[p[i],p[j]]==conjugate(p,g)
    triangle_holonomies=[]
    for i,j,k in permutations(V,3):
        loop=compose(lift[k,i],compose(lift[j,k],lift[i,j]))
        assert loop[i]==i
        triangle_holonomies.append(loop)
        if name=='endpoint_swap':
            assert loop==swap(j,k) and loop!=identity
            assert all(lift[i,j][v]==v for v in V if v not in (i,j))
        else:
            assert loop==identity
            assert all(lift[i,j][v]!=v for v in V)
    retained_triangles=[(i,j,k) for i,j,k in permutations(V,3)
                        if (0,1) not in ((i,j),(j,k),(k,i))]
    assert len(retained_triangles)==18
    for i,j,k in retained_triangles:
        loop=compose(lift[k,i],compose(lift[j,k],lift[i,j]))
        assert (loop==identity)==(name=='double_swap')
    generated={identity}
    while True:
        expanded=generated|{compose(g,h) for g in lift.values() for h in generated}
        if expanded==generated: break
        generated=expanded
    if name=='double_swap':
        assert len(generated)==4
        # A chosen root supplies frames; all edges are their endpoint ratios.
        frames={i:identity if i==0 else lift[0,i] for i in V}
        for i,j in edges: assert lift[i,j]==compose(frames[j],inverse(frames[i]))
    else:
        assert len(generated)==24
        # Based triangle holonomies generate the full stabilizer of that point.
        based={compose(lift[k,0],compose(lift[j,k],lift[0,j]))
               for j,k in permutations((1,2,3),2)}
        closure={identity}
        while True:
            expanded=closure|{compose(g,h) for g in based for h in closure}
            if expanded==closure: break
            closure=expanded
        assert closure=={p for p in G if p[0]==0} and len(closure)==6
    profiles[name]={'seed':list(seed),'generated_group_order':len(generated),
                    'nonidentity_triangle_holonomies':sum(g!=identity for g in triangle_holonomies),
                    'triangle_count':24,'triangles_surviving_reference_edge_exclusion':18}

# Both transports agree on the requested endpoint. A loop's basepoint readout
# misses the curved lift; observing another labelled state separates it.
loop=swap(1,2)
assert loop[0]==identity[0] and loop[1]!=identity[1]
assert sum(loop[i]==i for i in V)==2

result={
 'status':'passed',
 'classification':'two_equivariant_permutation_edge_lifts_flatness_separated_by_spectator_action',
 'obligation':'conditional source-operation classification before reference attachment',
 'stratum':'Four labelled states; degree-zero S4 transport i->j; full conjugation equivariance; no physical implementation assumed',
 'checks':{'transporter_size':6,'equivariant_lift_count':2,
           'all_relabellings_checked':True,'inverse_edges_checked':True,
           'basepoint_only_loop_observation_insufficient':True},
 'profiles':profiles,
 'selection_boundary':{'spectators_fixed':'endpoint swap; nontrivial triangle holonomy',
                       'path_independent_endpoint_transport':'double swap; spectators exchanged'},
 'unsupported':['identifying carrier arrows with active permutation operations',
                'physical authorization of either spectator policy',
                'adapter to the shared-leg DG witnesses and rung4 metric'],
 'next_constructor':'Determine whether an elementary source arrow preserves the two nonparticipating labels or exchanges them; do not choose using the desired flatness.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
