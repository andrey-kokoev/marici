#!/usr/bin/env python3
"""Retain an explicit first-simple-root superfunction and test its normalization.

No owner producer is executed and no missing atlas data are reconstructed.
Exact rational fixtures are controls, not a symbolic positive-cell theorem.
"""
import itertools
import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/benincasa/.tmp_sympy'))
sys.path.insert(0, str(ROOT / 'research/nima'))
import sympy as s
from dual_r_invariant import generalized_r
from dual_spinor_kinematics import angle, momentum_conserving_kinematics, transport_spinor
from nnmhv_coherence_paths import compile_nnmhv_histories, terminal_r_state


def text(q):
    return str(s.factor(q))


def retain(meta):
    return {'prefactor': text(meta['prefactor']),
            'eta_linear_coefficients': {str(j): text(q) for j, q in sorted(meta['xi_coefficients'].items())},
            'denominator_factors': [text(q) for q in meta['denominator_factors']]}


def evaluate(shift):
    n = 8
    lam, til, x = momentum_conserving_kinematics(
        [(1, j*j+j+1+shift*j) for j in range(1, n+1)],
        [(1, j**3+2*j+1+shift*j*j) for j in range(1, n-1)])
    eps = s.Matrix([[0, 1], [-1, 0]])
    h = compile_nnmhv_histories(n)[3]
    assert h.outer_pair == (2, 5) and h.inner_pair == (3, 5)
    st = terminal_r_state(h)
    _, outer = generalized_r(lam, x, n, (), h.outer_pair, lam[1].T*eps, lam[5].T*eps)
    lower = transport_spinor(lam, x, st.lower_spinor.vertices)
    upper = transport_spinor(lam, x, st.upper_spinor.vertices)
    upper0 = lam[5].T*eps
    polynomial_t, updated = generalized_r(lam, x, n, h.inner_prefix, h.inner_pair, lower, upper)
    polynomial_0, unupdated = generalized_r(lam, x, n, h.inner_prefix, h.inner_pair, lower, upper0)
    ratio = s.factor(unupdated['prefactor'] / updated['prefactor'])
    q, qt = unupdated['xi_coefficients'], updated['xi_coefficients']
    qo = outer['xi_coefficients']
    wedge = qo.get(2, 0)*q.get(3, 0)-qo.get(3, 0)*q.get(2, 0)
    selector = s.factor(wedge**4 / angle(lam, 2, 3)**4)
    K = s.factor(outer['prefactor']*updated['prefactor']*selector)
    K0 = s.factor(outer['prefactor']*unupdated['prefactor']*selector)
    B = s.factor(K-K0)
    # All 70 momentum-conservation-quotiented one-SU(4) numerator coefficients.
    coefficients = {}
    for labels in itertools.combinations(range(1, 9), 4):
        coefficients[' '.join(map(str, labels))] = text(s.det(s.Matrix([
            [lam[j][0] for j in labels], [lam[j][1] for j in labels],
            [qo.get(j, 0) for j in labels], [q.get(j, 0) for j in labels]])))
    # Endpoint dependence is confined to angle_b and its denominator sandwich.
    a_t = s.det(s.Matrix.hstack(eps*upper.T, lam[4]))
    a_0 = s.det(s.Matrix.hstack(eps*upper0.T, lam[4]))
    ratio_formula = s.factor(a_0/a_t * updated['denominator_factors'][1]/unupdated['denominator_factors'][1])
    checks = {
        'cyclic_momentum_conservation': x[9] == s.zeros(2),
        'same_eta_linear_form': q == qt,
        'all_inner_polynomial_coefficients_scale': set(polynomial_0) == set(polynomial_t) and
            all(s.factor(polynomial_0[k]-ratio*polynomial_t[k]) == 0 for k in polynomial_0),
        'endpoint_ratio_formula': ratio == ratio_formula,
        'component_selector_nonzero': selector != 0,
        'K0_equals_ratio_K': s.factor(K0-ratio*K) == 0,
        'B_equals_one_minus_ratio_K': s.factor(B-(1-ratio)*K) == 0,
        'ratio_not_unit': ratio != 1,
        'all_localization_factors_nonzero': all(z != 0 for meta in [outer, updated, unupdated] for z in meta['denominator_factors']) and a_t != 0 and angle(lam, 2, 3) != 0,
    }
    assert all(checks.values()), checks
    return {'shift': shift,
            'kinematics': {'lambda': {str(j): list(map(text, lam[j])) for j in lam},
                           'tilde_lambda': {str(j): list(map(text, til[j])) for j in til}},
            'outer': retain(outer), 'transported_inner': retain(updated),
            'untransported_inner': retain(unupdated),
            'full_superfunction_encoding': 'prefactor_outer * prefactor_inner * product_{A=1..4}(q_outer^A q_inner^A); each q^A has the stored eta linear coefficients, with outer before inner',
            'one_SU4_quotient_numerator_coefficients': coefficients,
            'untransported_to_transported_ratio': text(ratio),
            'component': {'selector': 'product_A eta_2^A eta_3^A / <23>^4',
                          'K': text(K), 'K0': text(K0), 'B_11': text(B)},
            'checks': checks}


