"""Unit-current and separate propagator emitter tests, with exact conventions."""
from fractions import Fraction
from copy import deepcopy
from pathlib import Path
import json
from biadjoint_seed_net import PrimitiveNet,UnitCurrent,Channel,Scalar
cases=[(UnitCurrent('1'),Fraction(1)),(UnitCurrent('external_leg_7'),Fraction(1))]
cases += [(Channel('X_13',x),1/x) for x in (Fraction(2),Fraction(3,7),Fraction(-5))]
for request,value in cases:
    net=PrimitiveNet(request);expected=Scalar(value)
    assert net.observe()==(None,False) and net.meaning()==expected
    pair=net.enabled()[0];net.step(pair)
    assert net.observe()==(expected,False) and net.meaning()==expected
    snapshot=deepcopy(net.__dict__);net.observe();assert net.__dict__==snapshot
    try:net.step(pair)
    except ValueError:pass
    else:raise AssertionError('primitive replay')
    net.step(net.enabled()[0])
    assert net.observe()==(expected,True) and not net.enabled()
    assert sum(k=='VALUE' for k,_ in net.nodes.values())==1
    if isinstance(request,Channel):assert expected.value*request.value==1
for make in (lambda:Channel('X',Fraction(0)),lambda:UnitCurrent(''),
             lambda:Channel('X',2),lambda:PrimitiveNet(Scalar(Fraction(1)))):
    try:make()
    except (ValueError,TypeError):pass
    else:raise AssertionError('invalid request accepted')
report={'passed':True,'unit_seed':'J(i)=1, amputated rooted single-leg current',
 'propagator':'1/X, coupling/color/phase stripped, nonzero exact rational X',
 'cases':len(cases),'separate_publication_and_completion':True,
 'zero_channel_refused':True,
 'scope':'Two primitive emitters; no three-point vertex, recursive net composition, symbolic channel algebra, physical two-point S-matrix or i-epsilon propagator claim.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/biadjoint-seed-net.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
