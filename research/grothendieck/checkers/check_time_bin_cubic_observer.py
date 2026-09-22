"""Exact filter-norm audit, bounded-integral fixtures and cancellation regression."""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal,localcontext
import importlib.util,json
from flint import arb,acb,ctx

p=Path(__file__).with_name('evaluate_time_bin_cubic_observer.py')
s=importlib.util.spec_from_file_location('bin_receiver',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
o=m.TimeBinObserver();ctx.prec=2048
F=lambda pair:Fraction(int(pair[0]),int(pair[1]))
nodes=[F(v) for v in o.filters['nodes']];den=o.filters['nodal_denominator']
for f in o.filters['bulk']+[o.filters['weak']]:
    values=[Fraction(n,den) for n in f['nodal_numerators']]
    square=sum((b-a)*(p*p+p*q+q*q)/3 for a,b,p,q in zip(nodes,nodes[1:],values,values[1:]))
    assert square<F(f['normalizer'])**2
    assert values[-1]==0
assert Fraction(4,25)+Fraction(4,49)<F(o.filters['endpoint_normalizer'])**2
for j in (0,1,37,75):
    for k,node in enumerate(nodes):
        value=o.hat(j,arb(node.numerator)/node.denominator)
        assert value==int(j==k)
    assert o.hat(j,-1)==0 and o.hat(j,65)==0

# Actual bounded hat integrals of the weak calibration profile, not point samples.
times=[arb(n.numerator)/n.denominator for n in nodes]
def integrals(a,b):
    d=b-a;v=(-4*d).exp();left=(-4*a).exp()
    return left*(1-v)/4,left*(1-(1+4*d)*v)/(16*d)
hat_values=[]
for j in range(o.bins):
    i0,i1=integrals(times[j],times[j+1]);value=i0-i1
    if j: value+=integrals(times[j-1],times[j])[1]
    assert value>0
    hat_values.append(acb(value))
zeros=[acb(0)]*o.bins
feature={'fields':[zeros,zeros,hat_values,zeros],'endpoint':[acb(0),acb(0)]}
weak=o.feature(**feature)
certificate=json.loads((m.base.RESULTS/'time-bin-cubic-observer-certificate.json').read_text(encoding='utf-8'))
weak_cert=arb(certificate['rigorous_balls']['weak_response'].replace('[','').replace(']',''))
assert weak_cert.contains(weak.real) and weak.imag.is_zero()
rank=o.finite_rank_tensor([(['0','1'],feature,feature)])
assert (rank-acb(0,1)*weak*weak).contains(0)

# A rank-two joint matrix; multiplying marginals would introduce cross terms.
n=len(o.weights);matrix=[[acb(0)]*n for _ in range(n)]
matrix[0][0]=acb(1);matrix[1][1]=acb(1)
joint=o.joint_filter(matrix,'1e-550')
assert (joint['value']-(o.weights[0]**2+o.weights[1]**2)).contains(0)
assert not (joint['value']-(o.weights[0]+o.weights[1])**2).contains(0)
assert joint['error']>0
z={'value':acb(0),'error':arb(0)}
assert o.evaluate_acquired([z]*449)['meets_1e_minus540_budget']
assert not o.evaluate_acquired([{'value':acb(0),'error':arb('1e-540')}]*449)['meets_1e_minus540_budget']
try:o.feature([zeros],[])
except ValueError:pass
else:raise AssertionError('Wrong dimensions accepted')
try:o.joint_filter(matrix,'-1')
except ValueError:pass
else:raise AssertionError('Negative acquisition error accepted')

plus=next(i for i,r in enumerate(o.manifest['rows']) if r['coefficient']=='crossed' and r['sign']==1)
minus=next(i for i,r in enumerate(o.manifest['rows']) if r['coefficient']=='crossed' and r['sign']==-1)
readings=[['0','0'] for _ in range(449)]
with localcontext() as dc:
    dc.prec=900
    readings[plus]=['1e-193','0'];readings[minus]=[str(Decimal('1e-193')+Decimal('1e-540')),'0']
r=o.evaluate(readings,conjugate=False)
parse=lambda text:arb(text.replace('[','').replace(']',''))
assert parse(r['arithmetic_radius_upper_per_w_squared'])<arb('1e-200')
assert (parse(r['value_per_w_squared'])+o.coefficients['crossed']*arb('1e-540')).contains(0)
report={'schema':'marici.grothendieck.time-bin-receiver-tests.v1','passed':True,
        'bins':o.bins,'horizon':64,'feature_measurement_dimension':n,
        'full_joint_matrix_entries_per_block':n*n,'full_joint_matrix_entries_all_blocks':449*n*n,
        'checks':['exact rational L2 filter norms','continuous hats and finite support',
                  'analytic weak-field hat-integral fixture','ordered tensor bilinearity',
                  'nonfactorized joint matrix','aggregate error-budget acceptance/rejection',
                  '347-decimal-order cancellation'],
        'scope':'Receiver and analytical fixtures, not an experimental acquisition or a claim of exact calibration for the rational gains.'}
(m.base.RESULTS/'time-bin-cubic-observer-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