def main():
    runs = [evaluate(shift) for shift in (0, 1, 2)]
    ratios = {r['untransported_to_transported_ratio'] for r in runs}
    assert len(ratios) > 1, 'fixture family did not discriminate a nonconstant ratio'
    sources = ['research/nima/nnmhv_coherence_paths.py', 'research/nima/dual_r_invariant.py',
               'research/nima/dual_spinor_kinematics.py', 'research/nima/nnmhv-component-23-support-theorem.md',
               'research/nima/check_nnmhv_kernel_wall_tail_boundary.py']
    out = {
        'schema': 'marici.benincasa.untransported-simple-root-candidate.v1',
        'history_index': 3, 'root': [1, 1],
        'source_candidate': {'outer_pair': [2, 5], 'inner_pair': [3, 5], 'inner_prefix': [5, 2],
                             'xi_path': [8, 5, 2], 'lower_path': [2],
                             'transported_upper_path': [8, 2, 5], 'untransported_upper_path': [5]},
        'symbolic_endpoint_identity': {
            'definition': 'Let u_t=<8|x_82 tilde(x_25), u_0=<5|, k(u)=epsilon*u^T, xi=<8|x_85 tilde(x_52), L=xi*x_23*tilde(x_35).',
            'ratio_R0_over_Rt': 'c = det[k(u_0),lambda_4]/det[k(u_t),lambda_4] * (L*k(u_t))/(L*k(u_0))',
            'reason': 'generalized_r eta coefficients do not depend on boundary spinors; only angle_b and one denominator sandwich change',
            'full_product': 'F0=c*Ft; Ft-F0=(1-c)*Ft',
            'localization': 'All outer and both inner denominator factors nonzero; det[k(u_t),lambda_4] nonzero for ratio representation; <23> nonzero for normalized component.',
            'form_admission': 'Not supplied. This is a rational superfunction identity, not identification of c with a positive-chart log Jacobian.'},
        'runs': runs,
        'checks': {'all_exact_fixture_checks': all(all(r['checks'].values()) for r in runs),
                   'ratio_varies_with_kinematics': len(ratios) > 1,
                   'same_cell_unit_normalization_shortcut_rejected': all(r['checks']['ratio_not_unit'] for r in runs)},
        'canonical_admission': {'verdict': 'open',
                               'rejected_shortcut': 'Reuse the transported cell with its unchanged unit canonical normalization. Nonunit, varying c cannot be ignored.',
                               'remaining_candidates': 'A different admitted cell, chain, pushforward or source-derived coefficient-valued form may realize F0; none is constructed here.',
                               'orientation': 'Fixed algebraic Grassmann factor order outer then inner; positive dlog chart orientation not yet constructed.'},
        'evidence_level': 'Exact rational algebra at three nonsingular fixtures plus written endpoint identity read from the evaluator; no atlas, positive-domain or kernel proof.',
        'source_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'passed': True,
    }
    path = ROOT/'research/benincasa/results/untransported_simple_root_candidate.json'
    path.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'passed': out['passed'], 'ratios': [r['untransported_to_transported_ratio'] for r in runs],
                      'checks': out['checks'], 'canonical_admission': out['canonical_admission']}, indent=2))


if __name__ == '__main__':
    main()
