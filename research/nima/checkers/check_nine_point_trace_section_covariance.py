"""Exact section-independent two-sheet target trace on two rational targets."""
import json
from pathlib import Path
import sympy as s
import check_nine_point_paired_trace_samples as earlier
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
Z,K,D,variables=earlier.Z,earlier.K,earlier.D,earlier.variables
prior=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text());assert prior['passed']
q,a,b,c,d=s.symbols('q a b c d');T=s.Matrix([[a,b],[c,d]])
p,r,v,t=s.symbols('p r v t');S=s.Matrix([[p,r],[v,t]])
assert s.expand((T-S).det()-(T.det()-a*t-p*d+b*v+r*c+S.det()))==0
assert K*Z==s.zeros(2,6)
def m(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def fibre(Cbase):
 eq=[]
 for i,j in ((0,1),(2,3),(4,5),(6,7)):
  poly=s.Poly(m(Cbase+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  eq.append(poly.coeff_monomial(1)+sum(poly.coeff_monomial(z)*z for z in (a,b,c,d))+poly.coeff_monomial(a*d)*q)
 M,rhs=s.linear_eq_to_matrix(eq,(a,b,c,d));assert M.det()!=0
 sol=M.inv()*rhs;P=s.Poly(s.factor(q-sol[0]*sol[3]+sol[1]*sol[2]),q)
 assert P.degree()==2
 roots=s.solve(P.as_expr(),q);assert len(roots)==2 and all(z.is_Rational for z in roots)
 traces=[];matrices=[]
 for root in roots:
  source=Cbase+T.subs(dict(zip((a,b,c,d),(v.subs(q,root) for v in sol))))*K
  gauge=source[:,[0,2]].inv()*source
  point=dict(zip(variables,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7],
                            -gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert s.simplify(gauge-D.subs(point))==s.zeros(2,8)
  traces.append(earlier.target_density(point))
  matrices.append(tuple(source))
 return P,tuple(sorted(matrices)),s.factor(sum(traces))
rows=[]
for row in prior['rows']:
 values=[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]
 C=D.subs(dict(zip(variables,values)));Y=C*Z
 canonical=s.Matrix.hstack(Y*Z[:6,:].inv(),s.zeros(2,2))
 # Canonical first-six observation section has identically zero columns 7,8.
 # Its final pair condition is det(T)*det(K[:,7:8])=0, so q=det(T)
 # collapses BOTH fibre sheets to zero, and cannot be used to eliminate.
 assert canonical[:,6:8]==s.zeros(2,2) and K[:,6:8].det()!=0
 assert s.expand(m(canonical+T*K,6,7)-T.det()*K[:,6:8].det())==0
 shift=s.Matrix([[s.Rational(1,7),-s.Rational(1,9)],[s.Rational(1,11),s.Rational(2,13)]])
 shift2=s.Matrix([[s.Rational(2,5),s.Rational(1,8)],[-s.Rational(1,10),s.Rational(1,6)]])
 sections=(C,canonical+shift*K,canonical+shift2*K)
 observed=[fibre(base) for base in sections]
 assert all(base*Z==Y for base in sections)
 assert all(sources==observed[0][1] for _,sources,_ in observed)
 assert all(trace==s.Rational(row['two_sheet_algebraic_trace_coefficient']) for _,_,trace in observed)
 assert observed[0][0]!=observed[1][0] and observed[1][0]!=observed[2][0]
 rows.append({'original_weights':row['weights'],'canonical_observation_section_q_collapses':True,
  'three_shifted_sections_have_distinct_graph_quadratics':True,
  'same_two_source_matrices':True,'same_exact_two_sheet_target_trace':str(observed[0][2])})
packet={'schema':'marici.nima.nine-point-trace-section-covariance.v1','passed':True,
 'universal_kernel_shift_rule':'For Cbase_new=Cbase+S*K, T_new=T_old-S and q_new=q_old-a*t-p*d+b*v+r*c+det(S) for S=[[p,r],[v,t]], T_old=[[a,b],[c,d]].',
 'two_rational_targets_three_admissible_sections_each':rows,
 'canonical_section_obstruction':'The direct first-six-column observation section has columns 7 and 8 identically zero, forcing the final paired minor to det(K[:,7:8])*q. Hence the unshifted q=det(T) is zero on BOTH sheets and the four-by-four linear elimination matrix is singular. Generic rational kernel shifts repair this q-coordinate, without changing the target or source fibre.',
 'scope':'The traced target coefficient is unchanged under two admissible rational section shifts at two exact targets; universal shift identity holds algebraically. The canonical section is NOT directly usable by this q-elimination algorithm. This is not an explicit global rank-six rational target form or proof of coverage.'}
(OUT/'nine-point-trace-section-covariance.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'passed':True,'sample_targets':2,'sections_per_target':3,'traces_invariant':True},indent=2))
