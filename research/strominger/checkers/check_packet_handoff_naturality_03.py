"""Native phase occurrences and reader-complete typed histories, iteration3.
Only the pure proton assembler is invoked; producer entrypoints are not run.
"""
from dataclasses import dataclass,replace,fields
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from itertools import product as pairs
import json
import sys
from assemble_metric_coefficient_protocol import ROOT,A,ZERO,ONE,product,plus,scaled,read_operator,encode,integer_trace
from check_port_incidence_conjectures import identity,factor,transpose
from check_packet_handoff_naturality_02 import load,sub,column
from check_packet_stage_cost_comparison import source_electron_factors
from check_neutrino_three_port_boundary import from_spin
from check_rank_one_return_packets import LineInterface
from check_shared_packet_path_language import Language
from electron_packet_interface import Archive as ElectronArchive,Interface as ElectronInterface,ACTIONS

NIMA=ROOT/'research/nima/checkers'
if str(NIMA) not in sys.path:sys.path.insert(0,str(NIMA))
from assemble_triangle_arrow_source import assemble as pure_proton

CONTRACT=ROOT/'research/strominger/contracts/packet-handoff-naturality-03.v1.json'
OUT=ROOT/'research/strominger/results/packet-handoff-naturality-03-v1.json'
PRIOR=ROOT/'research/strominger/results/packet-handoff-naturality-02-v1.json'
PINPUT=ROOT/'research/nima/inputs/proton-six-arrows.json'
PMANIFEST=ROOT/'research/nima/results/twelve-triangle-1836-arrows.json'
NSTORE=ROOT/'research/strominger/results/neutron-arrow-native-bridge.json'
ESTORE=ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json'
PHASES=('raw','local','aligned')
COMMANDS='LGN'


def read(p):return json.loads(p.read_text(encoding='utf-8'))
def digest(p):return sha256(p.read_bytes()).hexdigest()
def complex_weight(a,b):
    c=[F(0)]*16;c[0]=F(a);c[10]=F(b);return A(tuple(c))
def reject(action,message):
    try:action()
    except ValueError as e:assert message in str(e),(message,str(e))
    else:raise AssertionError('accepted hostile: '+message)


@dataclass(frozen=True)
class History:
    source:str
    initial_phase:int
    commands:tuple=()


def replay(history,source):
    if history.source!=source:raise ValueError('source binding')
    if history.initial_phase not in range(3):raise ValueError('initial phase')
    p=history.initial_phase;epoch=0;trace=[p]
    for letter in history.commands:
        if letter!=COMMANDS[p]:raise ValueError('primitive phase domain')
        epoch+=int(letter=='N');p=(p+1)%3;trace.append(p)
    return p,epoch,trace


def append(history,letter,source):
    out=replace(history,commands=history.commands+(letter,));replay(out,source);return out


