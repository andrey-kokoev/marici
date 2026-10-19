"""Countermodels for a candidate formulation, not verification of the root."""
import copy
import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = 'research/conjecture_net/contracts/common-foundations-formulation-candidate.v1.json'
NOTE = 'research/voevodsky/common-foundations-formulation-candidate-v1.md'
OUT = 'research/voevodsky/results/common-foundations-formulation-candidate-v1.json'
ORDER = ['fix_F_K_E', 'exists_common_P_and_physical_binding', 'exists_coherent_realization_family',
         'forall_valid_M_in_K', 'forall_licensed_stages_operations_and_continuations']

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def validate(c):
    require(c['quantifier_order'] == ORDER, 'changed quantifiers')
    require(c['validity']['selected_mode'] is None, 'unreviewed validity selection')
    require(c['physical_account']['selected_source'] is None and not c['physical_account']['physical_binding_supplied'], 'unjustified physical selection')
    require(not any(c['boundaries'].values()), 'candidate promoted')
    require(len(c['unresolved_selection_gates']) == 4, 'selection obligations hidden')
    require({'operation_squares', 'admitted_domains_and_guards', 'resource_translation', 'completion_witnesses'} <= set(c['representation']['required']), 'missing stagewise obligation')

def check_double_negation(x, trace, origin, budget):
    require(type(x) is bool and all(type(y) is bool for y in trace), 'Boolean types')
    require(origin == 'computed_from_declared_not', 'independent answer seed')
    require(len(trace) == 3 and trace[0] == x, 'missing intermediate stage')
    require(budget >= 2, 'insufficient sequential resource')
    for a, b in zip(trace, trace[1:]):
        require(b == (not a), 'operation square fails')
    require(trace[-1] == x, 'law output')

def main():
    c = json.loads((ROOT / CONTRACT).read_text(encoding='utf-8')); validate(c)
    rejected = []
    for name, trace, origin, budget in (
        ('answer-insertion', [False], 'answer_seed', 2),
        ('endpoint-only', [False], 'computed_from_declared_not', 2),
        ('endpoint-correct-intermediate-wrong', [False, False, False], 'computed_from_declared_not', 2),
        ('resource-erasure', [False, True, False], 'computed_from_declared_not', 1)):
        try:
            check_double_negation(False, trace, origin, budget)
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError('invalid realization accepted: ' + name)
    for x in (False, True):
        check_double_negation(x, [x, not x, x], 'computed_from_declared_not', 2)
    # Finite countermodel to swapping exists P / forall M. This is a logic
    # control for the two-element fixture, NOT an obstruction to all processes.
    relation = lambda p, m: p == m
    domain = (0, 1)
    separate = all(any(relation(p, m) for p in domain) for m in domain)
    common = any(all(relation(p, m) for m in domain) for p in domain)
    require(separate and not common, 'quantifier-order control')
    # Same current observation but different operation guards at fixed budget.
    current = lambda state: 0
    enabled = lambda state: state['budget'] >= 1
    a, b = {'budget': 1}, {'budget': 0}
    require(current(a) == current(b) and enabled(a) != enabled(b), 'guard-sensitive identity')
    # A finite prefix is not an all-index/limit witness.
    prefix = 4
    zero = lambda n: 0
    delayed = lambda n: 0 if n < prefix else 1
    require(all(zero(n) == delayed(n) for n in range(prefix)) and zero(prefix) != delayed(prefix), 'finite-to-infinite control')
    for mode in ('swapped-quantifiers', 'pilot-universality', 'physical-promotion', 'missing-operation-square'):
        bad = copy.deepcopy(c)
        if mode == 'swapped-quantifiers':
            bad['quantifier_order'][1], bad['quantifier_order'][3] = bad['quantifier_order'][3], bad['quantifier_order'][1]
        elif mode == 'pilot-universality':
            bad['boundaries']['universal_coverage_proved'] = True
        elif mode == 'physical-promotion':
            bad['physical_account']['physical_binding_supplied'] = True
        else:
            bad['representation']['required'].remove('operation_squares')
        try:
            validate(bad)
        except ValueError:
            rejected.append(mode)
        else:
            raise AssertionError('schema corruption accepted: ' + mode)
    sources = [CONTRACT, NOTE, 'research/conjecture_net/contracts/common-foundations-conjecture-net.v1.json',
               'research/conjecture_net/contracts/common-witness-comparison-interface.v1.json',
               Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.common-foundations-formulation-candidate-validation.v1', passed=True,
                  positive_computations=2, rejected_candidates=rejected,
                  quantifier_swap_countermodel=True, guard_identity_countermodel=True,
                  finite_prefix_not_limit_witness=True, formulation_gate_discharged=False,
                  physical_source_selected=False, foundation_selected=False,
                  source_sha256={p: sha256((ROOT / p).read_bytes()).hexdigest() for p in sources})
    (ROOT / OUT).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))

if __name__ == '__main__':
    main()
