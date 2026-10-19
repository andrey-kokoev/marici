"""Connect ledger4320, replay its software interface, retain physical boundaries.

Imports pure constructor modules only; never runs owner checkers or rewrites
Nima/Strominger receipts. Cached formal receipts are integrity-checked, not
relabelled as a fresh compiler run.
"""
from contextlib import redirect_stdout
from dataclasses import replace
import hashlib
import importlib
import io
import json
from pathlib import Path
import sys
from marked137_endpoint_audit import ROOT, CHECKERS, source_table

HOME = Path(__file__).resolve().parent
LEDGER = ROOT / 'src/ledger/20261013-4320 Exact-Domain Transport and the Physical Reference Boundary.md'
CONTRACT = HOME / 'contracts/ledger4320-reference-boundary-net.v1.json'
SOFTWARE = ROOT / 'research/nima/contracts/T9-exact-domain-software.v1.json'
SOFTWARE_RECEIPT = ROOT / 'research/nima/results/pinned-T9-software-contract.json'
PACKETS = ['reference-port-binding', 'raw-sewing-reference-convention', 'clifford-comparison-bank',
           'joint-bank-extraction', 'passive-joint-bank-network']


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_input(owner, name):
    candidates = [ROOT / name, ROOT / 'research' / name, ROOT / 'research' / owner / 'checkers' / name]
    paths = [p.resolve() for p in candidates if p.is_file() and p.resolve().is_relative_to(ROOT)]
    require(len(set(paths)) == 1, 'missing/ambiguous receipt input: ' + name)
    return paths[0]


def sources():
    paths = {LEDGER, SOFTWARE, SOFTWARE_RECEIPT, ROOT / 'research/nima/pinned-T9-software-contract.md'}
    receipts = [('nima', SOFTWARE_RECEIPT)]
    for packet in PACKETS:
        paths.add(ROOT / 'research/strominger' / (packet + '.md'))
        receipt = ROOT / 'research/strominger/results' / (packet + '.json')
        paths.add(receipt)
        receipts.append(('strominger', receipt))
    for owner, receipt in receipts:
        data = json.loads(receipt.read_text())
        require(data['verification_status'] == 'pass', 'source receipt not passing: ' + str(receipt))
        for name, expected in data['inputs_sha256'].items():
            path = resolve_input(owner, name)
            require(sha(path) == expected, 'stale receipt input: ' + name)
            paths.add(path)
    software = json.loads(SOFTWARE_RECEIPT.read_text())
    require(software['contract_sha256'] == sha(SOFTWARE), 'software contract/receipt mismatch')
    for module, expected in software['formal_receipts_sha256'].items():
        receipt = ROOT / 'research/nima/results' / ('agda-' + module + '.json')
        require(sha(receipt) == expected, 'changed formal receipt: ' + module)
        formal = json.loads(receipt.read_text(encoding='utf-8-sig'))
        require(formal['passed'] and formal['ignore_interfaces'] and formal['inputs_stable_during_check'], 'invalid prior formal receipt')
        path = ROOT / 'research/nima/agda' / (module + '.agda')
        require(sha(path) == formal['owner_source_inventory_sha256'][path.name], 'formal owner source changed')
        paths.update((receipt, path))
    return sorted(paths)


def create(path, data):
    content = json.dumps(data, indent=2, sort_keys=True) + '\n'
    if path.exists():
        require(path.read_text() == content, 'refusing implicit replacement: ' + str(path))
    else:
        path.write_text(content, encoding='utf-8')


def validate_binding(binding):
    require(binding['ledger']['path'] == LEDGER.relative_to(ROOT).as_posix() and binding['ledger']['sha256'] == sha(LEDGER), 'ledger identity/drift')
    require(binding['software']['contract_id'] == 'nima.T9.exact-domain.software.v1' and binding['software']['selection_scope'] == 'software_only', 'software scope changed')
    require(binding['software']['fixture'] == {'records': 137, 'first_families': 32, 'final_families': 32, 'domain_pairs': 977}, 'software domain changed')
    require(all(value is False for value in binding['boundary'].values()), 'ledger evidence strength promotion')
    require(all(c['outcome'] is None for c in binding['conjectures']), 'unreviewed proof-outcome import')
    for name, expected in binding['evidence_sha256'].items():
        path = (ROOT / name).resolve()
        require(path.is_relative_to(ROOT) and sha(path) == expected, 'stale ledger evidence: ' + name)


