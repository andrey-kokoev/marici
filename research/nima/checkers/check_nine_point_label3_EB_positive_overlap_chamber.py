"""Compute exact E_B inverse source and positivity along a one-parameter positive E target family."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_square_full_chi3_target_trace as trace
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=trace.D,trace.vars
w2,w4,w5,w6,w7,w8,t,u=vars
e=s.symbols('e',positive=True)
p=dict(zip(vars,(e,1,1,1,1,1,3,2)))
Y=D.subs(p)*trace.Z
H=Y[:,:2];B=H.inv()*Y[:,2:]
z=trace.Z[:,2:]-trace.Z[:,:2]*B
h=trace.Z[:,:2]
J_E=s.factor(s.Matrix.hstack(*[s.Matrix(list(D.diff(v).subs(p)*z)) for v in vars]).det(method='domain-ge'))
threshold_low=s.Rational(44,445)
threshold_high=s.Rational(11531,250)
assert J_E.subs(e,threshold_low)!=0 and J_E.subs(e,threshold_high)!=0
checks=[]
for name in ('E_B','E_C','E_D'):
 cell=trace.bir.square.source[name]
 inverse=trace.inverse_one_sheet(Y,cell,trace.bir.zero_sets[name])
 formulas={str(v):str(s.factor(inverse[v])) for v in vars}
 boundary=s.factor(inverse[t]-inverse[u])
 assert all(s.factor((cell.subs(inverse)*z)[i,j])==0 for i in range(2) for j in range(4))
 checks.append({'cell':name,'inverse_source_parameters':formulas,
                'inverse_t_minus_u':str(boundary),
                'positivity_controls':[]})
 for val in (s.Rational(1,20),s.Rational(1,2),s.S.One,s.S(2),s.S(5)):
  signs={str(v):str(s.sign(s.factor(inverse[v].subs(e,val)))) for v in vars[:6]}
  signs['u']=str(s.sign(s.factor(inverse[u].subs(e,val))))
  signs['t-u']=str(s.sign(boundary.subs(e,val)))
  checks[-1]['positivity_controls'].append({'e':str(val),'signs':signs,
        'positive':all(z=='1' for z in signs.values())})
EB=next(z for z in checks if z['cell']=='E_B')
EC=next(z for z in checks if z['cell']=='E_C')
ED=next(z for z in checks if z['cell']=='E_D')
def parse(text):return s.sympify(text,locals={'e':e})
assert s.factor(parse(EB['inverse_source_parameters']['w2'])-
                2*(445*e-44)/895)==0
assert s.factor(parse(EB['inverse_source_parameters']['w4'])-
                (11531-250*e)/(3488*e+58879))==0
for parameter in ('w5','w6','w7','w8','u'):
 expr=s.factor(parse(EB['inverse_source_parameters'][parameter]))
 numerator,denominator=s.fraction(expr)
 assert all(x>=0 for x in s.Poly(numerator,e).coeffs())
 assert all(x>=0 for x in s.Poly(denominator,e).coeffs())
 assert numerator.subs(e,0)>0 and denominator.subs(e,0)>0
expr=s.factor(parse(EB['inverse_t_minus_u']))
numerator,denominator=s.fraction(expr)
assert all(x>=0 for x in s.Poly(numerator,e).coeffs())
assert all(x>=0 for x in s.Poly(denominator,e).coeffs())
assert numerator.subs(e,0)>0 and denominator.subs(e,0)>0
# E_C and E_D have w4<0 for every e>0 by explicit negative
# numerators and positive denominators (checked symbolically).
EC4=s.factor(parse(EC['inverse_source_parameters']['w4']))
ED4=s.factor(parse(ED['inverse_source_parameters']['w4']))
assert EC4==-s.Rational(484,615)
assert s.factor(ED4+484*(13*e+193)/(2423*e+16978))==0
report={'schema':'marici.nima.nine-point-label3-EB-positive-overlap-chamber.v1',
 'passed':True,'E_positive_source_family':'w2=e>0, (w4,w5,w6,w7,w8,t,u)=(1,1,1,1,1,3,2), positive moment-curve retained externals (1,3,4,5,6,7,8,9)',
 'other_three_rational_inverse_sources':checks,
 'complete_one_parameter_positive_chamber':'For e>0, E_B has a strictly positive inverse source IFF 44/445<e<11531/250. Its other six positivity factors are strictly positive for every e>0. E_C and E_D have w4<0 for EVERY e>0 and hence never enter the positive fibre along this E target family. At the two endpoints E_B respectively reaches the w2=0 and w4=0 source facets.',
 'E_target_Jacobian_along_family':str(J_E),
 'E_regular_at_both_EB_overlap_chamber_endpoints':True,
 'scope':'Exact rational one-parameter inverse sources and ALL-e>0 positivity classification on this fixed positive E target ray only. This does not establish global image coverage, contour weights or full n9 image form.'}
(OUT/'nine-point-label3-EB-positive-overlap-chamber.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'samples':[{z['cell']:[{'e':p['e'],'positive':p['positive']} for p in z['positivity_controls']]} for z in checks]},indent=2))
