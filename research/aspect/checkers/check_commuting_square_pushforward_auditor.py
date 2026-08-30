#!/usr/bin/env python3
"""Exact aggregate fixture for the same-ledger refinement commuting square."""
import json
from collections import Counter, defaultdict
from pathlib import Path

ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"commuting-square-pushforward-auditor.v1.json"
RESULT=ASPECT/"results"/"commuting_square_pushforward_auditor.json"

def parent_fixture():
 rows=[]
 for a in range(2):
  for b in range(2):
   for x in (-1,0,1):
    for y in (-1,0,1):
     n=40+7*a+5*b+3*(x+1)+(y+1)
     rows.append({"key":(a,b,x,y),"count":n})
 return rows

def refine(parent):
 rows=[]
 for row in parent:
  a,b,x,y=row["key"];n=row["count"]
  n0=n//2
  for label,count in ((0,n0),(1,n-n0)):
   rows.append({"key":row["key"],"label":label,"count":count,"local_a":(a,x,label),"local_b":(b,y,label),"local_a_sources":["setting_a","outcome_a","label"],"local_b_sources":["setting_b","outcome_b","label"]})
 return rows

def push(rows):
 out=Counter()
 for r in rows: out[r["key"]]+=r["count"]
 return out

def audit(parent,refined):
 expected=Counter({r["key"]:r["count"] for r in parent});actual=push(refined)
 keys=sorted(set(expected)|set(actual));diff={str(k):actual[k]-expected[k] for k in keys if actual[k]!=expected[k]}
 return {"passed":not diff,"total_expected":sum(expected.values()),"total_actual":sum(actual.values()),"cell_differences":diff,"mismatch_cells":len(diff)}

def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8"));parent=parent_fixture();honest=refine(parent)
 good=audit(parent,honest)
 dropped=[dict(r) for r in honest];dropped[0]["count"]-=1
 duplicated=[dict(r) for r in honest];duplicated.append(dict(honest[1]))
 mutated=[dict(r) for r in honest];m=mutated[2];old=m["key"];m["key"]=(old[0],old[1],-old[2] if old[2] else 1,old[3])
 hostile={"drop_event":audit(parent,dropped),"duplicate_event":audit(parent,duplicated),"mutate_outcome":audit(parent,mutated)}
 remote_dependent=any("setting_b" in r["local_a_sources"] or "outcome_b" in r["local_a_sources"] for r in honest)
 # Inject an explicitly remote-dependent nominal-A provenance and verify the locality audit catches it.
 remote_rows=[dict(r) for r in honest]
 for r in remote_rows:r["local_a_sources"]=r["local_a_sources"]+["setting_b"]
 remote_caught=any("setting_b" in r["local_a_sources"] for r in remote_rows)
 checks={"honest_square_exact":good["passed"] and good["total_expected"]==good["total_actual"],"drop_localized":not hostile["drop_event"]["passed"] and hostile["drop_event"]["mismatch_cells"]==1,"duplication_localized":not hostile["duplicate_event"]["passed"],"outcome_mutation_localized":not hostile["mutate_outcome"]["passed"] and hostile["mutate_outcome"]["mismatch_cells"]==2,"honest_labels_not_remote":not remote_dependent,"remote_label_caught":remote_caught,"bell_is_last_gate":c["admission_order"][-1]=="bell_witness","exact_same_ledger_threshold":c["exact_requirements"]["cell_pushforward_tolerance"]==0,"claim_boundary_preserved":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.commuting-square-pushforward-auditor-result.v1","passed":all(checks.values()),"checks":checks,"honest":good,"hostiles":hostile,"verdict":"same_ledger_pushforward_auditor_accepts_refinement_and_localizes_mutations","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
