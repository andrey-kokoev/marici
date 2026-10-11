"""Six factorized state comparisons, four faces, and full-state obstructions.
The cross-rank functional is DECLARED, not derived from particle construction.
No source state space is enlarged. All arithmetic is exact.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from hashlib import sha256
import json
import check_coupled_six_piece_belt as c
from check_belt_three_by_twelve import decode as decode_mode
from check_fourth_construction_bridge import decode,rows_of_blocks,matrix,encode_matrix
from check_particle_construction_routes import cast,R,ident,scale,plus,adj,trace,decode3,supports
from check_electron_charge_spin_frontier import gmm,G0
from check_geometric_cycle_reversal import geo
BASE=Path(__file__).resolve().parents[1]

def mm(a,b):return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)
def tr(a):return tuple(zip(*a))
def minus(a,b):return tuple(tuple(x-y for x,y in zip(r,s)) for r,s in zip(a,b))
def enc(m):return [[str(v) for v in row] for row in m]
def token(m):return sha256(json.dumps(enc(m),separators=(',',':')).encode()).hexdigest()
def mode_stage(a,v,d):return tuple(c.total(c.scale(1/d[j],c.mul(a.get((i,j),c.Z),v[j])) for j in range(len(v))) for i in range(len(v)))
def verify_mode(v,d,stages):
    norm=sum(c.norm(z)/di for z,di in zip(v,d));assert c.positive(norm)
    expected={(i,j):c.scale(1/norm,c.mul(a,c.conj(b))) for i,a in enumerate(v) for j,b in enumerate(v) if a!=c.Z and b!=c.Z}
    assert stages['N']==expected
    for m in stages.values():
        assert mode_stage(m,v,d)==v
        assert all(m.get((j,i),c.Z)==c.conj(z) for (i,j),z in m.items())
    return norm

def gram_determinant_polynomial():
    # Universal obstruction for an arbitrary complex row (a+ib,c+id).
    def add(a,b,sgn=1):
        out=dict(a)
        for k,v in b.items():out[k]=out.get(k,0)+sgn*v
        return {k:v for k,v in out.items() if v}
    def mul(a,b):
        out={}
        for ka,va in a.items():
            for kb,vb in b.items():
                k=tuple(x+y for x,y in zip(ka,kb));out[k]=out.get(k,0)+va*vb
        return {k:v for k,v in out.items() if v}
    a,b,c0,d=({tuple(int(i==j) for i in range(4)):1} for j in range(4))
    aa=add(mul(a,a),mul(b,b));bb=add(mul(c0,c0),mul(d,d))
    re=add(mul(a,c0),mul(b,d));im=add(mul(a,d),mul(b,c0),-1)
    return add(mul(aa,bb),add(mul(re,re),mul(im,im)),-1)

def comparisons(lp,ln=None):
    ln=lp if ln is None else ln;I=((F(1),F(0)),(F(0),F(1)))
    return {('E','X'):I,('E','N'):ln,('E','P'):lp,('X','N'):ln,('X','P'):lp,('N','P'):((F(1),),)}
def faces(m):
    return {''.join((a,b,c0)):mm(m[b,c0],m[a,b])==m[a,c0] for a,b,c0 in combinations(('E','X','N','P'),3)}

def main():
    paths={'proton':c.PROTON,'paired_belt':BASE/'results/opposite_branch_belt_store.json',
           'electron':BASE/'results/electron_tetrahedral_spinor_store.json',
           'fourth':BASE/'results/conditional_fourth_spinor_store.json',
           'bridge':BASE/'results/fourth_construction_bridge_store.json'}
    raw={k:p.read_bytes() for k,p in paths.items()};d={k:json.loads(v) for k,v in raw.items()}
    b=d['bridge']
    for k in ('proton','paired_belt','electron','fourth'):assert b['source_sha256'][k]==sha256(raw[k]).hexdigest()
    # Reconstruct the original proton's selected mode in its original raw ports.
    verified,rows=c.verify_proton(d['proton']);assert verified['verified']
    obj=d['proton']['objects'];geometry=obj[obj[d['proton']['root']]['geometry']]['payload']
    points={k:tuple(map(F,v)) for k,v in geo.POINTS.items()}
    for face in ('ABC','ABD','ACD','BCD'):points['F_'+face]=c.mean([points[k] for k in face])
    character=(c.ONE,(c.R(-F(1,2)),c.R(F(1,2))),(c.R(-F(1,2)),c.R(-F(1,2))))
    vectors={r['outer_arrow']:c.mv(c.transpose(tuple(points[k] for k in r['triangle'])),character) for r in geometry['triangles_and_transports']}
    ports=sorted({tuple(r['source'][1:]) for r in rows});indices={p:i for i,p in enumerate(ports)}
    vp=tuple(vectors[e]['xyz'.index(axis)] for e,axis in ports);dp=(F(1),)*len(vp)
    mp={k:{} for k in ('L','G','N')};stage={'raw':'L','local':'G','aligned':'N'}
    for r in rows:mp[stage[r['source'][0]]][indices[tuple(r['target'][1:])],indices[tuple(r['source'][1:])]]=(c.R(F(r['weight_real'])),c.R(F(r['weight_imag_sqrt3'])))
    kp=verify_mode(vp,dp,mp);assert kp==80 and len(vp)==36
    # Neutron candidate: numerator coordinates have metric diag(1/d_i).
    n=d['paired_belt'];vn=tuple(map(decode_mode,n['selected_numerators']));dn=tuple(F(r['d']) for r in n['coordinates'])
    mn={s:{} for s in ('L','G','N')}
    for r in n['arrows']:mn[r['stage']][r['target'],r['source']]=decode_mode(r['numerator'])
    kn=verify_mode(vn,dn,mn);assert len(vn)==36
    # Reverify BOTH isometries against actual retained spinor stages.
    ae=tuple(tuple(decode(z) for z in row) for row in b['electron_encoder_numerator'])
    cx=tuple(tuple(decode(z) for z in row) for row in b['fourth_encoder_numerator'])
    kx=decode(b['fourth_encoder_denominator_squared'])[0]
    assert decode(b['fourth_encoder_denominator_squared'])[1]==0
    assert ae==rows_of_blocks([tuple(tuple(decode3(z) for z in row) for row in p) for p in d['electron']['face_projectors']])
    for key,encoder,den,size,dec in [('electron',ae,cast(2),8,decode3),('fourth',cx,kx,12,decode)]:
        mats={s:[[G0]*size for _ in range(size)] for s in ('L','G','N')}
        for r in d[key]['arrows']:mats[r['stage']][r['target']][r['source']]=dec(r['weight'])
        mats={s:tuple(map(tuple,m)) for s,m in mats.items()}
        assert gmm(adj(encoder),encoder)==scale(den,ident(2))
        assert gmm(encoder,adj(encoder))==scale(den,mats['N'])
        for m in mats.values():assert adj(m)==m and gmm(m,encoder)==encoder
    assert gmm(cx,adj(ae))==tuple(tuple(decode(z) for z in row) for row in b['bridge_numerator'])
    I=((F(1),F(0)),(F(0),F(1)));l0=((F(1),F(0)),);l1=((F(0),F(1)),)
    l2=((F(3,5),F(4,5)),);dimensions={'E':2,'X':2,'N':1,'P':1}
    examples=[]
    for ell in (l0,l1,l2):
        m=comparisons(ell);fs=faces(m);assert len(fs)==4 and all(fs.values())
        assert mm(mm(m['N','P'],m['X','N']),m['E','X'])==mm(m['N','P'],mm(m['X','N'],m['E','X']))==m['E','P']
        q={'E':I,'X':I,'N':ell,'P':ell}
        assert mm(ell,tr(ell))==((F(1),),)
        assert all(mm(v,q[a])==q[z] for (a,z),v in m.items())
        # Reverse adjoints commute too, but only include a chosen line in E/X.
        assert all(mm(tr(m[a,b0]),tr(m[b0,c0]))==tr(m[a,c0]) for a,b0,c0 in combinations(('E','X','N','P'),3))
        assert all(mm(v,tr(v))==tuple(tuple(F(int(i==j)) for j in range(dimensions[z])) for i in range(dimensions[z])) for (a,z),v in m.items())
        assert mm(tr(ell),ell)!=I
        examples.append({'ell':enc(ell),'all_four_faces':fs,'six_root_squares':True,'reverse_inclusion_faces':True})
    m=comparisons(l0);lost=((F(0),),(F(1),));assert mm(l0,lost)==((F(0),),)
    assert mm(l1,lost)==((F(1),),)
    roundtrip=mm(tr(l0),l0);assert minus(I,roundtrip)==((F(0),F(0)),(F(0),F(1)))
    mixed=faces(comparisons(l0,l1));assert mixed=={'EXN':True,'EXP':True,'ENP':False,'XNP':False}
    assert gram_determinant_polynomial()=={}
    # Hostile: a DIFFERENT, wrong-sign fourth protocol also passes these
    # abstract state-coherence tests. It is excluded by retained sign data,
    # not by four-face commutation alone.
    lx=matrix(d['fourth']['arrows'],12,'L')
    px=[tuple(tuple(lx[2*i+a][2*i+b] for b in range(2)) for a in range(2)) for i in range(6)]
    alt=[plus(ident(2),scale(-1,p)) if s<0 else p for p,s in zip(px,d['fourth']['face_signs'])]
    au=rows_of_blocks(alt);assert gmm(adj(au),au)==scale(3,ident(2))
    nu=scale(F(1,3),gmm(au,adj(au)))
    assert adj(nu)==nu and gmm(nu,nu)==nu and trace(nu)==(cast(2),cast(0))
    assert nu!=matrix(d['fourth']['arrows'],12,'N')
    assert supports(alt,nu)=={'L':24,'G':120,'N':120}
    # Matrix words are materialized before SCC compares their canonical hashes.
    arrows=[{'id':a+z,'source':a,'target':z,'map_token':token(v)} for (a,z),v in m.items()]
    cells=[]
    for a,b0,c0 in combinations(('E','X','N','P'),3):
        comp=mm(m[b0,c0],m[a,b0]);arrows.append({'id':a+b0+c0,'source':a,'target':c0,'map_token':token(comp)})
        cells.append({'id':a+b0+c0,'routes':[[a+c0],[a+b0+c0]],'witness':'Exact logical composite, lifted by source-verified J_i isometries.'})
    diagram={'id':'voevodsky-conditional-directed-meta-tetrahedron','objects':[{'id':k,'dimension':v,'type':'selected_complex_state'} for k,v in dimensions.items()],
        'arrows':arrows,'cells':cells,'obstructions':[{'id':'full_state_equivalence','reason':'Ranks 2,2,1,1. Any complex row has singular two-by-two Gram matrix.'}],
        'claims':[{'id':'conditional_directed_coherence','requires':['declared_functional','source_encoders','four_faces']},{'id':'source_derived_meta_tetrahedron','requires':['source_selected_comparison_functional','common_full_construction_record','geometry_and_transport_comparison']}],
        'available_witnesses':['declared_functional','source_encoders','four_faces'],
        'higher_coherence':[{'id':'strict_selected_state_tetrahedron','degree':3,'state':'verified','witness':'Exact three-step composite equals both parenthesizations and the direct EP map; source encoder Gram identities lift it to the raw spaces.'},{'id':'comparison_of_complete_construction_procedures','degree':3,'state':'unsupported'}]}
    (BASE/'contracts/meta-tetrahedron-comparisons.json').write_text(json.dumps(diagram,indent=2)+'\n',encoding='utf-8')
    def mode_encoder(v,metric,k,labels):return {'numerator':[c.encoded(z) for z in v],'complex_encoding':'(a+b sqrt(2)) + i sqrt(3) (c+d sqrt(2))','norm_squared_Qsqrt2':[str(k.a),str(k.b)],'inner_product_diagonal':list(map(str,metric)),'ports':labels,'normalization':'positive sqrt(norm_squared)'}
    store={'convention':'T_ab=J_b B_ab J_a^sharp. Sharp is the declared metric adjoint. Composite proof contracts J_b^sharp J_b=I; maps are stored as exact factors, not dense rounded matrices.',
        'encoders':{'P':mode_encoder(vp,dp,kp,ports),'N':mode_encoder(vn,[1/di for di in dn],kn,[{'triangle':v['triangle'],'axis':v['axis']} for v in n['coordinates']]),
            'E':{'numerator':b['electron_encoder_numerator'],'denominator_squared':b['electron_encoder_denominator_squared'],'inner_product':'identity','complex_encoding':d['fourth']['field']},
            'X':{'numerator':b['fourth_encoder_numerator'],'denominator_squared':b['fourth_encoder_denominator_squared'],'inner_product':'identity','complex_encoding':d['fourth']['field']}},
        'comparison_provenance':'ell=(1,0) is an explicit additional choice, not inferred from equal ranks or endpoint projectors.',
        'six_comparisons':[{'source':a,'target':z,'logical_matrix':enc(v),'formula':f'J_{z} B_{a}{z} J_{a}^sharp'} for (a,z),v in m.items()]}
    checks={'proton_mode_and_return_bound_to_original_geometry':True,'neutron_mode_and_metric_return_reverified':True,
        'electron_and_fourth_encoders_match_retained_returns':True,'all_four_encoders_fixed_by_each_original_stage':True,
        'existing_electron_fourth_bridge_unchanged':True,'all_six_factored_maps_defined':len(m)==6,
        'all_four_oriented_faces_commute':all(faces(m).values()),'all_six_common_input_squares_commute':all(mm(v,{'E':I,'X':I,'N':l0,'P':l0}[a])=={'E':I,'X':I,'N':l0,'P':l0}[z] for (a,z),v in m.items()),
        'two_other_functionals_pass_but_give_different_views':len(examples)==3 and mm(l0,lost)!=mm(l1,lost),
        'independent_nuclear_functionals_break_exactly_two_faces':mixed=={'EXN':True,'EXP':True,'ENP':False,'XNP':False},
        'strict_three_step_tetrahedral_composite_agrees':mm(mm(m['N','P'],m['X','N']),m['E','X'])==m['E','P'],
        'wrong_sign_264_transfer_control_also_admits_state_coherence':gmm(adj(au),au)==scale(3,ident(2)) and all(faces(m).values()),
        'reverse_inclusions_do_not_cover_full_spinor_state':roundtrip!=I,
        'universal_complex_row_Gram_determinant_is_zero':gram_determinant_polynomial()=={},
        'all_source_artifacts_unchanged':all(p.read_bytes()==raw[k] for k,p in paths.items())}
    report={'verification_passed':all(checks.values()),'checks':checks,
        'classification':'conditional_directed_coherence_with_declared_lossy_functional_not_full_state_equivalence',
        'selected_dimensions':{'P':1,'N':1,'E':2,'X':2},'raw_dimensions':{'P':36,'N':36,'E':8,'X':12},
        'orientation':['E','X','N','P'],'six_maps':'T_ab=J_b B_ab J_a^sharp; exact factors retained in companion store',
        'functionals_tested':examples,'mixed_functional_face_results':mixed,
        'return_trip_defect':enc(minus(I,roundtrip)),
        'wrong_sign_control':{'total_transfers':264,'same_fourth_return':False,'same_abstract_face_equations_pass':True,'admissible_under_retained_neutron_sign_requirement':False,'meaning':'State coherence alone does not select the signed 312-transfer candidate; the retained geometry/sign comparison must remain a separate gate.'},
        'universal_obstruction':'For every complex-linear functional ell:C^2->C, det(ell^sharp ell)=0, whereas det(I_2)=1.',
        'stage_scope':'Each stage is self-adjoint in its source metric and fixes J_i. Factored maps therefore intertwine the retained L/G/N operators, but annihilate all source components orthogonal to the selected return.',
        'missing_constructor':'A construction-derived comparison functional, together with common full source data and geometry/transport compatibility. Coherence alone does not select the functional.',
        'disposition':'All four triangles close conditionally as a directed selected-state diagram. Reversing arrows gives inclusions covering only a line in the spinor endpoints. Neither is a reversible full-state tetrahedron or a derived equivalence of the four complete construction procedures.',
        'source_sha256':{k:sha256(v).hexdigest() for k,v in raw.items()},'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/meta_tetrahedron_comparisons.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/meta_tetrahedron_comparison_store.json').write_text(json.dumps(store,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']:raise SystemExit(1)
if __name__=='__main__':main()
