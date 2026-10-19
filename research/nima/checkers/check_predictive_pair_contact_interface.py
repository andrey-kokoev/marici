"""Audit the existing contact-singlet operator against the geometric quotient.

Fresh exact logical-gate tests, not a replay of the raw embedding/energy model.
The independent logical/contact extension is a non-descent control, not a
claimed source binding of spin states to geometric histories.
"""
from contextlib import redirect_stdout
from dataclasses import dataclass
from pathlib import Path
import hashlib
import io
import json
import sys

from check_actual_pair_phase_rung_bridge import main as build
from predictive_pair_quotient import PredictivePairQuotient

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OWNER = ROOT / 'research/voevodsky'
sys.path.insert(0, str(OWNER / 'checkers'))
from check_proton_electron_contact_binding import ZERO, ONE, S2, outer, norm, act


@dataclass(frozen=True)
class InterfaceProbe:
    geometric_state: int
    at_contact: bool
    logical_pair: tuple


def effect(probe, projector):
    # The existing A=C tensor Pi on a definite relative-position sector.
    return act(projector, probe.logical_pair) if probe.at_contact else (ZERO,) * 4


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    with redirect_stdout(io.StringIO()):
        binding = build()
    q = PredictivePairQuotient(binding)
    singlet = (ZERO, ONE / S2, -ONE / S2, ZERO)
    triplet = (ZERO, ONE / S2, ONE / S2, ZERO)
    projector = outer(singlet)
    check('logical/singlet-normalized', norm(singlet) == ONE)
    check('logical/triplet-normalized', norm(triplet) == ONE)
    check('existing-effect/singlet-fixed', act(projector, singlet) == singlet)
    check('existing-effect/triplet-annihilated', act(projector, triplet) == (ZERO,) * 4)
    for i in range(4):
        basis = tuple(ONE if j == i else ZERO for j in range(4))
        check(f'existing-effect/idempotent/{i}',
              act(projector, act(projector, basis)) == act(projector, basis))
    # This Cartesian extension deliberately leaves the added source variables
    # independent. No undocumented preparation policy may be used to remove
    # the colliding probes and manufacture a function on geometric states.
    for state in range(len(q.states)):
        a = InterfaceProbe(state, True, singlet)
        b = InterfaceProbe(state, True, triplet)
        c = InterfaceProbe(state, False, singlet)
        check(f'fiber/same-geometric-projection/{state}',
              a.geometric_state == b.geometric_state == c.geometric_state)
        check(f'fiber/spin-changes-effect/{state}',
              norm(effect(a, projector)) == ONE and norm(effect(b, projector)) == ZERO)
        check(f'fiber/contact-changes-effect/{state}', norm(effect(c, projector)) == ZERO)
        for policy in ('inherited', 'common'):
            record = q.retain(q.witnesses[state], policy)
            check(f'transport/no-new-interface-data/{policy}/{state}',
                  q.project_rung(record) == state and q.restore(record) == q.witnesses[state])

    paths = [Path(__file__), HERE / 'predictive_pair_quotient.py',
             HERE / 'check_actual_pair_phase_rung_bridge.py',
             OWNER / 'checkers/check_proton_electron_contact_binding.py',
             OWNER / 'proton-electron-contact-binding.md',
             OWNER / 'checkers/check_pentachoron_spin_interfaces.py',
             OWNER / 'checkers/check_pentachoron_cycle_transport.py',
             HERE.parent / 'results/actual-pair-phase-rung-bridge.json']
    report = {
        'schema': 'marici.nima.predictive-pair-contact-interface.v1',
        'verification_status': 'pass', 'binding_status': 'unresolved', 'checks': checks,
        'existing_shared_operator': 'A = contact_projector tensor singlet_projector',
        'fresh_scope': 'Logical effect using existing exact arithmetic/action helpers; '
                       'fresh geometric phase bridge. Raw embeddings and energy model not replayed.',
        'non_descent_control': {
            'domain': 'Independent product of each geometric state with contact and logical-pair data',
            'geometric_states_checked': len(q.states),
            'same_fiber_effect_squared_norms': {
                'contact_singlet': '1', 'contact_triplet': '0', 'separated_singlet': '0'},
            'conclusion': 'The existing operator does not factor through forgetting spin/contact '
                          'on this independent extension. This is not proof against a supplied '
                          'restricted preparation binding.'},
        'missing_binding': [
            'Source preparation mapping or relation from geometric histories to logical pair states',
            'Proton spin extension and electron chirality/lift selection at the same interface',
            'Relative-position/contact datum independent of the geometric endpoint letters',
            'Action of all 11 geometric requests on spin, relative position and retained mediator',
            'Policy saying whether to preserve an effect, a sector, a value or a transported reference'],
        'closed_restricted_domain': None,
        'reason_not_computed': 'No predicate on the 60 states is supplied by this operator; '
                               'turning its projector into Boolean admission would add a policy.',
        'input_sha256': {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                         for path in paths},
    }
    output = HERE.parent / 'results/predictive-pair-contact-interface.json'
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} exact contact-interface checks')
    print('Existing contact-singlet effect varies within every independent geometric-state fiber.')
    print('BLOCKED: spin/contact preparation and request-action binding; no restricted graph invented.')


if __name__ == '__main__':
    main()
