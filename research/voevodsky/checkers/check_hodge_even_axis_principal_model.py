"""An actual even-axis principal successor with licensed cohomology/cycle maps."""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import check_hodge_indecomposable_principal_model as old
import check_hodge_cyclic_prym_odd_axis_obstruction as odd
import check_hodge_two_branch_odd_axis_obstruction as ram

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-even-axis-principal-model.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-even-axis-principal-model-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-even-axis-principal-model-v1.json'
PAIRS=((0,1),(2,6),(3,4),(5,7))
BLOCKS=tuple((tuple(j for i in pair for j in (2*i,2*i+1)),old.real_matrix(old.HADAMARD)) for pair in PAIRS)
POLICY=['Prym_membership_constructed','all_even_axis_ppavs_are_Pryms',
    'Y2_exclusions_transferred_across_isogeny','marking_matrix_is_endomorphism_of_Y2',
    'original_fixed_X_or_alpha_changed','all_elliptic_curves_enumerated',
    'finite_slope_controls_counted_as_actual_curves','nonzero_exceptional_cycle_constructed',
    'Chow_retraction_claimed','inverse_cohomology_matrix_is_inverse_Chow_map',
    'actual_theta_dimension_computed','Hodge_proved','Hodge_refuted','global_witness_search_completed']
GEOMETRY={'new_auxiliary_model':'Y3','same_sign_Gaussian_pairs_zero_based':[list(p) for p in PAIRS],
    'marking_on_each_pair':'H=[[1,1],[1,-1]]','successor_degree':256,'composite_degree':589824,
    'step_polarization_multiplier':2,'composite_polarization_multiplier':4,
    'elliptic_axis_step_kernel_orders':[1,1],'elliptic_axis_theta_degrees':[4,6],
    'all_elliptic_theta_degrees_even':True,'elliptic_theta_degree_lower_bound':4}
TRANSFER={'Gaussian_step_determinant':[16,0],'Gaussian_composite_determinant':[0,768],
    'normalized_transfer_denominator':768,'R6_forward_image':'I3','I6_forward_image':'-R3',
    'factorized_inverse_local_exterior_columns':64,'global_H8_crosscheck_columns':4,
    'all_four_exceptional_channels_transported':True}
INPUTS={'old_model':'research/voevodsky/results/hodge-indecomposable-principal-model-v1.json',
    'odd_axis':'research/voevodsky/results/hodge-cyclic-prym-odd-axis-obstruction-v1.json',
    'two_branch':'research/voevodsky/results/hodge-two-branch-odd-axis-obstruction-v1.json'}
Z=(Q(0),Q(0))


def require(c,m):
    if not c:raise ValueError(m)


def gaussian_matrix(pairs=PAIRS):
    require(sorted(i for p in pairs for i in p)==list(range(8)) and
        all(len(p)==2 and old.DY[p[0]]==old.DY[p[1]] for p in pairs),'same-sign pair partition')
    m=[[Z for _ in range(8)] for _ in range(8)]
    for p in pairs:
        for i,a in enumerate(p):
            for j,b in enumerate(p):m[a][b]=old.HADAMARD[i][j]
    return m


def matmul(a,b):
    return [[tuple(sum(old.cmul(a[i][k],b[k][j])[v] for k in range(8)) for v in (0,1))
        for j in range(8)] for i in range(8)]


@lru_cache(maxsize=2)
def compounds(back=False):
    return [{s:old.full_pullback(old.inverse(m) if back else m,{s:Q(1)})
        for k in range(len(coords)+1) for s in combinations(range(len(coords)),k)} for coords,m in BLOCKS]


@lru_cache(maxsize=None)
def substitution(block,indices,back=False):
    coords=BLOCKS[block][0];inside=tuple(i for i in indices if i in coords);outside=tuple(i for i in indices if i not in coords)
    sign_in=(-1)**sum(i>j for i in outside for j in inside);local=tuple(coords.index(i) for i in inside)
    return {tuple(sorted(outside+tuple(coords[i] for i in t))):v*sign_in*
        (-1)**sum(i>j for i in outside for j in tuple(coords[k] for k in t))
        for t,v in compounds(back)[block][local].items()}


