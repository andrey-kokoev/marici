"""Test local geometric restriction as a source for meta-tetrahedron maps.
A failed proposed comparison is a scientific result, not a checker failure.
No arbitrary scalar functional, new pairing, or source-mode enlargement is used.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from hashlib import sha256
import json
import check_coupled_six_piece_belt as modes
from check_belt_three_by_twelve import decode as decode_mode
from check_fourth_construction_bridge import decode,matrix
from check_particle_construction_routes import R,cast,ident,scale,plus,adj,trace,decode3,encode
from check_electron_charge_spin_frontier import ga,gs,gm,gmm,G0
BASE=Path(__file__).resolve().parents[1]

def inv_real74(x):
    a,b,c,d=x.c;assert b==d==0
    den=a*a-74*c*c;assert den!=0
    return R((a/den,0,-c/den,0))
def det(m):return ga(gm(m[0][0],m[1][1]),gs(-1,gm(m[0][1],m[1][0])))
def enc(m):return [[encode(z) for z in row] for row in m]
def rank_one_projector(q):return adj(q)==q and gmm(q,q)==q and trace(q)==(cast(1),cast(0))

def main():
    names={'proton':'proton_merkle_store.json','neutron':'opposite_branch_belt_store.json',
        'electron':'electron_tetrahedral_spinor_store.json','fourth':'conditional_fourth_spinor_store.json',
        'bridge':'fourth_construction_bridge_store.json','ambient':'coupled_six_piece_belt_store.json',
        'intrinsic':'belt_three_by_twelve_store.json','geometry':'four_six_center_cones.json'}
    paths={k:BASE/'results'/v for k,v in names.items()};raw={k:p.read_bytes() for k,p in paths.items()};data={k:json.loads(v) for k,v in raw.items()}
    b=data['bridge'];n=data['neutron'];ambient=data['ambient'];intr=data['intrinsic'];geo=data['geometry']
    for source,key in [('proton','proton'),('paired_belt','neutron'),('electron','electron'),('fourth','fourth'),('geometry','geometry')]:
        assert b['source_sha256'][source]==sha256(raw[key]).hexdigest()
    assert n['source_root']==intr['source_root']==ambient['root']
    assert sha256(json.dumps(ambient['record'],sort_keys=True,separators=(',',':')).encode()).hexdigest()==ambient['root']
    assert ambient['record']['geometry_sha256']==sha256(raw['geometry']).hexdigest()
    assert n['source_intrinsic_sha256']==sha256(raw['intrinsic']).hexdigest() and n['coordinates']==intr['coordinates']
    # Recover the ACTUAL two-face sectors from the retained coordinate order.
    owners=ambient['record']['face_owners'];coords=n['coordinates'];assert len(coords)==36
    pairs=[sorted({owners[v['triangle']] for v in coords[s:s+12]}) for s in range(0,36,12)]
    assert pairs==[[0,4],[1,3],[2,5]]
    assert all(len(set(geo['belt_faces'][i])&set(geo['belt_faces'][j]))==2 for i,j in pairs)
    z=tuple(map(decode_mode,n['selected_numerators']));ds=tuple(F(v['d']) for v in coords)
    actual={(r['target'],r['source']):decode_mode(r['numerator']) for r in n['arrows'] if r['stage']=='L'}
    expected={}
    for start in range(0,36,12):
        k=sum(modes.norm(z[i])/ds[i] for i in range(start,start+12));assert modes.positive(k)
        expected.update({(i,j):modes.scale(1/k,modes.mul(z[i],modes.conj(z[j]))) for i in range(start,start+12) for j in range(start,start+12)})
    assert expected==actual # Each original neutron local sector selects ONE mode.
    pv,prows=modes.verify_proton(data['proton']);assert pv['verified']
    obj=data['proton']['objects'];pg=obj[obj[data['proton']['root']]['geometry']]['payload']
    triangles=pg['triangles_and_transports'];assert len(triangles)==12
    assert {r['triangle'][0][2:] for r in triangles}=={'ABC','ABD','ACD','BCD'}
    # Local input Gram matrices retain the entire face block, not one sampled
    # intensity. Encoders and metrics are those already fixed in the stores.
    ae=tuple(tuple(decode(v) for v in row) for row in b['electron_encoder_numerator'])
    cx=tuple(tuple(decode(v) for v in row) for row in b['fourth_encoder_numerator'])
    kx=decode(b['fourth_encoder_denominator_squared']);assert kx[1]==0
    assert gmm(adj(ae),ae)==scale(2,ident(2)) and gmm(adj(cx),cx)==scale(kx[0],ident(2))
    assert gmm(cx,adj(cx))==scale(kx[0],matrix(data['fourth']['arrows'],12,'N'))
    assert ae==tuple(row for p in data['electron']['face_projectors'] for row in tuple(tuple(decode3(v) for v in row) for row in p))
    fe=[scale(F(1,2),gmm(adj(ae[2*i:2*i+2]),ae[2*i:2*i+2])) for i in range(4)]
    fx=[scale(inv_real74(kx[0]),gmm(adj(cx[2*i:2*i+2]),cx[2*i:2*i+2])) for i in range(6)]
    qe=[scale(2,f) for f in fe];qx=[scale(3,f) for f in fx]
    assert all(trace(f)==(cast(F(1,2)),cast(0)) for f in fe)
    assert all(trace(f)==(cast(F(1,3)),cast(0)) for f in fx)
    assert all(rank_one_projector(q) for q in qe+qx)
    assert qe==[tuple(tuple(decode3(v) for v in row) for row in p) for p in data['electron']['face_projectors']]
    assert {trace(gmm(a,b0)) for a,b0 in combinations(qe,2)}=={(cast(F(1,3)),cast(0))}
    distinct=list(dict.fromkeys(qx));assert len(distinct)==3
    assert {trace(gmm(a,b0)) for a,b0 in combinations(distinct,2)}=={(cast(F(1,4)),cast(0))}
    # Normalized tetrahedral local rays are not one common scalar view.
    assert len(set(qe))==4
    # Adjacent two-face blocks are injective on BOTH spinor components.
    sector_grams=[];major=[];minor=[]
    for i,j in pairs:
        h=plus(fx[i],fx[j]);assert adj(h)==h
        assert trace(h)==(cast(F(2,3)),cast(0)) and det(h)==(cast(F(1,12)),cast(0))
        poly=plus(plus(gmm(h,h),scale(-F(2,3),h)),scale(F(1,12),ident(2)))
        assert poly==scale(0,ident(2)) # Eigenvalues 1/2 and 1/6, both positive.
        q=plus(scale(3,h),scale(-F(1,2),ident(2)));r=plus(ident(2),scale(-1,q))
        assert rank_one_projector(q) and rank_one_projector(r)
        assert gmm(h,q)==scale(F(1,2),q) and gmm(h,r)==scale(F(1,6),r)
        sector_grams.append(h);major.append(q);minor.append(r)
    assert len(set(major))==len(set(minor))==3
    assert {trace(gmm(a,b0)) for a,b0 in combinations(major,2)}=={(cast(F(1,4)),cast(0))}
    # Even choosing one spectral line in EACH sector cannot sew to the fixed
    # global nuclear line: all eight assignments have differing input rays.
    assignments=[]
    for mask in range(8):
        q=[minor[i] if mask&(1<<i) else major[i] for i in range(3)]
        agrees=q[0]==q[1]==q[2];assert not agrees
        assignments.append({'minor_selection_bits':mask,'one_common_input_ray':agrees})
    # Fake repair: opposite panels share a ray but are NOT the retained pairs.
    opposite=[(i,j) for i,j in combinations(range(6),2) if qx[i]==qx[j]]
    assert opposite==[(0,3),(1,5),(2,4)]
    for i,j in opposite:
        assert det(plus(fx[i],fx[j]))==G0
        assert len(set(geo['belt_faces'][i])&set(geo['belt_faces'][j]))==0
    assert all(set(p)!=set(q) for p in pairs for q in opposite)
    checks={'actual_sectors_recovered_from_retained_coordinate_order':True,
        'original_neutron_local_selectors_are_rank_one':expected==actual,
        'proton_triangles_bind_to_all_four_actual_faces':True,
        'face_input_Grams_reconstructed_from_exact_encoders':True,
        'proton_face_views_are_four_distinct_scalar_rays':len(set(qe))==4,
        'each_actual_belt_sector_Gram_has_positive_determinant_one_twelfth':all(det(h)==(cast(F(1,12)),cast(0)) for h in sector_grams),
        'both_sector_eigenchannels_are_nonzero':True,
        'principal_eigenline_rule_fails_common_view_sewing':len(set(major))==3,
        'all_eight_spectral_line_assignments_fail_sewing':all(not a['one_common_input_ray'] for a in assignments),
        'facewise_unitary_comparison_excluded_by_overlap_invariant':F(1,3)!=F(1,4),
        'opposite_pair_repair_changes_the_source_pairing':all(set(p)!=set(q) for p in pairs for q in opposite),
        'source_artifacts_unchanged':all(p.read_bytes()==raw[k] for k,p in paths.items())}
    report={'verification_passed':all(checks.values()),'checks':checks,
        'classification':'local_geometric_restriction_and_spectral_selection_rules_falsified',
        'actual_neutron_face_pairs':pairs,'sector_Gram_trace':'2/3','sector_Gram_determinant':'1/12','sector_Gram_eigenvalues':['1/2','1/6'],
        'normalized_face_ray_overlaps':{'tetrahedron':'1/3','signed_belt_distinct_directions':'1/4'},
        'spectral_assignments':assignments,'inadmissible_opposite_pair_repair':opposite,
        'exact_residual':'A two-face restriction has rank two, whereas every old local nuclear selector has rank one. Spectral truncation is additional loss and its sector-dependent rays do not factor through one shared scalar functional.',
        'scope':'Refutes direct geometric restriction, a common principal-line selection, all eight per-sector eigenline selections, and an isometric face-local E/X identification. It does not rule out source-derived coherent mixing or adapters carrying additional data.',
        'first_missing_constructor':'A spinor-to-cyclic-mode adapter, including relative phases and stated discarded information, that is supplied by the assembly operations and sews across the original local sectors.',
        'disposition':'The source-derived meta-tetrahedron is not completed. Do not replace the original adjacent pairs by opposite pairs, silently truncate an eigenchannel, or identify raw face projectors with normalized input effects.',
        'source_sha256':{k:sha256(v).hexdigest() for k,v in raw.items()},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    store={'field':data['fourth']['field'],'tetrahedral_face_effects':list(map(enc,fe)),
        'belt_face_effects':list(map(enc,fx)),'actual_pair_Grams':list(map(enc,sector_grams)),
        'pair_principal_projectors':list(map(enc,major)),'pair_secondary_projectors':list(map(enc,minor))}
    (BASE/'results/geometry_selected_comparisons.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/geometry_selected_comparison_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)
if __name__=='__main__':main()
