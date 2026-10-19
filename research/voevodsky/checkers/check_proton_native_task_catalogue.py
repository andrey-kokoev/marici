"""Exact tasks of the native typed 1836-transfer schedule.

No new matter/energy law. Readouts concern arbitrary coefficient inputs of the
fixed source realization. G acts on local-stage data, never directly on raw x.
Only owner-local receipts are written. All arithmetic is exact Q(sqrt(-3)).
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from hashlib import sha256
import itertools,json,random,sys

ROOT=Path(__file__).resolve().parents[3]
OWNER=ROOT/'research/nima'
sys.path.insert(0,str(OWNER/'checkers'))
from assemble_triangle_arrow_source import assemble

ZERO=(F(0),F(0));ONE=(F(1),F(0))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return (a[0]*b[0]-3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def div(a,b):
    d=b[0]**2+3*b[1]**2
    if not d:raise ZeroDivisionError('zero field denominator')
    c=mul(a,conj(b));return (c[0]/d,c[1]/d)
def total(xs):
    s=ZERO
    for x in xs:s=add(s,x)
    return s

def eye(n):return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def mzero(n,m):return [[ZERO for j in range(m)] for i in range(n)]
def adj(a):return [[conj(x) for x in col] for col in zip(*a)]
def madd(a,b):return [[add(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def msub(a,b):return [[sub(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def mm(a,b):
    assert len(a[0])==len(b)
    out=mzero(len(a),len(b[0]));sparse=[[(j,x) for j,x in enumerate(row) if x!=ZERO] for row in b]
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if x!=ZERO:
                for j,y in sparse[k]:out[i][j]=add(out[i][j],mul(x,y))
    return out

def mv(a,v):return [total(mul(x,y) for x,y in zip(row,v) if x!=ZERO and y!=ZERO) for row in a]
def vadd(a,b):return list(map(add,a,b))
def vsub(a,b):return list(map(sub,a,b))
def norm(v):return total(mul(conj(x),x) for x in v)
def trace(a):return total(a[i][i] for i in range(len(a)))
def column(a,j):return [row[j] for row in a]
def rref(a):
    if not a:return [],[]
    a=[list(row) for row in a];pivots=[];r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]!=ZERO),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];d=a[r][c];a[r]=[div(x,d) for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]!=ZERO:
                z=a[i][c];a[i]=[sub(x,mul(z,y)) for x,y in zip(a[i],a[r])]
        pivots.append(c);r+=1
        if r==len(a):break
    return a[:r],pivots

def rank(a):return len(rref(a)[1])
def nullspace(a,n=36):
    reduced,pivots=rref(a);free=[i for i in range(n) if i not in pivots];out=[]
    for j in free:
        v=[ZERO]*n;v[j]=ONE
        for row,p in zip(reduced,pivots):v[p]=neg(row[j])
        out.append(v)
    return out

def sparse(a):
    return {'shape':[len(a),len(a[0])], 'entries':[[i,j,str(z[0]),str(z[1])] for i,row in enumerate(a) for j,z in enumerate(row) if z!=ZERO]}
def vector(v):return [[str(x),str(y)] for x,y in v]

def parse(records):
    labels=sorted({r['source'][1] for r in records});ports=[(t,c) for t in labels for c in 'xyz'];index={p:i for i,p in enumerate(ports)}
    stages={'raw':('local',0),'local':('aligned',1),'aligned':('raw',2)}
    matrices=[mzero(len(ports),len(ports)) for _ in range(3)];seen=set();counts=Counter()
    for record in records:
        source,target=tuple(record['source']),tuple(record['target'])
        assert (source,target) not in seen,'duplicate primitive endpoints'
        seen.add((source,target));expected,k=stages[source[0]]
        assert target[0]==expected,'invalid native stage transition'
        z=F(record['weight_real']),F(record['weight_imag_sqrt3'])
        assert z!=ZERO,'zero support arrow'
        matrices[k][index[target[1:]]][index[source[1:]]]=z;counts[k]+=1
    assert len(ports)==36 and [counts[k] for k in range(3)]==[108,432,1296]
    return ports,matrices

def observe(anchors,I,L,N):return [A[j] for A in (I,L,N) for j in anchors]
def predicted_rank(anchors):
    k=[sum(3*t+i in anchors for i in range(3)) for t in range(12)]
    d=[0,2,3,3];return sum(d[c] for c in k)+int(0<k.count(0)<12)

def decoder_for_omissions(omitted,L):
    # 24 raw coordinates and one local output per triangle; 36 scalars total.
    raw=[3*t+a for t in range(12) for a in range(3) if a!=omitted[t]]
    local=[next(3*t+a for a in range(3) if a!=omitted[t]) for t in range(12)]
    D=mzero(36,36);slots={i:j for j,i in enumerate(raw)}
    for i,j in slots.items():D[i][j]=ONE
    for t,axis in enumerate(omitted):
        missing=3*t+axis;row=local[t];den=L[row][missing]
        assert den!=ZERO
        D[missing][24+t]=div(ONE,den)
        for a in range(3):
            i=3*t+a
            if i!=missing:D[missing][slots[i]]=neg(div(L[row][i],den))
    return raw,local,D

def main():
    contract_path=ROOT/'research/voevodsky/inputs/proton-native-task-catalogue-v1.json'
    contract=json.loads(contract_path.read_text());source_path=ROOT/contract['source'];archive_path=ROOT/contract['manifest']
    source=json.loads(source_path.read_text());report,records=assemble(source)
    assert records==json.loads(archive_path.read_text()),'fresh source/archived coefficient mismatch'
    assert report['closed_walk_union_covers_every_arrow'] and report['closed_cycle_weights_positive']
    ports,(L,G,N)=parse(records);I=eye(36);Z=mzero(36,36)
    for A,expected in ((L,12),(G,3),(N,1)):
        assert adj(A)==A and mm(A,A)==A and rank(A)==expected
    assert mm(G,L)==N and mm(L,G)==N and mm(N,mm(G,L))==N
    assert mm(L,N)==mm(G,N)==mm(N,N)==N
    checks=['fresh_seed_reconstruction_and_all_1836_coefficients','typed_schedule_and_projector_identities']

    # All three components are readout differences of actual prefix states.
    diagnostics=[msub(I,L),msub(L,N),N];dims=[24,11,1]
    assert madd(madd(*diagnostics[:2]),diagnostics[2])==I
    for i,Q in enumerate(diagnostics):
        assert adj(Q)==Q and mm(Q,Q)==Q and rank(Q)==dims[i]
        for j,R in enumerate(diagnostics):
            if i!=j:assert mm(Q,R)==Z
    checks.append('orthogonal_24_11_1_diagnostic_decomposition')

    # Local scalar amplitudes use a column of the actual collective map, not
    # a supplied target eigenvector. Every local block has the same norm.
    b=column(N,0);b=[div(z,b[0]) for z in b];B=mzero(36,12);C=mzero(12,36)
    block_norms=[]
    for t in range(12):
        v=b[3*t:3*t+3];q=norm(v);block_norms.append(q)
        assert all(z!=ZERO for z in v)
        for a in range(3):B[3*t+a][t]=v[a];C[t][3*t+a]=div(conj(v[a]),q)
    J=[[(F(1,12),F(0))]*12 for _ in range(12)]
    assert len(set(block_norms))==1
    assert mm(C,B)==eye(12) and mm(B,C)==L
    assert mm(G,B)==mm(B,J) and mm(N,B)==mm(B,J)
    assert mm(mm(B,J),C)==N
    comparison=mzero(11,12)
    for t in range(1,12):comparison[t-1][t]=ONE;comparison[t-1][0]=neg(ONE)
    assert rank(comparison)==11 and mm(comparison,J)==mzero(11,12)
    assert rank(msub(eye(12),J))==11
    checks.append('source_derived_local_encoder_mean_return_and_11_comparisons')

    # Exact structural ingredients of the all-mask theorem: every occupied
    # triangle's local observer row span contains b_t; rank depends only on
    # its number of selected axes. An empty block is the only obstruction to
    # the global row being in the local row span.
    local_cases=[]
    for t in range(12):
        for bits in range(8):
            chosen=[a for a in range(3) if bits>>a&1]
            rows=[[I[3*t+a][3*t+c] for c in range(3)] for a in chosen]+[[L[3*t+a][3*t+c] for c in range(3)] for a in chosen]
            d=rank(rows);assert d==[0,2,3,3][len(chosen)]
            if chosen:assert rank(rows+[[conj(z) for z in b[3*t:3*t+3]]])==d
            local_cases.append({'triangle':ports[3*t][0],'axis_mask':bits,'rank':d})
    masks=[[],list(range(36)),[3*t for t in range(12)], [3*t+a for t in range(12) for a in (0,1)],list(range(9)),list(range(18))]
    masks += [[j] for j in range(36)]
    rng=random.Random(1836)
    masks += [[j for j in range(36) if rng.randrange(4)<threshold] for threshold in (1,2,3) for _ in range(6)]
    profiles=[]
    for anchors in masks:
        observed=rank(observe(anchors,I,L,N));expected=predicted_rank(set(anchors));assert observed==expected
        profiles.append({'anchors':anchors,'rank':observed,'hidden_dimension':36-observed})
    assert rank([I[0],L[0],N[0]])==3
    assert rank([I[0],L[0],G[0],N[0]])==4
    checks.extend(['all_96_local_mask_cases_and_general_rank_formula','60_global_mask_controls','raw_G_substitution_detectably_changes_the_task'])

    # Complete left inverse, checked on every input basis vector at once.
    raw,local,D=decoder_for_omissions([2]*12,L)
    measurement=[I[j] for j in raw]+[L[j] for j in local]
    assert mm(D,measurement)==I
    # All three possible omissions in every local triangle: independent 3x3
    # identities suffice for every one of the 3^12 combined layouts.
    for t in range(12):
        for missing in range(3):
            omission=[2]*12;omission[t]=missing
            rr,ll,dd=decoder_for_omissions(omission,L)
            assert mm(dd,[I[j] for j in rr]+[L[j] for j in ll])==I
    # Every one-address deletion from the minimal design exposes a kernel.
    deletion_witnesses=[]
    for j in raw:
        reduced=[i for i in raw if i!=j];O=observe(reduced,I,L,N)
        assert rank(O)==35
        witness=nullspace(O)[0];assert mv(O,witness)==[ZERO]*len(O) and any(z!=ZERO for z in witness)
        deletion_witnesses.append({'removed_address':j,'kernel_witness':vector(witness)})
    checks.append('24_address_decoder_all_basis_vectors_all_local_omissions_and_24_deletions')

    # Actual two seed parent faces: derive from source cycles and constructor
    # triangle ownership, not six consecutive rows of a chosen ordering.
    seed_faces={frozenset(c) for c in report['derived_cycles']}
    owners={''.join(r['outer_arrow']):frozenset(r['triangle'][0].split('_')[1:]) for r in report['triangles_and_transports']}
    seed_triangles=[t for t in range(12) if owners[ports[3*t][0]] in seed_faces]
    seed_addresses=[3*t+a for t in seed_triangles for a in range(3)]
    assert len(seed_triangles)==6
    Oseed=observe(seed_addresses,I,L,N)
    assert rank(Oseed)==19 and rank(mm(Oseed,B))==7
    outside=[t for t in range(12) if t not in seed_triangles];amplitudes=[ZERO]*12
    amplitudes[outside[0]]=ONE;amplitudes[outside[1]]=neg(ONE)
    w=mv(B,amplitudes);x=vadd(b,w);y=vsub(b,w)
    assert x!=y and mv(L,x)==x and mv(L,y)==y
    assert mv(N,x)==mv(N,y)==b and mv(Oseed,x)==mv(Oseed,y)
    assert norm(x)==norm(y) and norm(w)!=ZERO
    seed_kernel=nullspace(mm(Oseed,B),12)
    assert len(seed_kernel)==5
    checks.append('two_seed_faces_equal_norm_indistinguishable_pair_and_five_hidden_local_modes')

    # A prescribed local-stage record is attainable iff Ly=y; if attainable,
    # its raw preimages are y+ker L. The displayed witness uses a true native
    # rejected direction. Terminal records analogously have 35-dimensional fibers.
    rejected=column(diagnostics[0],0);disagreement=column(diagnostics[1],0)
    assert any(z!=ZERO for z in rejected) and mv(L,rejected)==[ZERO]*36
    assert any(z!=ZERO for z in disagreement) and mv(L,disagreement)==disagreement and mv(N,disagreement)==[ZERO]*36
    assert mv(L,vadd(b,rejected))==b and mv(N,vadd(b,disagreement))==b
    checks.append('constructive_local_and_terminal_preimage_fibers')

    # Malformed primitives fail rather than silently changing the problem.
    bad=[dict(r) for r in records];bad[0]=dict(bad[0],target=['aligned']+bad[0]['target'][1:])
    for malformed in (records+[records[0]],records[1:],bad):
        try:parse(malformed)
        except AssertionError:pass
        else:raise AssertionError('malformed manifest admitted')
    tampered=[row[:] for row in N];tampered[0][0]=add(tampered[0][0],ONE)
    assert tampered!=mm(G,L) and mm(tampered,tampered)!=tampered
    checks.append('primitive_deletion_duplication_stage_and_coefficient_hostiles')

    files=[contract_path,source_path,archive_path,Path(__file__),OWNER/'checkers/assemble_triangle_arrow_source.py',OWNER/'checkers/check_twelve_triangle_positive_geometry.py',OWNER/'checkers/check_triangle_half_phase.py',OWNER/'checkers/check_collective_four_state_identity.py']
    result={'schema':'marici.voevodsky.native-task-catalogue-result.v1','status':'passed','verification_passed':True,
      'classification':'exact_native_schedule_task_and_readout_theorems_on_the_fixed_coefficient_carrier',
      'active_obligation':contract['active_obligation'],'checks':[{'name':s,'passed':True} for s in checks],
      'source_hashes':{p.resolve().relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in files},
      'source_reconstruction':report,'coordinate_addresses':[list(p) for p in ports],
      'prefix_maps':['I','L','GL=N','NGL=N'],'new_information_from_repeating_return':False,
      'diagnostic_dimensions':{'local_rejection':24,'locally_valid_collective_disagreement':11,'collective_amplitude':1},
      'local_mode_encoder':sparse(B),'local_mode_decoder':sparse(C),'independent_compatibility_comparisons':sparse(comparison),
      'all_mask_theorem':{'domain':'all 2^36 coordinate-address subsets; same addresses read at raw/local/aligned stages',
        'rank_formula':'sum_t d(k_t) + indicator(0 < number_of_empty_triangles < 12), d=(0,2,3,3)',
        'local_exhaustive_cases':local_cases,'global_regressions':profiles,
        'full_recovery_iff':'at least two coordinate addresses in every triangle','minimum_addresses':24,
        'minimum_independent_complex_readings':36,'one_address_rank':3,'one_address_hidden_dimension':33},
      'reconstruction':{'raw_addresses':raw,'local_addresses':local,'measurement':sparse(measurement),'decoder':sparse(D),
        'decoder_times_measurement_is_identity':True,'all_3_power_12_two_coordinate_layouts':'proved by independent local decoder identities',
        'one_address_deletion_witnesses':deletion_witnesses},
      'seed_face_counterexample':{'seed_faces':[sorted(f) for f in sorted(seed_faces,key=lambda s:sorted(s))],
        'observed_addresses':seed_addresses,'raw_input_observation_rank':19,'raw_hidden_dimension':17,
        'locally_admitted_observation_rank':7,'locally_admitted_hidden_dimension':5,
        'collective_vector':vector(b),'hidden_difference_direction':vector(w),'input_x':vector(x),'input_y':vector(y),
        'equal_norm':vector([norm(x)]),'both_locally_admitted':True,'same_seed_observations_and_global_return':True,
        'local_amplitude_kernel_basis':[vector(v) for v in seed_kernel]},
      'preimage_tasks':{'local_record':'empty unless Ly=y; otherwise y+ker L, dimension 24',
        'terminal_record':'empty unless Ny=y; otherwise y+ker N, dimension 35',
        'local_rejection_witness':vector(rejected),'collective_disagreement_witness':vector(disagreement)},
      'forbidden_stage_substitution':{'actual_single_address_rank':3,'rank_if_raw_G_probe_is_added':4,'raw_G_probe_admitted':False},
      'scope_limits':contract['scope_limits'],'physical_amplitude_measurement_derived':False,
      'prior_results_rechecked':['native projector ranks','local validity does not imply collective compatibility'],
      'new_task_results':['all-mask stage-readout rank formula','sharp 24-address decoder','two-seed-face equal-norm ambiguity certificate'],
      'shared_sources_or_stores_modified':False}
    out=ROOT/'research/voevodsky/results/proton-native-task-catalogue-v1.json';out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'diagnostic_dimensions':dims,'minimum_stage_addresses':24,'seed_face_hidden_local_modes':5,'result':out.relative_to(ROOT).as_posix()},indent=2))

if __name__=='__main__':main()
