"""Quarantined maximum-hierarchy claim; no such optimization was checked."""
import json

if __name__ == '__main__':
    print(json.dumps({
        'status': 'quarantined', 'verification_performed': False,
        'reason': 'The stated 4:1:1 source derivation depends on wrong subgroup counts; the claimed maximum compatible with mixing was not established.',
        'original': 'quarantine/20261007-generation-evidence/checkers/check_symmetry_breaking_hierarchy.py',
        'comparison': 'twelve-arrow-blocks-and-generation-selection.md'
    }, indent=2))
    raise SystemExit(2)
