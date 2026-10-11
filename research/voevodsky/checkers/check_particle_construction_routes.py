"""Source-bound route comparison and a conditional fourth construction.
No particle name is assigned to the fourth output. The shared object recovered
here is a labelled tetrahedral geometry, not an established universal process.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from check_coupled_six_piece_belt import PROTON,verify_proton
from check_geometric_cycle_reversal import geo
import check_coupled_six_piece_belt as core
from check_belt_three_by_twelve import decode as decode_weight, sparse_product
from check_electron_charge_spin_frontier import ga,gs,gm,gc,gt,gmm,G0,G1

BASE=Path(__file__).resolve().parents[1]
# Exact real field Q(sqrt(3),sqrt(74)); the displayed belt has gap 7/10.
@dataclass(frozen=True,eq=False)
class R:
    c:tuple=(F(0),F(0),F(0),F(0))
    def __post_init__(self):object.__setattr__(self,'c',tuple(map(F,self.c)))
    def __add__(self,x):return R(tuple(a+b for a,b in zip(self.c,cast(x).c)))
    __radd__=__add__
    def __neg__(self):return R(tuple(-a for a in self.c))
    def __sub__(self,x):return self+-cast(x)
    def __rsub__(self,x):return cast(x)+-self
    def __mul__(self,x):
        x=cast(x);out=[F(0)]*4
        for i,a in enumerate(self.c):
            for j,b in enumerate(x.c):
                common=i&j;out[i^j]+=a*b*(3 if common&1 else 1)*(74 if common&2 else 1)
        return R(tuple(out))
    __rmul__=__mul__
    def __truediv__(self,x):
        if not isinstance(x,(F,int)):raise TypeError('Only rational division is used')
        return R(tuple(a/x for a in self.c))
    def __eq__(self,x):
        if isinstance(x,(R,F,int)):return self.c==cast(x).c
        return False
    def __hash__(self):return hash(self.c[0]) if all(x==0 for x in self.c[1:]) else hash(self.c)
def cast(x):return x if isinstance(x,R) else R((x,0,0,0))
def real(z):return (cast(z),R())
def ident(n):return tuple(tuple(G1 if i==j else G0 for j in range(n)) for i in range(n))
def scale(q,a):return tuple(tuple(gs(q,z) for z in row) for row in a)
def plus(a,b):return tuple(tuple(ga(x,y) for x,y in zip(u,v)) for u,v in zip(a,b))
def adj(a):return tuple(tuple(gc(z) for z in row) for row in zip(*a))
def trace(a):return gt(a[i][i] for i in range(len(a)))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def h(n):
    x,y,z=n;return ((real(z),(x,-y)),((x,y),real(-z)))
def projector(n,chi):return scale(F(1,2),plus(ident(2),scale(-chi,h(n))))
def sum_m(ms):return tuple(tuple(gt(m[i][j] for m in ms) for j in range(2)) for i in range(2))
def return_matrix(ps,inv):
    return tuple(tuple(gmm(gmm(ps[i//2],inv),ps[j//2])[i%2][j%2] for j in range(2*len(ps))) for i in range(2*len(ps)))
def supports(ps,N):return {'L':sum(z!=G0 for p in ps for row in p for z in row),'G':sum(z!=G0 for row in N for z in row),'N':sum(z!=G0 for row in N for z in row)}
def encode(z):return [list(map(str,cast(x).c)) for x in z]
def decode3(z):return tuple(R((F(a),F(b),0,0)) for a,b in z)

def main():
    paths={'proton':PROTON,'geometry':BASE/'results/four_six_center_cones.json',
           'ambient_belt':BASE/'results/coupled_six_piece_belt_store.json',
           'paired_belt':BASE/'results/opposite_branch_belt_store.json',
           'intrinsic_belt':BASE/'results/belt_three_by_twelve_store.json',
           'electron':BASE/'results/electron_tetrahedral_spinor_store.json'}
    raw={k:p.read_bytes() for k,p in paths.items()};data={k:json.loads(v) for k,v in raw.items()}
    verified,proton_rows=verify_proton(data['proton']);assert verified['verified']
    pobjects=data['proton']['objects'];pgeom=pobjects[pobjects[data['proton']['root']]['geometry']]['payload']
    assert {t['outer_arrow'] for t in pgeom['triangles_and_transports']}=={a+b for a in 'ABCD' for b in 'ABCD' if a!=b}
    geom=data['geometry'];assert geom['verification_passed'] and F(geom['gap'])==F(7,10)
    ambient=data['ambient_belt'];paired=data['paired_belt'];electron=data['electron']
    assert sha256(json.dumps(ambient['record'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==ambient['root']
    assert ambient['record']['geometry_sha256']==sha256(raw['geometry']).hexdigest()
    assert paired['source_root']==ambient['root'] and len(paired['arrows'])==1836
    assert paired['source_intrinsic_sha256']==sha256(raw['intrinsic_belt']).hexdigest()
    z=tuple(map(decode_weight,paired['selected_numerators']));d=tuple(F(c['d']) for c in paired['coordinates'])
    for c,w in zip(paired['coordinates'],z):
        old=decode_weight(c['selected_numerator']);sign=paired['face_signs'][ambient['record']['face_owners'][c['triangle']]]
        assert w==(old if sign==1 else core.conj(old))
    stages={s:{} for s in ('L','G','N')}
    for ar in paired['arrows']:stages[ar['stage']][ar['target'],ar['source']]=decode_weight(ar['numerator'])
    assert sparse_product(stages['G'],stages['L'],d)==sparse_product(stages['L'],stages['G'],d)==stages['N']
    nsum=sum(core.norm(w)/di for w,di in zip(z,d))
    assert stages['N']=={(i,j):core.scale(1/nsum,core.mul(x,core.conj(y))) for i,x in enumerate(z) for j,y in enumerate(z)}
    source_page=Path(geom['source_page']);assert sha256(source_page.read_bytes()).hexdigest()==geom['source_sha256']
    # The belt constructor uses an opposed copy of the same regular-tetrahedron
    # base, translated by an independently supplied gap. Check the actual recipe.
    page=source_page.read_text(encoding='utf-8')
    assert all(x in page for x in ['opposite.rotation.x = Math.PI;','tetrahedron.position.y = h / 4 + gap / 2;','opposite.position.y = -h / 4 - gap / 2;'])
    bp={k:tuple(map(F,v)) for k,v in geom['belt_scaled_coordinates'].items()}
    assert all(bp['L'+str(i)]==(bp['U'+str(i)][0],-bp['U'+str(i)][1],-bp['U'+str(i)][2]) for i in range(3))
    assert tuple(sum(v[i] for k,v in bp.items() if k!='O') for i in range(3))==(0,0,0)
    # All regular tetrahedra here have the same shape, with explicit different
    # scale/placement conventions. They are not identified merely by the center.
    tp={k:tuple(map(F,v)) for k,v in geo.POINTS.items()}
    edge_sq={sum((tp[a][i]-tp[b][i])**2 for i in range(3)) for a in tp for b in tp if a!=b}
    assert edge_sq=={8} and tuple(sum(p[i] for p in tp.values()) for i in range(3))==(0,0,0)
    gp={k:tuple(map(F,v)) for k,v in geom['proton_scaled_coordinates'].items() if k!='O'}
    assert {sum(m*(gp[a][i]-gp[b][i])**2 for i,m in enumerate((3,2,1))) for a in gp for b in gp if a!=b}=={3}
    determinant=lambda p:dot(sub(p['B'],p['A']),cross(sub(p['C'],p['A']),sub(p['D'],p['A'])))
    assert determinant(tp)==-16 and determinant(gp)==F(3,2)
    oriented_display={**gp,'C':gp['D'],'D':gp['C']}
    assert determinant(oriented_display)==-F(3,2)
    # Recover the actual four-face spinor projectors from the proton tetrahedron.
    root3=R((0,1,0,0));root222=R((0,0,0,1));root74=R((0,0,1,0))
    tnorm=[]
    for f in ('ABC','BAD','CDA','DCB'):
        a,b,c=[tp[k] for k in f];v=cross(sub(b,a),sub(c,a));tnorm.append(tuple(x*root3/12 for x in v))
    tps=[projector(n,1) for n in tnorm]
    assert tps==[tuple(tuple(decode3(z) for z in row) for row in p) for p in electron['face_projectors']]
    assert sum_m(tps)==scale(2,ident(2))
    Nt=return_matrix(tps,scale(F(1,2),ident(2)))
    Lt=tuple(tuple(tps[i//2][i%2][j%2] if i//2==j//2 else G0 for j in range(8)) for i in range(8))
    assert len(electron['arrows'])==144 and all((Lt if a['stage']=='L' else Nt)[a['target']][a['source']]==decode3(a['weight']) for a in electron['arrows'])
    # Apply precisely the electron branch rule to the ACTUAL paired belt signs.
    # Electron P^- is the spinorial opposite of the proton's positive cyclic
    # mode, so use P_i=(I-chi_i n_i.sigma)/2, retaining each belt chi_i.
    physical={k:(root3*v[0],cast(v[1]),cast(v[2])) for k,v in bp.items()}
    normals=[]
    for f in geom['belt_faces']:
        a,b,c=[physical[k] for k in f];n=tuple(x*root222*F(10,222) for x in cross(sub(b,a),sub(c,a)))
        assert dot(n,n)==1;normals.append(n)
    assert tuple(sum(n[i] for n in normals) for i in range(3))==(0,0,0)
    signs=paired['face_signs'];assert signs==[-1,-1,-1,1,1,1]
    ps=[projector(n,s) for n,s in zip(normals,signs)];S=sum_m(ps)
    sy=((G0,(R(),cast(-1))),((R(),cast(1)),G0))
    a=root74*F(5,74)
    expectedS=plus(scale(3,ident(2)),scale(-3*a,sy))
    assert S==expectedS
    inv=plus(scale(F(74,147),ident(2)),scale(root74*F(5,147),sy))
    assert gmm(S,inv)==gmm(inv,S)==ident(2)
    naive=return_matrix(ps,scale(F(1,3),ident(2)))
    assert trace(naive)==(cast(2),R()) and gmm(naive,naive)!=naive
    N=return_matrix(ps,inv)
    assert adj(N)==N and gmm(N,N)==N and trace(N)==(cast(2),R())
    L=tuple(tuple(ps[i//2][i%2][j%2] if i//2==j//2 else G0 for j in range(12)) for i in range(12))
    assert gmm(L,N)==gmm(N,L)==N
    counts=supports(ps,N);assert counts=={'L':24,'G':144,'N':144}
    # Control: discarding the recorded belt branch signs produces a different,
    # valid spinor return. It is not the same proposed fourth route.
    uniform_ps=[projector(n,1) for n in normals];assert sum_m(uniform_ps)==scale(3,ident(2))
    uniform=return_matrix(uniform_ps,scale(F(1,3),ident(2)))
    assert gmm(uniform,uniform)==uniform and uniform!=N
    uniform_counts=supports(uniform_ps,uniform);assert uniform_counts=={'L':24,'G':120,'N':120}
    # A center alone does not determine even the belt's geometry.
    centers=[]
    for gap in (F(3,5),F(7,10),F(4,5)):
        pp={k:(v[0],gap/2 if k[0]=='U' else -gap/2,v[2]) for k,v in bp.items() if k!='O'}
        centers.append(tuple(sum(p[i] for p in pp.values())/6 for i in range(3)))
    assert centers==[(0,0,0)]*3
    checks={
        'proton_arrow_source_verified':verified['verified'],
        'belt_store_binds_to_actual_geometry_and_branch_assignment':True,
        'belt_signs_match_actual_selected_coefficients':True,
        'paired_belt_return_reverified_with_intrinsic_metric':True,
        'displayed_belt_comes_from_opposed_translated_tetrahedral_bases':True,
        'proton_geometries_have_same_regular_shape_with_explicit_scale_change':True,
        'orientation_comparison_retains_required_C_D_relabelling':True,
        'electron_face_projectors_recovered_from_proton_geometry':True,
        'electron_return_matches_retained_coefficients':True,
        'same_center_does_not_fix_gap_or_route':len(set(centers))==1,
        'literal_scalar_normalization_fails_on_paired_belt':gmm(naive,naive)!=naive,
        'frame_operator_and_inverse_verified_exactly':gmm(S,inv)==ident(2),
        'conditional_fourth_return_is_Hermitian_rank_two_projector':gmm(N,N)==N and adj(N)==N,
        'conditional_fourth_support_is_312':sum(counts.values())==312,
        'erasing_belt_signs_changes_fourth_return_and_support':uniform!=N and sum(uniform_counts.values())==264,
        'all_input_artifacts_unchanged':all(p.read_bytes()==raw[k] for k,p in paths.items()),
    }
    routes={
        'common_geometric_seed':'Regular tetrahedron T with retained labels and orientation; comparison to the displayed seed needs the explicit C/D relabelling below. Not merely O=(0,0,0).',
        'seed_comparison':{'squared_length_scale':'3/8','source_labelled_determinant':'-16','display_scaled_labelled_determinant':'3/2','orientation_preserving_label_map':{'A':'A','B':'B','C':'D','D':'C'},'status':'Declared comparison of the two source presentations; neither original constructor is relabelled or overwritten.'},
        'proton':['T','twelve directed endpoint records','face centroids and proper tetrahedral rotations','twelve cyclic triangle modes','three-stage rank-one coherent return'],
        'neutron_candidate':['T','choose a base face; make opposed rotated copy','translate copies using supplied gap 7/10','nearest-stitch six base vertices into six belt panels','eighteen centroid-edge triangle modes','three adjacent face pairs and intrinsic plane coordinates','conjugate recorded nine modes','three-stage rank-one coherent return'],
        'electron_candidate':['T','four outward face normals','supply spinor doublet and Pauli projection rule','four negative-polarization projections','normalize by sum P_i=2I','three-stage rank-two coherent return'],
        'conditional_fourth':['neutron belt geometry and recorded branch signs','apply the electron spinor projection rule with those signs retained','compute S=sum P_i rather than assume S=3I','use J_i=P_i S^(-1/2)','form N_ij=P_i S^(-1)P_j; coherent rank two'],
        'branch_inputs_not_derived_from_the_common_seed':['belt gap and adjacent pairing choice','belt opposite-circulation selection','spinor carrier and its rotation lift'],
        'missing_meta_tetrahedron_data':['source identification of a common full construction record','typed comparisons among the three endpoint protocols','coherence/completion law selecting a fourth route']}
    report={'verification_passed':all(checks.values()),'checks':checks,'routes':routes,
        'normalization_residual':{'paired_belt_S':'3(I - (5/sqrt(74)) sigma_y)','S_inverse':'(74 I + 5 sqrt(74) sigma_y)/147',
            'naive_weights_for_two_y_spin_states':['1-5/sqrt(74)','1+5/sqrt(74)'],
            'invertibility':'S has eigenvalues 3(1 +/- 5/sqrt(74)), both strictly positive since 25<74.',
            'canonical_extension':'Positive S^(-1/2) supplies a state-independent isometry; this normalization generalizes the electron scalar normalization.'},
        'conditional_fourth':{'raw_complex_coordinates':12,'coherent_rank':2,'support':counts,'total':sum(counts.values()),'assigned_particle_name':None},
        'control_ignoring_neutron_branch_signs':{'support':uniform_counts,'total':sum(uniform_counts.values()),'same_return':False},
        'disposition':'Recovered a common geometric seed and three explicit partial routes. Combining the belt route with the spinor route gives a testable fourth construction, but needs non-scalar frame normalization. This conditional completion is not a uniquely forced fourth particle or a verified meta-tetrahedral coherence law.',
        'source_sha256':{k:sha256(v).hexdigest() for k,v in raw.items()},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    store={'field':'Q(sqrt(3),sqrt(74),i); real basis [1,sqrt(3),sqrt(74),sqrt(222)]',
        'source_sha256':report['source_sha256'],'face_signs':signs,'frame_operator':[[encode(z) for z in row] for row in S],
        'frame_inverse':[[encode(z) for z in row] for row in inv],
        'arrows':[{'stage':stage,'target':i,'source':j,'weight':encode(m[i][j])} for stage,m in [('L',L),('G',N),('N',N)] for i in range(12) for j in range(12) if m[i][j]!=G0]}
    (BASE/'results/particle_construction_routes.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/conditional_fourth_spinor_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
