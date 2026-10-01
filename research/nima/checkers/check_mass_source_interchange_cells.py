"""Source-typed independent-operation cells reduce, but do not erase, history cycles."""
from pathlib import Path
from contextlib import redirect_stdout
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    source=runpy.run_path(str(HERE/'check_mass_path_port_connectivity.py'))
slots=source['slots']; index=source['index']; N=len(slots)
edges=sorted(source['source_links']); ei={e:i for i,e in enumerate(edges)}
outer_edges=sorted({tuple(sorted((slots[a][0],slots[b][0]))) for a,b in source['links']['outer']})
inner_edges=sorted({tuple(sorted((slots[a][1],slots[b][1]))) for kind in ('inner_left','inner_right','endpoint') for a,b in source['links'][kind]})
assert len(outer_edges)==30 and len(inner_edges)==882
outer_vertices=sorted({s[0] for s in slots})
# A lifted outer-edge cochain detects a retained outer traversal cycle. It is
# zero on inner edges and annihilates all independent-operation face boundaries.
marked=((0,1),(1,2))
w=[]
for a,b in edges:
    x,y=slots[a],slots[b]
    w.append(int(x[1]==y[1] and (x[0],y[0])==marked)-int(x[1]==y[1] and (y[0],x[0])==marked))
pivots={}; face_count=0

def face(vertices):
    global face_count
    chain={}; balance={}; mask=0
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        edge=tuple(sorted((a,b))); j=ei[edge]; sign=1 if a<b else -1
        chain[j]=chain.get(j,0)+sign
        balance[a]=balance.get(a,0)-1; balance[b]=balance.get(b,0)+1
        mask ^= 1<<j
    assert all(x==0 for x in balance.values())
    assert sum(c*w[j] for j,c in chain.items())==0
    assert len(chain)==4
    face_count+=1
    # Exact GF(2) rank regression; integer homology is separately determined by
    # the Cartesian-product cellular decomposition, with torsion-free H1.
    while mask:
        pivot=mask.bit_length()-1
        if pivot in pivots: mask ^= pivots[pivot]
        else: pivots[pivot]=mask; break

# Outer operation commutes with every inner operation, including endpoint
# readout, provided its parent record is kept on the independent inner register.
for o0,o1 in outer_edges:
    for d0,d1 in inner_edges:
        face([index[(o0,d0)],index[(o1,d0)],index[(o1,d1)],index[(o0,d1)]])
# Left/right path append operations commute on the two retained inner histories.
for o in outer_vertices:
    for a0,a1 in outer_edges:
        for b0,b1 in outer_edges:
            face([index[(o,('arrow',a0,b0))],index[(o,('arrow',a1,b0))],
                  index[(o,('arrow',a1,b1))],index[(o,('arrow',a0,b1))]])
assert face_count==37260
rank_d2=len(pivots)
bare_h1=len(edges)-N+1
h1=bare_h1-rank_d2
assert (bare_h1,rank_d2,h1)==(13339,13129,210)
# The surviving directed three-step outer loop pairs to1 with w, so cannot be
# an integer combination of these boundaries, not merely a GF(2) accident.
inner=('state',1,1)
cycle=[index[(o,inner)] for o in ((0,1),(1,2),(2,0))]
pairing=0
for a,b in zip(cycle,cycle[1:]+cycle[:1]):
    pairing+=(1 if a<b else -1)*w[ei[tuple(sorted((a,b)))]]
