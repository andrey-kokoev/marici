"""Exact falsifier for universal necessity of singleton occurrence selectors."""
from fractions import Fraction as F
from pathlib import Path
import json

S=[[F(0),F(1)],[F(1),F(0)]]
q=[[F(1),F(1)]]
E1=[[F(1),F(0)],[F(0),F(0)]]
r=[[F(1),F(0)]]

def mm(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]

qS=mm(q,S)
qE1=mm(q,E1)
rS=mm(r,S)
checks={
 "symmetric_readout_descends":qS==q,
 "swap_is_strict_unitary":mm(S,S)==[[F(1),0],[0,F(1)]],
 "singleton_selector_does_not_descend":qE1!=q and qE1!=[[F(0),F(0)]],
 "asymmetric_readout_detects_forgetting":rS!=r,
}
result={"status":"pass" if all(checks.values()) else "fail","arithmetic":"fractions.Fraction only","checks":checks,"qS":[str(x) for x in qS[0]],"qE1":[str(x) for x in qE1[0]],"rS":[str(x) for x in rS[0]],"conclusion":"coherence can descend after occurrence forgetting when every admitted constructor coequalizes the occurrences; singleton identity is required only relative to a jointly distinguishing family"}
out=Path("research/aspect/results/occurrence_forgetting_coherent_quotient.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
raise SystemExit(0 if result["status"]=="pass" else 1)
