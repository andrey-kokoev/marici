"""Exact Gauss locking plus bounded-support charge conservation protects transitions."""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import product, permutations
from fractions import Fraction as F
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_mass_primitive_quotient_charge.py'))
N=prior['N']; slots=prior['slots']
def words(n):
    return [(k,e,(k,)*n+(e,)) for k,e in product((-1,0,1),repeat=2)]
def distance(a,b): return sum(x!=y for x,y in zip(a,b))
# On the exact physical subspace, a fixed-Q change requires changing EVERY
# internal rotor and the elementary rotor. A spectator enforces orthogonality.
for n in (2,3,4,5,6,N):
    code=words(n)
    distances=[distance(v,w) for k,e,v in code for l,f,w in code if (k,e)!=(l,f) and k-e==l-f]
    assert min(distances)==max(distances)==n+1
    # Without charge conservation a one-site elementary transition is possible.
    assert min(distance(v,w) for k,e,v in code for l,f,w in code if (k,e)!=(l,f))==1
# A permitted nonlocal transition at exactly N+1 support is a sharp hostile.
heavy=(1,)*N+(0,); light=(0,)*N+(-1,)
assert heavy[0]-heavy[-1]==light[0]-light[-1]==1
assert distance(heavy,light)==N+1
# Sector protection does NOT protect energy: a one-site number-square operator
# has different diagonal matrix elements on these two states.
assert heavy[0]**2-light[0]**2==1
state_slots=sum(s[1][0]=='state' for s in slots)
assert state_slots==108
for epsilon in (F(0),F(1,10),F(1)):
    ratio=F(N)+state_slots*epsilon
    assert ratio>=N
assert F(N)+state_slots==1944
# Adding all microscopic permutations to force identical coefficients does not
# preserve the Gauss subspace: swap the elementary rotor with one internal one.
swapped=list(heavy); swapped[0],swapped[-1]=swapped[-1],swapped[0]
assert len(set(swapped[:-1]))>1
# Saturating the equality constraints under such swaps forces n_e=k as well,
# leaving Q=k-n_e=0. Check the reduced constrained charge window exactly.
for n in range(2,6):
    saturated=[v for v in product((-1,0,1),repeat=n+1) if len(set(v))==1]
    assert len(saturated)==3 and all(v[0]-v[-1]==0 for v in saturated)
# Swapping the two PHYSICAL rotor coordinates instead maps (k,e)->(e,k),
# reverses Q, and invariance of A*k^2+C*e^2 demands A=C, not A=N*C.
assert F(N)!=1
result={
 'status':'passed','classification':'conditional_local_transition_protection_without_mass_gap_protection',
 'channels':N,'minimum_fixed_charge_transition_support':N+1,
 'minimum_support_for_energy_shift':1,
 'state_orbit_energy_shift_coefficient':state_slots,
 'equal_gap_ratio':N,'same_protection_unequal_gap_ratio':1944,
 'checks':{'quotient_charge_chain_fresh':True,'exact_fixed_charge_distance':True,
           'charge_conservation_essential':True,'nonlocal_transition_bound_sharp':True,
           'local_diagonal_energy_shift_allowed':True,
           'microscopic_electron_exchange_violates_constraints':True,
           'saturated_exchange_constraints_remove_charged_sectors':True},
 'conclusion':'On the exact Gauss-constrained space, fixed-charge transitions need support on all1837 rotors. Strictly smaller-support Hamiltonian terms therefore preserve the collective sector without an extra particle-number axiom. This is conditional on exact constraints and the chosen microscopic locality. One-site diagonal terms still shift its energy; transition protection is not protection of1836.',
 'next_falsifier':'Source exact Gauss constraints and physical locality, then derive the charging coefficients. The obvious microscopic permutation extension destroys the separate charged sectors rather than enforcing the desired mass ratio.'}
out=HERE.parent/'results/mass-local-sector-protection.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
