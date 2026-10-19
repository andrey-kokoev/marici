"""Exact endpoint-role and partial-readout audit; imported sources read-only."""
import ast
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from marked137_endpoint_audit import ROOT, source_table, assembly_views, MarkedEndpointObserver

HOME = Path(__file__).resolve().parent
CONTRACT = HOME / 'contracts/marked137-endpoint-audit.v1.json'
SOURCE_PATHS = [ROOT / path for path in (
    'research/nima/checkers/check_rung_transport_diagram.py',
    'research/nima/checkers/check_shared_leg_dg_realization.py',
    'research/nima/checkers/biclique_complex.py',
    'research/nima/checkers/check_mass_path_port_connectivity.py')]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_contract(contract):
    require(all(value is False for value in contract['boundary'].values()), 'endpoint audit boundary promotion')
    require(contract['risky_consequences'] == {
        'common_assembly_source_target': ['A', 'B'], 'carrier_source_port_count': 32, 'carrier_target_port_count': 32,
        'parent_inner_domain': {'arrow_pairs': 144, 'state_pairs': 9, 'total': 153},
        'marked_domain': {'arrow_pairs': 121, 'state_pairs': 16, 'total': 137},
        'typed_overlap': 130, 'inherited_readout_count': 145, 'reachable_state_keys': 9,
        'state_keys_outside_parent_domain': 7}, 'endpoint domain/role contract changed')


