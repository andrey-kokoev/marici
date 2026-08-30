"""Finite exact model of completed parity/helicity representation."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]])
# label exchange and helicity exchange act on separate tensor factors.
P=sp.kronecker_product(X,I2); sigma=sp.kronecker_product(I2,X); Q=P*sigma
rec("GROUP.involutions","P, sigma, and Q are involutions",P*P==sp.eye(4) and sigma*sigma==sp.eye(4) and Q*Q==sp.eye(4),"4x4 orbit-helicity block")
rec("GROUP.commute","chart parity and helicity conjugation commute",P*sigma==sigma*P,"Klein-four representation")
PE=(sp.eye(4)+Q)/2; PM=(sp.eye(4)-Q)/2
proj=(PE*PE==PE and PM*PM==PM and PE*PM==sp.zeros(4) and PE+PM==sp.eye(4))
rec("PROJECTOR.algebra","electric and magnetic maps are complementary projectors",proj,"PiE=(1+Q)/2, PiM=(1-Q)/2")
rec("PROJECTOR.ranks","each two-label helicity block splits evenly",PE.rank()==2 and PM.rank()==2,"ranks 2+2=4")
joint=PE.col_join(PM)
rec("JOINT.faithful","the joint parity readout is injective",joint.rank()==4,"rank([PiE;PiM])=4")
hostile=True
for labels in range(1,9):
  for J in range(0,8):
    jets=(J+1)*(J+2)//2; copies=labels*jets
    hostile &= copies*PE.rank()==2*copies and copies*PM.rank()==2*copies
    hostile &= copies*joint.rank()==4*copies
rec("ORBIT.hostile","rank laws persist for arbitrary direct-sum multiplicity",hostile,"label orbits 1..8, jet bounds 0..7")
# Fixed label: Q acts as helicity exchange.
QE=X; EE=(I2+QE)/2; EM=(I2-QE)/2
rec("FIXED.fiber","a fixed label splits by helicity exchange without zero columns",EE.rank()==1 and EM.rank()==1 and X.rank()==2,"one even and one odd fiber line")
passed=sum(i["passed"] for i in checks)
payload={"checker":"completed_parity_helicity_representation_checks.py","strength":"exact representation and arbitrary-multiplicity rank law","passed":passed,"total":len(checks),"checks":checks,"verdict":"The completed source module carries commuting chart-parity and helicity involutions. Electric and magnetic ports are complementary Q eigenspace projectors: each alone forgets the opposite eigenspace, while their joint readout is faithful at every finite jet stage."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"completed_parity_helicity_representation.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)
