"""Exact charged-core dressing model; a mechanism, not a derived particle mass."""
from fractions import Fraction as F
from pathlib import Path
from contextlib import redirect_stdout
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    source=runpy.run_path(str(HERE/'check_proton_electron_comparison_slots.py'))
slots=source['expanded']
counts={kind:sum(s[1][0]==kind for s in slots) for kind in ('arrow','state')}
assert counts=={'arrow':1728,'state':108}
# Binary core c, elementary excitation e and one neutral occupation per slot.
# Q=c-e. H=de*e+mu*c+sum(delta_s*n_s+J_s*(n_s-c)^2).
# All operators commute. Exact Q=+1/-1 minima factor into single-slot minima.
def sectors(da=F(1),ds=F(1),J=F(2),mu=F(0),de=F(1)):
    assert min(da,ds,J,de)>0 and mu>=0
    deltas=[da if kind=='arrow' else ds for _,(kind,_,_) in slots]
    plus=mu+sum(min(d,J) for d in deltas)
    minus=de
    full=all(J>d for d in deltas)
    gap=min(abs(J-d) for d in deltas)
    return plus/minus,full,gap
assert sectors()==(F(1836),True,F(1))
# These deformations preserve the carrier relabellings, Q and complete dressing.
assert sectors(ds=F(2),J=F(3))[0:2]==(F(1944),True)
assert sectors(mu=F(1))[0:2]==(F(1837),True)
assert sectors(de=F(2))[0:2]==(F(918),True)
# Insufficient stiffness prefers empty channels even in the positive sector.
assert sectors(J=F(1,2))==(F(918),False,F(1,2))
# At the threshold, empty and filled slots are degenerate, not obligatory.
assert sectors(J=F(1))==(F(1836),False,F(0))
# Small exact enumeration independently checks the factorized sector minima.
from itertools import product
for count in range(1,7):
    energies={q:[] for q in (-1,0,1)}
    for c,e in product((0,1),repeat=2):
        for ns in product((0,1),repeat=count):
            E=e+sum(n+2*(n-c)**2 for n in ns)
            energies[c-e].append(E)
    assert min(energies[-1])==1 and min(energies[1])==count and min(energies[0])==0
# Charge-conserving off-diagonal dressing also changes the energy. A neutral
# slot term -g X has eigenvalues (d+J)/2 +/- sqrt((d+J*(1-2c))^2/4+g^2).
# For d=1,J=2,g=2: sqrt(9/4+4)=5/2 in c=0; c=1 has sqrt(1/4+4)=sqrt(17)/2.
# Hence per-slot core energy relative to the dressed vacuum is (5-sqrt(17))/2,
# not 1. Q conservation alone does not protect the integer coefficient.
import math
shifted=counts['arrow']+counts['state']
shifted*= (5-math.sqrt(17))/2
assert abs(shifted-1836)>100
result={
 'status':'passed','classification':'conditional_charged_core_dressing_not_forced_mass_ratio',
 'counts':counts,'baseline_ratio':1836,'fixed_charge_neutral_gap':1,
 'hostiles':{'state_gap_changed':1944,'bare_core_energy_added':1837,
             'elementary_gap_changed':918,'weak_stiffness_incomplete_dressing':918,
             'threshold_degenerate':True,'charge_preserving_transverse_ratio':shifted},
 'conclusion':'A charged core can energetically require all comparison channels and store1836 unit gaps. Carrier symmetry and charge conservation do not force equal gaps, zero bare core energy, the elementary gap normalization, or absence of quantum dressing shifts.',
 'next_falsifier':'Derive a source symmetry or constraint tying the two slot gaps to the elementary gap and protecting the core energy, without inserting the target ratio.'}
out=HERE.parent/'results/mass-comparison-dressing.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
