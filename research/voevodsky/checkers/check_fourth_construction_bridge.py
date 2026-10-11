"""Materialize a state-preserving electron/fourth bridge and its route square.
All matrices are exact. Positive normalizers are stored as numerators with
one explicitly retained positive square-root denominator.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_particle_construction_routes import R,cast,ident,scale,plus,adj,trace,encode,decode3
from check_electron_charge_spin_frontier import ga,gs,gm,gt,gmm,G0,G1
from check_coupled_six_piece_belt import PROTON,verify_proton,total,ONE
from check_belt_three_by_twelve import decode as decode_weight

BASE=Path(__file__).resolve().parents[1]
def decode(z):return tuple(R(tuple(map(F,c))) for c in z)
def matrix(rows,size,stage):
    out=[[G0]*size for _ in range(size)]
    for a in rows:
        if a['stage']==stage:out[a['target']][a['source']]=decode(a['weight'])
    return tuple(map(tuple,out))
def rows_of_blocks(ps):return tuple(row for p in ps for row in p)
def encode_matrix(m):return [[encode(z) for z in row] for row in m]

def main():
    files={'fourth':BASE/'results/conditional_fourth_spinor_store.json',
           'electron':BASE/'results/electron_tetrahedral_spinor_store.json',
           'paired_belt':BASE/'results/opposite_branch_belt_store.json','proton':PROTON,
           'geometry':BASE/'results/four_six_center_cones.json',
           'routes':BASE/'results/particle_construction_routes.json'}
    raw={k:p.read_bytes() for k,p in files.items()};d={k:json.loads(v) for k,v in raw.items()}
    x,e=d['fourth'],d['electron'];assert d['routes']['verification_passed']
    assert x['source_sha256']['electron']==sha256(raw['electron']).hexdigest()
    assert x['source_sha256']['paired_belt']==sha256(raw['paired_belt']).hexdigest()
    assert x['source_sha256']['geometry']==sha256(raw['geometry']).hexdigest()
    lx=matrix(x['arrows'],12,'L');nx=matrix(x['arrows'],12,'N')
    px=[tuple(tuple(lx[2*i+a][2*i+b] for b in range(2)) for a in range(2)) for i in range(6)]
    pe=[tuple(tuple(decode3(z) for z in row) for row in p) for p in e['face_projectors']]
    ax,ae=rows_of_blocks(px),rows_of_blocks(pe)
    S=tuple(tuple(decode(z) for z in row) for row in x['frame_operator'])
    inverse=tuple(tuple(decode(z) for z in row) for row in x['frame_inverse'])
    ne=scale(F(1,2),gmm(ae,adj(ae)))
    assert gmm(adj(ax),ax)==S and gmm(adj(ae),ae)==scale(2,ident(2))
    root74=R((0,0,1,0));a=root74*F(5,74);delta=root74*F(21,74)
    sy=((G0,(R(),cast(-1))),((R(),cast(1)),G0))
    B=plus(scale(3+delta,ident(2)),scale(3*a,sy))
    k=delta*delta*(6+2*delta)
    # W=B/sqrt(k) is the POSITIVE inverse square root of S:
    # B is Hermitian with eigenvalues 3+delta +/-3a, both positive.
    # delta>0, 0<a<1, k>0. The remaining identities are checked exactly.
    assert adj(B)==B and gmm(B,B)==scale(k,inverse)
    assert gmm(B,S)==gmm(S,B)
    c=gmm(ax,B) # J_x=c/sqrt(k)
    assert gmm(adj(c),c)==scale(k,ident(2))
    assert gmm(c,adj(c))==scale(k,nx)
    f=gmm(c,adj(ae)) # T=f/sqrt(2k)
    assert gmm(adj(f),f)==scale(2*k,ne)
    assert gmm(f,adj(f))==scale(2*k,nx)
    assert gmm(nx,f)==gmm(f,ne)==f
    # Direct route z -> J_x z equals z -> J_e z -> T J_e z.
    assert gmm(f,ae)==scale(2,c)
    # Scalar face-count normalization passes direct/through route equality
    # but fails isometry: route agreement alone is not sufficient.
    f0=gmm(ax,adj(ae)) # naive bridge /sqrt(6)
    assert gmm(f0,ae)==scale(2,ax)
    assert gmm(adj(f0),f0)!=scale(6,ne)
    # A phase-altered bridge preserves endpoints but changes the rooted route.
    minus=scale(-1,f)
    assert gmm(adj(minus),minus)==scale(2*k,ne)
    assert gmm(minus,adj(minus))==scale(2*k,nx)
    assert gmm(minus,ae)!=scale(2,c)
    # Source-state rank obstruction applies to lossless selected-state views,
    # not to arbitrary construction records or explicitly lossy projections.
    pv,pr=verify_proton(d['proton']);assert pv['verified'] and len(pr)==1836
    nb=d['paired_belt'];metric=[F(v['d']) for v in nb['coordinates']]
    ntrace=total(tuple(v/metric[ar['target']] for v in decode_weight(ar['numerator'])) for ar in nb['arrows'] if ar['stage']=='N' and ar['target']==ar['source'])
    assert ntrace==ONE
    assert trace(ne)==trace(nx)==(cast(2),cast(0))
    checks={
        'source_stores_and_route_receipt_bound':True,
        'fourth_positive_normalizer_reconstructed_exactly':gmm(B,B)==scale(k,inverse),
        'fourth_encoder_is_an_isometry':gmm(adj(c),c)==scale(k,ident(2)),
        'fourth_encoder_recovers_retained_return':gmm(c,adj(c))==scale(k,nx),
        'bridge_source_projector_is_electron_return':gmm(adj(f),f)==scale(2*k,ne),
        'bridge_target_projector_is_fourth_return':gmm(f,adj(f))==scale(2*k,nx),
        'direct_and_electron_routes_agree_on_all_inputs':gmm(f,ae)==scale(2,c),
        'naive_route_equality_does_not_imply_state_preservation':gmm(f0,ae)==scale(2,ax) and gmm(adj(f0),f0)!=scale(6,ne),
        'endpoint_projectors_do_not_fix_rooted_bridge_phase':gmm(minus,ae)!=scale(2,c),
        'original_proton_and_belt_returns_have_only_one_selected_mode':pv['verified'] and ntrace==ONE,
        'all_input_files_unchanged':all(p.read_bytes()==raw[key] for key,p in files.items()),
    }
    report={'verification_passed':all(checks.values()),'checks':checks,
        'constructed_route':'J_e=A_e/sqrt(2), J_x=C/sqrt(k), T=F/sqrt(2k), with C=A_x B and F=C A_e*',
        'identities':['T J_e=J_x','T* T=N_e','T T*=N_x','J_x* J_x=I_2'],
        'bridge_shape':[12,8],'coherent_dimension':2,
        'normalizer':{'delta':'21/sqrt(74)','B':'(3+delta)I+(15/sqrt(74))sigma_y','k':'delta^2*(6+2delta)','W':'B/sqrt(k), positive square root convention'},
        'negative_controls':{'naive':'Using only sqrt(3) permits route equality but loses isometry.',
            'phase':'T and -T preserve identical endpoint projectors; only T agrees with the retained common-input route.'},
        'relationship_to_original_three':{'electron':'An explicit lossless bridge is constructed in the retained common spinor frame.',
            'neutron_candidate':'Geometry and signed face data are retained; its old rank-one selected state is not identified losslessly with the fourth doublet.',
            'proton':'Its geometry supplies the seed; its old rank-one selected state is not identified losslessly with the fourth doublet.'},
        'scope':'One coherent comparison square is constructed, not all six edges and four coherent faces of the proposed meta-tetrahedron. Lossy or history-retaining views require explicit additional maps.',
        'source_sha256':{key:sha256(v).hexdigest() for key,v in raw.items()},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    store={'field':x['field'],'source_sha256':report['source_sha256'],'electron_encoder_numerator':encode_matrix(ae),
           'electron_encoder_denominator_squared':encode((cast(2),cast(0))),
           'fourth_encoder_numerator':encode_matrix(c),'fourth_encoder_denominator_squared':encode((k,cast(0))),
           'bridge_numerator':encode_matrix(f),'bridge_denominator_squared':encode((2*k,cast(0))),
           'positive_normalizer_numerator':encode_matrix(B),'normalizer_denominator_squared':encode((k,cast(0)))}
    (BASE/'results/fourth_construction_bridge.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/fourth_construction_bridge_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)

if __name__=='__main__':main()