def reconstruct(objects):
    # The source constructor returns objects without writing to any result path.
    report,manifest=pure_proton(read(PINPUT));old=read(PMANIFEST)
    assert manifest==old and len(manifest)==1836
    p=objects['proton'];labels=p['source']['source']['coordinates'];maps=[{} for _ in range(3)]
    for a in manifest:
        i=labels.index(':'.join(a['target'][1:]));j=labels.index(':'.join(a['source'][1:]))
        s=PHASES.index(a['source'][0]);assert a['target'][0]==PHASES[(s+1)%3]
        maps[s][i,j]=complex_weight(a['weight_real'],a['weight_imag_sqrt3'])
    assert all(m==p['ops'][k] for k,m in zip(COMMANDS,maps))
    n=objects['neutron'];native=read(NSTORE);coords=native['coordinates']
    d=tuple(F(c['d']) for c in coords)
    def ncoefficient(row):
        c=[F(0)]*16
        for a,mask in zip(row,(0,1,10,11)):c[mask]=F(a)
        return A(tuple(c))
    z=[ncoefficient(c['selected_numerator']) for c in coords]
    assert z[:12]==z[12:24]==z[24:] and d[:12]==d[12:24]==d[24:]
    rho=sum((z[i].flip(8)*z[i]/A(d[i]) for i in range(12)),ZERO)
    L={(i,j):z[i]*z[j].flip(8)/(rho*A(d[j])) for i in range(36) for j in range(36) if i//12==j//12}
    G={(i,j):A(F(1,3)) for i in range(36) for j in range(36) if i%12==j%12}
    N={(i,j):z[i]*z[j].flip(8)/(A(3)*rho*A(d[j])) for i in range(36) for j in range(36)}
    assert [L,G,N]==[n['ops'][k] for k in COMMANDS]
    for letter in COMMANDS:
        restored={(a['target'],a['source']):ncoefficient(a['numerator'])/A(d[a['source']]) for a in native['arrows'] if a['stage']==letter}
        assert restored==n['ops'][letter]
    e=objects['electron'];store=read(ESTORE)
    def ecoefficient(row):
        c=[F(0)]*16
        for a,mask in zip([v for pair in row for v in pair],(0,2,8,10)):c[mask]=F(a)
        return A(tuple(c))
    P=[{(i,j):ecoefficient(z) for i,row in enumerate(face) for j,z in enumerate(row) if ecoefficient(z)!=ZERO} for face in store['face_projectors']]
    L={(2*f+i,2*f+j):x for f,p in enumerate(P) for (i,j),x in p.items()}
    N={}
    for f,g in pairs(range(4),repeat=2):N.update({(2*f+i,2*g+j):x/A(2) for (i,j),x in product(P[f],P[g]).items()})
    assert L==e['ops']['L'] and N==e['ops']['G']==e['ops']['N']
    # Matrix equality does not identify occurrences in different phase fibers.
    Grows={(a['target'],a['source'],json.dumps(a['weight'])) for a in store['arrows'] if a['stage']=='G'}
    Nrows={(a['target'],a['source'],json.dumps(a['weight'])) for a in store['arrows'] if a['stage']=='N'}
    assert Grows==Nrows and len(Grows)==64
    no_stage={(a['target'],a['source'],json.dumps(a['weight'])) for a in store['arrows']}
    assert len(no_stage)==80 and len({(a['target'],a['source']) for a in store['arrows']})==64
    return {'proton_pure_constructor':{'source_arrows':len(read(PINPUT)['arrows']),'native_arrows':len(manifest),
             'exact_typed_manifest_match':True,'native_stage_order':list(COMMANDS),'source_replay_checks':report['closed_walk_union_covers_every_arrow']},
            'neutron_denominator_aware_reconstruction':True,'electron_face_projector_reconstruction':True,
            'phase_typing':{'proton':'explicit original endpoints',
                'neutron':'conservative stage-labelled cover, not stored endpoint phases',
                'electron':'conservative stage-labelled cover, not stored endpoint phases'},
            'electron_stage_erasure':{'original':144,'retain_weight_erase_stage':80,'retain_only_coordinate_pair':64}}


def typed_protocol(o):
    n=o['n'];fs=o['f'];I=identity(n)
    K=[I,fs['L']['K'],fs['G']['K']];D=[I,fs['L']['D'],fs['G']['D']]
    dims=[n,fs['L']['rank'],fs['G']['rank']]
    ops=[o['ops'][k] for k in COMMANDS]
    T=[product(D[(s+1)%3],product(op,K[s])) for s,op in enumerate(ops)]
    for s,op in enumerate(ops):
        assert product(K[(s+1)%3],T[s])==product(op,K[s])
    cycles=[]
    for start in range(3):
        end=identity(dims[start]);raw=K[start]
        for j in range(3):
            s=(start+j)%3;end=product(T[s],end);raw=product(ops[s],raw)
            assert product(K[(s+1)%3],end)==raw
        Q=product(D[start],product(o['ops']['N'],K[start]))
        assert end==Q and product(end,end)==end
        cycles.append({'start_phase':start,'return_rank':integer_trace(end),'full_input_dimension':dims[start]})
    # Raw and local are sections over the SAME supplied local port family,
    # not identical spaces. Every local support block is rank one.
    local_blocks=o['components']['L']
    assert len(local_blocks)==dims[1] and sum(b['dimension'] for b in local_blocks)==dims[0]
    assert all(b['rank']==1 for b in local_blocks)
    local_role='M' if o['m']=='L' else 'C';aligned_role='M' if o['m']=='G' else 'C'
    roles=[local_role,local_role,aligned_role]
    windows=[]
    for start in range(3):
        h=History(digest_source(o),start)
        for _ in range(2):
            phase=replay(h,h.source)[0];h=append(h,COMMANDS[phase],h.source)
        end,epoch,trace=replay(h,h.source)
        windows.append({'phases':trace,'roles':[roles[p] for p in trace],
                        'dimensions':[dims[p] for p in trace],'commands':list(h.commands),'epoch_crossings':epoch})
    # Two atomic edges shift the actual phase by2 mod3: NOT a stationary
    # per-cycle role map with a1- or2-period on these nonconstant role cycles.
    strobes=[]
    for start in range(3):
        phase_trace=[(start+2*k)%3 for k in range(7)]
        role_trace=[roles[p] for p in phase_trace]
        assert phase_trace[0]==phase_trace[3] and phase_trace[0] not in phase_trace[1:3]
        assert all(any(role_trace[i]!=role_trace[i+period] for i in range(7-period)) for period in (1,2))
        strobes.append({'initial_phase':start,'phases':phase_trace,'roles':role_trace,'minimal_phase_and_role_period':3})
    valid_partitions=[]
    # Every equivalence relation on3 phases has this restricted-growth form.
    partitions=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2)]
    for q in partitions:
        valid=all(q[a]!=q[b] or (roles[a]==roles[b] and q[(a+1)%3]==q[(b+1)%3]) for a,b in pairs(range(3),repeat=2))
        if valid:valid_partitions.append(q)
    assert valid_partitions==[(0,1,2)]
    # Native enabled letters already distinguish every pair of phases.
    for s in range(3):
        h=History(digest_source(o),s)
        for letter in COMMANDS:
            if letter==COMMANDS[s]:append(h,letter,h.source)
            else:reject(lambda:append(h,letter,h.source),'primitive phase domain')
    defect=sub(I,o['ops']['L']);v=column(defect)
    assert not product(o['ops']['L'],v) and v
    witness_row=min(i for i,j in v)
    return {'phase_dimensions':dims,'primitive_maps':{k:encode(t) for k,t in zip(COMMANDS,T)},
            'phase_roles_with_raw_base_family_not_retyping':roles,
            'local_raw_fiber_dimensions':[b['dimension'] for b in local_blocks],
            'native_two_arrow_windows':windows,'two_atomic_arrow_strobes':strobes,
            'full_three_edge_returns':cycles,'minimal_role_preserving_deterministic_phase_states':3,
            'role_partition_is_markov_at_atomic_phase_clock':False,
            'raw_local_not_same_full_task':{'raw_minus_L_rank':integer_trace(defect),'input':encode(v),
                'L_reader':'zero','raw_reader_coordinate':witness_row,'raw_reader_value':v[witness_row,0].record()},
            'primitive_N_output_remains_full_raw_type':True}


