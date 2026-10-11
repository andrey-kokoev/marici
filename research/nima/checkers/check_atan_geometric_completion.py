"""Check arctangent support and the nonnegative small-grid Cayley bridge, not Machin endpoints."""
import argparse
import json
import subprocess
from pathlib import Path
from check_half_turn_coefficients import AGDA, SEARCH, ROOT, REPO, closure, digest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--module', choices=['TickAtanGeometricCompletion', 'TickAtanCompletionFirstOrder', 'TickAtanCompletionSlope', 'TickOperationalTrigFirstOrder', 'TickCompletionTrigSmallAngle', 'TickCompletionTelescoping', 'TickCayleyGridSlope', 'TickAtanCayleyIncrement', 'TickCayleyRotationalBracket', 'TickCayleyNormalizedBracket', 'TickRotationDefectTransport', 'TickCayleyConcreteTransport', 'TickCayleyInvariantStep', 'TickCayleyInvariantConstancy', 'TickOperationalCayleyIdentity'], default='TickAtanGeometricCompletion')
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=900)
    args = parser.parse_args()
    source = ROOT / 'agda' / (args.module + '.agda')
    sources = closure(source) | {Path(__file__).resolve(), Path(__file__).with_name('check_half_turn_coefficients.py')}
    before = {p: digest(p) for p in sources}
    command = [str(AGDA), '--safe', '--cubical', '--guardedness', '--transliterate']
    if not args.cached:
        command.append('--ignore-interfaces')
    for path in SEARCH:
        command.extend(['-i', str(path)])
    command.append(str(source))
    try:
        run = subprocess.run(command, capture_output=True, timeout=args.timeout)
        output, code = run.stdout + run.stderr, run.returncode
    except subprocess.TimeoutExpired as error:
        output, code = (error.stdout or b'') + (error.stderr or b''), None
    stable = all(digest(p) == h for p, h in before.items())
    verified = code == 0 and stable
    modules = {p.stem for p in sources}
    result = {
        'status': 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail'),
        'module': source.stem, 'exit_code': code, 'command': command,
        'fresh_dependency_check': not args.cached, 'sources_stable': stable,
        'compiler_sha256': digest(AGDA),
        'source_sha256': {p.relative_to(REPO).as_posix(): h for p, h in before.items() if p.is_relative_to(REPO)},
        'external_dependency_sha256': {str(p): h for p, h in before.items() if not p.is_relative_to(REPO)},
        'theorem_scope': ('exact implemented cosine/sine Cayley identities at doubled arctangent of N/(d+1), for natural N,d and magnitude at most one half, via actual outer-factor transport and concrete dyadic telescoping; no negative-input extension or Machin/pi endpoint theorem'
                          if args.module == 'TickOperationalCayleyIdentity' else
                          'actual Cayley comparison invariant constant on nonnegative half-radius rational grid inputs, by concrete dyadic meshes, checked endpoint representation paths, and componentwise fine-mesh telescoping; zero evaluation and explicit Cayley rearrangement remain open'
                          if args.module == 'TickCayleyInvariantConstancy' else
                          'actual Cayley comparison invariant differences bounded uniformly quadratically on fine small grids, using checked rational rotor composition and concrete outer-factor bounds; dyadic endpoint construction and telescoping application remain open'
                          if args.module == 'TickCayleyInvariantStep' else
                          'actual grid bracket transported through the concrete operational and rational inverse outer rotors with proved uniform bounds; the preceding-invariant rational composition path and telescoping application remain open'
                          if args.module == 'TickCayleyConcreteTransport' else
                          'closed completion product magnitude bound and transport of the actual normalized grid bracket through two outer rotor factors, conditional on their bounds; not yet the invariant step or telescoping application'
                          if args.module == 'TickRotationDefectTransport' else
                          'normalized actual operational rotation versus relative rational Cayley rotation on fine grids, with constructed denominator inverse and uniform real/imaginary error bounds 34*e² and 99*e²'
                          if args.module == 'TickCayleyNormalizedBracket' else
                          'actual denominator-cleared operational rotational bracket bounds on small grids, explicit error budgets, and verified small-angle radius from arctangent increment estimates'
                          if args.module == 'TickCayleyRotationalBracket' else
                          'completion arctangent relative Cayley increment discrepancy bounded quadratically on nonnegative shared-denominator small grids'
                          if args.module == 'TickAtanCayleyIncrement' else
                          'constructed positive rational grid inverses, exact finite Cayley increment cancellation with quadratic bound, and equality of the completion slope with the rational grid inverse'
                          if args.module == 'TickCayleyGridSlope' else
                          'finite completion telescoping, dyadic quadratic accumulated-error budget, and exact endpoint equality criterion with explicit local-bound hypotheses'
                          if args.module == 'TickCompletionTelescoping' else
                          'quadratic operational sine/cosine remainder bounds on arbitrary completion inputs of magnitude at most 1/4, by closed-bound limit preservation and density'
                          if args.module == 'TickCompletionTrigSmallAngle' else
                          'quadratic small-angle remainders for presentations explicitly identified with implemented completion sine and cosine on rational inputs'
                          if args.module == 'TickOperationalTrigFirstOrder' else
                          'small rational arctangent denominator-free completion slope remainder bound, inverse slope identity, and exact zero initial value'
                          if args.module == 'TickAtanCompletionSlope' else
                          'small rational arctangent completion-level denominator-cleared quadratic remainder bound under actual scheduled completion operations'
                          if args.module == 'TickAtanCompletionFirstOrder' else
                          'small rational arctangent quadratic remainders, geometric series completion convergence, and inverse of the embedded denominator 1+q² under actual completion multiplication'),
        'completion_inverse_proved': 'TickAtanGeometricCompletion' in modules and verified,
        'completion_first_order_bound_proved': 'TickAtanCompletionFirstOrder' in modules and verified,
        'operational_trig_small_angle_bound_proved': 'TickOperationalTrigFirstOrder' in modules and verified,
        'completion_trig_small_angle_bound_proved': 'TickCompletionTrigSmallAngle' in modules and verified,
        'quadratic_telescoping_criterion_proved': 'TickCompletionTelescoping' in modules and verified,
        'concrete_cayley_invariant_constancy_proved': 'TickCayleyInvariantConstancy' in modules and verified,
        'operational_cayley_local_defect_bound_proved': 'TickCayleyInvariantStep' in modules and verified,
        'concrete_outer_rotor_transport_proved': args.module == 'TickCayleyConcreteTransport' and verified,
        'completion_product_magnitude_bound_proved': 'TickCompletionProductMagnitude' in modules and verified,
        'conditional_outer_rotor_transport_proved': args.module == 'TickRotationDefectTransport' and verified,
        'rational_cayley_increment_bound_proved': 'TickCayleyGridIncrement' in modules and verified,
        'completion_grid_slope_identification_proved': 'TickCayleyGridSlope' in modules and verified,
        'atan_relative_cayley_increment_bound_proved': 'TickAtanCayleyIncrement' in modules and verified,
        'grid_small_angle_radius_proved': 'TickAtanGridSmallAngle' in modules and verified,
        'denominator_cleared_rotational_bracket_bound_proved': 'TickCayleyRotationalBracket' in modules and verified,
        'normalized_rotational_bracket_bound_proved': args.module == 'TickCayleyNormalizedBracket' and verified,
        'uniform_quadratic_rotational_bracket_bound_proved': args.module == 'TickCayleyNormalizedBracket' and verified,
        'denominator_free_slope_bound_proved': args.module == 'TickAtanCompletionSlope' and code == 0 and stable,
        'atan_zero_initial_value_proved': args.module == 'TickAtanCompletionSlope' and code == 0 and stable,
        'all_completion_increments_derivative_proved': False,
        'operational_cayley_bridge_proved': 'TickOperationalCayleyIdentity' in modules and verified,
        'operational_cayley_bridge_domain': 'nonnegative rational grid inputs N/(d+1) bounded by one half',
        'machin_endpoints_proved': False,
        'unitary_half_turn_proved': False,
    }
    prefix = {'TickAtanGeometricCompletion': 'atan-geometric-completion-',
              'TickAtanCompletionFirstOrder': 'atan-completion-first-order-',
              'TickAtanCompletionSlope': 'atan-completion-slope-',
              'TickOperationalTrigFirstOrder': 'operational-trig-first-order-',
              'TickCompletionTrigSmallAngle': 'completion-trig-small-angle-',
              'TickCompletionTelescoping': 'completion-telescoping-',
              'TickCayleyGridSlope': 'cayley-grid-slope-',
              'TickAtanCayleyIncrement': 'atan-cayley-increment-',
              'TickCayleyRotationalBracket': 'cayley-rotational-bracket-',
              'TickCayleyNormalizedBracket': 'cayley-normalized-bracket-',
              'TickRotationDefectTransport': 'rotation-defect-transport-',
              'TickCayleyConcreteTransport': 'cayley-concrete-transport-',
              'TickCayleyInvariantStep': 'cayley-invariant-step-',
              'TickCayleyInvariantConstancy': 'cayley-invariant-constancy-',
              'TickOperationalCayleyIdentity': 'operational-cayley-identity-'}[args.module]
    stem = prefix + ('cached' if args.cached else 'fresh')
    (ROOT / 'results' / (stem + '.log')).write_bytes(output)
    (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'fresh_dependency_check', 'completion_inverse_proved', 'completion_first_order_bound_proved', 'operational_cayley_bridge_proved', 'machin_endpoints_proved')}))
    raise SystemExit(0 if result['status'] == 'pass' else 1)


if __name__ == '__main__':
    main()
