from __future__ import annotations
import itertools,json,math
from collections import Counter,defaultdict
from pathlib import Path
import sympy as sp
import check_six_point_nmhv_ordering_relations as rel
from check_six_point_nmhv_universal_ddm_dressing import basis_orders,half_ladder_trace

ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/"research/nima/results/six-point-full-super-color-dressing.json"
TRIPLES=list(itertools.combinations(rel.LABELS,3));MONOMIALS=list(itertools.combinations_with_replacement(range(20),4))

def wedge_component(linear,target):
 total=0;target=set(target)
 for i,j in itertools.combinations(rel.LABELS,2):
  if i not in target or j not in target:continue
  for k in rel.LABELS:
   if k in (i,j) or {i,j,k}!=target:continue
   seq=[i,j,k];inv=sum(seq[a]>seq[b] for a in range(3) for b in range(a+1,3))
   total+=(-1 if inv%2 else 1)*rel.bracket(rel.LAM[i],rel.LAM[j])*linear[k]
 return sp.cancel(total)
def rank_one_fourth(vector,scale,out):
 for monomial in MONOMIALS:
  counts=Counter(monomial);mult=math.factorial(4)
  value=scale
  for index,count in counts.items():mult//=math.factorial(count);value*=vector[index]**count
  if value:out[monomial]+=mult*value
def super_polynomial(order):
 mus=rel.reconstruct_mus(order,rel.LAM,rel.TILDE);z={i:rel.LAM[i]+mus[i] for i in order};transport=rel.chi_transport(order);o=order
 terms=[(o[0],o[1],o[2],o[3],o[4]),(o[0],o[1],o[2],o[4],o[5]),(o[0],o[2],o[3],o[4],o[5])]
 pt=sp.prod(rel.bracket(rel.LAM[o[i]],rel.LAM[o[(i+1)%6]]) for i in range(6));out=defaultdict(lambda:sp.Integer(0))
 for labels in terms:
  a,b,c,d,e=labels;cyclic=[(a,(b,c,d,e)),(b,(c,d,e,a)),(c,(d,e,a,b)),(d,(e,a,b,c)),(e,(a,b,c,d))]
  linear={j:sum(rel.four(z,q)*transport[i][j] for i,q in cyclic) for j in rel.LABELS}
  vector=[wedge_component(linear,t) for t in TRIPLES]
  den=rel.four(z,(a,b,c,d))*rel.four(z,(b,c,d,e))*rel.four(z,(c,d,e,a))*rel.four(z,(d,e,a,b))*rel.four(z,(e,a,b,c))*pt
  rank_one_fourth(vector,sp.cancel(1/den),out)
 return {m:sp.cancel(v) for m,v in out.items() if sp.cancel(v)!=0}
def dress(basis,polynomials):
 out=defaultdict(lambda:defaultdict(lambda:sp.Integer(0)))
 for order in basis:
  for word,color_coefficient in half_ladder_trace(order).items():
   target=out[word]
   for monomial,value in polynomials[order].items():target[monomial]+=color_coefficient*value
 return out
def main():
 b16=basis_orders(1,6);b26=basis_orders(2,6);orders=set(b16+b26);polynomials={o:super_polynomial(o) for o in orders};left=dress(b16,polynomials);right=dress(b26,polynomials);words=set(left)|set(right);residual_count=0
 for word in words:
  for monomial in set(left[word])|set(right[word]):
   if sp.cancel(left[word].get(monomial,0)-right[word].get(monomial,0))!=0:residual_count+=1
 hostile_order=b16[0];hostile_nonzero=any(value!=0 for value in polynomials[hostile_order].values()) and any(c!=0 for c in half_ladder_trace(hostile_order).values())
 checks={"full_grassmann_tensor_ddm_basis_independent":residual_count==0,"all_48_ordered_superamplitudes_nonzero":all(bool(p) for p in polynomials.values()),"hostile_half_ladder_sign_flip_has_nonzero_support":hostile_nonzero,"symmetric_tensor_coordinate_count":len(MONOMIALS)==8855}
 out={"schema":"marici.nima.six_point_full_super_color_dressing.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"ordered_superamplitude_count":len(polynomials),"cyclic_color_word_count":len(words),"grassmann_tensor_coordinate_count":len(MONOMIALS),"nonzero_basis_residual_count":residual_count,"claim_boundary":"Exact coefficientwise DDM endpoint-basis comparison of the complete degree-12 six-point NMHV superamplitude, represented as Sym^4 of the 20-dimensional one-R-symmetry degree-three Grassmann space, in the free cyclic trace-word color module at one rational fixture."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
