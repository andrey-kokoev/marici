from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
from check_six_point_chy_localization_algebra import G,u,x3,x4,x5
from check_six_point_bcj_quotient_rank import DDM
from check_six_point_worldsheet_universal_quotient import relation_matrix

ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/"research/nima/results/six-point-parke-taylor-kernel-theorem.json"
def eval_poly(expr,C):
 p=sp.Poly(expr,x5,domain=sp.QQ);return sum((c*C**k for (k,),c in p.terms()),sp.zeros(6))
def main():
 tri={}
 for v in (x3,x4):
  q=[p.as_expr() for p in G.polys if sp.degree(p.as_expr(),v)==1 and p.as_expr().free_symbols<={v,x5}][0];tri[v]=sp.solve(q,v)[0]
 mod=sp.Poly([p.as_expr() for p in G.polys if p.as_expr().free_symbols<={x5}][-1],x5,domain=sp.QQ).monic();cs=mod.all_coeffs()[1:];C=sp.zeros(6)
 for i in range(5):C[i+1,i]=1
 for i,c in enumerate(reversed(cs)):C[i,5]=-c
 I=sp.eye(6);Z={1:sp.zeros(6),2:I,3:eval_poly(tri[x3],C),4:eval_poly(tri[x4],C),5:C,6:-I}
 columns=[]
 for order in DDM:
  M=I
  for r in range(6):M=M*(Z[order[r]]-Z[order[(r+1)%6]]).inv()
  columns.append(M[:,0])
 W=sp.Matrix.hstack(*columns);B=relation_matrix();stacked=B.col_join(W)
 checks={"parke_taylor_class_map_rank_6":W.rank()==6,"all_120_bcj_rows_in_parke_taylor_kernel":W*B.T==sp.zeros(6,120),"parke_taylor_kernel_dimension_18":24-W.rank()==18,"bcj_and_parke_taylor_rowspaces_are_complementary":stacked.rank()==24}
 out={"schema":"marici.nima.six_point_parke_taylor_kernel_theorem.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"parke_taylor_map_shape":[W.rows,W.cols],"parke_taylor_rank":W.rank(),"kernel_dimension":24-W.rank(),"bcj_rank":B.rank(),"claim_boundary":"At the exact generic six-point fixture, DDM Parke-Taylor classes are represented in the saturated scattering-equation coordinate algebra. Their kernel equals the full BCJ rowspace. This identifies the universal six-dimensional ordering quotient with the worldsheet solution algebra at this fixture; stable-boundary naturality remains separate."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
