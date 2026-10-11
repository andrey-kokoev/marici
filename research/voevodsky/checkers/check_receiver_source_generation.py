"""Trace the actual packet and 1836 constructors with the proposed input.

No unsupported combined coefficient count is emitted. Target-only receiver
records are an explicit extension of the source-grouping rule, not old output.
"""
import ast
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json

from check_proton_merkle_reassembly import verify
from check_three_arrow_receiver import simple_cycles, WEIGHTS
from check_reversed_coefficient_attachment import encode
from check_geometric_cycle_reversal import geo
from check_triangle_half_phase import TwoPacket, cycle_from_packets

BASE=Path(__file__).resolve().parents[1]
NIMA=BASE.parent/'nima/checkers'
PACKETS=NIMA/'check_twelve_packets_to_tetrahedron.py'
GENERATOR=NIMA/'check_twelve_triangle_positive_geometry.py'
PRIMITIVES=NIMA/'check_triangle_half_phase.py'
PROTON=BASE/'results/proton_merkle_store.json'


def literal_assignment(path,name,inside=None):
    tree=ast.parse(path.read_text(encoding='utf-8'))
    statements=tree.body if inside is None else next(n.body for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==inside)
    for n in statements:
        if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets):
            return ast.literal_eval(n.value)
    raise ValueError(name)


def grouping(packets,include_targets=False):
    records=defaultdict(list)
    for i,(a,b) in enumerate(packets): records[a].append(i)
    if include_targets:
        for a,b in packets: records.setdefault(b,[])
    return dict(records)


def clique_cells(edges):
    undirected={frozenset(e) for e in edges}
    vertices=sorted({x for e in edges for x in e})
    return {k:[tuple(c) for c in combinations(vertices,k) if all(frozenset(e) in undirected for e in combinations(c,2))] for k in range(2,6)}


