#!/usr/bin/env python3
"""Inventory the exact Branch C D35 inputs, without substituting absent blocks.

This is an input-gate audit, NOT a certificate of a spatial comparison.
The script hashes available bytes, checks Python/JSON syntax, and reports
missing files. It never runs the old falsifiers or executes downloaded code.

Usage:
  python check_marici_d35_input_gate.py --root /mnt/data --output report.json
  python check_marici_d35_input_gate.py --root /path/to/marici --require-all
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

REQUIRED = (
    'research/chatgpt/marici_native_pullback_obstruction.md',
    'research/chatgpt/check_marici_native_pullback_obstruction.py',
    'research/chatgpt/marici_native_pullback_obstruction_certificate.json',
    'research/chatgpt/marici_physical_endpoint_pullback.md',
    'research/chatgpt/check_marici_physical_endpoint_pullback.py',
    'research/chatgpt/marici_comparison_fibre_adjunction_bar.md',
    'research/chatgpt/check_marici_comparison_fibre_adjunction_bar.py',
    'research/chatgpt/marici_physical_change_of_rings.md',
    'research/chatgpt/check_marici_physical_change_of_rings.py',
    'research/chatgpt/marici_primitive_conormal_column_20260908.md',
    'research/chatgpt/check_marici_primitive_conormal_column_20260908.py',
    'research/voevodsky/physical-conormal-first-jet-adapter.json',
    'research/voevodsky/endpoint-to-conormal-cohomology-mate.json',
    'research/voevodsky/native-endpoint-operation-action.json',
    'research/voevodsky/conormal-variance-antipode-mate.json',
    'research/voevodsky/check_conormal_variance_antipode_mate.py',
    'research/voevodsky/agda/DGPyramidRelativeOperationOrbitMate.agda',
    'research/voevodsky/agda/DGPyramidThreeLayerHigherHom.agda',
)
DEFERRED = (
    'research/chatgpt/arxiv_2609.04805v1.html',
    'research/voevodsky/agda/DGPyramidP24TraceDeformation.agda',
    'research/voevodsky/agda/DGPyramidDoubleQCartanNullhomotopy.agda',
)


def inspect(root: Path, name: str) -> dict:
    exact = root / name
    flat = root / Path(name).name
    path = exact if exact.is_file() else flat if flat.is_file() else None
    if path is None:
        return {'requested_path': name, 'status': 'missing', 'sha256': None}
    blob = path.read_bytes()
    record = {'requested_path': name, 'status': 'available',
              'layout': 'repository' if path == exact else 'flat_upload',
              'bytes': len(blob), 'sha256': hashlib.sha256(blob).hexdigest()}
    try:
        text = blob.decode('utf-8')
        if path.suffix == '.py':
            ast.parse(text)
            record['syntax'] = 'Python AST parsed; not executed'
        elif path.suffix == '.json':
            json.loads(text)
            record['syntax'] = 'JSON parsed; claims not rerun'
        else:
            record['syntax'] = 'UTF-8 text; no proof-assistant check'
    except (UnicodeDecodeError, SyntaxError, json.JSONDecodeError) as error:
        record['status'] = 'invalid'
        record['error'] = str(error)
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('/mnt/data'))
    parser.add_argument('--output', type=Path,
                        default=Path('marici_d35_input_gate_certificate.json'))
    parser.add_argument('--require-all', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f'Not a directory: {root}')
    records = [inspect(root, name) for name in REQUIRED]
    missing = [r['requested_path'] for r in records if r['status'] == 'missing']
    invalid = [r['requested_path'] for r in records if r['status'] == 'invalid']
    status = 'blocked_missing_inputs' if missing or invalid else 'inputs_available_not_mathematically_verified'
    report = {
        'scope': 'Exact input availability and syntax only; not a spatial theorem',
        'status': status,
        'requested_input_count': len(REQUIRED),
        'available_input_count': sum(r['status'] == 'available' for r in records),
        'missing_input_count': len(missing),
        'inputs': records,
        'missing_paths': missing,
        'invalid_paths': invalid,
        'deferred_inputs_not_read': list(DEFERRED),
        'new_spatial_chain_calculations': 0,
        'old_falsifiers_retested': False,
        'decision_3_obstruction_certified': False,
        'decision_4_after_all_inputs_consumed': False if missing or invalid else None,
        'physical_comparison_exists': None,
        'physical_reflection_parity': None,
        'next_required_export': {
            'name': 'native framed primitive-column adapter',
            'source': 'G_native_(sigma,T), with the actual physical source differential',
            'target': 'ker(pi_beta: E_(beta,k) tensor Pi^vee[3] -> C tensor Pi^vee[3])',
            'required_data': [
                'ordered source basis and full native B-action',
                'D0, D35/D04, nu0, nu35/nu04 in that same basis',
                'closed primitive row kappa and its native-linearity equations',
                'source-to-target occurrence, Rees, determinant, Pi^vee and excess-line dictionary',
                'per-stalk support/localization maps and labelled-family transitions',
            ],
            'entries': None,
        },
        'full_target_export_also_required': {
            'objects': ['omega[2]', 'E_(beta,k) tensor Pi^vee[3]', 'C tensor Pi^vee[3]'],
            'blocks': ['d_omega[2]', 'd_E[3]', 'd_C[3]', 'q', 'pi_beta'],
            'native_actions_and_frame_transitions': None,
            'warning': 'Missing matrices are null, never zero matrices.',
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('status','requested_input_count','available_input_count','missing_input_count','new_spatial_chain_calculations')}, indent=2))
    return 2 if args.require_all and (missing or invalid) else 0

if __name__ == '__main__':
    raise SystemExit(main())
