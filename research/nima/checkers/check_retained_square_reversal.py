"""Audit the fresh formal receipt for the retained square reversal."""
from pathlib import Path
import hashlib
import json
import re

OWNER = Path(__file__).resolve().parents[1]
receipt = json.loads((OWNER/'results/agda-RetainedSquareReversal.json').read_text(encoding='utf-8-sig'))
assert receipt['passed'] and receipt['ignore_interfaces']
seen = {}
def visit(module):
    path = OWNER/'agda'/(module.replace('.', '/')+'.agda')
    if not path.exists() or module in seen:
        return
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == receipt['owner_source_inventory_sha256'][path.name].lower(), module
    seen[module] = digest
    for dependency in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'), re.M):
        visit(dependency)
visit('RetainedSquareReversal')
print(json.dumps({'classification':'actual_source_square_reversed_with_retained_section_and_schedules',
                  'fresh_formal_receipt':True, 'current_local_modules':len(seen),
                  'scope':'Canonical reversal of the existing square, not full rules 3 through 5.'}))
