#!/usr/bin/env python3
"""DPC prototype for provenance-carrying sparse modular elimination."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_rees_labelled_generator_capability_constructor.json').read_text());assert prior['passed']
p=101
def clean(a):return {k:v%p for k,v in a.items() if v%p}
def add_scaled(a,b,c):
 z=dict(a)
 for k,v in b.items():z[k]=(z.get(k,0)+c*v)%p
 return clean(z)
def scale(a,c):return clean({k:c*v for k,v in a.items()})
def linear(combo,rows):
 z={}
 for i,c in combo.items():z=add_scaled(z,rows[i],c)
 return z
base=[{0:2,1:1},{1:3,2:1},{0:1,2:4,3:1}]
rows=base+[linear({0:2,1:3},base),{2:2,3:5}]
rows.append(linear({2:1,4:1},rows))
pivots={};nulls=[]
for rid,original in enumerate(rows):
 row=clean(original);combo={rid:1}
 while row:
  pivot=max(row)
  if pivot not in pivots:break
  prow,pcombo=pivots[pivot];c=row[pivot]
  row=add_scaled(row,prow,-c);combo=add_scaled(combo,pcombo,-c)
 if not row:
  nulls.append(combo);continue
 pivot=max(row);inv=pow(row[pivot],p-2,p);row=scale(row,inv);combo=scale(combo,inv);pivots[pivot]=(row,combo)
assert len(pivots)==4 and len(nulls)==2
pivot_replays={str(k):linear(c,rows)==r for k,(r,c) in pivots.items()};null_replays=[linear(c,rows)=={} for c in nulls];assert all(pivot_replays.values()) and all(null_replays)
# Deliberate corruption: change one coefficient in every certificate.
def corrupt(c):
 z=dict(c);k=min(z);z[k]=(z[k]+1)%p;return clean(z)
corrupt_pivot_residuals={str(k):linear(corrupt(c),rows)!=r for k,(r,c) in pivots.items()};corrupt_null_residuals=[linear(corrupt(c),rows)!={} for c in nulls];assert all(corrupt_pivot_residuals.values()) and all(corrupt_null_residuals)
out={'schema':'marici.benincasa.cosmology-rees-modular-provenance-prototype.v1','problem':'test whether sparse input-row combinations certify modular pivots and dependencies','bold_conjecture':'carrying a provenance vector through each row operation yields replayable certificates and detects corruption','rivals':['rank-only reduction','pivot-row output without source combinations','provenance vectors with no replay test'],'risky_consequences':'every pivot combination must replay exactly; every null combination must replay to zero; one-coefficient corruption must leave a nonzero residual','strongest_falsification_attempt':{'prime':p,'input_rows':len(rows),'rank':len(pivots),'null_certificates':len(nulls),'pivot_replays':pivot_replays,'null_replays':null_replays,'corrupt_pivot_residuals_nonzero':corrupt_pivot_residuals,'corrupt_null_residuals_nonzero':corrupt_null_residuals},'exact_residual':'zero replay residuals for valid certificates and nonzero residuals for every corrupted certificate','conjecture_disposition':'retained for the bounded modular prototype','protocol_fields':['stable row id','normalized sparse pivot row','sparse input-row combination','prime','input digest','replay residual'],'max_pivot_row_nnz':max(len(r) for r,c in pivots.values()),'max_provenance_nnz':max(len(c) for r,c in pivots.values()),'integral_generator_constructed':False,'next_conjecture':'provenance density remains bounded enough for the full Rees presentation or can be controlled by checkpointed replay','next_falsifier':'measure row counts, widths, and provenance density on representative full-engine prefixes','passed':True};(R/'cosmology_rees_modular_provenance_prototype.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
