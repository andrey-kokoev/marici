"""Quarantined print-only generation/minimality claim; not a test suite."""
import json

if __name__ == '__main__':
    print(json.dumps({
        'status': 'quarantined', 'verification_performed': False,
        'reason': 'Generation counts were printed from a supplied 4n rule; the original also omitted its json import.',
        'original': 'quarantine/20261007-generation-evidence/checkers/check_larger_carrier.py',
        'comparison': 'twelve-arrow-blocks-and-generation-selection.md'
    }, indent=2))
    raise SystemExit(2)
