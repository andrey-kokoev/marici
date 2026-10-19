"""Native port geometry, partial isometries, tetrahedral code and cycle origin.
Retained source inspection only: no native producer or shared source is changed.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from itertools import product as pairs
import json
import sys
from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,read_operator,product,plus,scaled,sharp,integer_trace,encode
from check_port_incidence_conjectures import identity,transpose,factor,incidence,pivot_columns
from check_packet_stage_cost_comparison import source_electron_factors
from check_neutrino_three_port_boundary import from_spin
from electron_packet_interface import ACTIONS,STORE

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-02.v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-02-v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-01-v1.json'
BINDING=ROOT/'research/strominger/results/baryon-coefficient-spin-binding-v1.json'
MERKLE=ROOT/'research/voevodsky/results/proton_merkle_store.json'
BELT=ROOT/'research/voevodsky/results/belt_three_by_twelve_store.json'


def read(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def sub(a,b):return plus(a,scaled(-ONE,b))
def adj(a):return transpose(a,True)
def kron(a,b,width):return {(i*width+k,j*width+l):x*y for (i,j),x in a.items() for (k,l),y in b.items() if x*y!=ZERO}
def trace(a):return sum((x for (i,j),x in a.items() if i==j),ZERO)
def column(a):
    j=min(j for i,j in a)
    return {(i,0):x for (i,k),x in a.items() if k==j}
def record_factor(f):return {k:encode(f[k]) for k in ('K','D','gram')}|{'rank':f['rank'],'columns':f['columns']}


def load():
    prior=read(PRIOR);binding=read(BINDING)
    assert prior['status']==binding['status']=='pass'
    pins={}
    for r in (prior,binding):
        assert all(digest(ROOT/p)==h for p,h in r['source_sha256'].items()),'stale prerequisite'
        for p,h in r['source_sha256'].items():
            assert p not in pins or pins[p]==h
            pins[p]=h
    objects={}
    for name in ('proton','neutron','electron'):
        path=ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json'
        s=read(path);n=len(s['source']['metric']);metric=tuple(map(F,s['source']['metric']))
        ops={k:read_operator(s['operators'][k],n) for k in 'LGN'}
        for k,key in (('L','local'),('G','alignment')):assert ops[k]==read_operator(s['source'][key],n)
        assert product(ops['L'],ops['G'])==product(ops['G'],ops['L'])==ops['N']
        for p in ops.values():assert product(p,p)==p and sharp(p,metric)==p
        fs={k:factor(p,n,metric) for k,p in ops.items()}
        assert fs['L']['rank']!=fs['G']['rank'],'equal-capacity role rule deliberately undefined'
        m,c=sorted('LG',key=lambda k:fs[k]['rank'])
        fm,fc=fs[m],fs[c]
        B=product(fc['D'],product(ops[c],fm['K']))
        R=product(fm['D'],product(ops[m],fc['K']))
        qm=product(R,B);qc=product(B,R)
        assert product(fc['K'],B)==product(ops[c],fm['K'])
        assert product(fm['K'],R)==product(ops[m],fc['K'])
        assert product(adj(B),fc['gram'])==product(fm['gram'],R)
        assert product(qm,qm)==qm and product(qc,qc)==qc
        assert product(B,product(R,B))==B and product(R,product(B,R))==R
        assert integer_trace(qm)==integer_trace(qc)==fs['N']['rank']
        assert qm==product(fm['D'],product(ops['N'],fm['K']))
        assert qc==product(fc['D'],product(ops['N'],fc['K']))
        components={}
        for k in 'LG':
            cc=incidence(ops[k]);rows=[]
            for comp in cc:
                assert comp['inputs']==comp['outputs'] and comp['complete']
                ids=comp['inputs'];p={(i,j):x for (i,j),x in ops[k].items() if i in ids and j in ids}
                assert product(p,p)==p
                rows.append({'coordinates':ids,'labels':[s['source']['coordinates'][i] for i in ids],
                             'dimension':len(ids),'rank':integer_trace(p)})
            components[k]=rows
        objects[name]={'source':s,'n':n,'metric':metric,'ops':ops,'f':fs,'m':m,'c':c,
                      'B':B,'R':R,'qm':qm,'qc':qc,'components':components}
        pins[path.relative_to(ROOT).as_posix()]=digest(path)
    for p in (PRIOR,BINDING,MERKLE,BELT,STORE,CONTRACT,Path(__file__).resolve()):pins[p.relative_to(ROOT).as_posix()]=digest(p)
    return objects,binding,pins


def geometry(objects):
    p=objects['proton'];merkle=read(MERKLE)
    geometry=merkle['objects'][merkle['objects'][merkle['root']]['geometry']]['payload']
    placements=sorted(geometry['triangles_and_transports'],key=lambda r:r['outer_arrow'])
    assert [r['outer_arrow']+':'+a for r in placements for a in 'xyz']==p['source']['source']['coordinates']
    U={(3*t+i,3*t+j):A(F(x)) for t,r in enumerate(placements) for i,row in enumerate(r['rotation']) for j,x in enumerate(row) if F(x)}
    assert product(adj(U),U)==identity(36)
    L,G=[product(adj(U),product(p['ops'][k],U)) for k in 'LG']
    pm={(i,j):x for (i,j),x in L.items() if i<3 and j<3}
    pc={(i//3,j//3):x for (i,j),x in G.items() if i%3==j%3==0}
    assert L==kron(identity(12),pm,3) and G==kron(pc,identity(3),3)
    assert integer_trace(pm)==integer_trace(pc)==1
    assert product(pm,pm)==pm and product(pc,pc)==pc
    # G's physical-coordinate components are transported body-axis families,
    # not naively the three globally fixed x/y/z labels.
    assert any(len({label.rsplit(':',1)[1] for label in b['labels']})>1 for b in p['components']['G'])
    n=objects['neutron'];L,G=[n['ops'][k] for k in 'LG']
    pc_n={(i,j):x for (i,j),x in L.items() if i<12 and j<12}
    pm_n={(i//12,j//12):x for (i,j),x in G.items() if i%12==j%12==0}
    assert L==kron(identity(3),pc_n,12) and G==kron(pm_n,identity(12),12)
    assert integer_trace(pc_n)==integer_trace(pm_n)==1
    assert n['metric'][:12]==n['metric'][12:24]==n['metric'][24:]
    store=read(BELT)
    assert [f"triangle-{r['triangle']}:axis-{r['axis']}" for r in store['coordinates']]==n['source']['source']['coordinates']
    assert n['metric']==tuple(1/F(r['d']) for r in store['coordinates'])
    ratios={}
    for name,o in objects.items():
        fs=o['f'];lhs=fs['L']['rank']*fs['G']['rank'];rhs=o['n']*fs['N']['rank']
        ratios[name]={'rankL_times_rankG':lhs,'raw_dimension_times_rankN':rhs,'independent_tensor_preparation':lhs==rhs}
    assert ratios['proton']['independent_tensor_preparation'] and ratios['neutron']['independent_tensor_preparation']
    assert not ratios['electron']['independent_tensor_preparation']
    return {'proton':{'raw_body_frame':encode(U),'C_factor_dimension':12,'M_factor_dimension':3,
                     'L_body':'I_C tensor P_M','G_body':'P_C tensor I_M','P_M':encode(pm),'P_C':encode(pc)},
            'neutron':{'M_factor_dimension':3,'C_factor_dimension':12,
                       'L':'I_M tensor P_C','G':'P_M tensor I_C','P_M':encode(pm_n),'P_C':encode(pc_n)},
            'tensor_rank_identity':ratios,
            'electron_obstruction':'Any complementary-factor projections I_C tensor P_M and P_C tensor I_M obey rankL*rankG=raw_dimension*rankN. Actual electron violates it (8 !=16), independent of chart.'}


def electron_code(o):
    K,D=source_electron_factors();fm,fc=o['f'][o['m']],o['f'][o['c']]
    assert o['m']=='G' and o['c']=='L' and product(K,D)==o['ops']['G']
    assert product(D,K)==identity(2)
    code=product(fc['D'],K);decode=product(D,fc['K'])
    assert product(decode,code)==identity(2) and product(code,decode)==o['qc']
    assert product(adj(code),product(fc['gram'],code))==scaled(A(2),identity(2))
    assert product(fc['K'],code)==K
    effects=[]
    for face in range(4):
        slot={(2*face+i,2*face+i):ONE for i in range(2)}
        effect=product(D,product(slot,K));effects.append(effect)
        assert effect==adj(effect) and trace(effect)==A(F(1,2))
        assert product(effect,effect)==scaled(A(F(1,2)),effect)
    assert plus(*effects)==identity(2)
    for i,j in pairs(range(4),repeat=2):assert trace(product(effects[i],effects[j]))==A(F(1,4) if i==j else F(1,12))
    vectors={(2*i+j,f):x for f,e in enumerate(effects) for (i,j),x in e.items()}
    assert len(pivot_columns(vectors,4,4))==4
    assert product(effects[0],effects[1])!=product(effects[1],effects[0])
    return {'logical_to_four_face_channels':encode(code),'face_decoder':encode(decode),
            'logical_metric':'2 I (native unnormalized stack convention)',
            'face_effects':list(map(encode,effects)),'effect_linear_span_dimension':4,
            'off_diagonal_effect_trace_overlap':'1/12','noncommuting_face_readers':True,
            'four_native_faces_not_twelve_chosen_sector_charts':True}


def native_squares(objects,binding):
    actions={n:[read_operator(r['coefficient_action'],36) for r in binding['bindings'] if r['carrier']==n] for n in ('proton','neutron')}
    K,D=source_electron_factors()
    faces=[{(i,j):K[2*f+i,j] for i,j in pairs(range(2),repeat=2) if (2*f+i,j) in K} for f in range(4)]
    actions['electron']=[]
    for action in ACTIONS:
        u=from_spin(action)
        perm=[next(i for i,q in enumerate(faces) if product(u,product(p,adj(u)))==q) for p in faces]
        W={(2*target+i,2*source+j):x for source,target in enumerate(perm) for (i,j),x in u.items()}
        assert product(W,K)==product(K,u)
        actions['electron'].append(W)
    rows={}
    for name,o in objects.items():
        m,c=o['m'],o['c'];fm,fc=o['f'][m],o['f'][c];cert=[]
        for W in actions[name]:
            assert product(sharp(W,o['metric']),W)==identity(o['n'])
            for p in o['ops'].values():assert product(W,p)==product(p,W)
            am=product(fm['D'],product(W,fm['K']));ac=product(fc['D'],product(W,fc['K']))
            assert product(W,fm['K'])==product(fm['K'],am)
            assert product(W,fc['K'])==product(fc['K'],ac)
            assert product(ac,o['B'])==product(o['B'],am)
            assert product(am,o['R'])==product(o['R'],ac)
            assert product(adj(am),product(fm['gram'],am))==fm['gram']
            assert product(adj(ac),product(fc['gram'],ac))==fc['gram']
            cert.append({'M_action':encode(am),'C_action':encode(ac)})
        rows[name]={'checked_actions':len(cert),'channel_action_squares':cert}
    assert {n:r['checked_actions'] for n,r in rows.items()}=={'proton':2,'neutron':1,'electron':24}
    return rows


def frame_control(o):
    n=o['n'];S=plus(identity(n),{(0,3):A(F(2,3))});Si=sub(identity(n),{(0,3):A(F(2,3))})
    assert product(S,Si)==identity(n)
    H={(i,i):A(x) for i,x in enumerate(o['metric'])};H2=product(adj(Si),product(H,Si))
    ops={k:product(S,product(p,Si)) for k,p in o['ops'].items()}
    for p in ops.values():assert product(H2,p)==product(adj(p),H2)
    fs={k:{'K':product(S,f['K']),'D':product(f['D'],Si)} for k,f in o['f'].items()}
    for k,f in fs.items():
        assert product(f['K'],f['D'])==ops[k]
        assert product(adj(f['K']),product(H2,f['K']))==o['f'][k]['gram']
    m,c=o['m'],o['c']
    assert product(fs[c]['D'],product(ops[c],fs[m]['K']))==o['B']
    for k in 'LG':
        total={}
        for block in o['components'][k]:
            P={(i,i):ONE for i in block['coordinates']};P2=product(S,product(P,Si))
            assert product(P2,P2)==P2 and integer_trace(P2)==len(block['coordinates'])
            assert product(H2,P2)==product(adj(P2),H2)
            total=plus(total,P2)
        assert total==identity(n)
    # All raw linear readers transport as r'=r S^-1; r' K'=r K.
    assert product(Si,fs[m]['K'])==o['f'][m]['K']
    return {'nonmonomial_raw_shear':encode(S),'transported_metric':encode(H2),
            'image_maps_and_primitive_ports_transport':True,
            'arbitrary_chart_sparsity_is_not_a_new_physical_port_decomposition':True}


def cyclic_task(o):
    f=o['f'];m,c=o['m'],o['c'];L,G,N=[o['ops'][k] for k in 'LGN']
    roles={'L':'M' if m=='L' else 'C','G':'M' if m=='G' else 'C','N':'M' if m=='L' else 'C'}
    # N returns raw coordinates; exporting its L-image chart is an EXPLICIT
    # lossless endpoint adapter, not a claim about its primitive arrow type.
    adapters={'L':f['L']['D'],'G':f['G']['D'],'N':f['L']['D']}
    encoders={'L':f['L']['K'],'G':f['G']['K'],'N':f['L']['K']}
    operators={'L':L,'G':G,'N':N};letters='LGN';windows=[]
    for start in range(3):
        word=[letters[(start+j)%3] for j in range(3)]
        transitions=[]
        for a,b in zip(word,word[1:]):
            T=product(adapters[b],product(operators[b],encoders[a]))
            # Input is the complete corresponding stage output, not only a
            # selected coordinate column. Check every projected raw reader.
            assert product(encoders[b],product(T,product(adapters[a],operators[a])))==product(operators[b],operators[a])
            transitions.append(encode(T))
        windows.append({'phases':word,'roles':[roles[k] for k in word],'transitions':transitions})
    # Canonical grammar of partial isometries, not an extra sector bit.
    fm,fc=f[m],f[c];B,R=o['B'],o['R'];q=o['qc']
    defect=sub(identity(fc['rank']),q);v=column(defect)
    assert product(R,v)=={} and product(q,v)=={}
    raw=product(fc['K'],v)
    assert raw and product(o['ops'][c],raw)==raw
    assert not product(N,raw)
    row=min(i for i,j in raw)
    out={'role_by_phase_with_declared_N_adapter':roles,'native_cyclic_windows':windows,
         'full_C_defect_rank':integer_trace(defect),'full_M_defect_rank':fm['rank']-f['N']['rank'],
         'full_C_not_recoverable_from_its_return_code':{'C_input':encode(v),'raw_input':encode(raw),
           'same_decoded_M_as_zero':True,'raw_reader_coordinate':row,'raw_reader_value':raw[row,0].record()},
         'N_primitive_raw_output_not_silently_retyped':True}
    if o['qm']==identity(fm['rank']):
        # Same complete M input task, same projected source and every raw
        # endpoint reader. Terminal M vs encoded C is a format/history choice.
        assert product(fc['K'],product(q,B))==product(fm['K'],product(R,B))==fm['K']
        out['encode_then_persist_vs_decode']={'persist_roles':['M','C','C'],'roundtrip_roles':['M','C','M'],
           'equal_all_raw_endpoint_readers_for_every_M_input':True,
           'equivalent_terminal_M_and_code_C_via_declared_B_adapter':True,
           'equivalent_full_M_and_full_C_preparation_tasks':False}
    return out


def main():
    contract=read(CONTRACT);objects,binding,pins=load()
    geom=geometry(objects);ec=electron_code(objects['electron']);native=native_squares(objects,binding)
    frames={n:frame_control(o) for n,o in objects.items()};tasks={n:cyclic_task(o) for n,o in objects.items()}
    expected={'proton':[12,3,1],'neutron':[3,12,1],'electron':[4,2,2]}
    for n,o in objects.items():assert [o['f'][k]['rank'] for k in 'LGN']==expected[n]
    assert [len(objects[n]['components'][k]) for n,k in pairs(('proton','neutron','electron'),'LG')]==[12,3,3,12,4,1]
    assert [b['rank'] for b in objects['electron']['components']['G']]==[2]
    assert tasks['proton']['native_cyclic_windows'][0]['roles']==['C','M','C']
    assert tasks['neutron']['native_cyclic_windows'][0]['roles']==['M','C','M']
    assert tasks['electron']['native_cyclic_windows'][1]['roles']==['M','C','C']
    assert tasks['proton']['role_by_phase_with_declared_N_adapter']==tasks['electron']['role_by_phase_with_declared_N_adapter']
    checks={k:True for k in (
       'fresh_source_hashes_and_actual_projector_metric_relations',
       'native_port_incidence_reconstructed_with_internal_multiplicity',
       'common_capacity_role_constructor_without_particle_name_branch',
       'metric_adjoint_cross_maps_and_exact_partial_isometry_identities',
       'full_stage_reader_squares_not_only_active_vectors',
       'proton_actual_geometric_transport_frames_give_independent_tensor_factors',
       'proton_alignment_ports_are_transported_body_axes_not_global_xyz',
       'neutron_actual_intrinsic_metric_and_sector_tensor_factors',
       'electron_rank_identity_obstructs_complementary_tensor_preparation',
       'electron_logical_to_four_face_line_encoder_is_lossless',
       'electron_four_effects_are_tetrahedral_tight_and_informationally_complete',
       'electron_noncommuting_readers_not_a_classical_two_label_partition',
       'source_bound_baryon_generators_intertwine_both_channel_spaces',
       'all24_native_electron_face_spin_actions_intertwine_code',
       'nonmonomial_raw_frame_metric_and_primitive_ports_transport',
       'native_three_phase_windows_have_full_projected_reader_squares',
       'all_three_proposed_words_have_source_bound_realizations_with_declared_adapter',
       'proton_and_electron_role_cycle_agrees_up_to_entry_phase',
       'electron_persistence_and_decoding_agree_for_same_complete_M_input_task',
       'full_C_preparation_distinguished_from_active_return_code',
       'cycle_origin_and_return_output_format_are_not_selected_by_endpoint_data')}
    for module in tuple(sys.modules.values()):
        file=getattr(module,'__file__',None)
        if file:
            p=Path(file).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                key=p.relative_to(ROOT).as_posix();assert key not in pins or pins[key]==digest(p)
                pins[key]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items()),'source changed during check'
    rows={n:{'stage_image_dimensions':[o['f'][k]['rank'] for k in 'LGN'],
              'M_stage':o['m'],'C_stage':o['c'],'M_C_dimensions':[o['f'][o['m']]['rank'],o['f'][o['c']]['rank']],
              'source_port_components':o['components'],'factors':{k:record_factor(f) for k,f in o['f'].items()},
              'M_to_C':encode(o['B']),'C_to_M':encode(o['R']),
              'M_return_projector':encode(o['qm']),'C_return_projector':encode(o['qc'])} for n,o in objects.items()}
    report={'schema':'marici.packet-handoff-naturality-iteration-check.v1','status':'pass','iteration':2,
            'checks':checks,'native_interfaces':rows,'geometric_tensor_preparations':geom,
            'electron_native_face_code':ec,'native_action_squares':native,'frame_controls':frames,'cycle_tasks':tasks,
            'conditional_source_bound_typed_path_realizations_constructed':True,
            'common_partial_isometry_interface_constructed':True,
            'source_selected_cycle_origin':False,'source_selected_terminal_format':False,
            'full_C_task_identified_with_return_code':False,
            'source_native_handoff_constructed':False,'physical_particle_assignment_verified':False,
            'formal_proof_recompiled':False,'native_producers_executed':False,
            'next_executable_scope':contract['next_executable_scope'],'source_sha256':pins}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':2,'check_groups':len(checks),
          'M_C_dimensions':{n:r['M_C_dimensions'] for n,r in rows.items()},
          'native_phase_words':{n:[w['roles'] for w in t['native_cyclic_windows']] for n,t in tasks.items()},
          'tetrahedral_face_effect_span':4,'source_selected_cycle_origin':False},indent=2))


if __name__=='__main__':main()
