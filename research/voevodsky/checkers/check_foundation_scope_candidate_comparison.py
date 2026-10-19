"""Compare bounded F/K/E candidates without selecting a universal foundation."""
import json
import subprocess
import sys
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NOTE = 'research/voevodsky/foundation-scope-candidate-comparison-v1.md'
SELECTOR = 'research/conjecture_net/contracts/physics-programme-current.v1.json'
CHARTER = 'research/nima/contracts/physics-target-charter.v1.json'
OUT = 'research/voevodsky/results/foundation-scope-candidate-comparison-v1.json'

def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8'))

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def validate_claim(c):
    require(not any(c.values()), 'unsupported profile promotion')

def main():
    current = load(SELECTOR); charter = load(CHARTER)
    programme = load(current['contract'])
    require(current['contract'].endswith('programme-hierarchy.v18.json'), 'physical selector changed; review required')
    require(programme['selected_physical_targets'] == charter['selected_physical_targets'], 'target selection drift')
    require(charter['common_source_witness_id'] is None and not charter['physical_realization_admitted']
            and not charter['empirical_evidence_admitted'], 'physical admission changed; review required')
    require(charter['empirical_acceptance']['acquired_dataset'] is None, 'new empirical records require review')
    targets = {t['id']: t for t in charter['targets']}
    cavity = targets['reciprocal-lossy-cavity-ordered-response']
    detector = targets['finite-dead-time-detector-records']
    require(cavity['regime']['maximum_steps'] == detector['regime']['maximum_steps'] == 3, 'regime drift')
    p = {k: Q(cavity['nominal_fixture'][k]) for k in ('r1', 't1', 'r2', 'a')}
    u, x = Q(4, 5), Q(3, 5)
    reflected = -p['r1']*u + p['t1']*x
    forward = p['t1']*u + p['r1']*x
    stored = p['a']*p['r2']*forward
    next_reflected = p['t1']*stored
    require(reflected == 0 and stored == Q(12, 25), 'dark state calculation')
    require(next_reflected == Q(cavity['reference_predictions']['next_zero_drive_reflected']) == Q(48, 125), 'continuation mismatch')
    eta = Q(detector['nominal_fixture']['eta'])
    pcc = eta*0  # after first click the second photon meets dead memory
    reset_pcc = eta**2
    require(pcc == Q(detector['reference_predictions']['p_CC_given_inputs_11']) == 0, 'memory law')
    require(reset_pcc == Q(detector['reference_predictions']['iid_reset_p_CC']) == Q(81, 625), 'reset hostile')
    script = 'research/nima/checkers/check_native_table_equivalence.py'
    run = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, capture_output=True, text=True, timeout=180)
    require(run.returncode == 0, 'native table evidence failed\n' + run.stdout + run.stderr)
    claims = dict(arbitrary_atoms_natively_generated=False, target_charter_is_physical_admission=False,
                  finite_syntax_implies_finite_execution=False, bounded_profile_is_universal=False)
    validate_claim(claims)
    rejected = []
    for key in claims:
        bad = dict(claims); bad[key] = True
        try:
            validate_claim(bad)
        except ValueError:
            rejected.append(key)
        else:
            raise AssertionError('profile promotion accepted')
    paths = [NOTE, SELECTOR, current['contract'], CHARTER, script,
             'research/nima/native-table-equivalence.md', 'research/nima/two-sided-transport-foundation.md',
             'research/nima/agda/WholePackageSigmaPi.agda', 'research/nima/agda/WholePackageResolution.agda',
             'research/conjecture_net/contracts/common-foundations-formulation-candidate.v1.json',
             Path(__file__).relative_to(ROOT).as_posix()]
    result = dict(schema='marici.foundation-scope-candidate-comparison.v1', passed=True,
                  candidate_profiles=['native-retained-tables', 'classical-analytic-package', 'bounded-physical-target-pair'],
                  native_table_check=dict(returncode=run.returncode, summary=run.stdout.strip()),
                  exact_controls=dict(dark_current=str(reflected), stored=str(stored), next_reflected=str(next_reflected),
                                      detector_CC=str(pcc), reset_rival_CC=str(reset_pcc)),
                  rejected_promotions=rejected, formulation_gate_discharged=False,
                  universal_foundation_selected=False, physical_realization_admitted=False,
                  fresh_Agda_compilation=False,
                  source_sha256={p: sha256((ROOT / p).read_bytes()).hexdigest() for p in paths})
    (ROOT / OUT).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))

if __name__ == '__main__':
    main()
