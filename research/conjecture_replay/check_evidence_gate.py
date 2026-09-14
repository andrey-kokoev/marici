#!/usr/bin/env python3
"""Fail on new or modified epistemically untyped replay results."""
import hashlib,json,sys
from pathlib import Path
from evidence_policy import validate_result
ROOT=Path(__file__).resolve().parent
BASE=json.loads((ROOT/'legacy_evidence_baseline.json').read_text(encoding='utf-8'))['files']
failures=[];compliant=0;grandfathered=0
seen=set()
for p in sorted((ROOT/'results').glob('*.json')):
 rel=str(p.relative_to(ROOT.parent.parent)).replace('\\','/');seen.add(rel)
 try:
  obj=json.loads(p.read_text(encoding='utf-8'));errors=validate_result(obj)
 except Exception as exc: errors=[f'parse error: {exc}']
 if not errors:
  compliant+=1;continue
 digest=hashlib.sha256(p.read_bytes()).hexdigest();old=BASE.get(rel,{}).get('sha256')
 if old==digest: grandfathered+=1
 else: failures.append({'path':rel,'errors':errors,'reason':'new untyped artifact' if old is None else 'modified untyped artifact'})
# Baseline entries may be removed or migrated without failure; stale entries are reported.
stale=sorted(set(BASE)-seen)
out={'schema':'marici.conjecture-replay.evidence-gate.v1','execution_status':'passed' if not failures else 'failed','claim_status':'supported','evidence':[{'class':'SYMBOLIC','claim':'Every result was schema-checked; legacy exceptions were accepted only after SHA-256 equality with the frozen baseline.','checker':'research/conjecture_replay/check_evidence_gate.py'}],'counts':{'compliant':compliant,'grandfathered_unchanged':grandfathered,'failures':len(failures),'stale_baseline':len(stale)},'failures':failures,'stale_baseline':stale}
(ROOT/'results'/'evidence_gate_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'execution_status':out['execution_status'],**out['counts']}))
sys.exit(1 if failures else 0)
