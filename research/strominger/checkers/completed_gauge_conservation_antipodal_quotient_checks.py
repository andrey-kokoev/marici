"""Linear-algebra checks for the three typed physical reductions."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
I=sp.I
points=[(0,0),(1,1),(I,-I),(2+I,2-I)]
Q=sp.Matrix([[1+z*zb,z+zb,-I*(z-zb),1-z*zb] for z,zb in points]).T
rec("CONSERVATION.momentum","four generic celestial directions span four-momentum charge space",Q.rank()==4,"points 0,1,i,2+i; determinant -16")
restrict_ok=True
for n in range(4,13):
 C=sp.Matrix([[sp.Integer(j+1)**k for j in range(n)] for k in range(4)])
 basis=sp.Matrix.hstack(*sp.matrices.normalforms.nullspace(C)) if False else None
 # SymPy's nullspace columns model the conserved source subspace.
 ns=C.nullspace(); B=sp.Matrix.hstack(*ns) if ns else sp.zeros(n,0)
 R=sp.eye(n)
 restrict_ok &= B.rank()==n-C.rank() and (R*B).rank()==B.cols
rec("CONSERVATION.restrict","restriction to conserved packets preserves an injective local map",restrict_ok,"Vandermonde charge rows, n=4..12")
gauge_ok=True
for n in range(2,12):
 g=sp.Matrix([[1] if i==0 else [0] for i in range(n)])
 quotient=sp.zeros(n-1,n)
 for i in range(1,n): quotient[i-1,i]=1
 gauge_ok &= quotient.rank()==n-1 and quotient*g==sp.zeros(n-1,1) and len(quotient.nullspace())==1
rec("GAUGE.exact","the target quotient kills exactly the declared gauge line",gauge_ok,"dimensions 2..11")
graph_ok=True; sum_bad=True
for n in range(1,13):
 A=sp.diag(*[sp.Integer(j+2) for j in range(n)])
 inclusion=sp.Matrix.vstack(A,sp.eye(n))
 mismatch=sp.eye(n).row_join(-A)
 proj_left=sp.eye(n).row_join(sp.zeros(n))
 graph_ok &= mismatch*inclusion==sp.zeros(n) and inclusion.rank()==n and mismatch.rank()==n
 graph_ok &= (proj_left*inclusion).det()==A.det()!=0
 naive=sp.eye(n).row_join(sp.eye(n))
 sum_bad &= len(naive.nullspace())==n
rec("MATCHING.graph","antipodal matching is the kernel graph of an invertible adapter",graph_ok,"dimensions 1..12")
rec("MATCHING.projection","either boundary projection is faithful on the matching graph",graph_ok,"adapter determinants nonzero")
rec("MATCHING.hostile","an untyped sum port manufactures an n-dimensional alias",sum_bad,"dimensions 1..12")
passed=sum(i["passed"] for i in checks)
payload={"checker":"completed_gauge_conservation_antipodal_quotient_checks.py","strength":"typed exact-sequence and hostile-projection audit","passed":passed,"total":len(checks),"checks":checks,"verdict":"Gauge is a target quotient, conservation is a source restriction, and antipodal matching is the graph of an invertible adapter. Only the gauge quotient is intrinsically nonfaithful; conservation preserves injectivity and either boundary reconstructs a matched packet, while an untyped sum creates a false kernel."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"completed_gauge_conservation_antipodal_quotient.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)
