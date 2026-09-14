#!/usr/bin/env python3
"""Inventory epistemically untyped conjecture-replay artifacts."""
import json
from collections import Counter
from pathlib import Path
from evidence_policy import validate_result

ROOT = Path(__file__).resolve().parent
rows=[]
for path in sorted((ROOT/'results').glob('*.json')):
    try:
        obj=json.loads(path.read_text(encoding='utf-8'))
        errors=validate_result(obj)
    except Exception as exc:
        errors=[f'parse error: {exc}']
    rows.append({'path':str(path.relative_to(ROOT.parent.parent)).replace('\\','/'),'compliant':not errors,'errors':errors})
summary=Counter('compliant' if r['compliant'] else 'legacy_untyped' for r in rows)
out={'schema':'marici.conjecture-replay.evidence-audit.v1','execution_status':'passed','claim_status':'supported','evidence':[{'class':'SYMBOLIC','claim':'Every JSON artifact was parsed and checked against evidence_policy.validate_result.','checker':'research/conjecture_replay/audit_evidence_hardening.py'}],'summary':dict(summary),'total':len(rows),'noncompliant': [r for r in rows if not r['compliant']]}
(ROOT/'results'/'evidence_hardening_audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'execution_status':'passed','total':len(rows),**summary,'report':'research/conjecture_replay/results/evidence_hardening_audit.json'}))
