import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
A,B,C,det,detA,k=g["A"],g["B"],g["C"],g["det"],g["detA"],g["k"]
def dm(M,R,S):return F(1) if not R else det([[M[i][j] for j in S] for i in R])
def comp(S):return [i for i in range(k) if i not in S]
def source_terms(R,S):
 out=[]
 for K in itertools.combinations(range(k),len(R)):
  z=(-1)**(sum(R)+sum(K))*dm(A,comp(K),comp(R))*dm(B,K,S)
  if z:out.append((K,z))
 return out
identity_count=0;first_identity_failure=None;terminal_count=0;first_sign_failure=None;first_mixed_summand_sign=None;coherent_terminal_sums=0
for r in range(1,k+1):
 for R in itertools.combinations(range(k),r):
  for S in itertools.combinations(range(k),r):
   z=sum(v for _,v in source_terms(R,S));target=detA*dm(C,R,S);identity_count+=1
   if z!=target and first_identity_failure is None:first_identity_failure={"rows":R,"columns":S,"residual":str(z-target)}
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));terms=source_terms(R,S);z=sum(v for _,v in terms);expected_terminal=(-1)**(j-i+1) if i<j else (-1)**(i-j)
   expected=expected_terminal*(-1)**(sum(x>i for x in T)+sum(x>j for x in T))
   terminal_count+=1
   if not z*expected>0 and first_sign_failure is None:first_sign_failure={"base":T,"i":i,"j":j,"numerator":str(z)}
   signs={1 if v>0 else -1 for _,v in terms}
   if len(signs)==1 and signs=={expected}:coherent_terminal_sums+=1
   elif first_mixed_summand_sign is None:first_mixed_summand_sign={"base":T,"i":i,"j":j,"expected":expected,"positive_terms":sum(v>0 for _,v in terms),"negative_terms":sum(v<0 for _,v in terms),"nonzero_terms":len(terms)}
checks={"all_12869_source_minor_identities_exact":identity_count==12869 and first_identity_failure is None,"all_3584_oriented_terminal_numerators_have_expected_sign":terminal_count==3584 and first_sign_failure is None,"summand_sign_coherence_classified":coherent_terminal_sums+int(first_mixed_summand_sign is not None)>0}
result={"schema":"marici.strominger.rh_quarter_hurwitz_terminal_minor_source_formula.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Jacobi plus Cauchy-Binet gives an exact source formula det(A) det(C[R,S]) = sum_K (-1)^(sum R+sum K) det A[K^c,R^c] det B[K,S]. It verifies every order-eight transfer minor and every oriented terminal sign. The first mixed-sign summand set determines whether endpoint minor sign-regularity alone proves the all-order rule or cancellation control remains necessary.","identity_count":identity_count,"oriented_terminal_count":terminal_count,"coherent_terminal_sum_count":coherent_terminal_sums,"first_identity_failure":first_identity_failure,"first_terminal_sign_failure":first_sign_failure,"first_mixed_summand_sign":first_mixed_summand_sign,"checks":checks}
(base/"results"/"rh_quarter_hurwitz_terminal_minor_source_formula.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
