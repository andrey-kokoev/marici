"""Quarantined source-selection report, not a checked SU2 promotion."""
import json


def main():
    print(json.dumps({
        'schema':'marici.nima.quarantined-evidence.v1','status':'quarantined',
        'reason':'The original script reports an assumed nonabelian promotion without calculating one or selecting SU2. The completed abelian phase lift remains consistent; a Maurer-Cartan identity does not select a fiber group.',
        'original':'quarantine/20261007-constraint-evidence/checkers/check_su2_promotion.py',
        'comparison_packet':'finite-canonical-actions-versus-adm-constraints.md',
        'historical_receipt':'not modified'
    },indent=2))
    raise SystemExit(2)


if __name__ == '__main__':
    main()
