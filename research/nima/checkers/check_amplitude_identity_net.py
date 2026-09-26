"""n=2 interface tests; no claim of a physical two-point amplitude."""
from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
from amplitude_identity_net import IdentityNet,Scalar

values=[Fraction(0),Fraction(1),Fraction(-1),Fraction(2,3),Fraction(-19,7)]
checks=0
for x in values:
    payload=Scalar(x);net=IdentityNet(payload)
    assert net.observe()==(None,False) and net.meaning()==payload
    pair=net.enabled()[0];net.step(pair)
    assert net.observe()==(payload,False) and net.meaning()==payload
    before=deepcopy(net.__dict__);net.observe();assert net.__dict__==before
    try:net.step(pair)
    except ValueError:pass
    else:raise AssertionError('source replay')
    net.step(net.enabled()[0])
    assert net.observe()==(payload,True) and net.meaning()==payload
    assert not net.enabled()
    assert sorted(k for k,_ in net.nodes.values())==['ACK','DONE','OUT','VALUE']
    # Host-level sequential identity law, explicitly not net-level composition.
    next_net=IdentityNet(net.observe()[0])
    while next_net.enabled():next_net.step(next_net.enabled()[0])
    assert next_net.observe()==net.observe()
    checks+=1
for invalid in (0,'1',Fraction(1)):
    try:IdentityNet(invalid)
    except TypeError:pass
    else:raise AssertionError('untyped input accepted')
net=IdentityNet(Scalar(Fraction(1)))
a,b=net.enabled()[0]
try:net.link((a,'p'),(b,'p'))
except ValueError:pass
else:raise AssertionError('double wiring accepted')
report={'passed':True,'model':'n=2 typed identity interface, NOT a scattering amplitude',
 'exact_scalar_cases':checks,'output_precedes_completion':True,
 'linear_source_consumption':True,'zero_distinct_from_pending':True,
 'host_sequential_identity_checked':True,
 'scope':'Exact rational attributed payloads. No propagator, coupling, net-level recursive composition or amplitude-emission claim.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/amplitude-identity-net.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
