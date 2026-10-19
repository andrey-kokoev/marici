"""Classify specified complex-linear symmetry categories, not just generators.
Finite exact hypotheses + standard unitary/Schur classification theorems.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import contextlib,io,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
log=io.StringIO()
with contextlib.redirect_stdout(log):
    import check_simplex_interface_algebra as g
s=g.s;A,Z,O=g.A,g.ZERO,g.ONE
labels=s.r.labels;edges=tuple(s.r.patches)
indices=[[labels.index(edge+':'+axis) for axis in 'xyz'] for edge in edges]
def trace(M):return sum((v for (i,j),v in M.items() if i==j),Z)
def integer(v):
    assert all(x==0 for x in v.c[1:]) and v.c[0].denominator==1
    return int(v.c[0])
def corner(M):return g.mul(g.mul(s.Binv,M),s.B)
Lp,Gp=corner(g.L),corner(g.G)
P={(i,j):Lp.get((indices[0][i],indices[0][j]),Z) for i in range(3) for j in range(3)}
K={(i,j):s.K.get((indices[0][i],indices[0][j]),Z) for i in range(3) for j in range(3)}
I3={(i,j):A(int(i==j)) for i in range(3) for j in range(3)}
assert integer(trace(P))==1 and g.mul(P,P)=={k:v for k,v in P.items() if v!=Z}
# Exact tensor identities, not an inferred numerical pattern.
for a,ii in enumerate(indices):
    for b,jj in enumerate(indices):
        for i in range(3):
            for j in range(3):
                assert Lp.get((ii[i],jj[j]),Z)==(P[i,j] if a==b else Z)
                assert Gp.get((ii[i],jj[j]),Z)==I3[i,j]/12
                assert s.K.get((ii[i],jj[j]),Z)==(K[i,j] if a==b else Z)
# Corner metric self-adjointness is inherited from B*B and source L.
assert g.mul(s.adjoint(P),K)==g.mul(K,P)
# Any arrow-fixing linear map is diag(T_e). Commuting with G forces T_e=T_f.
# It remains to classify 3x3 T commuting with rank-one K-orthogonal P.
rows={}
for i in range(3):
    for j in range(3):
        row=[Z]*9
        for k in range(3):
            row[3*i+k]=row[3*i+k]+P[k,j]
            row[3*k+j]=row[3*k+j]-P[i,k]
        if any(v!=Z for v in row):rows[tuple(v.c for v in row)]=row
rows=list(rows.values());pivot=0
for col in range(9):
    found=next((i for i in range(pivot,len(rows)) if rows[i][col]!=Z),None)
    if found is None:continue
    rows[pivot],rows[found]=rows[found],rows[pivot]
    coefficient=rows[pivot][col];rows[pivot]=[v/coefficient for v in rows[pivot]]
    for i in range(len(rows)):
        if i!=pivot and rows[i][col]!=Z:
            coefficient=rows[i][col];rows[i]=[x-coefficient*y for x,y in zip(rows[i],rows[pivot])]
    pivot+=1
assert 9-pivot==5 # End(C) + End(C^2)
# Explicit exact witnesses beyond the old finite generated subgroup.
clean=lambda M:{key:value for key,value in M.items() if value!=Z}
complement=g.add(I3,g.scale(A(-1),P))
vectors=[tuple(complement.get((i,j),Z) for i in range(3)) for j in range(3)]
vectors += [tuple(vectors[0][i]+A(2)*vectors[1][i] for i in range(3))]
def householder(v):
    row=tuple(sum((v[i].flip(8)*K[i,j] for i in range(3)),Z) for j in range(3))
    norm=sum((row[i]*v[i] for i in range(3)),Z)
    assert norm!=Z and norm.flip(8)==norm
    return g.add(I3,{(i,j):-A(2)*v[i]*row[j]/norm for i in range(3) for j in range(3)})
reflections=[householder(v) for v in vectors if any(x!=Z for x in v)]
assert any(g.mul(X,Y)!=g.mul(Y,X) for X in reflections for Y in reflections)
phase=A(tuple(F(3,5) if i==0 else F(4,5) if i==8 else F(0) for i in range(16)))
phase_map=g.add(g.scale(phase,P),complement)
for T in reflections+[phase_map]:
    assert g.mul(T,P)==g.mul(P,T)
    assert g.mul(g.mul(s.adjoint(T),K),T)==clean(K)
T12={(ii[i],ii[j]):phase_map.get((i,j),Z) for ii in indices for i in range(3) for j in range(3)}
phase_native=g.mul(g.mul(s.B,T12),s.Binv)
assert g.token(phase_native) not in {g.token(M) for M in g.matrices.values()}
# The actual named corner cycle is not K-unitary and does not commute with P.
# Do not replace it by three orthogonal eigenchannels.
C={(i,j):s.sourceCycle.get((indices[0][i],indices[0][j]),Z) for i in range(3) for j in range(3)}
assert g.mul(g.mul(C,C),C)=={k:v for k,v in I3.items() if v!=Z}
assert g.mul(s.adjoint(C),K)!=g.mul(K,g.mul(C,C))
assert g.mul(P,C)!=g.mul(C,P)
for a,ii in enumerate(indices):
    for b,jj in enumerate(indices):
        for i in range(3):
            for j in range(3):assert s.sourceCycle.get((ii[i],jj[j]),Z)==(C[i,j] if a==b else Z)
combined=[]
for block in (P,C):
    for i in range(3):
        for j in range(3):
            row=[Z]*9
            for k in range(3):
                row[3*i+k]=row[3*i+k]+block[k,j]
                row[3*k+j]=row[3*k+j]-block[i,k]
            combined.append(row)
rank=0
for col in range(9):
    found=next((i for i in range(rank,len(combined)) if combined[i][col]!=Z),None)
    if found is None:continue
    combined[rank],combined[found]=combined[found],combined[rank]
    coefficient=combined[rank][col];combined[rank]=[v/coefficient for v in combined[rank]]
    for i in range(len(combined)):
        if i!=rank and combined[i][col]!=Z:
            coefficient=combined[i][col];combined[i]=[x-coefficient*y for x,y in zip(combined[i],combined[rank])]
    rank+=1
assert rank==8 # Scalar commutant only; metric-unitary part is U(1).
omega=A(tuple(F(-1,2) if i==0 else F(1,2) if i==10 else F(0) for i in range(16)))
assert omega*omega+omega+O==Z
# A4 class characters for the full non-fiber-preserving commutant.
def compose(p,q):return tuple(p[q[i]] for i in range(4))
def inverse(p):return tuple(p.index(i) for i in range(4))
def order(p):
    current=(0,1,2,3)
    for n in range(1,13):
        current=compose(p,current)
        if current==(0,1,2,3):return n
remaining=set(g.U);classes=[]
while remaining:
    p=min(remaining);cl={compose(compose(q,p),inverse(q)) for q in g.U}
    classes.append(cl);remaining-=cl
classes.sort(key=lambda cl:(order(min(cl)),min(cl)))
assert [len(cl) for cl in classes]==[1,3,4,4]
characters=[(O,O,O,O),(O,O,omega,omega*omega),(O,O,omega*omega,omega),(A(3),A(-1),Z,Z)]
for i,chi in enumerate(characters):
    for j,psi in enumerate(characters):
        assert sum((A(len(cl))*x*y.flip(8) for cl,x,y in zip(classes,chi,psi)),Z)/12==A(int(i==j))
sectors=[]
for name,projector,rank in zip(('LG','L-LG','G-LG','I-L-G+LG'),g.sectors,g.ranks):
    values=[]
    for cl in classes:
        traces=[trace(g.mul(projector,g.U[p])) for p in sorted(cl)]
        assert all(v==traces[0] for v in traces);values.append(traces[0])
    multiplicities=[integer(sum((A(len(cl))*v*chi[k].flip(8) for k,(cl,v) in enumerate(zip(classes,values))),Z)/12) for chi in characters]
    assert all(m>=0 for m in multiplicities)
    assert sum(d*m for d,m in zip((1,1,1,3),multiplicities))==rank
    sectors.append({'sector':name,'rank':rank,'class_characters':[integer(v) for v in values],
                    'multiplicities_1_1prime_1doubleprime_3':multiplicities,
                    'unitary_commutant_factors':[f'U({m})' for m in multiplicities if m]})
assert [r['multiplicities_1_1prime_1doubleprime_3'] for r in sectors]==[[1,0,0,0],[0,1,1,3],[2,0,0,0],[0,2,2,6]]
commutant_dim=sum(m*m for row in sectors for m in row['multiplicities_1_1prime_1doubleprime_3'])
algebra_dim=sum(d*d for row in sectors for d,m in zip((1,1,1,3),row['multiplicities_1_1prime_1doubleprime_3']) if m)
assert commutant_dim==60 and algebra_dim==24
# The alignment reflection is not an arrow-fiber-preserving operation.
RGp=corner(g.RG)
off_arrow=sum(RGp.get((indices[a][i],indices[b][j]),Z)!=Z for a in range(12) for b in range(12) if a!=b for i in range(3) for j in range(3))
assert off_arrow>0
# Exhaust endpoint incidence automorphisms; an arrow/slot map is forced by its parents.
all_edges={(a,b) for a in range(4) for b in range(4) if a!=b}
perms=list(permutations(range(4)));reference=(0,1)
assert all({(p[a],p[b]) for a,b in all_edges}==all_edges for p in perms)
fixed=[p for p in perms if (p[0],p[1])==reference]
assert len(fixed)==2
# Every abstract coframed vertex relabelling preserves tensor L,G,K.
# This is NOT a claim that odd relabellings realize native spatial reflections.
for p in perms:
    V={}
    for j,label in enumerate(labels):
        edge,axis=label.split(':');new=''.join('ABCD'[p['ABCD'.index(c)]] for c in edge)
        V[labels.index(new+':'+axis),j]=O
    assert g.mul(V,Lp)==g.mul(Lp,V) and g.mul(V,Gp)==g.mul(Gp,V)
    assert g.mul(V,s.sourceCycle)==g.mul(s.sourceCycle,V)
    assert g.mul(g.mul(s.adjoint(V),s.K),V)==s.K
report={'schema':'marici.rung-automorphism-classification.v1','status':'pass',
 'tensor_form':{'field':'C^12 tensor C^3 in the existing corner coframes','metric':'I12 tensor K3','L':'I12 tensor rank-one K3-orthogonal P','G':'J12/12 tensor I3'},
 'class_sizes':[len(cl) for cl in classes],'sector_decomposition':sectors,
 'classified_categories':{
  'metric_only':'U(36)',
  'metric_and_named_L_G':'U(1) x U(11) x U(2) x U(22)',
  'metric_L_G_and_pointwise_named_A4_action':'U(1)^3 x U(2)^3 x U(3) x U(6)',
  'fix_each_arrow_fiber_metric_L_G':'U(1) x U(2)',
  'fix_each_arrow_fiber_metric_L_G_and_named_corner_cycle':'U(1)',
  'endpoint_incidence_preserving_coframed_metric_L_G':'S4 x (U(1) x U(2))',
  'fixed_directed_reference_version':'S2 x (U(1) x U(2))',
  'proper_geometric_subfamily':'A4 x (U(1) x U(2))',
  'proper_geometric_fixed_reference_version':'U(1) x U(2)'},
 'commutant_complex_dimension':commutant_dim,'generated_associative_algebra_complex_dimension':algebra_dim,
 'arrow_fiber_commutant_complex_dimension':5,'with_named_corner_cycle_commutant_complex_dimension':1,'named_corner_cycle_metric_unitary':False,'alignment_reflection_cross_arrow_entries':off_arrow,
 'explicit_local_unitary_witnesses':len(reflections)+1,'noncommuting_complement_reflections_checked':True,'local_phase_outside_old_48_checked':True,
 'finite_endpoint_permutations_checked':24,'fixed_reference_endpoint_permutations':len(fixed),
 'scope':'Full groups only within the explicitly stated complex-linear/unitary and endpoint-incidence categories. Antiunitary maps, projective quotients, unlabeled nonlinear slot automorphisms, and arbitrary scalar-observer stabilizers are not classified. Geometric relabelling may normalize named A4 operations; pointwise commutation is a different category.',
 'method':'Exact tensor identities and class characters; standard finite-dimensional complex unitary and Schur commutant classification. No new formal proof-assistant theorem.',
 'prior_simplex_replay':log.getvalue()}
atlas_path=ROOT/'research/strominger/rung-symmetry-atlas-v3.json'
atlas=json.loads(atlas_path.read_text(encoding='utf8'))
assert atlas['schema']=='marici.rung-symmetry-atlas.v3'
assert sorted(row['rung'] for row in atlas['rungs'])==list(range(4,13))
for row in atlas['rungs']:
    assert row['completeness']
    assert row['full_fixed_reference_profile'] in atlas['profiles']
    assert row['with_corner_cycle_profile'] in atlas['profiles']
    assert (row['role']=='transport')==(row['rung'] in (9,8,7))
assert atlas['evidence']['A4_multiplicities']==[r['multiplicities_1_1prime_1doubleprime_3'] for r in sectors]
assert atlas['evidence']['commutant_complex_dimension']==commutant_dim
assert atlas['evidence']['generated_algebra_complex_dimension']==algebra_dim
for profile,category in [('endpoint_fixed_reference','fixed_directed_reference_version'),('arrow_fibers_fixed','fix_each_arrow_fiber_metric_L_G'),('arrow_fibers_and_corner_cycle_fixed','fix_each_arrow_fiber_metric_L_G_and_named_corner_cycle'),('reference_transport_family','endpoint_incidence_preserving_coframed_metric_L_G'),('proper_geometric_reference_transport_family','proper_geometric_subfamily'),('projector_metric_only','metric_and_named_L_G'),('projector_metric_named_A4_pointwise','metric_L_G_and_pointwise_named_A4_action')]:
    assert atlas['profiles'][profile]['group']==report['classified_categories'][category]
report['atlas_positions_checked']=9
paths=[Path(__file__),Path(g.__file__),Path(s.__file__),atlas_path,ROOT/'research/strominger/rung-automorphism-classification-v1.md']
report['direct_source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
out=ROOT/'research/strominger/results/rung-automorphism-classification';out.mkdir(parents=True,exist_ok=True)
(out/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ('prior_simplex_replay','direct_source_hashes')},indent=2))
