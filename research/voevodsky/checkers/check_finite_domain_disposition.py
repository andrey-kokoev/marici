"""Review the finite pilot disposition without promoting it to native generation."""
import copy
import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = 'research/conjecture_net/contracts/mathematical-realization-conjecture-net.v1.json'
RECEIPT = 'research/voevodsky/results/finite-domain-interface-audit-v1.json'

def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))

def require(ok, message):
    if not ok:
        raise ValueError(message)

def validate(branch, receipt):
    node = next(n for n in branch['conjectures'] if n['id'] == 'finite-domain-wg-example')
    require(node['status'] == 'resolved' and node['verdict'] == 'constructed', 'disposition missing')
    require(node['resolution_kind'] == 'bounded_supplied_operation_adapter_audit', 'scope promotion')
    require(node['outcome'] is None, 'formal outcome admission not supplied')
    for key in ('native_category_law_generation', 'arbitrary_dependent_payload_action_instantiated',
                'universal_coverage_proved'):
        require(node[key] is False, 'unsupported ' + key)
    require('finite-domain-interface-audit' in node['evidence'], 'missing evidence link')
    artifact = next(a for a in branch['artifacts'] if a['id'] == 'finite-domain-interface-audit')
    require(artifact['receipt'] == RECEIPT, 'wrong receipt')
    require(artifact['note'] in receipt['source_sha256'], 'review note not pinned')
    require(receipt['passed'] and receipt['returncode'] == 0, 'safe compilation missing')
    require({'--safe', '--ignore-interfaces'} <= set(receipt['command']), 'stale or unsafe compile')
    require({'supplied-law-recovered', 'same-operation-response', 'retained-length',
             'request-endpoint'} <= set(receipt['theorems']), 'missing obligations')
    for key in ('native_category_law_generation', 'multi_step_native_category_binding', 'universal_realization'):
        require(receipt[key] is False, 'receipt overclaim')
    controls = receipt['negative_controls']
    require({c['module'] for c in controls} == {'BadRepeatedCompute', 'BadRequestRelabel'}, 'missing controls')
    for control in controls:
        require(control['returncode'] != 0 and 'error: [UnequalTerms]' in control['diagnostic_tail'],
                'negative control not rejected for type mismatch')
    for p, expected in receipt['source_sha256'].items():
        require(sha256((ROOT / p).read_bytes()).hexdigest() == expected, 'evidence source drift: ' + p)

def main():
    branch, receipt = load(BRANCH), load(RECEIPT)
    validate(branch, receipt)
    rejected = []
    for key in ('native_category_law_generation', 'arbitrary_dependent_payload_action_instantiated',
                'universal_coverage_proved', 'outcome'):
        bad = copy.deepcopy(branch)
        n = next(n for n in bad['conjectures'] if n['id'] == 'finite-domain-wg-example')
        n[key] = True
        try:
            validate(bad, receipt)
        except ValueError:
            rejected.append(key)
        else:
            raise AssertionError('promotion accepted: ' + key)
    result = {'passed': True, 'disposition': 'bounded_supplied_operation_adapter_audit',
              'promotion_controls_rejected': rejected,
              'formal_outcome_admitted': False, 'universal_realization_proved': False}
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
