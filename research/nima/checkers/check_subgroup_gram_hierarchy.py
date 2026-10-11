"""Quarantined subgroup-count derivation; supplied matrix retained in archive."""
import json

if __name__ == '__main__':
    print(json.dumps({
        'status': 'quarantined', 'verification_performed': False,
        'reason': 'The 3456/1152/576 matrix is neither the asserted point-transfer count nor the fixed-label probe Gram on S4^3.',
        'original': 'quarantine/20261007-generation-evidence/checkers/check_subgroup_gram_hierarchy.py',
        'comparison': 'twelve-arrow-blocks-and-generation-selection.md'
    }, indent=2))
    raise SystemExit(2)
