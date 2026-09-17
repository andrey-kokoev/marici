#!/usr/bin/env python3
"""Inventory completed directed rank-670 prime-overlap row chunks."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';covered=[];files=[]
for p in sorted(root.glob('prime_overlap_arb_670_rows_*.json')):
 d=json.loads(p.read_text());
 if d.get('passed') and d.get('dimension')==670:covered.extend(range(d['row_range'][0],d['row_range'][1]+1));files.append(p.name)
covered=sorted(set(covered));missing=[i for i in range(670) if i not in covered];out={'schema':'marici.voevodsky.prime-overlap-arb-670-inventory.v1','completed_rows':len(covered),'first_missing_row':missing[0] if missing else None,'chunk_files':files,'complete':not missing,'passed':True,'rh_proved':False};p=root/'prime_overlap_arb_670_inventory.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
