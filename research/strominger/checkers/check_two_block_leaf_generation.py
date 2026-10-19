"""Reuse the existing independent-family constructor on BOTH source blocks.

The branch-preserving continuation is an explicit candidate policy. It is not
inferred from137 or identified with the operator's complete rung schedule.
"""
import contextlib
from dataclasses import dataclass
import io
import json
from pathlib import Path
import runpy
from itertools import permutations

ROOT = Path(__file__).resolve().parents[3]
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(ROOT/'research/nima/checkers/check_recursive_independent_comparison.py'))
Record, compare, promote = (source[k] for k in ('Record','compare_families','promote'))

@dataclass(frozen=True)
class Packet:
    level: int
    parent: object
    blocks: dict
    families: dict

full_edges = tuple((i,j) for i in range(4) for j in range(4) if i != j)
reference = (0,1)
selected_edges = tuple(e for e in full_edges if e != reference)
# Separate role namespaces are retained by the block tag. Pair positions are
# ordered: reuse of one source does not identify its left/right occurrences.
arrows = {(i,):Record((a,),(b,)) for i,(a,b) in enumerate(selected_edges)}
states = {(i,):Record((i,),(i,)) for i in range(4)}
frame = {'full_edges':full_edges, 'reference':reference, 'states':tuple(range(4)),
         'selection':'exclude marked arrow only from counted arrow branch'}
initial = Packet(0,frame,{'arrow':arrows,'state':states},{})

def advance(packet):
    blocks, witnesses = {}, {}
    for tag, rows in packet.blocks.items():
        blocks[tag], witnesses[tag] = compare(rows, packet.level)
    return Packet(packet.level+1,packet,blocks,witnesses)

first = advance(initial)
second = advance(first)

def counts(packet): return {tag:len(rows) for tag,rows in packet.blocks.items()}
def leaves(packet):
    return {(tag,rid):r for tag,rows in packet.blocks.items() for rid,r in rows.items()}

checks = {
    'retained_frame_has_twelve_arrows':len(frame['full_edges'])==12,
    'counted_input_separates_eleven_arrows_and_four_states':counts(initial)=={'arrow':11,'state':4},
    'first_generation_creates_137':counts(first)=={'arrow':121,'state':16},
    'second_typed_generation_creates_14897':counts(second)=={'arrow':14641,'state':256},
    'exact_parent_packets_retained':second.parent is first and first.parent is initial,
    'reference_not_deleted_from_frame':reference in first.parent.parent['full_edges'],
}
for packet in (first,second):
    for tag,rows in packet.blocks.items():
        old = packet.parent.blocks[tag]
        for rid,row in rows.items():
            l,r=row.parents
            assert l in old and r in old and rid==l+r
            assert row.source==old[l].source+old[r].source
            assert row.target==old[l].target+old[r].target
checks['all_ordered_parent_occurrences_recover'] = True

# These are the actual family roles at the output, not independent new leaves.
first_families = {tag:promote(rows,first.level) for tag,rows in first.blocks.items()}
checks['rung4_candidate_target_view_has_32_families_137_members'] = (
    sum(len(fs) for fs in first_families.values()) == 32 and
    sum(len(members) for fs in first_families.values() for members in fs.values()) == 137)

# Compare with the previously documented137 domain without importing its
# numerical fixture: actual parent labels recover each ordered slot exactly.
arrow_slot_labels = {
    (selected_edges[rid[0]],selected_edges[rid[1]]) for rid in first.blocks['arrow']}
state_slot_labels = set(first.blocks['state'])
checks['generated_labels_match_121_plus_16_domain'] = (
    arrow_slot_labels == {(a,b) for a in selected_edges for b in selected_edges}
    and state_slot_labels == {(a,b) for a in range(4) for b in range(4)})

# Source relabelling covariance, with reference and all endpoints transported.
for perm in permutations(range(4)):
    relabelled={tag:{rid:Record(tuple(perm[x] for x in row.source),
                              tuple(perm[x] for x in row.target),row.parents)
                     for rid,row in rows.items()}
                for tag,rows in initial.blocks.items()}
    candidate=advance(Packet(0,frame,relabelled,{}))
    for tag,rows in first.blocks.items():
        assert candidate.blocks[tag] == {
            rid:Record(tuple(perm[x] for x in row.source),
                       tuple(perm[x] for x in row.target),row.parents)
            for rid,row in rows.items()}
checks['twenty_four_simultaneous_relabellings'] = True

# Rival continuation adds mixed-type slots. It preserves the same first state
# and its history but is a DIFFERENT next domain, not a covert implementation.
all_first=leaves(first)
unrestricted={(l,r) for l in all_first for r in all_first}
homogeneous={p for p in unrestricted if p[0][0]==p[1][0]}
mixed=unrestricted-homogeneous
checks['rival_next_count_18769'] = len(unrestricted)==18769
checks['homogeneous_next_count_14897'] = len(homogeneous)==14897
checks['mixed_cross_branches_explain_gap'] = len(mixed)==3872==2*121*16

controls = {
    'constant_row_reindexing_is_not_generation':len(leaves(initial))!=len(leaves(first)),
    'outer_family_count_is_not_leaf_count':sum(map(len,first_families.values()))!=len(leaves(first)),
    'next_recurrence_not_determined_by_137':len(homogeneous)!=len(unrestricted),
    'same_type_policy_not_unrestricted_product':len(leaves(initial))**2!=len(leaves(first)),
}
assert all(checks.values()) and all(controls.values())
out={'schema':'marici.two-block-leaf-generation.v1','status':'pass',
     'checks':checks,'negative_controls':controls,
     'source_frame':{'retained_arrows':12,'states':4,'reference':reference},
     'stages':[{'stage':p.level,'block_counts':counts(p),'comparison_records':sum(counts(p).values())}
               for p in (initial,first,second)],
     'rival_next':{'same_type':len(homogeneous),'unrestricted':len(unrestricted),'mixed':len(mixed)},
     'scope':'Two-block candidate using the owner generator, not selected all-rung semantics or numerical amplitudes.'}
(ROOT/'research/strominger/results/two-block-leaf-generation-v1.json').write_text(
    json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
