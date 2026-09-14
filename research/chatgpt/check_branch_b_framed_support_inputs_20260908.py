#!/usr/bin/env python3
"""Audit or package exactly the 23 inputs of Branch B's second follow-up.

This is an input-availability checker, NOT a proof of a framed line/support
adapter. It never executes prerequisite checkers, infers missing matrices, or
promotes input availability to a mathematical success.

Examples:
  python check_branch_b_framed_support_inputs_20260908.py audit \
      --root /mnt/data --attachments --output input_certificate.json
  python check_branch_b_framed_support_inputs_20260908.py pack \
      --root /path/to/marici --output branch_b_framed_inputs.zip
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any

BINDING = [
    'research/chatgpt/marici_native_variance_mate_20260908.md',
    'research/chatgpt/check_marici_native_variance_mate_20260908.py',
    'research/chatgpt/marici_native_variance_mate_certificate_20260908.json',
    'research/chatgpt/marici_native_variance_mate_local_inputs_20260908.json',
]
REQUIRED = [
    'research/chatgpt/marici_physical_endpoint_pullback.md',
    'research/chatgpt/check_marici_physical_endpoint_pullback.py',
    'research/chatgpt/marici_physical_endpoint_pullback_certificate.json',
    'research/chatgpt/marici_comparison_fibre_adjunction_bar.md',
    'research/chatgpt/check_marici_comparison_fibre_adjunction_bar.py',
    'research/chatgpt/marici_comparison_fibre_adjunction_bar_certificate.json',
    'research/chatgpt/marici_physical_change_of_rings.md',
    'research/chatgpt/check_marici_physical_change_of_rings.py',
    'research/chatgpt/marici_physical_change_of_rings_certificate.json',
    'research/chatgpt/marici_primitive_conormal_column_20260908.md',
    'research/chatgpt/check_marici_primitive_conormal_column_20260908.py',
    'research/voevodsky/check_physical_conormal_first_jet_adapter.py',
    'research/voevodsky/physical-conormal-first-jet-adapter.json',
    'research/voevodsky/check_endpoint_to_conormal_cohomology_mate.py',
    'research/voevodsky/endpoint-to-conormal-cohomology-mate.json',
    'research/voevodsky/check_native_endpoint_operation_action.py',
    'research/voevodsky/native-endpoint-operation-action.json',
    'research/voevodsky/check_conormal_variance_antipode_mate.py',
    'research/voevodsky/conormal-variance-antipode-mate.json',
]
ALL = BINDING + REQUIRED


def validate_bytes(name: str, data: bytes) -> dict[str, Any]:
    text = data.decode('utf-8')
    kind = PurePosixPath(name).suffix
    if kind == '.json':
        json.loads(text)
        validation = 'JSON parsed, not mathematically verified'
    elif kind == '.py':
        ast.parse(text, filename=name)
        validation = 'Python source parsed, not executed'
    else:
        validation = 'UTF-8 text read'
    return {'sha256': hashlib.sha256(data).hexdigest(),
            'size_bytes': len(data), 'validation': validation}


def audit(root: Path, attachments: bool) -> dict[str, Any]:
    """Read exact paths; attachment mode also accepts matching mounted names.

    Only archives directly in root are inspected. No network or recursive
    filesystem search is performed. All matching copies are hash-compared.
    """
    archive_index = []
    if attachments:
        for archive in sorted(root.glob('*.zip')):
            with zipfile.ZipFile(archive) as z:
                archive_index.append((archive, tuple(z.namelist())))
    records = []
    for rel in ALL:
        paths = [root / rel]
        if attachments:
            paths += [root / PurePosixPath(rel).name,
                      root / 'files' / PurePosixPath(rel).name]
        copies = []
        for path in dict.fromkeys(paths):
            if path.is_file():
                copies.append({'location': path.relative_to(root).as_posix(),
                               **validate_bytes(rel, path.read_bytes())})
        for archive, members in archive_index:
            for member in members:
                if (member == rel or member.endswith('/' + rel)
                        or PurePosixPath(member).name == PurePosixPath(rel).name):
                    with zipfile.ZipFile(archive) as z:
                        data = z.read(member)
                    copies.append({'location': archive.name + '::' + member,
                                   **validate_bytes(rel, data)})
        hashes = {c['sha256'] for c in copies}
        status = ('not_mounted_in_audited_input_root' if not copies else
                  'conflicting_copies' if len(hashes) > 1 else 'read')
        records.append({'requested_path': rel,
                        'group': 'binding' if rel in BINDING else 'required',
                        'status': status, 'copies': copies})
    present = sum(r['status'] == 'read' for r in records)
    return {
        'schema': 'marici.branch_b.framed_support_input_audit.v1',
        'task': 'branch-b-second-followup-task.md',
        'result': ('inputs_available_adapter_not_tested' if present == len(ALL)
                   else 'decision_3_input_consumption_incomplete'),
        'requested_total': len(ALL), 'read_total': present,
        'binding_read': sum(r['status'] == 'read' and r['group'] == 'binding'
                            for r in records),
        'required_read': sum(r['status'] == 'read' and r['group'] == 'required'
                             for r in records),
        'all_required_inputs_consumed': present == len(ALL),
        'binding_result_recomputed': False,
        'network_used': False,
        'new_mathematical_assertions': 0,
        'chi_certified': False,
        'framed_obstruction_certified': False,
        'eight_frame_results': None,
        'first_unrecoverable_interface': {
            'line': 'Complete ordered L_sigma,T: occurrence determinant, '
                    'Cartier dual, endpoint-normal block, external conormal, '
                    'Pi_dual, both distinct excess labels, shifts and weights.',
            'support': 'Derived support/adjunction map retaining '
                       '(t_T,t_i1,t_i2,t_i3) and its full Koszul data.',
            'symmetry': 'Source and Dk_sigma line-transport matrices, '
                        'including endpoint-exchanging reflection.'},
        'files': records,
        'scope': 'Availability and syntax only. Missing inputs are not zero '
                 'maps and do not constitute mathematical obstructions.'
    }


def json_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, sort_keys=True, indent=2) + '\n').encode('utf-8')


def pack(root: Path, output: Path) -> None:
    """Package exact working-tree bytes; fail without creating a partial zip."""
    report = audit(root, attachments=False)
    if not report['all_required_inputs_consumed']:
        missing = [r['requested_path'] for r in report['files'] if r['status'] != 'read']
        raise FileNotFoundError('Cannot create a complete input bundle. Missing:\n'
                                + '\n'.join(missing))
    payload = {rel: (root / rel).read_bytes() for rel in ALL}
    payload['branch_b_input_manifest.json'] = json_bytes(report)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_STORED) as z:
        for name in sorted(payload):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, payload[name])
    with zipfile.ZipFile(output) as z:
        for name, data in payload.items():
            if z.read(name) != data:
                raise RuntimeError('Archive readback mismatch: ' + name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('audit', 'pack'))
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--attachments', action='store_true')
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error('--root must name an existing directory')
    if args.mode == 'pack' and args.attachments:
        parser.error('pack uses exact repository paths, not attachment aliases')
    try:
        if args.mode == 'pack':
            pack(args.root.resolve(), args.output)
            print(str(args.output))
        else:
            report = audit(args.root.resolve(), args.attachments)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(json_bytes(report))
            print(json.dumps({k: report[k] for k in
                              ('result', 'requested_total', 'read_total',
                               'binding_read', 'required_read',
                               'new_mathematical_assertions')}, sort_keys=True))
        return 0
    except (OSError, ValueError, SyntaxError, zipfile.BadZipFile) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
