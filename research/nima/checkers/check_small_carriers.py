"""Quarantined hard-coded gauge-group/minimality table."""
import json

if __name__ == '__main__':
    print(json.dumps({
        'status': 'quarantined', 'verification_performed': False,
        'reason': 'No carrier-to-continuous-gauge embedding or minimality theorem was computed.',
        'original': 'quarantine/20261007-generation-evidence/checkers/check_small_carriers.py',
        'comparison': 'twelve-arrow-blocks-and-generation-selection.md'
    }, indent=2))
    raise SystemExit(2)
