"""Metric readout, information-loss controls and a typed rectangular DG trial.
The fixed two-by-two numerical fixture is not silently replaced.
"""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,json,runpy,sys,hashlib
from field_refibration import EDGES
from field_metric_comparisons import readout,project,pairing,rectangular_legs,matmul,rank
ROOT=Path(__file__).resolve().parents[3]
log=io.StringIO()
with contextlib.redirect_stdout(log):
    import check_simplex_interface_algebra as group
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
try:
    with contextlib.redirect_stdout(log):adapter=runpy.run_path(str(Path(__file__).with_name('check_generated_rung4_adapter.py')))
finally:sys.path.pop(0)
s=group.s;A,Z,O=group.A,group.ZERO,group.ONE
indices=[[s.r.labels.index(edge+':'+axis) for axis in 'xyz'] for edge in s.r.patches]
Lp=group.mul(group.mul(s.Binv,group.L),s.B)
K={(i,j):s.K.get((indices[0][i],indices[0][j]),Z) for i in range(3) for j in range(3)}
P={(i,j):Lp.get((indices[0][i],indices[0][j]),Z) for i in range(3) for j in range(3)}
I3={(i,j):A(int(i==j)) for i in range(3) for j in range(3)}
Q=group.add(I3,group.scale(A(-1),P))
# Deterministic complex fixture, not fitted DG coefficients or physical data.
field={edge:tuple(A(tuple(F(((i+2)*(j+3)**2)%17-8) if mask==0 else F(((i+4)**2*(j+2))%19-9) if mask==8 else F(0) for mask in range(16))) for j in range(3)) for i,edge in enumerate(EDGES)}
reference=(0,1);observed=readout(field,K,reference,Z)
blocks=observed['blocks'];ranks={name:rank(matrix,Z) for name,matrix in blocks.items()}
assert ranks=={'arrow':3,'state':4}
for matrix in blocks.values():
    for i in range(len(matrix)):
        for j in range(len(matrix)):assert matrix[i][j]==matrix[j][i].flip(8)
        assert all(c==0 for c in matrix[i][i].c[1:]) and matrix[i][i].c[0]>0
assert sum(len(m)**2 for m in blocks.values())==137
# The common corner metric + recorded frames define this comparison policy.
# Native spatial-dot comparison is a different, also available policy.
labels=s.r.labels
flat=[field[tuple('ABCD'.index(c) for c in label.split(':')[0])]['xyz'.index(label.split(':')[1])] for label in labels]
def apply(M,v):
    out=[Z]*len(v)
    for (i,j),x in M.items():out[i]=out[i]+x*v[j]
    return out
nativeflat=apply(s.B,flat)
def unflatten(values):
    output={edge:[Z]*3 for edge in EDGES}
    for label,value in zip(labels,values):
        edge,axis=label.split(':');output[tuple('ABCD'.index(c) for c in edge)]['xyz'.index(axis)]=value
    return {edge:tuple(v) for edge,v in output.items()}
native=unflatten(nativeflat)
assert unflatten(apply(s.Binv,nativeflat))==field
native_observed=readout(native,I3,reference,Z)
policy_difference=sum(blocks[name][i][j]!=native_observed['blocks'][name][i][j] for name in blocks for i in range(len(blocks[name])) for j in range(len(blocks[name])))
assert policy_difference>0
for p,U in s.targetActions.items():
    moved=unflatten(apply(s.Binv,apply(U,nativeflat)))
    expected={tuple(p[i] for i in edge):v for edge,v in field.items()}
    assert moved==expected
    new=readout(moved,K,(p[0],p[1]),Z)
    old_edges=observed['selected_edges'];new_edges=new['selected_edges']
    for i,e in enumerate(old_edges):
        for j,f in enumerate(old_edges):
            ni=new_edges.index(tuple(p[k] for k in e));nj=new_edges.index(tuple(p[k] for k in f))
            assert new['blocks']['arrow'][ni][nj]==blocks['arrow'][i][j]
    for i in range(4):
        for j in range(4):assert new['blocks']['state'][p[i]][p[j]]==blocks['state'][i][j]
