"""Construct the explicit strict-transform collar over the qg2 relative chain."""
import json
import sympy as s
r,t,k,p=s.symbols('r t k p');xi=-1+t*(1-k);a=p-r*(k/s.Integer(2)-1)
qg2=s.expand(a-p+r*(k/s.Integer(2)-1));qg1=xi+1
assert s.simplify(qg2)==0
assert s.simplify(xi.subs(t,0)+1)==0 and s.simplify(xi.subs(t,1)+k)==0
assert s.simplify(qg1.subs(t,0))==0
out={'schema':'marici.nima.qg2-tubular-prism.v1','status':'strict_transform_wall_collar_constructed',
'prism':'H(r,t)=(x=r, a=p-r(kappa/2-1), xi=-1+t(1-kappa))',
'qg2_pullback':str(qg2),'special_face':'r=0 is the endpoint-to-conductor relative chain',
'physical_face':'r=epsilon is its strict-transform wall lift','endpoint_face':'t=0 lies on qg1: xi+1=0',
'conductor_face':'t=1 specializes to xi=-kappa; higher-order ambient conductor transport still requires verification',
'scope':'exact qg2 strict-transform collar and first nearby-cycle prism, not full ringed filtered Q comparison'}
open('research/nima/results/qg2-tubular-prism.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
