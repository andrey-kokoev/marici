"""Trace both algebraic sheets of the four-pair rational map at two targets."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
prior=json.loads((OUT/'nine-point-paired-pushforward-samples.json').read_text());assert prior['passed']
labels=[1,2,4,5,6,7,8,9];Z=s.Matrix([[j**d for d in range(6)] for j in labels]);K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
w2,w4,w5,w6,w7,w8,t,u=s.symbols('w2 w4 w5 w6 w7 w8 t u');variables=(w2,w4,w5,w6,w7,w8,t,u)
D=s.Matrix([[1,w2,0,0,-w5,-w6,-w7,-w8],
            [0,0,1,w4,w5*t,w6*t,w7*u,w8*u]])
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def target_density(point):
 Y=D.subs(point)*Z;A=Y[:,0:2];B=A.inv()*Y[:,2:]
 cols=[]
 for v in variables:
  deriv=D.diff(v).subs(point)*Z;dB=A.inv()*(deriv[:,2:]-deriv[:,0:2]*B)
  cols.append(s.Matrix([dB[i,j] for i in range(2) for j in range(4)]))
 J=s.Matrix.hstack(*cols).det();assert J!=0
 source=-s.S.One/(s.prod(point[x] for x in variables[:6])*point[u]*(point[t]-point[u]))
 return s.factor(source/J)
rows=[]
for row in prior['rows']:
 initial=dict(zip(variables,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(initial);q=s.symbols('q');a,b,c,d=s.symbols('a b c d');T=s.Matrix([[a,b],[c,d]])
 def lifted(i,j):
  f=s.Poly(s.expand(minor(C+T*K,i,j)),a,b,c,d)
  assert f.coeff_monomial(a*d)==-f.coeff_monomial(b*c)
  return f.coeff_monomial(1)+sum(f.coeff_monomial(z)*z for z in (a,b,c,d))+f.coeff_monomial(a*d)*q
 pairs=((0,1),(2,3),(4,5),(6,7));M,rhs=s.linear_eq_to_matrix([lifted(*p) for p in pairs],(a,b,c,d));solution=M.inv()*rhs
 P=s.Poly(q-solution[0]*solution[3]+solution[1]*solution[2],q);assert P.degree()==2 and P.eval(0)==0
 roots=s.solve(P.as_expr(),q);assert len(roots)==2 and all(z.is_Rational for z in roots)
 sheets=[]
 for root in roots:
  Tq=T.subs(dict(zip((a,b,c,d),(v.subs(q,root) for v in solution))))
  F=C+Tq*K;gauge=F[:,[0,2]].inv()*F
  point=dict(zip(variables,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7],
                            -gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert s.simplify(gauge-D.subs(point))==s.zeros(2,8)
  coeff=target_density(point)
  sheets.append({'kernel_area':str(root),'positive_sheet':root==0,'continued_target_coefficient':str(coeff)})
 assert s.Rational(next(item['continued_target_coefficient'] for item in sheets if item['positive_sheet']))==s.Rational(row['pushed_local_target_coefficient'])
 trace=s.factor(sum(s.Rational(z['continued_target_coefficient']) for z in sheets))
 assert trace!=s.Rational(row['pushed_local_target_coefficient'])
 rows.append({'weights':row['weights'],'t':row['t'],'u':row['u'],'sheets':sheets,
              'two_sheet_algebraic_trace_coefficient':str(trace),'trace_differs_from_positive_local_sheet':True})
result={'schema':'marici.nima.nine-point-paired-two-sheet-trace.v1','passed':True,'rows':rows,
 'scope':'Exact algebraic trace of intrinsic source form at two rational targets, including nonpositive sheet by rational continuation. Not a sourced generalized-R form, proof of global equality, or image-cover claim.'}
(OUT/'nine-point-paired-two-sheet-trace.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
