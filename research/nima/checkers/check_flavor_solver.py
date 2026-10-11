"""Quarantined phase-only mass fit; original functions and scan are preserved."""
import json

if __name__ == '__main__':
    print(json.dumps({
        'status': 'quarantined', 'verification_performed': False,
        'reason': 'The original matrix is diagonally unitarily conjugate to its base. Its singular values cannot split; a finer phase scan cannot reach the stated mass target. Mixing frames also have a repeated-eigenvalue ambiguity.',
        'original': 'quarantine/20261007-phase-readout-evidence/checkers/check_flavor_solver.py',
        'comparison': 'twelve-point-phase-readout-descent.md'
    }, indent=2))
    raise SystemExit(2)
