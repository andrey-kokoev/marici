"""Fresh six-hypothesis suite plus the source-driven proton regression.

'Checks passed' means the explicit reconstruction/obstruction tests passed,
not that all six candidate hypotheses were established.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parent.parent
TESTS = [
    (4, 'check_common_assembly_symmetry.py', 'common_assembly_symmetry.json'),
    (2, 'check_common_assembly_cones.py', 'common_assembly_cones.json'),
    (5, 'check_common_assembly_constraints.py', 'common_assembly_constraints.json'),
    (3, 'check_common_assembly_gluing.py', 'common_assembly_gluing.json'),
    (6, 'check_common_assembly_refinement.py', 'common_assembly_refinement.json'),
    (1, 'check_common_assembly_dimension_cycle.py', 'common_assembly_dimension_cycle.json'),
]


def main():
    results = []
    for hypothesis, checker, artifact in TESTS:
        path = BASE/'checkers'/checker
        execution = subprocess.run([sys.executable, str(path)], cwd=ROOT,
                                   capture_output=True, text=True, timeout=120)
        if execution.returncode:
            raise RuntimeError(f'{checker} failed:\n{execution.stdout}\n{execution.stderr}')
        receipt_path = BASE/'results'/artifact
        raw = receipt_path.read_bytes()
        receipt = json.loads(raw)
        assert receipt['hypothesis'] == hypothesis and receipt['status'] == 'tested'
        results.append({'hypothesis': hypothesis, 'checks_passed': True,
                        'checker_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'receipt': artifact, 'receipt_sha256': hashlib.sha256(raw).hexdigest(),
                        'conclusion': receipt['conclusion']})
        print(f'H{hypothesis}: checks passed', flush=True)
    baseline = BASE.parent/'nima/checkers/check_triangle_arrow_source_input.py'
    execution = subprocess.run([sys.executable, str(baseline)], cwd=ROOT,
                               capture_output=True, text=True, timeout=120)
    if execution.returncode:
        raise RuntimeError(f'Proton source-input regression failed:\n{execution.stdout}\n{execution.stderr}')
    baseline_result = json.loads(execution.stdout)
    assert baseline_result['status'] == 'passed' and baseline_result['exact_historical_manifest_match']
    report = {'status': 'all_six_test_batches_passed', 'test_order': [h for h, _, _ in TESTS],
              'results': results, 'proton_source_input_regression': baseline_result,
              'baseline_checker_sha256': hashlib.sha256(baseline.read_bytes()).hexdigest(),
              'suite_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'Six bounded geometric hypothesis tests completed. Several simple versions are rejected. No common minimal-source particle constructor or neutron/electron coefficient derivation is claimed.'}
    (BASE/'results/common_assembly_hypotheses.json').write_text(json.dumps(report, indent=2)+'\n')
    print('All six test batches and exact source-driven proton regression passed.')


if __name__ == '__main__':
    main()
