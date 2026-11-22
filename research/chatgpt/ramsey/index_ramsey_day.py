"""Rebuild the local artifact index for a fixed UTC mtime window, not a claim about research authorship times."""
import ast
from datetime import datetime, timedelta
from pathlib import Path

root = Path(__file__).parent
end = datetime.fromisoformat('2026-11-22T05:57:05+00:00')
start = end - timedelta(days=1)
files = sorted((p for p in root.iterdir() if p.is_file() and start.timestamp() <= p.stat().st_mtime <= end.timestamp()), key=lambda p: (p.stat().st_mtime, p.name))
lines = ['# Local Ramsey research artifact inventory', '', f'Window: {start.isoformat()} through {end.isoformat()} (filesystem modification times). {len(files)} files. Python descriptions below are the author’s module summaries, not independent validation.', '']
for p in files:
    text = ''
    if p.suffix == '.py':
        text = ' '.join((ast.get_docstring(ast.parse(p.read_text(encoding='utf-8-sig'))) or '').split())
    lines.append(f'- [{p.name}]({p.name})' + (f' — {text}' if text else ''))
(root/'2026-11-22_ramsey_artifact_inventory.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
