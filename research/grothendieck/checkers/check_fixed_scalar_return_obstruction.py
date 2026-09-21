"""Numerical regression for the fixed scalar return obstruction."""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=60
M=lambda x:mp.log((x+1)/(x-1))
for x in (mp.mpf(2),mp.mpf(3),mp.mpf(10)):
    assert abs(M(x)-mp.quad(lambda t:1/(x-t),[-1,1]))<mp.mpf('1e-55')
assert M(3)<M(2)
# Same fixed alpha at gamma=2,3 would require w=M(3)-M(2)<0.
required_weight=M(mp.mpf(3))-M(mp.mpf(2))
assert required_weight<0
for w in (mp.mpf('.1'),mp.mpf(1),mp.mpf(10)):
    assert 3-M(mp.mpf(3))/w > 2-M(mp.mpf(2))/w
result={'schema':'marici.grothendieck.fixed-scalar-return-obstruction.v1',
        'passed':True,'two_ordinate_required_weight':mp.nstr(required_weight,25),
        'scope':'Flat spectral-density fixture; general Schwartz decay proof and Xi application are in companion note.'}
p=Path(__file__).resolve().parents[1]/'results/fixed-scalar-return-obstruction.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