def replay_software():
    previous = list(sys.path)
    try:
        sys.path.insert(0, str(CHECKERS))
        constructor = importlib.import_module('retained_rung_transport')
        fixture = source_table()
        rows = fixture['source']
        output = constructor.T9(rows, fixture)
        observed = output.observe(fixture)
        require(len(rows) == 137 and len(output.final) == 32, 'software carrier counts')
        require(fixture['leaves'](output.final) == rows, 'original rows not recovered')
        original = {(a.label, b.label) for a in rows for b in rows if a.target == b.target}
        promoted = set()
        for family in output.final:
            members = fixture['leaves']((family,))
            promoted.update((a.label, b.label) for a in members for b in members)
        require(promoted == original and len(original) == 977, 'exact comparison-domain equality failed')
        require(tuple(observed['masses']) == (121, 16), 'branch masses changed')
        indexed_source = fixture['indexed'](rows, 'source')
        indexed_target = fixture['indexed'](fixture['unindex'](indexed_source), 'target')
        require(constructor.T8(indexed_source, fixture) == output.source_view(fixture), 'upper square failed')
        require(constructor.T7(indexed_target, fixture) == output.target_view(fixture), 'lower square failed')
        require(observed['J4'] == fixture['read_at_four'](indexed_target) == fixture['read_at_four'](output.target_view(fixture)), 'J4 changed')
        corrupted = tuple(replace(row, source=('assembly', 'A'), target=('assembly', 'B')) for row in rows)
        try:
            constructor.T9(corrupted, fixture)
        except ValueError:
            pass
        else:
            raise ValueError('assembly endpoint role silently accepted')
        return {'records': 137, 'final_families': 32, 'domain_pairs': len(original),
                'domain_equality': True, 'both_squares': True, 'J4_unchanged': True,
                'branch_masses': [121, 16], 'assembly_role_corruption_rejected': True}
    finally:
        sys.path[:] = previous


def attach(binding):
    previous_path = HOME / 'contracts/programme-hierarchy.v15.json'
    hierarchy = json.loads(previous_path.read_text())
    hierarchy.update(schema='marici.conjecture-net.programme-hierarchy.v16', id='marici.relational-carrier-physics-programme.v16',
                     phase='ledger4320_exact_domain_software_and_physical_reference_boundary', predecessor=previous_path.relative_to(ROOT).as_posix())
    hierarchy['ledger_evidence_links'] = [{
        'id': binding['id'], 'contract': CONTRACT.relative_to(ROOT).as_posix(), 'ledger': binding['ledger'],
        'software_contract': SOFTWARE.relative_to(ROOT).as_posix(), 'software_binding_complete': True,
        'scope': 'Selected exact-domain software transport; conditional reference/bank/network constructions.',
        'physical_realization_established': False, 'discharges_parent_obligation': False, 'proof_bearing': False,
        'related_scattering_net': 'scattering.high-energy.v1',
        'scattering_relation': 'shared_reference_preparation_calibration_boundary_not_a_physical_bridge', 'outcome': None}]
    hierarchy['endpoint_role_binding_gate'] = {
        'software_status': 'selected_exact_domain_contract_locally_replayed',
        'software_contract': SOFTWARE.relative_to(ROOT).as_posix(),
        'supersedes_software_unselected_gate': 'research/conjecture_net/contracts/programme-hierarchy.v15.json',
        'first_missing_object': 'Physical reference/preparation and endpoint/instrument calibration map; software selection does not supply it.',
        'acceptance_test': 'Supply source-derived physical preparation, port/boundary transport, gain, clock and calibration on the declared resources.',
        'authority_only_branch_actionable': False, 'physical_T9_selected': False}
    create(HOME / 'contracts/programme-hierarchy.v16.json', hierarchy)


