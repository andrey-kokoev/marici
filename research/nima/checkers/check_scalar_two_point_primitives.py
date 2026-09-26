"""Exact scalar primitive identities, convention checks and linear emission."""
from copy import deepcopy
from pathlib import Path
import json
import sympy as s
from scalar_two_point_primitives import Block,Request,TwoPointNet,evaluate,regular_product,kinetic
p=s.symbols('p0:4',real=True);q=s.symbols('q1:4',real=True)
m=s.Symbol('m',positive=True);X=s.Symbol('X',nonzero=True)
sigma=s.Symbol('Sigma')
requests=[Request('unit_current',('i',)),Request('stripped_edge',(X,)),
          *[Request(op,(p,m)) for op in ('kinetic','inverse_propagator','feynman','time_ordered','wightman')],
          Request('dressed_feynman',(p,m,sigma,'test-supplied symbolic self-energy')),
          Request('one_particle_identity',(p[1:],q,m))]
requests.append(Request('identity',(evaluate(requests[0]),)))
outputs={}
for request in requests:
    net=TwoPointNet(request);expected=evaluate(request)
    assert net.observe()==(None,False) and net.meaning()==expected
    pair=net.enabled()[0];net.step(pair)
    assert net.observe()==(expected,False) and net.meaning()==expected
    before=deepcopy(net.__dict__);net.observe();assert net.__dict__==before
    try:net.step(pair)
    except ValueError:pass
    else:raise AssertionError('request replayed')
    net.step(net.enabled()[0]);assert net.observe()==(expected,True) and not net.enabled()
    outputs[request.operation]=expected
K=kinetic(p,m);eps=s.Symbol('epsilon',positive=True)
assert s.simplify(regular_product(outputs['feynman'],outputs['inverse_propagator']).expression-1)==0
assert outputs['kinetic'].expression==K
assert s.simplify(outputs['inverse_propagator'].expression-K)!=0
assert outputs['time_ordered'].expression==outputs['feynman'].expression
assert s.simplify(outputs['dressed_feynman'].expression.subs(sigma,0)-outputs['feynman'].expression)==0
assert s.simplify(outputs['feynman'].expression-s.I/(K+s.I*eps))==0
assert outputs['stripped_edge'].expression*X==1
assert outputs['wightman'].expression==2*s.pi*s.Heaviside(p[0])*s.DiracDelta(K)
energy=s.sqrt(sum(v**2 for v in p[1:])+m**2)
assert outputs['one_particle_identity'].expression==2*energy*(2*s.pi)**3*s.prod(s.DiracDelta(a-b) for a,b in zip(p[1:],q))
assert evaluate(Request('identity',(outputs['wightman'],)))==outputs['wightman']
refused=[]
def refusal(label,fn):
    try:fn()
    except (TypeError,ValueError):refused.append(label)
    else:raise AssertionError(label)
refusal('zero stripped channel',lambda:TwoPointNet(Request('stripped_edge',(0,))))
refusal('inexact float',lambda:TwoPointNet(Request('stripped_edge',(0.5,))))
refusal('untyped identity',lambda:TwoPointNet(Request('identity',(1,))))
refusal('negative mass',lambda:TwoPointNet(Request('kinetic',(p,-1))))
refusal('unknown operation',lambda:TwoPointNet(Request('interacting_correlator',())))
refusal('missing self-energy provenance',lambda:TwoPointNet(Request('dressed_feynman',(p,m,sigma,''))))
refusal('distribution multiplication',lambda:regular_product(outputs['wightman'],outputs['wightman']))
refusal('mixed conventions',lambda:regular_product(outputs['unit_current'],Block('unit',s.S.One,'regular','test','different metric')))
report={'passed':True,'emitted_request_types':list(outputs),'negative_controls':refused,
 'free_scalar_convention':'3+1 dimensions, +---, Fourier exp(-ip.x), covariant one-particle normalization',
 'inverse_propagator_distinguished_from_kinetic_kernel':True,
 'formal_distributions_not_integrated':True,'self_energy_supplied_not_derived':True,
 'scope':'Typed exact attributed primitive library, not a complete QFT building-block set. Vertices, LSZ, sewing, color, general correlators and recursive net composition remain separate.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/scalar-two-point-primitives.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