def q_pull(form,back=False):
    require(all(tuple(sorted(set(s)))==s and all(0<=i<16 for i in s) for s in form),'Y3 exterior coordinates')
    for block in range(4):
        r={}
        for s,v in form.items():
            for t,c in substitution(block,s,back).items():r[t]=r.get(t,Q(0))+v*c
        form={s:v for s,v in r.items() if v}
    return form


def q_push(form):return old.scale(q_pull(form,True),256)


def forward(form):return old.scale(q_push(old.forward_new(form)),Q(1,16))


def reverse(form):return old.scale(old.reverse_new(q_pull(form)),Q(1,16))


def channels(form):return old.channels_new(q_pull(form))


def exceptional(form):return old.scale(q_push(old.exceptional_new(q_pull(form))),Q(1,256))


def axis_kernel_order(column):
    require(any(c!=Z for c in column),'nonzero axis column')
    return sum(all(x.denominator==y.denominator==1 for x,y in
        (old.cmul(c,(Q(a,2),Q(b,2))) for c in column)) for a,b in product(range(2),repeat=2))


@lru_cache(maxsize=1)
def exact_core():
    m=gaussian_matrix();composite=matmul(m,old.gaussian_matrix())
    require(old.gdet(m)==(Q(16),0) and old.gdet(composite)==(0,Q(768)),'Y3 determinant and retained phase')
    count=0
    for coords,b in BLOCKS:
        inv=old.inverse(b)
        for k in range(5):
            for s in combinations(range(4),k):
                v={s:Q(1)}
                require(old.full_pullback(inv,old.full_pullback(b,v))==v and
                    old.full_pullback(b,old.full_pullback(inv,v))==v,'Y3 local exterior inverse')
                count+=1
    require(count==64,'Y3 local exterior coverage')
    full=[[Q(0)]*16 for _ in range(16)]
    for coords,b in BLOCKS:
        for i,a in enumerate(coords):
            for j,c in enumerate(coords):full[a][c]=b[i][j]
    samples=(tuple(range(8)),tuple(range(0,16,2)),(0,1,3,6,10,12,14,15),(1,2,5,7,9,11,12,15))
    for s in samples:
        v={s:Q(1)}
        require(q_pull(v)==old.full_pullback(full,v) and q_pull(q_push(v))==old.scale(v,256) and
            q_push(q_pull(v))==old.scale(v,256),'Y3 global Koszul/inverse control')
    enew={(2*k,2*k+1):Q(d) for k,d in enumerate(old.DY)}
    require(q_pull(enew)==old.scale(enew,2),'Y3 principal polarization pullback')
    require(q_pull({tuple(range(16)):Q(1)})=={tuple(range(16)):Q(256)},'Y3 isogeny degree')
    oldm=old.gaussian_matrix();bp=[oldm[i][6] for i in range(8)]
    bm=[old.cmul(oldm[i][7],(Q(1,2),Q(-1,2))) for i in range(8)]
    def apply(v):return [tuple(sum(old.cmul(m[i][k],v[k])[j] for k in range(8)) for j in (0,1)) for i in range(8)]
    cp,cm=apply(bp),apply(bm)
    require(axis_kernel_order(cp)==axis_kernel_order(cm)==1,'Y3 axis step kernels')
    sp={i for i,c in enumerate(cp) if c!=Z};sm={i for i,c in enumerate(cm) if c!=Z}
    require(sp=={0,1,2,6} and sm=={5,7} and sp.isdisjoint(sm) and
        cp[0]==(1,0) and cm[7]==(0,-1),'Y3 joint elliptic lattice saturation')
    require(odd.inner(cp,cp,old.DY)==(4,0) and odd.inner(cm,cm,old.DY)==(-6,0) and
        odd.inner(cp,cm,old.DY)==Z,'Y3 native elliptic polarization')
    controls=0
    for a,b in product(product(range(-2,3),repeat=2),repeat=2):
        if a==(0,0) and b==(0,0):continue
        d=4*odd.norm(a)+6*odd.norm(b)
        require(d>=4 and d%2==0,'Y3 universal degree-expression controls')
        controls+=1
    require(odd.invariant_fibre_divisibility(8) and odd.invariant_fibre_divisibility(12) and
        ram.residue_profiles(8) and ram.residue_profiles(12),'Y2 odd-axis exclusions not inherited')
    bad=gaussian_matrix(((0,6),(1,2),(3,4),(5,7)))
    badplus=[tuple(sum(old.cmul(bad[i][k],bp[k])[j] for k in range(8)) for j in (0,1)) for i in range(8)]
    require(axis_kernel_order(badplus)==4,'bad pairing leaves degree-one elliptic control')
    r8,i8=old.generators(8);r6,i6=old.generators(6)
    require(q_pull(r8)==old.scale(r8,16) and q_pull(i8)==old.scale(i8,16) and
        q_push(r8)==old.scale(r8,16) and q_push(i8)==old.scale(i8,16),'Y3 Weil step has no additional rotation')
    require(forward(r6)==i8 and forward(i6)==old.scale(r8,-1),'Y3 original alpha phase')
    ex={(2*k,2*k+1):Q(d) for k,d in enumerate(old.DS8[:6])};cube=old.wedge(old.wedge(ex,ex),ex)
    for v in (r6,i6,cube):require(reverse(forward(v))==v,'Y3 normalized cohomological retraction')
    require(not any(channels(forward(cube))) and exceptional(r8)==r8 and exceptional(i8)==i8,'Y3 full exceptional filter controls')
    return {'Gaussian_step_determinant':[16,0],'Gaussian_composite_determinant':[0,768],
        'successor_degree':256,'composite_degree':589824,'normalized_transfer_denominator':768,
        'elliptic_axis_step_kernel_orders':[1,1],'elliptic_axis_composite_kernel_orders':[1,2],
        'physical_elliptic_surface_polarization_degrees':[4,6],
        'all_elliptic_theta_degrees_even':True,'elliptic_theta_degree_lower_bound':4,
        'finite_quadratic_expression_controls':controls,'factorized_inverse_local_exterior_columns':64,
        'explicit_global_H8_sample_columns':4,'alpha_R6_forward_image':'I3',
        'rational_Hdg4_dimension':14,'divisor_Hdg4_dimension':6,'exceptional_Hdg4_dimension':8}


