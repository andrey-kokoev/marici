"""First source-bound open-channel compilation of the three-arrow receiver.

Bridge rule: primitive vertex i uses the normalized amplitude of the source
triangle on marked face ABC whose outer arrow starts at i. No phase is added
to that bridge. Keep arrival A and the two arrival differences as outputs.
"""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from copy import deepcopy
import json
from check_geometric_cycle_reversal import geo, SOURCE, verify as verify_proton, ONE, ZERO, conj
from check_reversed_coefficient_attachment import weight, times, plus, div, sub, multiply, encode, rank
from check_three_arrow_receiver import WEIGHTS, OMEGA, OMEGA2

BASE=Path(__file__).resolve().parents[1]
OPEN_SOURCE=BASE/'results/receiver_source_generation_store.json'

def digest(record):
    return sha256(b'marici.compiled-three-arrow-receiver.v1\0'+json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def make_arrow(s,t,w,role):
    assert w!=ZERO
    return {'source':list(s),'target':list(t),'weight_real':str(w[0]),'weight_imag_sqrt3':str(w[1]),'role':role}

def construct(source,opened):
    proof,rows=verify_proton(source)
    expected={(a,b) for a in 'ABCD' for b in 'ABCD' if a!=b}|{(a,'e') for a in 'ABC'}
    packets=opened['packets']
    if len(packets)!=15 or {(p['source'],p['target']) for p in packets}!=expected: raise ValueError('primitive source changed')
    if opened['proton_protocol_root']!=source['root']: raise ValueError('source root')
    if set(opened['records'])!=set('ABCD')|{'e'}: raise ValueError('record endpoints')
    for label,entry in opened['records'].items():
        if entry['outgoing_packet_ids']!=[p['id'] for p in packets if p['source']==label]: raise ValueError('outgoing references')
        if entry['incoming_packet_ids']!=[p['id'] for p in packets if p['target']==label]: raise ValueError('incoming references')
    if opened['records']['e']['outgoing_packet_ids']: raise ValueError('receiver not terminal')
    if opened['receiver_contract']['incoming_weights']!={a:encode(w) for a,w in zip('ABC',WEIGHTS)}: raise ValueError('receiver character')
    objects=source['objects']; geometry=objects[objects[source['root']]['geometry']]['payload']
    triangles=geometry['triangles_and_transports']
    selected={r['outer_arrow'][0]:r for r in triangles if r['triangle'][0]=='F_ABC'}
    if set(selected)!=set('ABC'): raise ValueError('marked face channels')
    P=dict(geo.POINTS)
    for f in ('ABC','ABD','ACD','BCD'): P['F_'+f]=geo.mean([P[k] for k in f])
    c=(ONE,OMEGA,OMEGA2); new=[]; bindings={}; vectors={}
    for r in triangles:
        vectors[r['outer_arrow']]=geo.zmv(geo.transpose(tuple(P[k] for k in r['triangle'])),c)
    for i,a in enumerate('ABC'):
        r=selected[a]; edge=r['outer_arrow']; v=vectors[edge]
        norm=sum(geo.znorm(z) for z in v)
        extraction=[geo.zscale(conj(z),1/norm) for z in v]
        channel=('receiver-source','ABC',a); arrival=('receiver-arrival','e',a)
        for axis,w in zip('xyz',extraction): new.append(make_arrow(('local',edge,axis),channel,w,'mode-amplitude-extraction'))
        new.append(make_arrow(channel,arrival,WEIGHTS[i],'primitive-receiver-leg'))
        bindings[a]={'source_triangle':edge,'source_ports':[['local',edge,axis] for axis in 'xyz'],
                     'normalization':str(norm),'extraction_weights':encode(extraction)}
    for a,b in [('A','B'),('A','C')]:
        target=('receiver-defect','e',a+b)
        new.append(make_arrow(('receiver-arrival','e',a),target,ONE,'compatibility-difference'))
        new.append(make_arrow(('receiver-arrival','e',b),target,(-Q(1),Q(0)),'compatibility-difference'))
    record={'kind':'compiled-three-arrow-receiver','proton_root':source['root'],
        'open_source_digest':digest(opened),'marked_face':'ABC',
        'bridge_rule':'vertex i reads the normalized amplitude on its marked-face outgoing source triangle; no character twist in extraction',
        'bindings':bindings,'new_arrows':new,
        'outputs':[['receiver-arrival','e','A'],['receiver-defect','e','AB'],['receiver-defect','e','AC']],
        'acceptance':'both defect outputs equal zero; common receiver value is arrival A',
        'proton_observable':'original complete return N, unchanged',
        'count_rule':'distinct nonzero arrows between typed coefficient ports; fixed implementation, no contraction of stages'}
    return record,rows,vectors

def matrices(new,labels):
    index={x:i for i,x in enumerate(labels)}; B=[[ZERO]*36 for _ in range(3)]
    F=[[ZERO]*3 for _ in range(3)]; J=[[ZERO]*3 for _ in range(2)]
    for r in new:
        s,t=r['source'],r['target']; z=weight(r)
        if r['role']=='mode-amplitude-extraction': B['ABC'.index(t[2])][index[tuple(s[1:])]]=z
        elif r['role']=='primitive-receiver-leg': F['ABC'.index(t[2])]['ABC'.index(s[2])]=z
        else: J[['AB','AC'].index(t[2])]['ABC'.index(s[2])]=z
    arrivals=multiply(F,B)
    output=[arrivals[0]]+multiply(J,arrivals)
    return B,F,J,output

def apply(a,x): return [row[0] for row in multiply(a,[[z] for z in x])]

def verify_packet(packet):
    record,_,_=construct(packet['proton'],packet['open_source'])
    if record!=packet['record'] or digest(record)!=packet['root']: raise ValueError('compiled receiver differs from source recipe')
    return True

def main():
    original=SOURCE.read_bytes(); open_bytes=OPEN_SOURCE.read_bytes()
    source=json.loads(original); opened=json.loads(open_bytes)
    record,rows,vectors=construct(source,opened)
    new=record['new_arrows']; labels=sorted({tuple(r['source'][1:]) for r in rows}); index={x:i for i,x in enumerate(labels)}
    L=[[ZERO]*36 for _ in range(36)]; N=[[ZERO]*36 for _ in range(36)]
    for r in rows:
        if r['source'][0] in ('raw','aligned'):
            m=L if r['source'][0]=='raw' else N
            m[index[tuple(r['target'][1:])]][index[tuple(r['source'][1:])]]=weight(r)
    B,F,J,T=matrices(new,labels); raw_output=multiply(T,L)
    u=[vectors[e]['xyz'.index(a)] for e,a in labels]
    coherent_arrivals=apply(multiply(F,B),u)
    coherent_outputs=apply(T,u)
    # A compatible nonzero receiver input exists, but it is a relative face
    # mode erased by the old collective return.
    x=[ZERO]*36
    for i,a in enumerate('ABC'):
        edge=record['bindings'][a]['source_triangle']
        for axis,z in zip('xyz',vectors[edge]): x[index[(edge,axis)]]=times((ONE,OMEGA,OMEGA2)[i],z)
    accepted_output=apply(raw_output,x)
    deletion=[]
    for i,r in enumerate(new):
        remaining=new[:i]+new[i+1:]
        *_,changed=matrices(remaining,labels)
        deletion.append({'arrow':i,'role':r['role'],'output_changed':multiply(changed,L)!=raw_output})
    combined=rows+new
    keys={(tuple(r['source']),tuple(r['target'])) for r in combined}
    ports={tuple(p) for r in combined for p in (r['source'],r['target'])}
    packet={'schema':'marici.compiled-three-arrow-receiver.v1','proton':source,'open_source':opened,
            'record':record,'root':digest(record)}
    replay=verify_packet(json.loads(json.dumps(packet)))
    mutated=deepcopy(packet); mutated['record']['new_arrows'].pop(); mutated['root']=digest(mutated['record'])
    try: verify_packet(mutated); mutation_rejected=False
    except ValueError: mutation_rejected=True
    checks={
        'all_original_1836_arrows_retained_exactly':len(rows)==1836 and combined[:1836]==rows,
        'bridge_uses_actual_face_triangles':{a:r['source_triangle'] for a,r in record['bindings'].items()}=={'A':'AB','B':'BC','C':'CA'},
        'nine_bridge_three_receiver_four_witness_transfers':{role:sum(r['role']==role for r in new) for role in ['mode-amplitude-extraction','primitive-receiver-leg','compatibility-difference']}=={'mode-amplitude-extraction':9,'primitive-receiver-leg':3,'compatibility-difference':4},
        'exact_unique_typed_arrow_count_1852':len(combined)==len(keys)==1852,
        'exact_port_count_116':len(ports)==116,
        'mode_extraction_agrees_before_and_after_local_selection':multiply(B,L)==B,
        'compiled_receiver_readout_retains_three_independent_inputs':rank(raw_output)==3,
        'each_added_transfer_deletion_changes_retained_readout':all(r['output_changed'] for r in deletion),
        'source_collective_mode_has_three_equal_face_amplitudes':apply(B,u)==[ONE]*3,
        'source_collective_mode_fails_nontrivial_receiver_compatibility':coherent_arrivals==list(WEIGHTS) and coherent_outputs[1:]!=[ZERO,ZERO],
        'receiver_accepts_a_nonzero_relative_face_mode':accepted_output==[ONE,ZERO,ZERO],
        'accepted_relative_face_mode_is_lost_by_old_collective_feedback':apply(N,x)==[ZERO]*36,
        'serialized_packet_replays':replay,
        'rehashed_missing_transfer_rejected':mutation_rejected,
        'historical_inputs_unchanged':SOURCE.read_bytes()==original and OPEN_SOURCE.read_bytes()==open_bytes,
    }
    result={'verification_passed':all(checks.values()),'checks':checks,'root':packet['root'],
        'counts':{'proton':1836,'source_channel_bridge':9,'incoming_receiver_legs':3,'compatibility_witness':4,'total_unique_coefficient_arrows':1852,'typed_ports':116},
        'observable':'old return N plus (arrival A, arrival A-arrival B, arrival A-arrival C)',
        'pruning':'old arrows protected by original return witness; each new arrow protected by receiver-output deletion test, with stages and other weights fixed',
        'coherent_proton':{'normalized_face_amplitudes':encode(apply(B,u)), 'receiver_arrivals':encode(coherent_arrivals),'receiver_outputs':encode(coherent_outputs)},
        'accepted_relative_face_mode':{'receiver_outputs':encode(accepted_output),'old_collective_return':'zero'},
        'deletions':deletion,
        'outcome':'This specified source-bound compiler has 1852 retained coefficient arrows. It is not a nonzero jointly coherent H-1 realization: the unchanged proton coherent mode and the chosen receiver character do not agree.',
        'source_sha256':sha256(original).hexdigest(),'open_source_sha256':sha256(open_bytes).hexdigest(),
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (BASE/'results/compiled_three_arrow_receiver_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/compiled_three_arrow_receiver.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='deletions'},indent=2))
    if not result['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
