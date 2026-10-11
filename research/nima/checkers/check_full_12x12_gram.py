"""Quarantined physical interpretation of the supplied full numerical model.

The ENTIRE original implementation is preserved and rerun by
collect_generation_diagnostics.py; it has not been replaced by a smaller model.
"""
import json

if __name__ == '__main__':
    print(json.dumps({
        'status': 'quarantined', 'verification_performed': False,
        'reason': 'The block partition and phases were supplied; subgroup counts and advertised full spectrum are incorrect. No physical generation or mixing prediction is established.',
        'original': 'quarantine/20261007-generation-evidence/checkers/check_full_12x12_gram.py',
        'comparison': 'twelve-arrow-blocks-and-generation-selection.md'
    }, indent=2))
    raise SystemExit(2)