def validate_contract(c):
    require(c['schema']=='marici.hodge-even-axis-principal-model.v1' and
        c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and c['node']=='even-axis-principal-model','Y3 identity')
    require(c['geometry']==GEOMETRY and c['transfer']==TRANSFER,'Y3 geometry or transfer changed')
    require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'Y3 promoted to cycle or Prym theorem')
    exact_core()


def report():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    rs={'old_model':old.report(),'odd_axis':odd.report(),'two_branch':ram.report()}
    for k,r in rs.items():require(json.loads((ROOT/INPUTS[k]).read_text(encoding='utf-8'))==r and r['passed'],'stale '+k)
    require(rs['old_model']['principal_polarization_indecomposable'] and
        rs['odd_axis']['fixed_Y2_smooth_etale_cyclic_quartic_principal_presentations_excluded'] and
        rs['two_branch']['fixed_Y2_natural_principal_two_branch_cyclic_quartic_presentations_excluded'],'Y3 input boundary lost')
    names=set(INPUTS.values())|{CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix()}
    return {'schema':'marici.hodge-even-axis-principal-model-result.v1','passed':True,
        'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'constructed',
        'verification_level':'Written Riemann/isotypic/PID/indecomposability and Chow-isogeny argument with exact lattice, exterior and cycle-channel controls; no Prym or target cycle.',
        'checks':{'principal_Riemann_lattice':True,'actual_even_degree_elliptic_surface':True,
            'indecomposable_principal_model':True,'determinant_phase_and_exterior_inverse':True,
            'all_four_cycle_channels':True,'prior_receipts_fresh':True,'scope':True},**exact_core(),
        'actual_principal_Gaussian_model_Y3_constructed':True,'principal_polarization_indecomposable':True,
        'four_exceptional_cycle_channels_transported':True,
        **{k:False for k in POLICY},
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k!='source_sha256'},indent=2))
