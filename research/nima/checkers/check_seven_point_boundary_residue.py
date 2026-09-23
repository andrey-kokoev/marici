"""Independent double residue of the standard top-cell cyclic Grassmannian form."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima'
prior=json.loads((N/'results/seven-point-chart-pushforward.json').read_text());assert len(prior['samples'])==2
w=s.symbols('w2:8');u,v,e,f=s.symbols('u v e f');weights=(s.Integer(1),)+w
t=(0,1,1+e,2,u,u+f,v);C=s.Matrix([weights,[weights[i]*t[i] for i in range(7)]])
# GL(2) fix columns 1 and 4 to identity; this chart is valid at all tested points.
M=C[:,[0,3]];assert s.factor(M.det())==2*w[2]
D=M.inv()*C;assert D[:,[0,3]]==s.eye(2)
freecols=(1,2,4,5,6);coords=[D[i,j] for j in freecols for i in range(2)]
params=(*w,u,v,e,f);jac=s.Matrix(coords).jacobian(params)
# Take residues at the two vanished ordered cyclic minors, using e,f as
# transverse coordinates. Change of GL gauge already included by D.
product=s.prod(s.det(D[:,[i,(i+1)%7]]) for i in range(7))
leading=s.factor((product/(e*f)).subs({e:0,f:0}))
assert leading!=0
rows=[]
for case in prior['samples']:
 values={**{w[i]:s.Integer(case['weights'][i+1]) for i in range(6)},u:s.Integer(case['u']),v:s.Integer(case['v']),e:s.Integer(0),f:s.Integer(0)}
 J=s.factor(jac.subs(values).det());L=s.factor(leading.subs(values))
 residue=s.factor(J/L);candidate=s.factor(1/(s.prod(values[x] for x in w)*(values[u]-2)*(values[v]-values[u])))
 rows.append({'weights':case['weights'],'u':case['u'],'v':case['v'],
   'gauge_jacobian':str(J),'cyclic_denominator_leading':str(L),
   'top_form_double_residue_coefficient':str(residue),'previous_candidate_coefficient':str(candidate),
   'ratio_to_previous_candidate':str(s.factor(residue/candidate))})
# Establish the correction as a rational identity, not an inference from two samples.
exact_jac=s.factor(jac.subs({e:0,f:0}).det())
exact_ratio=s.factor(exact_jac/leading*s.prod(w)*(u-2)*(v-u))
assert s.factor(exact_ratio-2/v)==0
assert all(s.Rational(row['ratio_to_previous_candidate'])==s.Rational(2,row['v']) for row in rows)
print(json.dumps({'universal_ratio':str(exact_ratio),'rows':rows},indent=2))
report={'schema':'marici.nima.seven-point-boundary-residue.v1',
 'top_form':'d^10 D_free / product Delta_(i,i+1)(D), with D[:,(1,4)]=I, free columns 2,3,5,6,7 in column-major order',
 'residue':'Coefficient of de/e wedge df/f, where t3=1+e and t6=u+f; sign depends on chosen coordinate order',
 'universal_ratio_to_previous_candidate':str(exact_ratio),
 'corrected_local_source_form':'(2/v)*prod dw_i/w_i wedge du/(u-2) wedge dv/(v-u), for the stated gauge and orientation',
 'rows':rows,'scope':'Symbolic source Grassmannian top-cell double residue; does not compare same-Z physical generalized-R history.'}
(N/'results/seven-point-boundary-residue.json').write_text(json.dumps(report,indent=2)+'\n')
