"""Exact positive global completions of one fixed local soft cut."""
from fractions import Fraction as F
from pathlib import Path
import json

local=F(1,4)
complements={"strict":F(1,2),"terminal":F(1),"superunit":F(3,2)}
rows={}
for name,c in complements.items():
 norm=max(local,c)
 rows[name]={"local_compression":str(local),"complement_eigenvalue":str(c),"global_norm":str(norm),"global_strict":norm<1,"positive_completion":local>=0 and c>=0}
checks={"same_local_compression":len({r["local_compression"] for r in rows.values()})==1,"all_completions_positive":all(r["positive_completion"] for r in rows.values()),"strict_completion_exists":rows["strict"]["global_strict"],"terminal_and_superunit_completions_exist":rows["terminal"]["global_norm"]=="1" and F(rows["superunit"]["global_norm"])>1}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"completions":rows,"conclusion":"one strict local positive cut admits positive global completions with strict, terminal, and superunit norms"}
out=Path("research/aspect/results/local_cut_global_completions.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
