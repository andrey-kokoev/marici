"""Last H6 budget cycle: bounded polynomial defect-action screen, not norm proof."""
import argparse
import json
from pathlib import Path
from check_finite_preconditioner import audit as finite_audit
from high_energy_scattering_net import ROOT,HOME,digest
from receipt_replay import assert_receipt_matches

NOTE=HOME/'POLYNOMIAL-PRECONDITIONER-SCREEN.md'
RESULT=HOME/'results/polynomial-preconditioner.v1.json'


def audit():
    finite=finite_audit(power_steps=8)
    rows=finite['polynomial_power_action_tests']
    below=[r['power'] for r in rows if max(r['prepared_action_norm_ratios'])<1]
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',HOME/'check_finite_preconditioner.py']
    return {'schema':'marici.scattering.polynomial-preconditioner.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'finite_response_audit':finite,'fixed_powers_tested':list(range(1,9)),
            'powers_with_all_four_prepared_ratios_below_one':below,
            'operator_norm_upper_bound_certified':False,'stationary_solver_error_certified':False,
            'full_band_covered':False,'bounded_H6_attempt_outcome':'inconclusive; six-cycle budget exhausted',
            'H6_disposition':'open; polynomial inverse route screened on stored columns, no exact-model error bound'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','power_tests':result['finite_response_audit']['polynomial_power_action_tests'],
                     'bounded_H6_attempt_outcome':result['bounded_H6_attempt_outcome']}))


if __name__=='__main__':main()