# All 137 scalars lose some projector-sensitive information: a K-unitary
# reflection mixing P and its complement leaves Gram data unchanged.
energy=lambda values:sum((pairing(v,v,K,Z) for v in project(values,P,Z).values()),Z)
witness=None
for axis in range(3):
    v=tuple(A(int(i==axis)) for i in range(3));norm=K[axis,axis]
    T=group.add(I3,{(i,j):-A(2)*v[i]*K[axis,j]/norm for i in range(3) for j in range(3)})
    if group.mul(T,P)==group.mul(P,T):continue
    assert group.mul(group.mul(s.adjoint(T),K),T)=={k:v for k,v in K.items() if v!=Z}
    changed=project(field,T,Z)
    assert readout(changed,K,reference,Z)==observed
    if energy(changed)!=energy(field):witness=(axis,changed);break
assert witness is not None
axis,changed=witness
refined=lambda values:tuple(readout(project(values,E,Z),K,reference,Z) for E in (P,Q))
split=refined(field);changed_split=refined(changed)
assert split!=changed_split
for name,matrix in blocks.items():
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            assert split[0]['blocks'][name][i][j]+split[1]['blocks'][name][i][j]==matrix[i][j]
phase=A(tuple(F(3,5) if i==0 else F(4,5) if i==8 else F(0) for i in range(16)))
T=group.add(group.scale(phase,P),Q)
assert refined(project(field,T,Z))==split and project(field,T,Z)!=field
# Fixed 2x2 owner: a scalar-times-I2 identification has a rank obstruction.
# Stacking Y_j X_i factors through the 2-dimensional intermediate, hence rank <=2.
lift_ranks={}
for name,matrix in blocks.items():
    n=len(matrix)
    lift=tuple(tuple(matrix[i//2][j//2] if i%2==j%2 else Z for j in range(2*n)) for i in range(2*n))
    lift_ranks[name]=rank(lift,Z)
assert lift_ranks=={'arrow':6,'state':8}
# A separately typed rectangular realization DOES fit the existing symbolic graph.
# A=B=C; U=C^3; V=C^12. State V slots retain destination labels with zeros.
owner=adapter['owner'];dimensions={'A':1,'B':1,'U':3,'V':12}
def zeros(n,m):return tuple(tuple(Z for _ in range(m)) for _ in range(n))
def add(a,b):
    assert len(a)==len(b) and all(len(x)==len(y) for x,y in zip(a,b))
    return tuple(tuple(x+y for x,y in zip(r,t)) for r,t in zip(a,b))
def scaled(c,m):return tuple(tuple(c*x for x in row) for row in m)
def evaluate(chain,assigned,arrows,source='A',target='B'):
    out=zeros(dimensions[target],dimensions[source])
    for path,coefficient in chain.items():
        at=source;value=tuple(tuple(A(int(i==j)) for j in range(dimensions[source])) for i in range(dimensions[source]))
        for name in path:
            a,b,_=arrows[name];assert a==at;at=b
            matrix=assigned[name];assert len(matrix)==dimensions[b] and all(len(row)==dimensions[a] for row in matrix)
            value=matmul(matrix,value,Z)
        assert at==target;out=add(out,scaled(A(coefficient),value))
    return out
profiles=[];terminal_values={}
for roots in ({'a':(0,0),'s':(0,0)},{'a':(3,7),'s':(2,1)}):
    arrows,delta,bases,rectangles,routes=owner['build'](roots)
    for d in (Z,A(2)):
        assigned=rectangular_legs(field,K,reference,Z);assigned['d']=((d,),)
        for name,(source,target,degree) in arrows.items():
            if degree==1:assigned[name]=evaluate(delta(owner['word'](name)),assigned,arrows,source,target)
        comparisons=[]
        for tag,size,branch in [('a',11,'arrow'),('s',4,'state')]:
            for i in range(size):
                for j in range(size):
                    first,second,filler=routes(tag,i,j)
                    numerical=matmul(assigned[f'{tag}y{j}'],assigned[f'{tag}x{i}'],Z)
                    assert numerical==((blocks[branch][i][j],),)
                    expected=((blocks[branch][i][j]-d,),)
                    assert evaluate(first,assigned,arrows)==evaluate(second,assigned,arrows)==expected
                    assert evaluate(delta(filler),assigned,arrows)==((Z,),)
                    if filler:
                        r,c=roots[tag]
                        dx=add(assigned[f'{tag}x{i}'],scaled(A(-1),assigned[f'{tag}x{r}']))
                        dy=add(assigned[f'{tag}y{j}'],scaled(A(-1),assigned[f'{tag}y{c}']))
                        assert evaluate(filler,assigned,arrows)==matmul(dy,dx,Z)
                    comparisons.append(expected[0][0])
        mean=sum(comparisons,Z)/137
        key=str(d.record());terminal_values.setdefault(key,mean);assert terminal_values[key]==mean
        # Reuse owning retained promotions with scalar matrices, not its 2x2 bind().
        rows=tuple(adapter['Row'](slot.row.label,slot.row.source,slot.row.target,((blocks['arrow' if slot.branch=='a' else 'state'][slot.parents[0][0]][slot.parents[1][0]],),)) for slot in adapter['bound'].slots)
        for policy in ('inherited','common'):
            terminal=adapter['indexed'](adapter['promote'](adapter['promote'](rows,1,policy),2,policy),'target')
            assert adapter['leaves'](adapter['unindex'](terminal))==rows
            result=adapter['diagram']['read_at_four'](terminal,adapter['diagram']['Reference'](4,((d,),)))
            assert result==((mean,),)
        profiles.append({'roots':roots,'supplied_d':d.record(),'comparisons':len(comparisons),'two_routes_equal':True,'both_promotions_preserve_readout':True})
assert terminal_values[str(A(2).record())]==terminal_values[str(Z.record())]-A(2)
# Owner bind's hard-coded 2x2 multiplication does not accept these rectangular legs.
rectangular=rectangular_legs(field,K,reference,Z);rectangular['d']=((Z,),)
try:adapter['bind'](adapter['first'],rectangular)
except (IndexError,ValueError,AssertionError):fixed_adapter_rejected=True
else:raise AssertionError('Rectangular legs silently accepted by fixed 2x2 adapter')
report={'schema':'marici.field-metric-dg-binding.v1','status':'pass',
 'comparison_policy':'Existing common corner metric with actual patch coframes; four state vectors aligned by destination labels with zero diagonal slots',
 'scalar_slots':137,'gram_ranks':ranks,'scalar_I2_lift_ranks':lift_ranks,
 'spatial_vs_coframed_comparisons_differ':policy_difference,'proper_rotation_covariance_checks':12,
 'information_loss':{'same_137_scalars_different_projector_energy':True,'mixing_reflection_axis':axis,'before_L_energy':energy(field).record(),'after_L_energy':energy(changed).record()},
 'projector_refinement':{'slots':137,'scalar_channels_per_slot':2,'recovers_unsplit_by_sum':True,'separates_exhibited_collision':True,'remaining_unitary_ambiguity':True,'lossless_field_recovery_claimed':False},
 'fixed_2x2_adapter':{'rectangular_legs_rejected':fixed_adapter_rejected,'scalar_identity_lift_factorization':'obstructed by ranks 6 and 8 exceeding intermediate dimension 2','scope':'This chosen scalar-I2 identification, not every nonlinear or matrix-valued adapter.'},
 'rectangular_candidate':{'dimensions':dimensions,'profiles':profiles,'symbolic_graph_reused':True,'fixed_original_numerical_realization':False,'direct_d_still_supplied':True},
 'scope':'Exact candidate readouts and a new dimension-typed boundary-response realization. Not a lossless scalar foliation, selected physical comparison, physical calibration, or a DG functor to zero-differential vector spaces.',
 'prerequisite_replay':log.getvalue()}
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v3.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))['readout_layers']
assert atlas['coframed_scalar_comparisons']['fixture_ranks']==ranks
assert atlas['coframed_scalar_comparisons']['slots']==137 and not atlas['coframed_scalar_comparisons']['lossless']
assert atlas['projector_resolved_comparisons']['scalar_channels_per_slot']==2
assert atlas['old_fixed_2x2_identification']['block_ranks']==list(lift_ranks.values())
assert atlas['rectangular_shared_leg_candidate']['object_dimensions']==dimensions
paths=[Path(__file__),Path(__file__).with_name('field_metric_comparisons.py'),Path(__file__).with_name('check_generated_rung4_adapter.py'),atlas_path,ROOT/'research/strominger/field-metric-dg-binding-v1.md']
report['direct_source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/field-metric-dg-binding';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prerequisite_replay','direct_source_hashes')},indent=2))
