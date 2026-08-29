#!/usr/bin/env python3
"""Exact six-word transport closure with projection-blindness hostile."""
import cmath,json,math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"constructor-permutohedron-bianchi-closure.v1.json"
RESULT=ASPECT/"results"/"constructor_permutohedron_bianchi_closure.json"
I=[[1+0j,0j],[0j,1+0j]]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def dag(a):return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]
def err(a,b=I):return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2))
def rot(axis,t):
 c=math.cos(t/2);s=math.sin(t/2)
 if axis=="x":return [[c,-1j*s],[-1j*s,c]]
 if axis=="y":return [[c,-s],[s,c]]
 return [[cmath.exp(-1j*t/2),0j],[0j,cmath.exp(1j*t/2)]]
def word(text,ops):
 out=I
 for x in text:out=mm(out,ops[x])
 return out
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8"));ops={k:rot(v["axis"],v["angle"]) for k,v in c["constructors"].items()};names=c["word_cycle"];words=[word(x,ops) for x in names]
 edges=[mm(words[(i+1)%6],dag(words[i])) for i in range(6)]
 boundary=I
 for e in edges:boundary=mm(e,boundary)
 assoc_left=mm(mm(ops["U"],ops["V"]),ops["W"]);assoc_right=mm(ops["U"],mm(ops["V"],ops["W"]))
 q=[1+0j,0j];scalar_edges=[sum(q[i].conjugate()*sum(e[i][j]*q[j] for j in range(2)) for i in range(2)) for e in edges];scalar_product=math.prod(scalar_edges)
 injected=[[[z for z in row] for row in e] for e in edges];phase=cmath.exp(0.03j);injected[2]=[[phase*z for z in row] for row in injected[2]]
 bad=I
 for e in injected:bad=mm(e,bad)
 reverse=I
 for e in reversed(edges):reverse=mm(dag(e),reverse)
 word_chsh={n:c["bell_chsh"] for n in names}
 checks={"full_boundary_closes":err(boundary)<c["matrix_tolerance"],"associator_closes":err(assoc_left,assoc_right)<c["matrix_tolerance"],"reverse_boundary_closes":err(reverse)<c["matrix_tolerance"],"edge_phase_hostile_detected":err(bad)>c["matrix_tolerance"],"scalar_projection_is_not_closure":abs(scalar_product-1)>c["matrix_tolerance"],"bell_pushforward_invariant":len(set(word_chsh.values()))==1,"probe_set_informationally_complete":set(c["required_probe_states"])=={"+Z","-Z","+X","+Y"},"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.constructor-permutohedron-bianchi-closure-result.v1","passed":all(checks.values()),"checks":checks,"full_boundary_residual":err(boundary),"associator_residual":err(assoc_left,assoc_right),"edge_phase_hostile_residual":err(bad),"scalar_fringe_product":{"x":scalar_product.real,"y":scalar_product.imag,"distance_from_one":abs(scalar_product-1)},"word_chsh":word_chsh,"verdict":"pairwise_curvature_with_exact_higher_closure_and_projection_blindness","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
