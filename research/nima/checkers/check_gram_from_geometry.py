"""Quarantined move-count/probe-Gram conflation and physical phase claims."""
import json

if __name__ == '__main__':
    print(json.dumps({
        'status': 'quarantined', 'verification_performed': False,
        'reason': 'The factorial entries require the already constructed fixed-label indicator probes, not counts of sigma(i)=j. Physical phases were fitted inputs.',
        'original': 'quarantine/20261007-generation-evidence/checkers/check_gram_from_geometry.py',
        'retained_correction': 'carrier-gram-restriction-tower.md',
        'comparison': 'twelve-arrow-blocks-and-generation-selection.md'
    }, indent=2))
    raise SystemExit(2)