def main():
    files=(PACKETS,GENERATOR,PRIMITIVES,PROTON)
    before={str(p):p.read_bytes() for p in files}
    packets=tuple(literal_assignment(PACKETS,'packets'))
    addresses=sorted({x for p in packets for x in p})
    label=dict(zip(addresses,'ABCD'))
    old=tuple((label[a],label[b]) for a,b in packets)
    new=old+tuple((a,'e') for a in 'ABC')
    source_records=grouping(new); open_records=grouping(new,True)
    unresolved=sorted({b for a,b in new if b not in source_records})
    source=json.loads(before[str(PROTON)]); proof,coefficient_rows=verify(source)
    objects=source['objects']; geometry=objects[objects[source['root']]['geometry']]['payload']
    # Read the actual hard-coded proper-rotation generators, not a new group.
    generators=literal_assignment(GENERATOR,'generators','main')
    group={(0,1,2,3)}; frontier=list(group)
    while frontier:
        p=frontier.pop()
        for g in generators:
            q=geo.compose(g,p)
            if q not in group: group.add(q); frontier.append(q)
    added=set(new)-set(old); orbit=set(); stabilizers=[]
    for p in sorted(group):
        rename=dict(zip('ABCD',('ABCD'[i] for i in p))); rename['e']='e'
        moved={(rename[a],rename[b]) for a,b in added}; orbit|=moved
        if moved==added: stabilizers.append(p)
    cliques=clique_cells(new)
    new_faces=[face for face in cliques[3] if 'e' in face]
    old_cycles=simple_cycles(set(old)); new_cycles=simple_cycles(set(new))
    cyclic_errors=[]
    for face in new_faces:
        a,b,e=face
        # Attempt the primitive composable-cycle constructor without adding
        # a missing return arrow. The two actual source legs end at e.
        packets_for_face=(TwoPacket('ab',a,b),TwoPacket('be',b,e),TwoPacket('ae',a,e))
        try:
            cycle_from_packets(packets_for_face)
            cyclic_errors.append(False)
        except ValueError:
            cyclic_errors.append(True)
    checks={
        'actual_twelve_packet_source_loaded':len(old)==12 and set(old)=={(a,b) for a in 'ABCD' for b in 'ABCD' if a!=b},
        'packet_labels_match_twelve_realized_outer_arrows':{a+b for a,b in old}=={r['outer_arrow'] for r in geometry['triangles_and_transports']},
        'original_1836_retained_protocol_freshly_verified':proof['verified'] and proof['arrows']==1836,
        'prepopulated_input_retains_old_packets_exactly':new[:12]==old and len(set(new))==15,
        'original_source_only_grouping_leaves_receiver_unresolved':unresolved==['e'],
        'old_three_packets_per_record_assumption_no_longer_holds':{k:len(v) for k,v in source_records.items()}=={'A':4,'B':4,'C':4,'D':3},
        'endpoint_complete_extension_retains_all_fifteen_once':len(open_records)==5 and open_records['e']==[] and sorted(i for v in open_records.values() for i in v)==list(range(15)),
        'no_receiver_return_packets_silently_added':not any(a=='e' for a,b in new),
        'undirected_clique_completion_has_two_tetrahedra':set(cliques[4])=={tuple('ABCD'),tuple('ABCe')} and not cliques[5],
        'new_triangles_have_no_source_directed_cycle':len(new_faces)==3 and all(cyclic_errors),
        'closed_cycles_are_exactly_the_old_ones':old_cycles==new_cycles,
        'actual_proper_rotation_group_has_twelve_elements':len(group)==12,
        'marked_receiver_preserves_only_three_proper_rotations':len(stabilizers)==3,
        'full_old_rotation_orbit_would_add_unrequested_D_leg':orbit-added=={('D','e')},
        'audited_sources_unchanged':all(p.read_bytes()==before[str(p)] for p in files),
    }
    packet={
        'kind':'endpoint-complete-three-arrow-receiver-source',
        'packets':[{'id':f'p{i+1:02}','source':a,'target':b,'role':'proton-source' if i<12 else 'receiver-leg'} for i,(a,b) in enumerate(new)],
        'records':{k:{'outgoing_packet_ids':[f'p{i+1:02}' for i in ids],
                       'incoming_packet_ids':[f'p{i+1:02}' for i,(a,b) in enumerate(new) if b==k],
                       'role':'terminal-cyclic-receiver' if k=='e' else 'source-record'} for k,ids in sorted(open_records.items())},
        'source_grouping_extension':'retain target-only records as explicit terminal interfaces; do not synthesize outgoing packets',
        'receiver_contract':{'channel_type':'Q(sqrt(-3))','incoming_weights':{a:encode(w) for a,w in zip('ABC',WEIGHTS)},
                             'observable':'three-way equal-image compatibility, retained separately from closed returns'},
        'proton_protocol_root':source['root'],
        'compiled_combined_coefficient_count':None,
    }
    report={
        'verification_passed':all(checks.values()),'checks':checks,
        'counts':{'primitive_input':15,'endpoint_complete_records':5,'undirected_edges':len(cliques[2]),
                  'clique_triangles':len(cliques[3]),'clique_tetrahedra':len(cliques[4]),
                  'unchanged_proton_coefficient_arrows':1836,'combined_retained_coefficient_arrows':None},
        'earliest_original_constructor_failure':'receiver e is not created by grouping only on packet source, so its incoming references do not resolve',
        'further_boundaries':[
            'the existing three-packet source-record shape becomes 4,4,4,3 plus a terminal record',
            'undirected tetrahedral completion does not provide the missing directed receiver face cycles',
            'the fixed A4 orbit constructor would generate D->e unless the face marking is retained',
            'the generator does not define a bridge from A/B/C receiver channels to its raw/local/aligned coefficient ports',
            'closed-cycle-only retention cannot retain arrows ending at a sink'],
        'required_extension':'a face-marked open-channel compiler that preserves the old closed subsystem and realizes the equal-image receiver observable',
        'source_hashes':{str(p.relative_to(BASE.parent.parent)).replace('\\','/'):sha256(before[str(p)]).hexdigest() for p in files},
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (BASE/'results/receiver_source_generation_store.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
    (BASE/'results/receiver_source_generation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if not report['verification_passed']: raise SystemExit(1)

if __name__=='__main__': main()
