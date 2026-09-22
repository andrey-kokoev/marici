"""Strict local-capacity gap, with an infinite support-only primal control.

Runs the owning single-valley proof fresh. A two-sided cut inequality proves
separation for EVERY capped lattice measure, not just exclusion of one atom.
The capped optimum is not asserted to be computed sharply.
"""
from pathlib import Path
from fractions import Fraction as Q
import runpy,json,hashlib
from flint import arb
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
z=runpy.run_path(str(HERE/'check_combined_tail_single_valley.py'))
assert z['status']=='CORROBORATED'
x=z['x'];aq=x['aq'];ends=x['ends'];kernel=x['kernel'];ts=x['ts'];root=z['root'];rootball=aq(root[0]).union(aq(root[1]))
psi=aq(x['psi'][0]).union(aq(x['psi'][1]))
def M(u):return x['capacity'](u)-psi
def at(u):
 i=next(i for i in range(len(ts)-1) if aq(ts[i])<u<aq(ts[i+1]))
 return kernel(u,i)[0]
def enc(a):return x['enc'](ends(a))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Freeze a modest neighbourhood, not a parameter optimized against the answer.
# N < L < exp(root) < Rn; no prime enumeration is performed here.
L=7800000;Rn=8200000
l=arb(L).log();r=arb(Rn).log();assert l<aq(root[0])<aq(root[1])<r
alpha=at(l)-at(aq(root[0]));beta=at(r)-at(aq(root[1]));assert alpha>0 and beta>0
# Every admissible capped integer measure satisfies A(r)-A(l)<=Bcap.
# There are exactly Rn-L possible integers and log(n)<=log(Rn).
Bcap=arb(Rn-L)*r
D=M(aq(root[1]))-Bcap;assert D>0
# For t=A(l), slack >= alpha*t + beta*max(0,D-t)
# >= min(alpha,beta)*D. Use lower rational endpoints throughout.
weight=min(ends(alpha)[0],ends(beta)[0]);deficit=ends(D)[0];gap=weight*deficit;assert gap>0
# Support-only primal: wait until n0=ceil(exp(root)); thereafter use
# A(u)=M(log(floor(exp(u)))). Its increments are uncapped lattice atoms.
eroot=ends(rootball.exp());n0=(eroot[1].numerator//eroot[1].denominator)+1
assert arb(n0-1)<rootball.exp()<arb(n0)
b=arb(n0).log();kroot=at(rootball);kb=at(b);assert kb<0
# Before log(n0), missing optimal mass costs at most M(b)(K(b)-K(root)).
# Afterwards M(u)-M(log floor(exp u)) <= 2log2+1/n0. Since K'>0,
# total remaining cost <= (2log2+1/n0)*integral_b^inf K' = ...*(-K(b)).
initial=M(b)*abs(kb-kroot)
rounding=(2*arb(2).log()+arb(1)/n0)*(-kb)
support_excess=ends(initial+rounding)[1];assert support_excess>=0
# The support-only control is strictly better than ALL capped measures.
separated=gap>support_excess;assert separated
old=tuple(Q(z['extremum'][k]) for k in ('lower','upper'))
# Nontrivial infinite capped primal: at integer n>L, use cumulative mass
# B_n=min(M(log n),15(n-L)), and zero beforehand. Each atom is <=15<log n.
# In x coordinates both branches are increasing and 15-Lipschitz. The
# capacity branch has derivative 2log2+1/x<15. They meet before H and
# the ramp branch stays above capacity thereafter.
rate=arb(15);Hn=9000000;h=arb(Hn).log()
assert l>rate and 2*arb(2).log()+arb(1)/L<rate
assert rate*(Hn-L)>M(h)
# Compare with the sharp continuous extremizer. Before the root, total
# extra cost <=M(root)(K(log L)-K(root)); after it and before log H,
# deficit cost <=M(log H)(K(log H)-K(root)). Discretizing down to floor(x)
# loses <=15 cumulative mass, costing at most 15 integral_root^inf K'.
capped_excess=ends(M(rootball)*abs(at(l)-kroot)+M(h)*abs(at(h)-kroot)+rate*(-kroot))[1]
capped=(old[0]+gap,old[1]+capped_excess);support=(old[0],old[1]+support_excess)
assert capped[0]>support[1] and capped[0]<=capped[1]
# Secondary decision test: this particular admitted relaxed measure still
# lies below the frozen threshold, even with upper endpoints elsewhere.
E=x['E'];C_upper=sum(Q(t['upper']) for t in E['bulk_before_prime_tail']+[E['endpoint'],E['h']])+capped[1]
H=z['H'];Lc=z['L'];X=z['X'];mu=z['mu']
factors=[C_upper+H[1]*(mu[j][1]-Lc[0]) for j in (0,1)]
assert min(factors)>0
gain_upper=2*X[0][1]*X[1][1]*factors[0]*factors[1]
secondary={'C_upper_at_capped_primal':str(C_upper),'gain_upper_at_capped_primal':str(gain_upper),'threshold':str(z['threshold']),'below_threshold':gain_upper<z['threshold']}
# A finite, independently replayable rational dual witness.
dual={'alpha_lower':str(ends(alpha)[0]),'beta_lower':str(ends(beta)[0]),'capacity_deficit_lower':str(deficit),'dual_weight':str(weight),'gap_lower':str(gap)}
out={'schema':'local-tail-capacity-gap.v1','status':'STRICT_LOCAL_CAPACITY_GAP_CERTIFIED','N':1000000,'integer_cut':[L,Rn],'n0':n0,'cut_alpha':enc(alpha),'cut_beta':enc(beta),'local_capacity_upper':str(ends(Bcap)[1]),'M_at_right_root_lower':str(ends(M(aq(root[1])))[0]),'dual':dual,'support_only_excess_upper':str(support_excess),'support_only_infimum_enclosure':x['enc'](support),'capped_infimum_enclosure':x['enc'](capped),'capped_sharp_optimum_computed':False,'capped_primal':{'integer_start':L,'atom_rate':15,'catchup_by_integer':Hn,'excess_upper':str(capped_excess)},'secondary_threshold_test':secondary,'support_only_separated_from_capped':separated,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'check_combined_tail_single_valley.py',R/'combined-tail-single-valley.json',R/'directed-C-only-Abel-branch.json')},'scope':'Both families are arithmetic relaxations; no prime-realizability or actual-source midpoint verdict. A capped infinite feasible primal is enclosed, but its sharp optimality is not claimed.'}
(R/'local-tail-capacity-gap.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'root_exp':list(map(float,eroot)),'gap_lower':float(gap),'support_only_excess_upper':float(support_excess),'capped_lower':float(capped[0]),'support_only_upper':float(support[1])},indent=2))
