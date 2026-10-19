# /// script
# dependencies = ["sympy"]
# ///
"""Adapt existing path/endpoint readout law to the marked137-slot domain.

The source domain is fixed E'=12 arrows minus(0,1), plus16 state pairs.
Endpoint readout is a directed observation; retained register implementation
is a declared reversible classical encoding, not a physical pulse selection.
"""
from collections import defaultdict, deque
from contextlib import redirect_stdout
from dataclasses import replace
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
OUT=ROOT/'results/137-retained-endpoint-readout.json'
OUT.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    roles=runpy.run_path(str(HERE/'check_assembly_vs_carrier_endpoint_roles.py'))
m=roles['m']; rows=m['source']; E=m['E']
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)
check('endpoint-role-audit-fresh',roles['result']['verification_status']=='pass')
check('marked-arrow-view-unchanged',len(E)==11 and (0,1) not in E)
slots=tuple(('a',i,j) for i,j in product(range(11),repeat=2))+tuple(('s',i,j) for i,j in product(range(4),repeat=2))
by_slot=dict(zip(slots,rows)); by_label={row.label:slot for slot,row in by_slot.items()}
check('all137-original-labels-retained',len(by_slot)==len(by_label)==137)

def endpoint(slot,side):
    tag,i,j=slot
    return (E[i][side],E[j][side]) if tag=='a' else (i,j)

# Carrier index readouts correspond to the ACTUAL row fields; assembly-role
# readouts A or B do not identify these16 state-pair slots.
for slot,row in by_slot.items():
    check('actual-from-column/'+str(slot),row.source==(slot[0],*endpoint(slot,0)))
    check('actual-to-column/'+str(slot),row.target==(slot[0],*endpoint(slot,1)))

adj={slot:set() for slot in slots}; events=[]
for slot in slots:
    tag,i,j=slot
    if tag!='a': continue
    for side,name in ((0,'source-readout'),(1,'target-readout')):
        a,b=endpoint(slot,side); target=('s',a,b)
        check('endpoint-state-is-in-original-domain/'+str((slot,side)),target in by_slot)
        event={'kind':name,'parent':by_slot[slot].label,'destination':by_slot[target].label,
               'carrier_endpoint':(a,b)}
        events.append(event); adj[slot].add(target)
    # Existing active-arrow continuation law, restricted to counted E'.
    # Its retained lift appends an edge; last-arrow projection alone is lossy.
    for k,edge in enumerate(E):
        if E[i][1]==edge[0]: adj[slot].add(('a',k,j))
        if E[j][1]==edge[0]: adj[slot].add(('a',i,k))
check('242_directed_readouts',len(events)==242)
check('no_state_to_arrow_operation_supplied',all(not adj[slot] for slot in slots if slot[0]=='s'))

def reachable(start):
    found={start}; todo=deque([start])
    while todo:
        for target in adj[todo.popleft()]:
            if target not in found: found.add(target); todo.append(target)
    return found
reach={slot:reachable(slot) for slot in slots}
arrow={slot for slot in slots if slot[0]=='a'}; state=set(slots)-arrow
check('every_arrow_reaches_all137_slots',all(reach[slot]==set(slots) for slot in arrow))
check('each_state_has_only_identity_reachability',all(reach[slot]=={slot} for slot in state))
check('directed_reachability_count',sum(map(len,reach.values()))==16593)
check('2176_reverse_or_state_cross_pairs_missing',137**2-sum(map(len,reach.values()))==2176)
check('17_strong_components_not_one_reversible_sector',len(arrow)==121 and len(state)==16)
# Concrete noninjective readout: same observed endpoint state, distinct parents.
a,b=next((a,b) for a,b in product(sorted(arrow),repeat=2) if a!=b and endpoint(a,1)==endpoint(b,1))
check('target_readout_cannot_recover_parent',by_slot[a].label!=by_slot[b].label and endpoint(a,1)==endpoint(b,1))
# Protecting only the four-state-pair observation is WEAKER than protecting
# the tagged carrier target/domain: arrow and state tags share that readout.
first=m['incoming_promotion'](rows,1,'inherited')
endpoint_first=tuple(replace(family,target=('endpoint-readout',*family.members[0].target[1:])) for family in first)
endpoint_final=m['incoming_promotion'](endpoint_first,2,'inherited')
check('endpoint_observation_quotient_has16_rows',len(endpoint_final)==16)
check('endpoint_observation_quotient_retains_original_rows',m['leaves'](endpoint_final)==rows)
check('endpoint_observation_quotient_preserves_J4',m['read_at_four'](m['indexed'](endpoint_final,'target'))==m['read_at_four'](m['indexed'](rows,'target')))
check('each_endpoint_family_has_one_observed_state_pair',all(len({row.target[1:] for row in m['leaves']((family,))})==1 for family in endpoint_final))
check('endpoint_only_quotient_adds_contexts',sum(len(m['leaves']((family,)))**2 for family in endpoint_final)==1219)
check('endpoint_only_readout_does_not_protect_branch_tag',any(len({row.target[0] for row in m['leaves']((family,))})==2 for family in endpoint_final))
check('each_observation_has_exactly_two_first_fibres',all(len(family.members)==2 for family in endpoint_final))
# Parent plus endpoint observation is a recoverable event, unlike state alone.
check('retained_readout_events_recover_all_parent_and_side_data',len({(e['parent'],e['kind']) for e in events})==242)