def digest_source(o):
    return o['source']['source']['provenance']['sha256']


def phase_action_squares(objects,binding,protocols):
    actions={n:[read_operator(r['coefficient_action'],36) for r in binding['bindings'] if r['carrier']==n] for n in ('proton','neutron')}
    K,D=source_electron_factors();adj=lambda x:transpose(x,True)
    faces=[{(i,j):K[2*f+i,j] for i,j in pairs(range(2),repeat=2) if (2*f+i,j) in K} for f in range(4)]
    actions['electron']=[]
    for u0 in ACTIONS:
        u=from_spin(u0)
        perm=[next(i for i,q in enumerate(faces) if product(u,product(p,adj(u)))==q) for p in faces]
        actions['electron'].append({(2*t+i,2*s+j):x for s,t in enumerate(perm) for (i,j),x in u.items()})
    counts={}
    for name,o in objects.items():
        fs=o['f'];K=[identity(o['n']),fs['L']['K'],fs['G']['K']];D=[identity(o['n']),fs['L']['D'],fs['G']['D']]
        maps=[read_operator(protocols[name]['primitive_maps'][k],o['n']) for k in COMMANDS]
        for W in actions[name]:
            a=[product(d,product(W,k)) for d,k in zip(D,K)]
            for k in o['ops'].values():assert product(W,k)==product(k,W)
            for s in range(3):
                assert product(W,K[s])==product(K[s],a[s])
                assert product(a[(s+1)%3],maps[s])==product(maps[s],a[s])
        counts[name]=len(actions[name])
    assert counts=={'proton':2,'neutron':1,'electron':24}
    return counts


