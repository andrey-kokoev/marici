"""Independent wheel/primal guards and exact arithmetic certificate replay.
The owning interval kernel proof is hash-bound, not reimplemented here.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
import json,hashlib,copy
from flint import arb,ctx
ctx.prec=256
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(q):return arb(q.numerator)/q.denominator
def check(r):
 for p,h in r['bindings'].items():assert sha(Path(p))==h
 c=load(R/'prime-tail-relational-cut-dpc-contract.json');assert sha(R/'prime-tail-relational-cut-dpc-contract.json')==r['contract_sha256']
 assert c['sieve_primes']==[2,3,5,7] and c['wheel_modulus']==210
 residues=[n for n in range(1,210) if gcd(n,210)==1];assert residues==r['residues']
 gaps=[b-a for a,b in zip(residues,residues[1:]+[211])];assert gaps==r['cyclic_gaps'] and max(gaps)==10
 def count(n):return sum((n-a)//210+1 for a in residues if a<=n)
 p=r['primal'];L=p['integer_start'];Hn=p['catchup_before'];last=p['last_wheel_node_before_catchup'];rate=p['atom_rate']
 assert L==6000000 and Hn==11000000 and rate==15 and gcd(last,210)==1
 assert last<=Hn and all(gcd(n,210)!=1 for n in range(last+1,Hn+1))
 assert count(last)-count(L)==p['slots_until_catchup']
 E=load(R/'directed-C-only-Abel-branch.json')['finite_pairing_evidence'];assert E['N']==c['N']==1000000
 psi=aq(Q(E['psi_N']['lower'])).union(aq(Q(E['psi_N']['upper'])))
 capacity=2*arb(2).log()*last+arb(last).log()+arb(2).log()-psi
 assert L>c['N'] and arb(L).log()>rate and capacity>0
 assert rate*p['slots_until_catchup']>capacity
 assert (2*arb(2).log()+arb(1)/L)*10<rate
 assert Q(r['capacity_increment_upper'])<rate
 for row in r['cut_checks']:
  assert row['wheel_slots']==count(row['right'])-count(row['left'])
 # All per-atom bounds imply all declared cuts, not merely adjacent ones.
 assert p['exception_power_atoms']==0
 factors=[(Q(a),Q(b)) for a,b in r['slack_product_upper_factors']];assert all(a>=0 and b>=0 for a,b in factors)
 excess=sum(a*b for a,b in factors);assert excess==Q(r['excess_over_old_minimum_upper'])
 shape=load(R/'combined-tail-single-valley.json');assert shape['status']=='CORROBORATED'
 tail=Q(shape['sharp_tail_minimum']['upper'])+excess;assert tail==Q(r['tail_at_primal_upper'])
 C=sum(Q(z['upper']) for z in E['bulk_before_prime_tail']+[E['endpoint'],E['h']])+tail;assert C==Q(r['C_at_primal_upper'])
 old=load(R/'projection-resolution-conjecture-attack.json');theta=load(R/'theta-mass-refinement.json');H=Q(old['h']['upper']);Lc=Q(old['L']['lower']);X=[Q(theta['windows'][w]['X']['upper']) for w in ('A1','B1')];mu=[Q(theta['windows'][w]['mu']['upper']) for w in ('A1','B1')]
 gain=2*X[0]*X[1]*(C+H*(mu[0]-Lc))*(C+H*(mu[1]-Lc));assert gain==Q(r['gain_at_primal_upper'])
 threshold=Q(load(HERE.parents[1]/'nima'/'results'/'signed-functional-dpc-contract.json')['threshold']);assert threshold==Q(r['threshold']) and gain<threshold
 assert r['status']=='REFUTED_FOR_FROZEN_FAMILY'
r=load(R/'prime-tail-relational-cut-dpc.json');check(r)
for mutate in ('rate','gain'):
 bad=copy.deepcopy(r)
 if mutate=='rate':bad['primal']['atom_rate']=16
 else:bad['gain_at_primal_upper']='0'
 try:check(bad)
 except AssertionError:pass
 else:raise AssertionError('corruption accepted: '+mutate)
print('PASS: infinite wheel-supported primal guards, cut admission, exact threshold refutation, binding and corruption checks')
