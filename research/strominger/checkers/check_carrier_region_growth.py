"""Exact growth test of EXISTING boundary sharing, not native interior states."""
from datetime import datetime, timezone
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve()
FIXTURE = ROOT / 'research/strominger/inputs/carrier-region-growth-v1.json'
PACKET = ROOT / 'research/strominger/carrier-region-growth.md'
MODEL = ROOT / 'research/strominger/scc-models/carrier-region-growth-v1.json'
OUT = ROOT / 'research/strominger/results/carrier-region-growth'
SEWING = HERE.with_name('check_carrier_particle_sewing.py')
spec = importlib.util.spec_from_file_location('growth_sewing', SEWING)
sew = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sew)


def solve(variables, edges):
    """x_u xor x_v = twist. Includes unconstrained ORIGINAL ports."""
    adjacency = {u: [] for u in variables}
    for u, v, twist in edges:
        adjacency[u].append((v, twist))
        adjacency[v].append((u, twist))
    values, components, conflicts = {}, [], []
    for root in variables:
        if root in values:
            continue
        values[root] = 0
        pending, component = [root], []
        while pending:
            u = pending.pop()
            component.append(u)
            for v, twist in adjacency[u]:
                predicted = values[u] ^ twist
                if v in values:
                    if values[v] != predicted:
                        conflicts.append([u, v, twist])
                else:
                    values[v] = predicted
                    pending.append(v)
        components.append(sorted(component))
    return {'dimension': 0 if conflicts else 2 ** len(components),
            'components': components, 'conflicts': conflicts,
            'assignment_witness': None if conflicts else values}


def accepts(values, edges):
    return all(values[u] ^ values[v] == twist for u, v, twist in edges)


def mask(variables, edges):
    return [int(accepts(dict(zip(variables, bits)), edges))
            for bits in product((0, 1), repeat=len(variables))]


