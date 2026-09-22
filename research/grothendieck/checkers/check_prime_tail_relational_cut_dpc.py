"""Frozen wheel-210 relational-cut DPC: construct an infinite primal control.
No primes beyond N are evaluated. Only a 210-residue wheel is enumerated.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
import runpy,json,hashlib
from flint import arb
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
contract_path=R/'prime-tail-relational-cut-dpc-contract.json';contract=load(contract_path);contract_hash=sha(contract_path)
assert contract['sieve_primes']==[2,3,5,7] and contract['wheel_modulus']==210 and contract['N']==1000000
z=runpy.run_path(str(HERE/'check_combined_tail_single_valley.py'));assert z['status']=='CORROBORATED'
x=z['x'];aq=x['aq'];ends=x['ends'];root=z['root'];kernel=x['kernel'];ts=x['ts']
residues=[r for r in range(1,210) if gcd(r,210)==1]
gaps=[b-a for a,b in zip(residues,residues[1:]+[residues[0]+210])];maxgap=max(gaps)
assert len(residues)==48 and maxgap==10
# Exact number of wheel-coprime positive integers <=n; no large sieve.
def count(n):return sum((n-r)//210+1 for r in residues if r<=n)
L=6000000;Hn=11000000;rate=15
prevH=Hn
while gcd(prevH,210)!=1:prevH-=1
psi=aq(x['psi'][0]).union(aq(x['psi'][1]))
def M(u):return x['capacity'](u)-psi
def K(u):
 i=next(i for i in range(len(ts)-1) if aq(ts[i])<u<aq(ts[i+1]))
 return kernel(u,i)[0]
l=arb(L).log();h=arb(Hn).log();p=arb(prevH).log();rootball=aq(root[0]).union(aq(root[1]))
assert l<aq(root[0])<aq(root[1])<p<=h
assert l>rate
rounding=(2*arb(2).log()+arb(1)/L)*maxgap
assert rounding<rate
num=count(prevH)-count(L);assert rate*num>M(p)
# Infinite measure: enumerate wheel-coprime n_j>L; set
# B(log n_j)=min(M(log n_j),rate*j), constant between nodes.
# Both branches increase <=rate per node; each atom <=rate<log n_j.
# At prevH the ramp has caught capacity, and remains caught forever because
# each future capacity increment is <rate. Hence all admissibility guards
# hold for the infinite sequence, not just the displayed cuts.
kroot=K(rootball);kl=K(l);kh=K(h);assert kroot<0 and kh<0
# The single-valley slack is nonnegative on both sides. Until H use full
# envelope upper bounds; thereafter only wheel-rounding capacity is missing.
factors_upper=[(ends(M(rootball))[1],ends(abs(kl-kroot))[1]),(ends(M(h))[1],ends(abs(kh-kroot))[1]),(ends(rounding)[1],ends(-kh)[1])]
assert all(a>=0 and b>=0 for a,b in factors_upper)
excess_upper=sum(a*b for a,b in factors_upper)
old_upper=Q(z['extremum']['upper']);tail_upper=old_upper+excess_upper
E=x['E'];C_upper=sum(Q(t['upper']) for t in E['bulk_before_prime_tail']+[E['endpoint'],E['h']])+tail_upper
H=z['H'];Lc=z['L'];X=z['X'];mu=z['mu'];factors=[C_upper+H[1]*(mu[j][1]-Lc[0]) for j in (0,1)];assert min(factors)>0
gain_upper=2*X[0][1]*X[1][1]*factors[0]*factors[1];threshold=z['threshold']
status='REFUTED_FOR_FROZEN_FAMILY' if gain_upper<threshold else 'UNRESOLVED'
cut_rows=[]
for left,right in zip(contract['declared_cut_integers'],contract['declared_cut_integers'][1:]):
 cut_rows.append({'left':left,'right':right,'wheel_slots':count(right)-count(left),'primal_atom_upper':rate,'admission':'Support and per-atom caps imply every declared interval capacity, including nonadjacent pairs. Exception atoms are zero.'})
out={'schema':'prime-tail-relational-cut-dpc-result.v1','status':status,'contract_sha256':contract_hash,'residues':residues,'cyclic_gaps':gaps,'primal':{'integer_start':L,'atom_rate':rate,'catchup_before':Hn,'last_wheel_node_before_catchup':prevH,'slots_until_catchup':num,'cumulative_formula':'min(M(log n_j),15*j) at wheel-coprime n_j>6000000; zero at all other atoms','exception_power_atoms':0},'capacity_increment_upper':str(ends(rounding)[1]),'capacity_at_catchup':x['enc'](ends(M(p))),'cut_checks':cut_rows,'slack_product_upper_factors':[[str(a),str(b)] for a,b in factors_upper],'excess_over_old_minimum_upper':str(excess_upper),'tail_at_primal_upper':str(tail_upper),'C_at_primal_upper':str(C_upper),'gain_at_primal_upper':str(gain_upper),'threshold':str(threshold),'bindings':{str(path):sha(path) for path in (Path(__file__),contract_path,HERE/'check_combined_tail_single_valley.py',R/'combined-tail-single-valley.json',R/'directed-C-only-Abel-branch.json')},'scope':'A counterexample to certification over the declared wheel relaxation, NOT actual prime realizability, source infeasibility, or a refutation of all finite relational cuts.'}
assert sha(contract_path)==contract_hash
(R/'prime-tail-relational-cut-dpc.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':status,'excess_upper':float(excess_upper),'C_upper':float(C_upper),'gain_upper':float(gain_upper),'threshold':float(threshold)},indent=2))
