"""Exact one-level refinement of unresolved cells from the 512-cell Chart-1 cover."""
from fractions import Fraction as F
from pathlib import Path
import json
source=Path("research/grothendieck/checkers/theta_chart1_scaled_taylor_interval.py").read_text()
ns={};exec(source.split("q0,q1=")[0],ns);evaluate=ns["evaluate"]
base=json.loads(Path("research/grothendieck/results/theta-chart1-scaled-taylor-q-cover.json").read_text())
accepted=[x for x in base["records"] if x["accepted"]];refined=[];unresolved=[]
for cell in (x for x in base["records"] if not x["accepted"]):
 ql,qh=map(F,cell["q"]);qm=(ql+qh)/2
 for a,b in ((ql,qm),(qm,qh)):
  H,J=evaluate(a,b);ok=H.hi < -14 and J.lo > F(7,10)
  rec={"q":[str(a),str(b)],"H_hi":float(H.hi),"J_lo":float(J.lo),"accepted":ok}
  (refined if ok else unresolved).append(rec)
result={"scope":"exact 512-cell base plus bisection of every unresolved q cell",
 "base_accepted":len(accepted),"refined_accepted":len(refined),"unresolved":len(unresolved),
 "total_final_cells":len(accepted)+len(refined)+len(unresolved),"unresolved_cells":unresolved,
 "minimum_refined_J_lower":min((x["J_lo"] for x in refined),default=None)}
out=json.dumps(result,indent=2)+"\n";Path("research/grothendieck/results/theta-chart1-scaled-taylor-refine.json").write_text(out);print(out,end="")