def register(paths):
    from collect import registry
    inventory_path = HOME / 'inventory.json'
    inventory = json.loads(inventory_path.read_text())
    entries = {x['source']: x for x in inventory['files']}
    for path in paths:
        if path.is_relative_to(HOME):
            continue
        name = path.relative_to(ROOT).as_posix()
        target = HOME / 'collection' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())
        entries[name] = {'source': name, 'collected': target.relative_to(HOME).as_posix(), 'sha256': sha(path),
                         'reason': 'ledger4320 exact-domain/reference boundary evidence'}
    inventory['files'] = [entries[name] for name in sorted(entries)]
    inventory_path.write_text(json.dumps(inventory, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    (HOME / 'registry.json').write_text(json.dumps(registry({k: v['reason'] for k, v in entries.items()}), indent=2, sort_keys=True) + '\n', encoding='utf-8')


def main():
    paths = sources()
    binding = {
        'schema': 'marici.conjecture-net.ledger4320-reference-boundary.v1', 'id': 'ledger4320.exact-domain-reference-boundary.v1',
        'ledger': {'entry': 4320, 'author': 'marici.Strominger', 'path': LEDGER.relative_to(ROOT).as_posix(), 'sha256': sha(LEDGER)},
        'software': {'contract_id': 'nima.T9.exact-domain.software.v1', 'contract': SOFTWARE.relative_to(ROOT).as_posix(),
                     'receipt': SOFTWARE_RECEIPT.relative_to(ROOT).as_posix(), 'selection_scope': 'software_only',
                     'fixture': {'records': 137, 'first_families': 32, 'final_families': 32, 'domain_pairs': 977}},
        'conjectures': [
            {'id': 'exact-domain-software-transport', 'status': 'selected_software_contract_verified', 'outcome': None,
             'statement': 'The selected software T9 preserves and reflects the original comparison domain, records, masses, J4 and branch summaries.'},
            {'id': 'conditional-reference-bank-network', 'status': 'conditional_constructions_reported', 'outcome': None,
             'statement': 'Clifford banks and normalized260-coordinate exchange admit an ideal passive factorization on explicitly supplied inputs.'},
            {'id': 'physical-reference-realization', 'status': 'deferred_missing_preparation_and_calibration', 'outcome': None,
             'statement': 'Physical source selection, joint preparation, port transport, gain, detector, reset and degradation require independent inputs.'}],
        'related_net': {'id': 'scattering.high-energy.v1', 'contract': 'research/scattering/high-energy/contracts/high-energy-scattering-conjecture-net.v1.json',
                        'target_claim': 'physical-calibration-and-species', 'relation': 'shared_unresolved_physical_reference_boundary'},
        'evidence_sha256': {p.relative_to(ROOT).as_posix(): sha(p) for p in paths},
        'boundary': {'physical_T9_selected': False, 'calibrated_apparatus_established': False,
                     'scattering_physical_bridge_constructed': False, 'new_formal_compiler_run': False,
                     'programme_proof_link_admitted': False, 'owner_receipts_regenerated': False}}
    create(CONTRACT, binding)
    validate_binding(binding)
    replay = replay_software()
    attach(binding)
    register(paths)
    validate_binding(binding)
    result = {'schema': 'marici.conjecture-net.ledger4320-connection-result.v1', 'status': 'pass', 'validation_only': True,
              'ledger_entry': 4320, 'software_binding_complete': True, 'software_replay': replay,
              'source_receipts_integrity_checked': True, 'new_formal_compiler_run': False,
              'owner_receipts_regenerated': False, 'physical_reference_boundary_open': True, 'root_outcome': None,
              'contract_sha256': sha(CONTRACT), 'checker_sha256': sha(Path(__file__))}
    (HOME / 'results/ledger4320-connection.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