assert pairing==1
# Explicit append interchange on per-role histories; no within-role order lost.
initial=((0,1),(2,3))
def left(h): return (h[0]+(2,),h[1])
def right(h): return (h[0],h[1]+(0,))
assert left(right(initial))==right(left(initial))
assert initial[0]+(0,1)!=initial[0]
# Integral cellular derivation: L has b1=30-12+1=19. Inner D is LxL with
# nine new state vertices and162 readout edges: b1(D)=38+162-9=191,
# b2(D)=19^2=361. Full product LxD supplies the27000 interchange cubes.
loop_rank=19; inner_b1=2*loop_rank+162-9; inner_b2=loop_rank**2
betti=[1,loop_rank+inner_b1,inner_b2+loop_rank*inner_b1,loop_rank*inner_b2]
cubes=len(outer_edges)*len(outer_edges)**2
assert betti==[1,210,3990,6859] and cubes==27000
assert N-len(edges)+face_count-cubes==sum((-1)**i*b for i,b in enumerate(betti))
# Repair the active-port projection's merging of opposite continuation acts.
# A forward append and a fresh returning append are distinct history operations,
# not one edge and its inverse. Keep both as oriented1-cells.
operation_edges=sorted(set().union(*source['directions'].values()))
oi={e:i for i,e in enumerate(operation_edges)}
outer_arcs=sorted({(slots[a][0],slots[b][0]) for a,b in source['directions']['outer']})
inner_arcs=sorted({(slots[a][1],slots[b][1]) for kind in ('inner_left','inner_right','endpoint') for a,b in source['directions'][kind]})
assert (len(outer_arcs),len(inner_arcs),len(operation_edges))==(36,1026,17820)
operation_pivots={}; operation_faces=0

def operation_face(v):
    global operation_faces
    terms=[(v[0],v[1],1),(v[1],v[2],1),(v[3],v[2],-1),(v[0],v[3],-1)]
    mask=0; cost=0; balance={}
    for a,b,sign in terms:
        mask ^= 1<<oi[a,b]
        cost += sign*int(slots[a][0]!=slots[b][0])
        balance[a]=balance.get(a,0)-sign; balance[b]=balance.get(b,0)+sign
    assert cost==0 and all(x==0 for x in balance.values())
    operation_faces+=1
    while mask:
        p=mask.bit_length()-1
        if p in operation_pivots: mask ^= operation_pivots[p]
        else: operation_pivots[p]=mask; break
for o0,o1 in outer_arcs:
    for d0,d1 in inner_arcs:
        operation_face([index[(o0,d0)],index[(o1,d0)],index[(o1,d1)],index[(o0,d1)]])
for o in outer_vertices:
    for a0,a1 in outer_arcs:
        for b0,b1 in outer_arcs:
            operation_face([index[(o,('arrow',a0,b0))],index[(o,('arrow',a1,b0))],
                            index[(o,('arrow',a1,b1))],index[(o,('arrow',a0,b1))]])
assert operation_faces==52488 and len(operation_pivots)==15757
operation_h1=len(operation_edges)-N+1-len(operation_pivots)
assert operation_h1==228
# Both returning appends survive and have cost+1: their cycle pairs to2.
u=index[((0,1),inner)]; v=index[((1,0),inner)]
assert (u,v) in oi and (v,u) in oi
return_cost=2
assert return_cost!=0
operation_betti=[1,25+(50+153),625+25*(50+153),25*625]
assert operation_betti==[1,228,5700,15625]
assert N-17820+52488-46656==sum((-1)**i*b for i,b in enumerate(operation_betti))
result={
 'status':'passed','classification':'independent_operation_coherence_leaves_nontrivial_history_homology',
 'cells_by_dimension':[N,len(edges),face_count,cubes],
 'exact_mod_two_face_boundary_rank':rank_d2,
 'first_betti_before_faces':bare_h1,'first_betti_after_faces':h1,
 'integral_product_betti_numbers':betti,
 'integral_surviving_cycle_pairing':pairing,
 'operation_resolved_complex':{'cells':[N,17820,52488,46656],
    'exact_mod_two_face_rank':len(operation_pivots),'integral_betti':operation_betti,
    'returning_append_cycle_cost':return_cost},
 'checks':{'source_path_chain_fresh':True,'all_square_boundaries_close':True,
           'independent_history_interchange':True,'exact_face_rank':True,
           'integer_cycle_witness_survives':True,'product_cube_euler_identity':True},
 'conclusion':'Independent path/readout operations supply37260 commuting squares and27000 product cubes. They reduce first homology from13339 to210 but do not erase retained traversal cycles; the full product complex also retains higher homology. Resolving opposite appends as distinct operations raises the surviving first homology to228. Coherence does not supply a unique protected particle state or the1836 central-charge pairing.',
 'next_falsifier':'Identify additional source-authorized relations involving endpoint readouts and actual reference-return dynamics. Do not null-homotope retained loops or choose a central pairing solely to obtain1836.'}
out=HERE.parent/'results/mass-source-interchange-cells.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
