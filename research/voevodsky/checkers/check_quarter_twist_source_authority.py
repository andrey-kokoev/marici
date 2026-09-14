#!/usr/bin/env python3
"""Audit quarter-twist monodromy against source-listed FRW epsilon values."""
from hashlib import sha256
from pathlib import Path
import cmath
import json

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / 'research/voevodsky/quarter_twist_is_not_authorized_by_the_source_frw_backgrounds.md'
PAGE = ROOT / 'references/extractions/pdf-search-all/cosmology-meets-cohomology-2308-03753/pdf-page-0007.txt'
MONO = ROOT / 'research/voevodsky/results/relative_combined_wall_monodromy.json'
RESULT = ROOT / 'research/voevodsky/results/quarter_twist_source_authority.json'
page = PAGE.read_text(encoding='utf-8')
text = PACKET.read_text(encoding='utf-8')
listed = [0, -1, -2, -3]
close = lambda z, w: abs(z-w) < 1e-12
checks = {
    'source_page_frw_context': 'de Sitter' in page and 'radiation' in page and 'matter-dominated' in page,
    'source_equation_213': '(2.13)' in page,
    'listed_integer_twists_trivial': all(close(cmath.exp(2j*cmath.pi*2*e), 1) for e in listed),
    'positive_quarter_gives_sign': close(cmath.exp(2j*cmath.pi*2*(1/4)), -1),
    'negative_quarter_gives_sign': close(cmath.exp(2j*cmath.pi*2*(-1/4)), -1),
    'quarter_not_listed': 1/4 not in listed and -1/4 not in listed,
    'conditional_prior': json.loads(MONO.read_text(encoding='utf-8'))['disposition']['quarter_twist_authority'] == 'missing',
    'analytic_not_physical': 'analytic twist construction, not a physical consequence' in text,
    'acceptance_test_retained': 'source-derived fractional local system or stacky character' in text,
    'ordinary_ramification_rejected': 'ordinary ramified pullback only multiplies residues' in text,
}
checks = {k: bool(v) for k, v in checks.items()}
result = {
    'schema': 'marici.voevodsky.quarter-twist-source-authority.v1',
    'packet_sha256': sha256(PACKET.read_bytes()).hexdigest(),
    'source_page_sha256': sha256(PAGE.read_bytes()).hexdigest(),
    'prior_monodromy_sha256': sha256(MONO.read_bytes()).hexdigest(),
    'source_listed_epsilon': listed,
    'required_minimal_epsilon': ['1/4', '-1/4'],
    'checks': checks,
    'passed': all(checks.values()),
    'disposition': {
        'quarter_twist_mathematics': 'valid conditionally',
        'listed_frw_authority': 'absent',
        'ordinary_ramified_pullback': 'insufficient',
        'required_source_object': 'quarter-exponent local system or stacky character',
    },
}
RESULT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'passed': result['passed'], 'checks': checks, 'disposition': result['disposition']}))
raise SystemExit(0 if result['passed'] else 1)
