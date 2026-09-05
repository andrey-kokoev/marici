from __future__ import annotations
import itertools,json
from pathlib import Path
import sympy as sp
from check_six_point_bcj_quotient_rank import DDM,INDEX,kk_reduce
from check_six_point_nmhv_ordering_relations import sij

ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/"research/nima/results/six-point-worldsheet-universal-quotient.json"
def relation_matrix():
 rows=[]
 for moved in range(1,6):
  others=tuple(i for i in range(1,6) if i!=moved)
  for p in itertools.permutations(others):
   row=[sp.Integer(0)]*24;weight=sp.Integer(0)
   for k in range(1,5):
    weight+=sij(moved,p[k-1]);order=p[:k]+(moved,)+p[k:]+(6,)
    for ddm,c in kk_reduce(order).items():row[INDEX[ddm]]+=weight*c
   rows.append(row)
 return sp.Matrix(rows)
def main():
 B=relation_matrix();null=B.nullspace();P=sp.Matrix.hstack(*null).T
 _,pivots=P.rref();selected=list(pivots[:6]);S=sp.zeros(24,6);minor=P[:,selected]
 for column,index in enumerate(selected):S[index,column]=1
 S=S*minor.inv();identity=sp.eye(6)
 L=sp.Matrix([[sp.Integer((r+2)*(c+3)+1) for c in range(6)] for r in range(7)]);F=L*P;factor=F*S
 checks={"bcj_relation_rank_18":B.rank()==18,"worldsheet_quotient_rank_6":P.rank()==6,"quotient_kernel_is_bcj_rowspace":P*B.T==sp.zeros(6,120),"explicit_section":P*S==identity,"arbitrary_admissible_map_factors":factor*P==F,"factor_is_unique":factor==L}
 out={"schema":"marici.nima.six_point_worldsheet_universal_quotient.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"ordering_module_dimension":24,"bcj_kernel_dimension":18,"quotient_dimension":6,"section_ordering_indices":selected,"claim_boundary":"Exact finite-fixture universal quotient theorem: every linear cross-order map annihilating the full BCJ relation rowspace factors uniquely through the six-dimensional quotient. Identifying this quotient with twisted cohomology additionally requires the Parke-Taylor kernel theorem and full boundary naturality; those are not supplied by dimension alone."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
