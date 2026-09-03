import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")));Q,D,mu=g["Q"],g["D"],g["mu"]
def add(a,b,s=1):
 r=[F(0)]*max(len(a),len(b))
 for i,z in enumerate(a):r[i]+=z
 for i,z in enumerate(b):r[i]+=s*z
 while len(r)>1 and r[-1]==0:r.pop()
 return r
def cross_real(p,q):
 pe=[(-1)**k*p[2*k] for k in range((len(p)+1)//2)];po=[(-1)**k*p[2*k+1] for k in range(len(p)//2)];qe=[(-1)**k*q[2*k] for k in range((len(q)+1)//2)];qo=[(-1)**k*q[2*k+1] for k in range(len(q)//2)];return add(mu(pe,qe),[F(0)]+mu(po,qo))
records=[];first_failure=None
for n in range(2,9):
 for s in range(3):
  P=mu(mu(Q(s+n-1),D(n-1,s)),D(n-1,s+2));R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));N=add(P,R);A=add(P,R,-1);gram=cross_real(N,A);direct=add(cross_real(P,P),cross_real(R,R),-1);identity=gram==direct;strict=all(z>0 for z in gram);rec={"n":n,"shift":s,"gram_dimension":len(gram),"cayley_numerator_identity_exact":identity,"diagonal_gram_positive_definite":strict,"zero_diagonal_entries":sum(z==0 for z in gram)};records.append(rec)
  if not(identity and strict) and first_failure is None:first_failure=rec
checks={"twenty_one_diagonal_gram_certificates":len(records)==21,"all_cayley_identities_exact":all(r["cayley_numerator_identity_exact"] for r in records),"all_diagonal_grams_positive_definite":all(r["diagonal_gram_positive_definite"] for r in records)}
result={"schema":"marici.strominger.rh_quarter_D_positive_real_diagonal_gram.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For each bounded Cayley pair N/A, Re(N(iw)conjugate(A(iw))) has a diagonal sum-of-squares Gram representation in the monomial vector (1,w,...). Every exact diagonal entry is positive, certifying strict boundary positive-realness for all 21 cases. This is a Gram certificate, not a standard state-space KYP matrix and not a uniform recurrence proof.","records":records,"first_failure":first_failure,"checks":checks}
(base/"results"/"rh_quarter_D_positive_real_diagonal_gram.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"first_failure":first_failure,"max_dimension":max(r["gram_dimension"] for r in records),"checks":checks},indent=2))
