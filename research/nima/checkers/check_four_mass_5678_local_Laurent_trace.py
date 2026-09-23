"""Trace sourced psi in a bounded exact Laurent algebra BEFORE the <5678> wall."""
import contextlib,functools,io,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
e=s.symbols('eps');Q=s.Rational
z=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
            [10+e,16,25,39],[2,3,5,7],[3,5,7,11],[5,8,13,21]])
@functools.lru_cache(None)
def br(i,j,k,l):return z[[i-1,j-1,k-1,l-1],:].det(method='domain-ge')
wall=s.cancel(br(5,6,7,8)/e);assert wall==-10
z0=z.subs(e,0);br0=lambda *seq:z0[[i-1 for i in seq],:].det(method='domain-ge')
e0,e1=br(8,5,6,3),br(8,5,6,4);f0,f1=br(5,6,3,7),br(5,6,4,7)
n0,n1=br(1,2,7,3),br(1,2,8,3);d0,d1=br(4,1,2,7),br(4,1,2,8)
A=e0*d1+e1*n1;B=e0*d0+e1*n0-f0*d1-f1*n1;C=-f0*d0-f1*n0
T=s.Matrix([[0,-C/A],[1,-B/A]]);I=s.eye(2)
def inv(M):
 det=s.cancel(M[0,0]*M[1,1]-M[0,1]*M[1,0]);assert det!=0
 return s.Matrix([[s.cancel(M[1,1]/det),s.cancel(-M[0,1]/det)],
                  [s.cancel(-M[1,0]/det),s.cancel(M[0,0]/det)]])
beta=(n0*I+n1*T)*inv(d0*I+d1*T)
def aux(seq,label):
 lo,hi=(7,8) if label=='A' else (3,4)
 field=T if label=='A' else beta
 return br(*(lo if x==label else x for x in seq))*I+br(*(hi if x==label else x for x in seq))*field
na=aux((2,3,4,'A'),'A');nb=aux((6,7,8,'B'),'B')
da=[aux(seq,'A') for seq in (('A',1,2,3),(2,3,4,'A'),(3,4,'A',1),(4,'A',1,2))]
db=[aux(seq,'B') for seq in (('B',5,6,7),(6,7,8,'B'),(7,8,'B',5),(8,'B',5,6))]
psi_num=aux(('A',4,1,2),'A')*aux(('B',8,5,6),'B')
psi_den=psi_num-aux(('A',4,5,6),'A')*aux(('B',8,1,2),'B')
assert s.cancel(br(5,6,7,8)/e)==wall
# A Laurent scalar is a finite exponent->exact rational map; each
# individual inverse is constructed over Q(eps) BEFORE specializing.
def series(expr,upper):
 expr=s.cancel(expr)
 if expr==0:return {}
 numerator,denominator=s.fraction(expr)
 num=s.Poly(numerator,e,domain=s.QQ);den=s.Poly(denominator,e,domain=s.QQ)
 nd=dict(num.terms());dd=dict(den.terms())
 n={ex[0]:v for ex,v in nd.items()};d={ex[0]:v for ex,v in dd.items()}
 nv,dv=min(n),min(d);shift=nv-dv
 if shift>upper:return {}
 d0=d[dv];coeff={}
 for k in range(upper-shift+1):
  rhs=n.get(nv+k,0)-sum(d.get(dv+i,0)*coeff.get(k-i,0) for i in range(1,k+1))
  coeff[k]=s.Rational(rhs,d0)
 return {shift+k:v for k,v in coeff.items() if v}
def mul(a,b,upper):
 out={}
 for i,x in a.items():
  for j,y in b.items():
   if i+j<=upper:out[i+j]=out.get(i+j,0)+x*y
 return {k:v for k,v in out.items() if v}
def smatrix(M,upper):return [[series(M[i,j],upper) for j in range(2)] for i in range(2)]
def multiply(X,Y,upper):return [[{k:v for k,v in (lambda a,b:{k:a.get(k,0)+b.get(k,0) for k in a.keys()|b.keys()})(mul(X[i][0],Y[0][j],upper),mul(X[i][1],Y[1][j],upper)).items() if v} for j in range(2)] for i in range(2)]
factors=[psi_num,inv(psi_den)]+[na]*4+[nb]*4+[inv(F) for F in da+db]+[(1/br(5,6,7,8))*I]
def compute(precision):
 # Retain extra positive powers in every factor to protect against
 # later negative valuations. Compare two independent precision bounds.
 out=smatrix(I,precision)
 for F in factors:out=multiply(out,smatrix(F,precision),precision)
 trace={i:out[0][0].get(i,0)+out[1][1].get(i,0) for i in out[0][0].keys()|out[1][1].keys()}
 return {i:v for i,v in trace.items() if v}
low=compute(14);high=compute(20)
assert {i:v for i,v in low.items() if i<=0}=={i:v for i,v in high.items() if i<=0}
# The valuation of each entire matrix is the minimum over its entries.
# To contribute to exponent -1, no individual factor can require a
# coefficient above -1 minus the sum of all OTHER factor minima.
factor_minima=[]
for F in factors:
 expansions=[series(F[i,j],20) for i in range(2) for j in range(2)]
 factor_minima.append(min(min(x) for x in expansions if x))
needed=max(-1-sum(factor_minima)+v for v in factor_minima)
assert needed<=14, ('increase_Laurent_precision',needed)
principal={i:v for i,v in high.items() if i<0 and v}
assert principal
# Independent off-wall exact quadratic-field evaluation, without
# reusing the Laurent multiplication engine.
with contextlib.redirect_stdout(io.StringIO()):import check_four_mass_complete_component_companion_trace as direct_checker
value=s.Rational(1,100000);numeric_z=z.subs(e,value)
def numeric_br(i,j,k,l):return numeric_z[[i-1,j-1,k-1,l-1],:].det(method='domain-ge')
direct,_=direct_checker.complete_component(numeric_br)
assert abs(value*direct-principal[-1])<s.Rational(1,1000)
report={'schema':'marici.nima.four-mass-5678-local-Laurent-trace.v1','passed':True,
 'wall':'<5678>=-10 eps',
 'Laurent_principal_part_in_eps':{str(k):str(v) for k,v in sorted(principal.items())},
 'leading_pole_order_in_eps':-min(principal),
 'simple_residue_in_eps':str(principal.get(-1,0)),
 'two_precision_agreement_through_constant_term':True,
 'maximum_factor_precision_needed_for_exact_residue':needed,
 'bracket_coordinate_residue':str(s.factor(wall*principal.get(-1,0))),
 'independent_offwall_exact_field_trace_limit_control':True,
 'method':'Construct each sourced psi factor as a rational 2x2 quadratic-field matrix over Q(eps), invert there BEFORE specialization, convert each factor independently to an exact bounded Laurent series and multiply/truncate. Agreement at two bounds checks the reported principal coefficients.',
 'boundary':'Exact one-parameter sourced supercomponent Laurent trace; direct Y0-fibre Laurent elimination and global Y-dependent bosonic form not executed.'}
(OUT/'four-mass-5678-local-Laurent-trace.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'leading_pole_order':-min(principal),
                  'principal_part':report['Laurent_principal_part_in_eps']},indent=2))
