import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

getcontext().prec=50
data=json.loads(Path('research/benincasa/results/five-site-region-pair-total-soft-angular-residues.json').read_text())
assert data['active_restriction']==['y5=-3*t-y3','y4=-3*t-y2']

expr=data['restricted_expression'].replace('^','**').replace('-2/5*','Fraction(-2,5)*',1)
for lam,x,a in [(Fraction(3),Fraction(1,2),Fraction(3,2)),(Fraction(5),Fraction(7,4),Fraction(9,4)),(Fraction(7),Fraction(11,4),Fraction(2,3))]:
    env={'Fraction':Fraction,'t':-lam,'y1':lam*a,'y2':Fraction(0),'y3':lam*x}
    lhs=eval(expr,{'__builtins__':{}},env)
    den=(2*x-5)*(a-1)*(x-1)*(x-2)*(x+2)*(x-a-2)*(x-4)*(x-5)
    rhs=Fraction(2,5)*lam**-8*(x*x-7*x+11)/den
    assert lhs==rhs

sqrt5=Decimal(5).sqrt()
x_minus=(Decimal(7)-sqrt5)/2
x_plus=(Decimal(7)+sqrt5)/2
assert Decimal(0)<x_minus<Decimal(3)<x_plus
for q in (Decimal('0.5'),Decimal('1.5'),Decimal('2.2'),Decimal('2.8')):
    assert q*q-7*q+11 != 0

packet={
 'schema':'marici.five_site_region_pair_active_soft_source_coefficient.v1',
 'occurrence':'y2=0',
 'positive_scale':'lambda=-t>0',
 'shape_ratios':['x=y3/lambda','a=y1/lambda'],
 'physical_chamber':['0<x<3','a>0'],
 'exact_coefficient':'C=(2/5)*lambda^-8*(x^2-7*x+11)/[(2*x-5)*(a-1)*(x-1)*(x-2)*(x+2)*(x-a-2)*(x-4)*(x-5)]',
 'numerator_roots':['(7-sqrt(5))/2','(7+sqrt(5))/2'],
 'physical_numerator_root':'(7-sqrt(5))/2',
 'physical_numerator_root_decimal':str(x_minus),
 'other_root_outside_chamber':True,
 'generic_second_rees_coefficient':'nonzero away from the numerator-zero ray, residual source walls, and polar c=0 section',
 'coefficient_zero_classification':'source numerator cancellation; not carrier support',
 'physical_fixed_x_poles':['x=1','x=2','x=5/2'],
 'other_poles':['a=1','a=x-2 when compatible with a>0'],
 'all_poles_classification':'restrictions of existing residual OFPT facets',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-active-soft-source-coefficient.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:packet[k] for k in ('physical_chamber','physical_numerator_root','physical_numerator_root_decimal','generic_second_rees_coefficient','all_poles_classification','new_carrier_datum')},sort_keys=True))
