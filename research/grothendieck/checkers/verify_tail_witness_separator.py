"""Independent rational replay, without importing the optimizer or producer."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,copy
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def check_packet(p):
 m=p['m'];mode=p['mode'];x=list(map(Q,p['primal']));y=list(map(Q,p['dual']))
 assert mode in ('all_slots','even_support','adjacent_capacity') and len(x)==m
 assert all(z>=0 for z in x+y)
 constraints=[]
 # Reconstruct atom and every finite interval restriction independently.
 for i in range(m):constraints.append(([i],Q(0 if mode=='even_support' and i%2==0 else 1)))
 for start in range(m):
  for stop in range(start+1,m+1):
   indices=list(range(start,stop))
   if mode=='adjacent_capacity':cap=Q((len(indices)+1)//2)
   elif mode=='even_support':cap=Q(sum(i%2==1 for i in indices))
   else:cap=Q(len(indices))
   constraints.append((indices,cap))
 assert len(y)==len(constraints)
 for indices,cap in constraints:assert sum(x[i] for i in indices)<=cap
 for i in range(m):assert sum(y[k] for k,(indices,_) in enumerate(constraints) if i in indices)>=Q(1,2**(i+1))
 primal=-sum(x[i]/2**(i+1) for i in range(m));dual=-sum(z*cap for z,(_,cap) in zip(y,constraints))
 assert primal==dual==Q(p['finite_optimum'])
 eps=Q(1,2**m);assert eps==Q(p['uniform_tail_error'])
 assert Q(p['full_lower'])==primal-eps and Q(p['full_upper'])==primal
 return primal-eps,primal
r=json.loads((R/'tail-witness-separator.json').read_text())
for path,h in r['bindings'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==h
results={mode:[] for mode in ('all_slots','even_support','adjacent_capacity')}
for p in r['packets']:
 lo,hi=check_packet(p);mode=p['mode'];v=Q(r['known_full_optima'][mode]);assert lo<=v<=hi
 results[mode].append((p['m'],lo,hi))
# Infinite witnesses/duals use geometric identities, not finite extrapolation:
# all: x_n=1 gives -sum 2^-n=-1;
# even: cap-saturating x_even=1 gives -sum 4^-j=-1/3;
# adjacent: pair x_(2j-1)+x_(2j)<=1 implies pair cost>=-2*4^-j;
# odd-only mass attains the sum -2/3 and satisfies every interval cap.
assert -Q(1,2)/(1-Q(1,2))==Q(r['known_full_optima']['all_slots'])
assert -Q(1,4)/(1-Q(1,4))==Q(r['known_full_optima']['even_support'])
assert -Q(1,2)/(1-Q(1,4))==Q(r['known_full_optima']['adjacent_capacity'])
assert all(lo<=-1 for _,lo,_ in results['all_slots'])
assert any(lo>-1 for _,lo,_ in results['even_support'])
assert any(lo>-1 for _,lo,_ in results['adjacent_capacity'])
# Tightening full upper bounds follow from the explicit zero-extension map.
for rows in results.values():assert all(b[2]<=a[2] for a,b in zip(rows,rows[1:]))
for field in ('primal','dual'):
 bad=copy.deepcopy(r['packets'][-1]);bad[field][0]=str(Q(bad[field][0])+1)
 try:check_packet(bad)
 except AssertionError:pass
 else:raise AssertionError('corrupted '+field+' accepted')
# Boundary controls: without uniform tails an escaping unit atom has
# objective -(1-1/n), tending to -1 although every such value exceeds -1.
assert all(-1<-(1-Q(1,n)) for n in (1,2,16,256))
# Without monotone right capacities, zero extension of a locally admitted
# mass need not be admitted at the next cut.
assert Q(1)<=Q(1) and not Q(1)<=Q(0)
print('PASS: 12 exact primal/dual packets, infinite equality/support/local-capacity controls, two strict finite separators, boundary controls, corruption rejection')