# Reversible classical write: (parent,register) -> (parent,register XOR readout).
# It provides a lossless OBSERVATION lift, not a free state->arrow operation.
registers=tuple(product(range(4),repeat=2))
def write(parent,register,side):
    a,b=endpoint(parent,side)
    return parent,(register[0]^a,register[1]^b)
for side in (0,1):
    outputs=set()
    for parent,register in product(slots,registers):
        output=write(parent,register,side)
        outputs.add(output)
        check('reversible-write-involution/'+str((side,parent,register)),write(*output,side)==(parent,register))
    check('reversible-write-is-bijective/'+str(side),len(outputs)==137*16)
    check('blank-register-gives-declared-readout/'+str(side),all(write(parent,(0,0),side)==(parent,endpoint(parent,side)) for parent in slots))

result={
 'schema':'marici.nima.137-retained-endpoint-readout.v1','verification_status':'pass','checks':checks,
 'domain':'Original121 marked arrow-pair slots plus16 state-pair slots; excluded(0,1) remains excluded from this view.',
 'endpoint_role_binding':'Carrier-index source/target columns equal endpoint-pair readouts; common assembly endpoints A,B are separate roles.',
 'directed_readout_events':242,'retained_parent':True,
 'endpoint_only_successor':{'final_rows':16,'comparison_pair_support':1219,'tagged_target_support':977,
                            'J4_unchanged':True,'branch_tag_protected':False,
                            'compatible_key_partitions':65536,
                            'partition_argument':'Each of16 observed pairs has one arrow fibre and one state fibre; each pair may be kept separate or merged independently.'},
 'continuation_and_readout_reachability':{'ordered_slot_pairs':16593,'strong_component_sizes':[121]+[1]*16,
                                        'missing_pairs':2176},
 'noninjective_target_readout_witness':{'parent_labels':[by_slot[a].label,by_slot[b].label],
                                      'readout':endpoint(a,1)},
 'reversible_observation_lift':'137 retained parent labels x16 register values; XOR-write is bijective and involutive in each endpoint convention.',
 'not_a_connector':'Reversing the retained write requires parent+register; a standalone state record has no selected parent or inverse route.',
 'scope':'Graph transitions/readout labels, not reference-return composition pairs; counts must not be equated with the earlier14657 route-comparison support.',
 'value_binding':'No claim that state matrix response equals endpoint readout of an arrow matrix; endpoint readout here observes carrier labels only.',
 'intended_T9_identified':False,'objective_complete':False,
 'next_obligation':'Choose whether rung endpoints are carrier-index observations or common assembly roles, and which observation must be protected by T9; physical connector admission still requires its own operation.',
 'inputs_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'check_mass_path_port_connectivity.py',HERE/'check_assembly_vs_carrier_endpoint_roles.py')}}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} retained endpoint-readout checks')
print('242 arrow-to-state readouts match actual carrier columns; retained XOR observation lift is reversible.')
print('No standalone inverse connector: states are sinks;2176 directed slot transitions remain unavailable.')
