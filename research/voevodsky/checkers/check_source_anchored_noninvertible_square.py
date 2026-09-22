"""Actual seven-reading -> two-vacuum comparison in four tower frames.

Source anchors, noninvertible maps, affine fibers and reconstructive
residuals are checked together. This is a finite filtered vector-space
comparison, not a splitting of the globally nonsplit observer extension.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import runpy,json,copy
ROOT=Path(__file__).resolve().parents[3]
t=runpy.run_path(str(ROOT/'research/nima/checkers/check_residual_tower_of_towers.py'))
a=t['a'];mm=t['mm'];inv=t['inv'];eye=t['eye'];apply=a.apply
f=a.f
D=runpy.run_path(str(ROOT/'research/voevodsky/certificates/reconstruct_seven_dimensional_ideal_slice.py'))
shapes=[tuple(('e',u,v,0) for u,v in seams) for seams in D['SEAMS']]
def transpose(M):return [list(row) for row in zip(*M)]
def rank(M):return len(a.rref(M,len(M[0]))[1])
def source(coefficients):return {(D['path'](b),(0,)*6):Q(c) for b,c in enumerate(coefficients) if c}
def readings(col):return [f['vacuum_rows'](0,63,col,len(sh)).get(sh,Q(0)) for sh in shapes]
def add(A,B):return [[x+y for x,y in zip(r,s)] for r,s in zip(A,B)]
def wire(M):return [[str(x) for x in row] for row in M]
# Source coordinates are coefficients on path_b-path_0, b=1..7.
source_basis=[[Q(int(i==b)-int(i==0)) for i in range(8)] for b in range(1,8)]
E=transpose([readings(source(col)) for col in source_basis])
assert rank(E)==7
Z=[[Q(b&mask==mask) for b in range(1,8)] for mask in range(1,8)]
# Concrete lower receiver: two separately acquired primitive vacuum rows.
P=[[Q(j==i) for j in range(7)] for i in range(2)]
W=mm(P,E)
assert rank(W)==2
# Four realization frames from the Nima prototype, restricted to m_empty=0.
frames=[t['sub'](A,range(1,8),range(1,8)) for A in t['frames'](3)]
anchors=[mm(A,Z) for A in frames]
from_readings=[mm(anchor,inv(E)) for anchor in anchors]
projections=[mm(W,inv(anchor)) for anchor in anchors]
comparisons={(i,j):mm(anchors[j],inv(anchors[i])) for i,j in product(range(4),repeat=2)}
squares=0;triangles=0
for i,j in product(range(4),repeat=2):
    F=comparisons[i,j]
    assert mm(F,anchors[i])==anchors[j]
    assert mm(projections[j],F)==projections[i]
    assert mm(projections[i],anchors[i])==W
    assert mm(projections[i],from_readings[i])==P
    squares+=1
for i,j,k in product(range(4),repeat=3):
    assert mm(comparisons[j,k],comparisons[i,j])==comparisons[i,k]
    triangles+=1

# Extend the actual quotient across jet depth by intersecting its row
# space with the available jet rows, not by pretending both vacuum values
# already descend. On the ideal slice the coarse dimensions are 0,0,1,2.
coarse_depth_dimensions=[];depth_frames={};depth_maps={};depth_indices={}
full_frames=t['frames'](3)
for depth in range(4):
    J=[mask for mask in range(1,8) if mask.bit_count()<=depth]
    Zm=[Z[mask-1] for mask in J]
    rz=rank(Zm) if Zm else 0
    intersection=rank(W)+rz-rank(W+Zm)
    assert intersection==[0,0,1,2][depth]
    coarse_depth_dimensions.append(intersection);depth_indices[depth]=J
    B=(mm(W,inv(Z)) if depth==3 else
       [[Q((-1)**mask.bit_count()) for mask in J]] if depth==2 else [])
    depth_frames[depth]=[t['sub'](A,J,J) for A in full_frames]
    depth_maps[depth]=[mm(B,inv(A)) for A in depth_frames[depth]]
all_depth_frame_squares=0;depth_squares=0
for depth in range(4):
    for i,j in product(range(4),repeat=2):
        F=mm(depth_frames[depth][j],inv(depth_frames[depth][i]))
        assert mm(depth_maps[depth][j],F)==depth_maps[depth][i]
        all_depth_frame_squares+=1
    for low in range(depth+1):
        Pmq=[[Q(t0==u0) for u0 in depth_indices[depth]] for t0 in depth_indices[low]]
        C=(eye(coarse_depth_dimensions[depth]) if low==depth else
           [[Q(1),Q(1)]] if (depth,low)==(3,2) else [])
        for i in range(4):
            assert mm(depth_maps[low][i],Pmq)==mm(C,depth_maps[depth][i])
            depth_squares+=1

# A chosen filtered LINEAR section: (u,v) -> (u+v)*mode_3+v*mode_7.
# This is explicit extra data, not a section of the complete source tower.
S=[[Q(x) for x in row] for row in ((1,0),(0,1),(0,0),(1,1),(0,0),(-1,-1),(0,0))]
N=[[Q(i==j+2) for j in range(5)] for i in range(7)]
R=[[Q(x) for x in row] for row in ((0,0,1,0,0,0,0),(-1,-1,0,1,0,0,0),
                                  (0,0,0,0,1,0,0),(1,1,0,0,0,1,0),(0,0,0,0,0,0,1))]
assert mm(P,S)==eye(2) and mm(R,N)==eye(5)
assert mm(P,N)==[[0]*5 for _ in range(2)]
assert mm(R,S)==[[0]*2 for _ in range(5)]
assert add(mm(S,P),mm(N,R))==eye(7)
for i in range(4):
    F=from_readings[i]
    Si,Ni,Ri=mm(F,S),mm(F,N),mm(R,inv(F))
    assert add(mm(Si,projections[i]),mm(Ni,Ri))==eye(7)

# Ideal filtration, inherited from the anchored source, NOT inferred from
# the dimensions of the carriers or from arbitrary frame-coordinate indices.
filtered=[]
for level in (1,2,3):
    modes=[]
    for mask in range(1,8):
        if mask.bit_count()<level:continue
        moments=[Q(int(i==mask)) for i in range(8)]
        coeffs=a.inverse(moments)
        col=source(coeffs)
        for depth in range(level):assert not f['vacuum_rows'](0,63,col,depth)
        modes.append(coeffs[1:])
    U=transpose(modes);Y=mm(E,U);V=mm(W,U)
    dr,cr=rank(Y),rank(V)
    filtered.append({'level':level,'rich_dimension':dr,'coarse_dimension':cr,'kernel_dimension':dr-cr})
    # The section preserves the inherited flag.
    assert rank([*transpose(Y),*transpose(mm(S,V))])==dr
    for i in range(4):
        assert mm(projections[i],mm(anchors[i],U))==V
assert [(r['rich_dimension'],r['coarse_dimension'],r['kernel_dimension']) for r in filtered]==[(7,2,5),(4,2,2),(1,1,0)]

# Compare COMPLETE affine source fibers, not just one compatible witness.
fiber_checks=0;sample_fibers=[]
for visible in ((Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(-1)),(Q(2,3),Q(-5,7))):
    true_fiber=a.solve(W,visible,7)
    rich_fiber=a.image(inv(E),a.solve(P,visible,7))
    assert a.canonical(true_fiber,7)==a.canonical(rich_fiber,7)
    assert len(true_fiber[1])==5
    for i in range(4):
        framed=a.image(inv(anchors[i]),a.solve(projections[i],visible,7))
        assert a.canonical(framed,7)==a.canonical(true_fiber,7)
        fiber_checks+=1
    sample_fibers.append({'vacuum_pair':[str(x) for x in visible],
       'point_in_source_basis':[str(x) for x in true_fiber[0]],
       'kernel_basis_in_source_coordinates':wire(true_fiber[1])})
# Scalar -> pair is evidence refinement, not an invertible coordinate change.
assert len(a.solve([W[0]],[0],7)[1])==6
assert len(a.solve(W,[0,0],7)[1])==5

# Wire protocol: preserve two visible values + five actual residual values.
# No original source or original seven-reading array is hidden in the state.
SECTION='pair12-and-top-filtered-linear-section-v1'
def encode(y):
    return json.loads(json.dumps({'schema':'vacuum-pair-with-residual-v1',
      'model_sha256':D['MODEL_SHA256'],'section':SECTION,
      'visible':[str(x) for x in apply(P,y)],'residual':[str(x) for x in apply(R,y)]}))
def decode(envelope):
    if set(envelope)!={'schema','model_sha256','section','visible','residual'}:raise ValueError('fields')
    if envelope['schema']!='vacuum-pair-with-residual-v1' or envelope['model_sha256']!=D['MODEL_SHA256'] or envelope['section']!=SECTION:raise ValueError('model/section')
    if len(envelope['visible'])!=2 or len(envelope['residual'])!=5:raise ValueError('lost coordinates')
    visible=list(map(Q,envelope['visible']));residual=list(map(Q,envelope['residual']))
    y=[x+z for x,z in zip(apply(S,visible),apply(N,residual))]
    payload={'schema':'seven-dimensional-ideal-readings-v1','model_sha256':D['MODEL_SHA256'],
             'readings':{name:str(value) for name,value in zip(D['IDS'],y)}}
    return D['reconstruct'](payload)
for c in source_basis+[list(map(Q,(-28,1,2,3,4,5,6,7)))]:
    envelope=encode(readings(source(c)))
    assert list(map(Q,decode(envelope)['path_coefficients']))==c
# Five explicit source kernel vectors certify that the lower view has no inverse.
kernel_sources=mm(inv(E),N)
assert rank(kernel_sources)==5 and mm(W,kernel_sources)==[[0]*5 for _ in range(2)]
assert mm(R,mm(E,kernel_sources))==eye(5)
# An adapted SOURCE basis explains the flag: three order-one residuals
# and two order-two residuals, with no residual of pure order three.
adapted=[]
for mask in (1,2,4,5,6):
    moments=[Q(0)]*8;moments[mask]=1;moments[3]-=(-1)**mask.bit_count()
    coefficients=a.inverse(moments)
    assert apply(W,coefficients[1:])==[0,0]
    for depth in range(mask.bit_count()):assert not f['vacuum_rows'](0,63,source(coefficients),depth)
    assert f['vacuum_rows'](0,63,source(coefficients),mask.bit_count())
    adapted.append({'interaction_label':mask,'ideal_order':mask.bit_count(),
                    'path_coefficients':[str(c) for c in coefficients]})
assert rank([list(map(Q,b['path_coefficients'][1:])) for b in adapted])==5
bad=copy.deepcopy(envelope);bad['residual'].pop()
try:decode(bad)
except ValueError:pass
else:raise AssertionError('missing residual accepted')
bad=copy.deepcopy(envelope);bad['section']='unspecified'
try:decode(bad)
except ValueError:pass
else:raise AssertionError('untracked section change accepted')
# History from Nima's history-indexed prototype: append H=P-Q twice.
# It restricts the final source to a two-dimensional reachable subspace.
H=[Q(1),Q(-1)]
T10=a.action(H,1);append_last=a.action(H,2);T21=append_last[1:]
T20=mm(T21,T10)
for c in a.basis(2):
    assert a.paths(apply(T10,c),0,2)==f['multiply'](a.paths(c,0,1),a.paths(H,1,1))
for c in a.basis(4):
    assert a.paths(apply(append_last,c),0,3)==f['multiply'](a.paths(c,0,2),a.paths(H,2,1))
assert mm(W,T20)==eye(2)
assert rank(transpose(T20))==2
assert rank(transpose(kernel_sources)+transpose(T20))==7
history_section=mm(E,T20)
assert history_section==[[Q(i==j) for j in range(2)] for i in range(7)]
assert mm(P,history_section)==eye(2)
history_residual=mm(R,history_section)
assert history_residual==[[0,0],[-1,-1],[0,0],[1,1],[0,0]]
# Its two vacuum readings refine at jet depth two to their sum, exactly
# the terminal coefficient of the initial packet.
assert mm([[Q(1),Q(1)]],mm(W,T20))==[[1,1]]
history_squares=0
for i,j in product(range(4),repeat=2):
    assert mm(projections[j],mm(comparisons[i,j],mm(anchors[i],T20)))==eye(2)
    history_squares+=1
# Retain correlated histories, not unrelated marginal possibilities.
constraints=[];rhs=[];width=13
for start,end,transition in ((0,2,T10),(2,6,T21)):
    for index,row in enumerate(transition):
        equation=[Q(0)]*width;equation[end+index]=1
        for j,c in enumerate(row):equation[start+j]-=c
        constraints.append(equation);rhs.append(Q(0))
terminal=[Q(1),Q(1)]+[Q(0)]*11
histories=a.solve(constraints+[terminal],rhs+[Q(1)],width)
assert len(histories[1])==1
vacuum_constraint=[Q(0)]*6+W[0]
refined=a.restrict(histories,[vacuum_constraint],[Q(1)])
assert refined is not None and not refined[1] and refined[0][:2]==[1,0]
assert a.restrict(refined,[vacuum_constraint],[Q(0)]) is None

# An invertible full-data change can fail to descend to the coarse view.
U=eye(7);U[0][2]=1
hidden=[Q(int(i==2)) for i in range(7)]
assert apply(P,hidden)==[0,0] and apply(mm(P,U),hidden)==[1,0]
assert rank(U)==7
corrupt=[row[:] for row in projections[0]];corrupt[0][0]+=1
assert mm(corrupt,anchors[0])!=W

report={'passed':True,'comparison':'actual seven-reading receiver -> separately retained canonical and reversed vacuum rows',
 'source_domain':D['MODEL']['source_domain'],'source_model_sha256':D['MODEL_SHA256'],
 'noninvertible_source_anchor':wire(W),'rich_source_anchor':wire(E),
 'kernel_dimension':5,'inherited_filtration':filtered,
 'four_realization_anchors':[wire(A) for A in anchors],
 'four_noninvertible_projections':[wire(A) for A in projections],
 'comparisons':{str(i)+'->'+str(j):wire(A) for (i,j),A in comparisons.items()},
 'commuting_noninvertible_squares':squares,'comparison_triangles':triangles,
 'rich_jet_dimensions':[0,3,6,7],'induced_coarse_jet_dimensions':coarse_depth_dimensions,
 'coarse_depth_three_to_two':'(canonical,reversed) -> canonical + reversed',
 'frame_squares_across_all_depths':all_depth_frame_squares,'actual_quotient_depth_squares':depth_squares,
 'whole_affine_fiber_comparisons':fiber_checks,'sample_source_fibers':sample_fibers,
 'residual_contract':{'section_id':SECTION,'section_matrix':wire(S),'kernel_embedding':wire(N),
                      'residual_extraction':wire(R),'coordinates':[2,5],
                      'section_status':'chosen filtered linear section on this finite slice, not a global bimodule section'},
 'kernel_source_basis':wire(kernel_sources),'filtration_adapted_kernel_basis':adapted,
 'history_restriction':{'source':'Nima history: append H=P-Q in blocks two and three',
   'stage_dimensions':[2,4,7],'T10':wire(T10),'T21':wire(T21),'T20':wire(T20),
   'reachable_final_dimension':2,'discarded_kernel_intersection_with_reachable_sources':0,
   'vacuum_pair_on_initial_source':wire(mm(W,T20)),
   'history_compatible_section':wire(history_section),'residual_determined_by_visible_pair':wire(history_residual),
   'observer_history_squares':history_squares,'initial_terminal_fiber_dimension':1,
   'fiber_dimension_after_canonical_vacuum_equals_one':0,
   'contradictory_repeat_rejected_without_overwriting_old_evidence':True},
 'negative_controls':{'invertible_frame_change_need_not_descend':True,
   'corrupted_noninvertible_map_rejected':True,'missing_residual_rejected':True,'untracked_section_rejected':True},
 'scope':'Finite source-anchored filtered linear comparison. The old 449 two-feature rows vanish on this forgotten full-corner slice; this is NOT their outstanding raw-to-minimal global comparison. No physical acquisition or global observer splitting is certified.'}
out=ROOT/'research/voevodsky/results'
(out/'source-anchored-noninvertible-square.json').write_text(json.dumps(report,indent=2)+'\n')
(out/'vacuum-pair-with-residual-example.json').write_text(json.dumps(envelope,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k in ('passed','comparison','kernel_dimension','inherited_filtration',
 'commuting_noninvertible_squares','comparison_triangles','whole_affine_fiber_comparisons','negative_controls','scope',
 'rich_jet_dimensions','induced_coarse_jet_dimensions','frame_squares_across_all_depths','actual_quotient_depth_squares')},indent=2))
