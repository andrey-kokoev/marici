"""Separate exact certificate checks for the finite cut dual and primal guards.
Does not independently reimplement the kernel's interval analysis.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,copy
from flint import arb,ctx
ctx.prec=256
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(q):return arb(q.numerator)/q.denominator
def verify(r):
 for p,h in r['bindings'].items():assert sha(Path(p))==h
 d=r['dual'];alpha=Q(d['alpha_lower']);beta=Q(d['beta_lower']);D=Q(d['capacity_deficit_lower']);w=Q(d['dual_weight']);g=Q(d['gap_lower'])
 assert 0<w<=min(alpha,beta) and D>0 and g==w*D
 assert alpha==Q(r['cut_alpha']['lower']) and beta==Q(r['cut_beta']['lower'])
 # Independently reconstruct the available-mass deficit from scalar bounds.
 assert D<=Q(r['M_at_right_root_lower'])-Q(r['local_capacity_upper'])
 # For 0<=t<=D, alpha*t+beta*(D-t)>=w*D; for t>=D,
 # alpha*t>=w*D. These two algebraic cases prove the cut dual universally.
 assert alpha-w>=0 and beta-w>=0
 old=load(R/'combined-tail-single-valley.json')['sharp_tail_minimum'];lo=Q(old['lower']);hi=Q(old['upper'])
 support=Q(r['support_only_excess_upper']);excess=Q(r['capped_primal']['excess_upper'])
 assert support>=0 and excess>=0
 assert Q(r['support_only_infimum_enclosure']['upper'])==hi+support
 assert Q(r['capped_infimum_enclosure']['lower'])==lo+g>hi+support
 assert Q(r['capped_infimum_enclosure']['upper'])==hi+excess
 E=load(R/'directed-C-only-Abel-branch.json')['finite_pairing_evidence']
 L=r['capped_primal']['integer_start'];Hn=r['capped_primal']['catchup_by_integer'];rate=r['capped_primal']['atom_rate']
 psi=aq(Q(E['psi_N']['lower'])).union(aq(Q(E['psi_N']['upper'])))
 def M(n):return 2*arb(2).log()*n+arb(n).log()+arb(2).log()-psi
 assert L>r['N'] and arb(L).log()>rate and M(L)>0
 assert 2*arb(2).log()+arb(1)/L<rate and rate*(Hn-L)>M(Hn)
 sec=r['secondary_threshold_test'];C=sum(Q(z['upper']) for z in E['bulk_before_prime_tail']+[E['endpoint'],E['h']])+hi+excess
 assert C==Q(sec['C_upper_at_capped_primal'])
 oldcal=load(R/'projection-resolution-conjecture-attack.json');theta=load(R/'theta-mass-refinement.json');H=Q(oldcal['h']['upper']);Lc=Q(oldcal['L']['lower'])
 X=[Q(theta['windows'][s]['X']['upper']) for s in ('A1','B1')];mu=[Q(theta['windows'][s]['mu']['upper']) for s in ('A1','B1')]
 gain=2*X[0]*X[1]*(C+H*(mu[0]-Lc))*(C+H*(mu[1]-Lc))
 threshold=Q(load(HERE.parents[1]/'nima'/'results'/'signed-functional-dpc-contract.json')['threshold'])
 assert gain==Q(sec['gain_upper_at_capped_primal'])<threshold==Q(sec['threshold'])
r=load(R/'local-tail-capacity-gap.json');verify(r)
bad=copy.deepcopy(r);bad['dual']['gap_lower']=str(2*Q(bad['dual']['gap_lower']))
try:verify(bad)
except AssertionError:pass
else:raise AssertionError('corrupted dual gap accepted')
print('PASS: cut dual, support-only separation, infinite capped primal guards, exact threshold check and corruption rejection')
