"""Exact hostile lifts of one relative coupling class."""
from fractions import Fraction as F
from pathlib import Path
import json

q=F(3,5)
lifts={"strict":(q,F(0)),"terminal":(q,F(4,5)),"superunit":(q,F(1))}
rows={}
for name,(visible,invisible) in lifts.items():
 norm2=visible*visible+invisible*invisible
 rows[name]={"relative_projection":str(visible),"invisible_coordinate":str(invisible),"norm_squared":str(norm2),"strict_return":norm2<1,"coercivity_margin":str(1-norm2)}
checks={"all_lifts_have_same_relative_class":len({r["relative_projection"] for r in rows.values()})==1,"strict_lift_exists":rows["strict"]["strict_return"],"terminal_lift_exists":rows["terminal"]["norm_squared"]=="1","superunit_lift_exists":F(rows["superunit"]["norm_squared"])>1}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"lifts":rows,"conclusion":"one relative class admits strict, terminal, and superunit absolute lifts"}
out=Path("research/aspect/results/relative_lift_coercivity_obstruction.json");out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if result["status"]=="pass" else 1)
