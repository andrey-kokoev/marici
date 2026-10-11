"""Quarantined formula report, not an executed holonomy/flux bracket check."""
import json


def main():
    print(json.dumps({
        'schema':'marici.nima.quarantined-evidence.v1','status':'quarantined',
        'reason':'The original script defines neither Poisson observables nor a bracket calculation. Its LQG identification and kappa/Planck-area matching were formula reports, not verified comparisons.',
        'original':'quarantine/20261007-constraint-evidence/checkers/check_holonomy_flux_algebra.py',
        'comparison_packet':'finite-canonical-actions-versus-adm-constraints.md',
        'historical_receipt':'not modified'
    },indent=2))
    raise SystemExit(2)


if __name__ == '__main__':
    main()
