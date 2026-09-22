"""Receiver tests independent of the expensive calibration build."""
import importlib.util
from pathlib import Path
from flint import arb,acb
p=Path(__file__).with_name('evaluate_finite_cubic_observer.py')
s=importlib.util.spec_from_file_location('receiver',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
o=m.Observer();n=len(o.cells)
zero=[['0','0'],['0','0']]
bulk=[[zero]*n,[zero]*n]
bulk[0][0]=[['1','2'],['3','-1']]
f=dict(bulk=bulk,endpoint=[['1','0'],['0','1']],weak_residual=['1','0'],weak_even=['0','1'])
value=o.feature(**f)
row=o.cells[0];a=arb(row[2])/o.den;b=arb(row[3])/o.den
expected=acb(4*a+3*b,a+2*b)/(2*arb.pi()*m.rational(o.manifest['bulk_normalizers'][0]))
expected+=acb(arb(2)/5,arb(2)/7)/m.rational(o.manifest['endpoint_normalizer'])
expected+=acb(1,1)*m.rational(o.manifest['weak_multiplier'])
assert (value-expected).contains(0)
# Complex bilinearity, not Hermitian pairing, in the ordered tensor slots.
tensor=o.finite_rank_tensor([(['0','1'],f,f),(['-1','0'],f,f)])
assert (tensor-acb(-1,1)*value*value).contains(0)
result=o.evaluate([['0','0']]*449,'1e-540')
assert result['value_per_w_squared']=='0'
for vals,err in [([], '0'),([['0','0']]*449,'-1')]:
    try:o.evaluate(vals,err)
    except ValueError:pass
    else:raise AssertionError('Invalid input accepted')
print('PASS: checksum, independent frequency signs, endpoint/weak coordinates, tensor bilinearity, error budget and input rejection')