def histories(objects):
    rows={}
    for name,o in objects.items():
        key=digest_source(o);K=o['f']['N']['K'];h=History(key,0)
        h3=h
        for c in COMMANDS:h3=append(h3,c,key)
        assert h!=h3 and replay(h,key)==(0,0,[0]) and replay(h3,key)==(0,1,[0,1,2,0])
        for c in 'LG':assert product(o['f'][c]['K'],product(o['f'][c]['D'],K))==K
        x=K
        for c in h3.commands:x=product(o['ops'][c],x)
        assert x==K
        reject(lambda:replay(replace(h,source='other'),key),'source binding')
        reject(lambda:replay(replace(h,initial_phase=3),key),'initial phase')
        reject(lambda:append(h,'G',key),'primitive phase domain')
        # Existing language is an active-image command language, not an
        # occurrence-level phase guard. Its freedom is not an implementation bug.
        r=o['f']['N']['rank'];language=Language(name,key,False,False,identity(r),{})
        free=language.empty()
        for c in 'GNL':free=language.append(free,'stage',c)
        assert language.evaluate(free)==identity(r) and len(free.tokens)==3
        reject(lambda:replay(History(key,0,tuple(c for _,c in free.tokens)),key),'primitive phase domain')
        if name!='electron':
            interface=LineInterface(ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json')
            source=interface.seed(ONE);out=interface.source_step(source,'G')
            assert out.numerator==source.numerator and out.archive!=source.archive
        rows[name]={'empty_and_full_cycle_same_raw_endpoint':True,'distinct_histories_preserved':True,
                    'empty_history_has_three_possible_marked_phase_lifts':len([History(key,s) for s in range(3)]),
                    'existing_image_language_accepts_non_phase_valid_word':list('GNL'),
                    'primitive_phase_requires_initial_port_mark':True}
    # Electron Archive records source and spin word; it does not carry an
    # alignment-entry mark. Freshly exercise its native source recovery as well.
    interface=ElectronInterface();source=interface.seed(((F(1),F(0)),(F(0),F(0))))
    assert interface.recover(interface.extract(source))==source
    assert [f.name for f in fields(ElectronArchive)]==['source_sha256','initial_spinor','word']
    rows['electron']['native_archive_has_alignment_entry_field']=False
    return rows


def main():
    contract=read(CONTRACT);prior=read(PRIOR)
    assert prior['status']=='pass' and all(prior['checks'].values())
    assert all(digest(ROOT/p)==h for p,h in prior['source_sha256'].items())
    objects,binding,pins=load()
    sources=reconstruct(objects);protocols={n:typed_protocol(o) for n,o in objects.items()}
    history=histories(objects);action_counts=phase_action_squares(objects,binding,protocols)
    # Exactly the requested two-edge words, now with NO output-chart adapter.
    selected={'proton':1,'neutron':1,'electron':2}
    wanted={'proton':['C','M','C'],'neutron':['M','C','M'],'electron':['M','C','C']}
    for n,s in selected.items():assert protocols[n]['native_two_arrow_windows'][s]['roles']==wanted[n]
    assert protocols['proton']['phase_roles_with_raw_base_family_not_retyping']==protocols['electron']['phase_roles_with_raw_base_family_not_retyping']
    assert protocols['electron']['phase_dimensions']==[8,4,2]
    checks={k:True for k in (
        'fresh_iteration2_and_all_inherited_source_pins',
        'six_arrow_proton_source_pure_replay_exact_typed_manifest',
        'native_neutron_selected_numerators_and_denominator_reconstruction',
        'native_electron_face_projector_stage_reconstruction',
        'proton_original_endpoint_types_retained_other_stage_covers_declared',
        'all_rectangular_primitive_maps_have_full_input_raw_reader_squares',
        'primitive_N_target_is_raw_not_a_silent_local_image_adapter',
        'raw_and_local_share_native_base_family_but_not_full_state_space',
        'all_three_candidate_words_realized_as_native_two_arrow_windows',
        'baryon_windows_enter_local_electron_window_enters_aligned',
        'proton_and_electron_same_role_cycle_alternative_windows_exist',
        'every_marked_three_edge_return_checked_on_full_phase_input',
        'prepared_packet_atomic_phase_return_three_not_payload_period_one',
        'repeated_two_atomic_arrow_strobes_have_period_three_all_sources',
        'only_three_state_partition_preserves_roles_and_deterministic_successor',
        'coarse_M_C_roles_are_not_markov_at_primitive_atomic_clock',
        'phase_domain_initial_mark_and_source_binding_guards',
        'electron_equal_G_N_weights_do_not_identify_occurrences_or_composability',
        'equal_endpoint_empty_and_full_cycle_histories_remain_distinct',
        'image_command_language_not_misidentified_as_primitive_phase_protocol',
        'electron_native_archive_and_roundtrip_do_not_supply_alignment_entry',
        'native_geometric_and_spin_actions_preserve_new_protocol_maps_via_intertwiners',
        'raw_local_task_mismatch_has_exact_retained_reader_witnesses',
        'no_species_specific_entry_or_two_arrow_reset_derived_from_inspected_sources')}
    # Protect every inspected native producer, but never invoke its main/CLI.
    additions=[PRIOR,CONTRACT,Path(__file__).resolve(),PINPUT,PMANIFEST,NSTORE,ESTORE,
       ROOT/'research/voevodsky/checkers/check_belt_three_by_twelve.py',
       ROOT/'research/voevodsky/checkers/check_electron_tetrahedral_spinor.py',
       ROOT/'research/nima/checkers/assemble_triangle_arrow_source.py',
       ROOT/'research/strominger/checkers/electron_packet_interface.py',
       ROOT/'research/strominger/checkers/check_shared_packet_path_language.py']
    for p in additions:pins[p.relative_to(ROOT).as_posix()]=digest(p)
    for module in tuple(sys.modules.values()):
        path=getattr(module,'__file__',None)
        if path:
            p=Path(path).resolve()
            if p.suffix=='.py' and p.is_relative_to(ROOT/'research'):
                key=p.relative_to(ROOT).as_posix();assert key not in pins or pins[key]==digest(p)
                pins[key]=digest(p)
    assert all(digest(ROOT/p)==h for p,h in pins.items())
    result={'schema':'marici.packet-handoff-naturality-iteration-check.v1','iteration':3,'status':'pass','checks':checks,
       'source_reconstruction':sources,'typed_phase_protocols':protocols,'history_comparison':history,
       'native_action_square_counts':action_counts,
       'proposed_window_initial_phases':selected,'source_selected_proposed_window_origins':False,
       'native_base_family_path_witnesses_without_endpoint_retyping':True,
       'M_C_are_single_fixed_full_objects':False,'stationary_two_atomic_arrow_cycle_law_constructed':False,
       'initial_phase_recoverable_from_active_payload_alone':False,
       'source_native_handoff_constructed':False,'physical_particle_assignment_verified':False,
       'pure_proton_source_assembler_executed_in_memory':True,'native_producer_entrypoints_executed':False,
       'formal_proof_recompiled':False,'next_executable_scope':contract['next_executable_scope'],'source_sha256':pins}
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','iteration':3,'check_groups':len(checks),
        'primitive_phase_dimensions':{n:r['phase_dimensions'] for n,r in protocols.items()},
        'requested_window_origins':selected,'minimal_phase_states':3,
        'two_atomic_arrow_strobe_period':3,'species_specific_entry_selected':False},indent=2))


if __name__=='__main__':main()
