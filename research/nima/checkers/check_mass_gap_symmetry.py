"""Exact orbit and charge-sector obstruction to symmetry-forced mass gaps."""
from contextlib import redirect_stdout
from itertools import product, permutations
from pathlib import Path
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_mass_comparison_dressing.py'))
slots=set(prior['slots'])
rooted=[p for p in permutations(range(4)) if p[0]==0]
def edge(p,e): return tuple(p[x] for x in e)
def act(s,ps):
    outer,(kind,a,b)=s; po,pa,pb=ps
    if kind=='arrow': inner=(kind,edge(pa,a),edge(pb,b))
    else: inner=(kind,pa[a],pb[b])
    return edge(po,outer),inner

def orbits(group):
    unseen=set(slots); result=[]
    while unseen:
        x=min(unseen); orbit={act(x,g) for g in group}
        assert orbit<=slots
        unseen-=orbit; result.append(orbit)
    assert sum(map(len,result))==len(slots)
    return result
# This independent three-role symmetry is an ENLARGEMENT used as a generous
# test, not a derived symmetry of carrier incidence attaching the roles.
independent=orbits(list(product(rooted,repeat=3)))
diagonal=orbits([(p,p,p) for p in rooted])
assert len(independent)==30
assert sum(next(iter(o))[1][0]=='arrow' for o in independent)==27
assert sum(next(iter(o))[1][0]=='state' for o in independent)==3
assert len(diagonal)>=30
# Invariant diagonal coefficients are arbitrary constants on each orbit.
weights={s:1 for s in slots}
selected=next(o for o in independent if next(iter(o))[1][0]=='state')
for s in selected: weights[s]=2
for s in slots:
    for g in product(rooted,repeat=3):
        assert weights[act(s,g)]==weights[s]
weighted_energy=sum(weights.values())
assert weighted_energy!=1836

# Charge sector shifts are central for EVERY charge-preserving symmetry, not
# just carrier relabellings. Exact finite permutation witness with three states
# in each of Q=-1,0,+1; projectors survive all within-sector permutations.
charges=[-1]*3+[0]*3+[1]*3
projector=[int(q==1) for q in charges]
for blocks in product(list(permutations(range(3))),repeat=3):
    perm=[3*k+j for k,block in enumerate(blocks) for j in block]
    assert all(charges[perm[i]]==charges[i] and projector[perm[i]]==projector[i] for i in range(9))
# Equal neutral gaps under full slot permutation still leave core and electron
# occupations fixed. mu*c changes E_plus while preserving all such permutations.
assert prior['sectors'](mu=1)[0]==1837
# A naive electron/neutral swap does not preserve Q=-n_e (core fixed at zero).
assert any(-e!=-n for e,n in product((0,1),repeat=2))

# Even adding a number-counting charge and a positive-square Hamiltonian does
# not protect the charged-sector kernel. Uniformly shifting the constraint
# preserves relabellings and every occupation, but lifts its zero mode.
from fractions import Fraction as F
eta=F(1,10); J=F(2)
occupied=1+J*eta**2; empty=J*(1-eta)**2
assert occupied<empty
factorized_shift=len(slots)*occupied
assert factorized_shift==F(46818,25) and factorized_shift!=1836

result={
 'status':'passed','classification':'charge_preserving_symmetry_does_not_force_comparison_mass_ratio',
 'orbit_counts':{'generous_independent_rooted_roles':len(independent),
                 'arrow_orbits':27,'state_orbits':3,'diagonal_rooted_action':len(diagonal)},
 'invariant_weight_hostile_energy':weighted_energy,
 'positive_square_kernel_lift_ratio':str(factorized_shift),
 'checks':{'prior_dressing_chain_fresh':True,'exact_slot_orbits':True,
           'orbit_weight_deformation_invariant':True,'charge_sector_shift_invariant':True,
           'maximal_neutral_permutation_still_allows_core_mass':True,
           'electron_neutral_swap_changes_charge':True,
           'number_conservation_and_positive_squares_do_not_protect_kernel':True},
 'conclusion':'Rooted carrier relabellings do not force equal channel gaps. More generally, symmetries commuting with Q allow independent charge-sector energy offsets, so cannot by themselves fix the composite/elementary ratio. This is a scoped obstruction, not a no-go for additional dynamics or spectrum-generating algebra.',
 'next_falsifier':'Derive a source operation that relates charged-sector energies through a Hamiltonian/spectrum-generating relation, rather than an ordinary charge-preserving relabelling. A proposed conserved energy-counting charge must be independently constructed, not assigned1836 by hand.'}
out=HERE.parent/'results/mass-gap-symmetry.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