def audit():
    source = source_table()
    rows = source['source']
    views = assembly_views(source)
    model = source['m']
    arrows = model['arrows']
    require(len([name for name, (_, _, degree) in arrows.items() if degree == 0]) == 31, 'shared primitive/reference leg domain changed')
    for view in views:
        left, right = view.path
        require(arrows[left][0] == 'A' and arrows[left][1] == arrows[right][0] and arrows[right][1] == 'B',
                'actual shared-leg path does not have common assembly endpoints')
        require(model['mul'](model['values'][right], model['values'][left]) == view.value,
                'slot-to-shared-leg response wiring mismatch')
        require(view.parent in rows and view.members == (view.parent,), 'assembly view erased source decoration')
    require(len({row.source for row in rows}) == len({row.target for row in rows}) == 32, 'carrier port count changed')
    require(len({view.source for view in views}) == len({view.target for view in views}) == 1, 'assembly endpoint role changed')
    require(source['leaves'](views) == rows, 'original137 rows lost in assembly view')
    carrier_first = source['incoming_promotion'](rows, 1, 'inherited')
    assembly_first = source['incoming_promotion'](views, 1, 'inherited')
    require(len(carrier_first) == 32 and len(assembly_first) == 1, 'endpoint-role regrouping counterexample changed')
    require(source['read_at_four'](source['indexed'](views, 'target')) == source['read_at_four'](source['indexed'](rows, 'target')),
            'fixed matrix readout changed under a retained endpoint-role view')

    # Bind the exact inherited label rule syntactically without rerunning the
    # unrelated153/1836 charging chain or writing its shared result files.
    tree = ast.parse(SOURCE_PATHS[-1].read_text(encoding='utf-8'))
    guards = [node for node in ast.walk(tree) if isinstance(node, ast.If)
              and ast.unparse(node.test) == 'a[end] != 0 and b[end] != 0']
    require(len(guards) == 1, 'inherited nonreference endpoint guard changed')
    calls = [node for node in ast.walk(guards[0]) if isinstance(node, ast.Call)]
    require(any(ast.unparse(call) == "link('endpoint', s, (outer, ('state', a[end], b[end])))" for call in calls),
            'inherited endpoint readout codomain changed')
    require(any(isinstance(node, ast.For) and ast.unparse(node.target) == 'end'
                and ast.unparse(node.iter) == '(0, 1)' for node in ast.walk(tree)), 'inherited endpoint-side inventory changed')
    edges = {(a, b) for a in range(4) for b in range(4) if a != b}
    marked_edges = set(source['E'])
    require(marked_edges == edges - {(0, 1)}, 'marked direct-reference exclusion changed')
    parent_inner = {('a', a, b) for a in edges for b in edges} | {('s', a, b) for a in range(1, 4) for b in range(1, 4)}
    marked_inner = {('a', a, b) for a in marked_edges for b in marked_edges} | {('s', a, b) for a in range(4) for b in range(4)}
    require(len(parent_inner) == 153 and len(marked_inner) == 137 and len(parent_inner & marked_inner) == 130,
            '153/137 interface pullback changed')
    extra_states = sorted(marked_inner - parent_inner)
    require(len(extra_states) == 7 and all(key[0] == 's' and 0 in key[1:] for key in extra_states),
            'extra marked state domain misidentified')
    observer = MarkedEndpointObserver(rows)
    packets = []
    rejected = 0
    for row in rows:
        for side in (0, 1):
            endpoint = row.source if side == 0 else row.target
            admitted = endpoint[0] == 'a' and 0 not in endpoint[1:]
            try:
                packet = observer.observe(row, side)
            except ValueError:
                require(not admitted, 'valid inherited endpoint readout rejected')
                rejected += 1
            else:
                require(admitted and packet.observed_state_key == ('s',) + endpoint[1:], 'endpoint observer domain extended silently')
                require(observer.restore_parent(packet) is row, 'retained endpoint parent changed')
                packets.append(packet)
    require(len(packets) == 145 and rejected == 129, 'partial observer request census changed')
    by_side = Counter(packet.side for packet in packets)
    require(by_side == {0: 81, 1: 64}, 'endpoint side multiplicities changed')
    require(len({packet.observed_state_key for packet in packets}) == 9, 'unprovided reference-index readout added')
    require(len({packet.parent.label for packet in packets}) == 109, 'readable parent support changed')
    fibres = defaultdict(list)
    for packet in packets:
        fibres[(packet.side, packet.observed_state_key)].append(packet)
    collision = next((a, b) for fibre in fibres.values() for a in fibre for b in fibre if a.parent.value != b.parent.value)
    a, b = collision
    require(a.parent.label != b.parent.label and a.observed_state_key == b.observed_state_key and a.side == b.side,
            'full-response descent hostile failed')
    require(observer.restore_parent(a).value != observer.restore_parent(b).value, 'parent retention failed to preserve the response hostile')
    for operation in (observer.inverse, observer.state_response):
        try:
            operation(a)
        except ValueError:
            pass
        else:
            raise ValueError('metadata readout promoted to a numerical response operation')
    return {
        'shared_assembly_primitive_reference_legs': 31, 'shared_composite_paths_checked': 137,
        'assembly_endpoint_signature': ['A', 'B'], 'carrier_source_ports': 32, 'carrier_target_ports': 32,
        'first_families_using_carrier_target': 32, 'first_families_using_assembly_target': 1,
        'same_fixed_J4_under_role_view': True, 'original_rows_recovered': 137,
        'parent153_marked137_overlap': 130, 'marked_states_outside_parent_domain': [list(key) for key in extra_states],
        'partial_endpoint_readouts': 145, 'source_side_readouts': 81, 'target_side_readouts': 64,
        'rejected_row_side_requests': 129, 'readable_arrow_parent_count': 109, 'reachable_state_keys': 9,
        'response_descent_hostile': {'side': a.side, 'state_key': list(a.observed_state_key),
            'parent_labels': [list(a.parent.label), list(b.parent.label)],
            'parent_values': [[[str(value) for value in row] for row in packet.parent.value] for packet in (a, b)]},
        'native_presentation_endpoint_alignment': 'Not supplied; decoded family keys are not identified with native outer presentations.',
        'state_response_transport_derived': False, 'intended_T9_selected': False,
        'scope': 'Exact source table wiring plus inherited partial discrete index readout; no physical vertex/state alignment or connector.'}


def main():
    validate_contract(json.loads(CONTRACT.read_text()))
    paths = SOURCE_PATHS + [CONTRACT, Path(__file__), HOME / 'marked137_endpoint_audit.py']
    pins = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    controls = audit()
    require(all(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected for path, expected in pins.items()),
            'endpoint audit sources changed during execution')
    receipt = {'schema': 'marici.conjecture-net.marked137-endpoint-audit.v1', 'status': 'pass',
               'validation_only': True, 'outcome': None, 'root_outcome': None, 'source_sha256': pins, 'controls': controls,
               'disposition': 'Partial observer constructed; total-domain, full-response and invertible-connector rivals rejected.',
               'original_sources_and_results_regenerated': False, 'new_kernel_theorem_proved': False,
               'physical_readout_authorized': False, 'programme_outcomes_promoted': False}
    (HOME / 'results/marked137-endpoint-audit.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'endpoint_role_grouping_counts': [32, 1],
                      'typed153_137_overlap': 130, 'partial_readouts': 145, 'response_descent': False}, indent=2))


if __name__ == '__main__':
    main()