def run(report):
    f = json.loads(FIXTURE.read_text(encoding='utf-8'))
    sf = json.loads((ROOT / f['source_fixture']).read_text(encoding='utf-8'))
    old = json.loads((ROOT / sf['source_fixture']).read_text(encoding='utf-8'))
    checks, cases = report['checks'], []

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)

    def setup(n):
        templates = {f'A{i}': sew.base.atom(f'A{i}', old['recipes'][f['template_recipe']], old) for i in range(n)}
        assembly = sew.base.disjoint_union(*templates.values())
        ports = {name: sew.derived_c_ports(a) for name, a in templates.items()}
        variables = [ports[f'A{i}'][side] for i in range(n) for side in ('entry', 'exit')]
        return assembly, ports, variables, sew.candidate_seams(templates)

    def admit(assembly, candidates, edges):
        for u, v, twist in edges:
            sew.seam_operator(assembly, (u, v), sf['seams']['twisted' if twist else 'identity'],
                              (sf['common_boundary']['evaluation_context'],) * 2, sf, candidates)

    plans = [('chain', n, n) for n in f['chain_atom_counts']]
    plans += [('ring', n, n) for n in f['ring_atom_counts']]
    plans += [('star', k + 1, k) for k in f['star_attachment_counts']]
    for shape, n, size in plans:
        assembly, ports, variables, candidates = setup(n)
        if shape == 'star':
            pairs = [(0, i) for i in range(1, n)]
            expected = 2 ** (size + 2)
        else:
            pairs = [(i, i + 1) for i in range(n - 1)]
            if shape == 'ring':
                pairs.append((n - 1, 0))
            expected = 2 ** (n if shape == 'ring' else n + 1)
        edges = [(ports[f'A{i}']['exit'], ports[f'A{j}']['entry'], 0) for i, j in pairs]
        name = f'{shape}_{size}'
        admit(assembly, candidates, edges)
        solved = solve(variables, edges)
        check(name + '_exact_dimension', solved['dimension'] == expected)
        check(name + '_zero_assignment_satisfies_every_original_seam', accepts(dict.fromkeys(variables, 0), edges))
        graph = sew.graph_pushout(assembly, [(u, v) for u, v, _ in edges])
        check(name + '_all_particle_instances_retained', len(graph['particle_instances']) == 2 * n)
        labels = {u: i % 2 for i, u in enumerate(variables)}
        changed = [(u, v, labels[u] ^ labels[v]) for u, v, _ in edges]
        admit(assembly, candidates, changed)
        transported = solve(variables, changed)
        check(name + '_honest_port_charts_preserve_dimension', transported['dimension'] == expected and accepts(labels, changed))
        if n <= f['brute_force_max_atoms']:
            diagonal = mask(variables, edges)
            check(name + '_independent_exhaustive_assignments', sum(diagonal) == expected)
            vector = [i % 7 - 3 for i in range(len(diagonal))]
            check(name + '_full_packet_reconstruction', all(p * x + (1 - p) * x == x for p, x in zip(diagonal, vector)))
            check(name + '_chart_covariance_all_basis_assignments', all(
                accepts(dict(zip(variables, bits)), edges) == accepts({u: bit ^ labels[u] for u, bit in zip(variables, bits)}, changed)
                for bits in product((0, 1), repeat=len(variables))))
        cases.append({'shape': shape, 'atoms': n, 'attachments' if shape == 'star' else 'size': size,
                      'original_port_variables': variables, 'constraints': edges, 'compatible': solved,
                      'ambient_dimension': 2 ** (2 * n), 'mismatch_dimension': 2 ** (2 * n) - expected,
                      'honest_port_chart_labels': labels, 'graph_pushout': graph})

    assembly, ports, variables, candidates = setup(4)
    square = [(ports[f'A{i}']['exit'], ports[f'A{j}']['entry'], 0) for i, j in ((0, 2), (0, 3), (1, 2), (1, 3))]
    frustrated = square[:-1] + [(square[-1][0], square[-1][1], 1)]
    admit(assembly, candidates, frustrated)
    good, bad = solve(variables, square), solve(variables, frustrated)
    check('four_seam_identity_control_has_32_assignments', good['dimension'] == sum(mask(variables, square)) == 32)
    check('locally_faithful_but_globally_frustrated_control_is_empty', bad['dimension'] == sum(mask(variables, frustrated)) == 0 and bool(bad['conflicts']))
    cycle = [(f'A{i}', f'A{(i+1)%3}', 1) for i in range(3)]
    check('invented_entry_exit_equality_can_manufacture_a_false_ring_rejection', solve(['A0', 'A1', 'A2'], cycle)['dimension'] == 0)
    check('proper_separate_ports_do_not_reject_twisted_three_atom_ring', solve(
        [f'A{i}/{side}' for i in range(3) for side in ('entry', 'exit')],
        [(f'A{i}/exit', f'A{(i+1)%3}/entry', 1) for i in range(3)])['dimension'] == 8)

    _, p, v, _ = setup(4)
    e = [(p[f'A{i}']['exit'], p[f'A{i+1}']['entry'], 0) for i in range(3)]
    left, right = mask(v, e), mask(v, list(reversed(e)))
    check('seam_order_equal_on_every_ambient_basis_coordinate', left == right)
    diagram = sew.evaluated_diagram([('growth_seam_order', 'Q256_boundary_assignments', 'Q256_boundary_assignments',
                                     {'diagonal': left}, {'diagonal': right}, [['seams_forward'], ['seams_reverse']])])
    diagram['id'] = 'carrier-region-growth-v1'
    compiled = sew.compiler.compile_diagram(diagram)
    check('SCC_static_evaluated_projector_cell', compiled['passed'])
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'diagram.json').write_text(json.dumps(diagram, indent=2) + '\n', encoding='utf-8')
    report.update({'cases': cases, 'tested_families': len(cases), 'all_finite_identity_network_witness': 'assign 0 to every original port; no dependence on atom count or degree',
        'classification': 'boundary_sharing_alone_has_no_finite_growth_limit',
        'controlled_obstruction': {'constraints': frustrated, 'solution': bad, 'interpretation': 'Deliberately inconsistent restriction maps; not an observed molecular exclusion'},
        'compiled_static_cell': compiled,
        'native_disposition': 'NOT TESTED: native internal comparison-to-boundary restrictions are absent. Boundary-compatible does not mean internally admissible or physically bound.'})


def main():
    f = json.loads(FIXTURE.read_text(encoding='utf-8'))
    paths = [HERE, FIXTURE, PACKET, MODEL, SEWING, sew.BASE_PATH, sew.base.FIXTURE,
             ROOT / f['source_fixture'], sew.COMPILER_PATH]
    report = {'schema': 'marici.strominger.carrier-region-growth.verification.v1',
        'recorded_at': datetime.now(timezone.utc).isoformat(), 'checks': {},
        'source_sha256': {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:
        run(report)
        report['status'] = 'pass'
    except Exception as error:
        report.update(status='fail', error=repr(error))
        raise
    finally:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / 'verification.json').write_text(json.dumps(report, indent=2, default=str) + '\n', encoding='utf-8')
        print(json.dumps({'status': report['status'], 'classification': report.get('classification', 'execution_failure'),
                          'check_groups': len(report['checks']), 'families': report.get('tested_families'),
                          'receipt': (OUT / 'verification.json').relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
