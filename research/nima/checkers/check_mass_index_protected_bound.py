"""Index protection fixes a declared bound, not its carrier charge assignment."""
from pathlib import Path
from contextlib import redirect_stdout
from fractions import Fraction as F
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_mass_local_sector_protection.py'))
N=prior['N']; slots=prior['slots']
def mm(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def transpose(A): return list(map(list,zip(*A)))
def add(A,B): return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def mv(A,v): return [sum(a*b for a,b in zip(row,v)) for row in A]
fixtures=[(F(0),F(0)),(F(1),F(2)),(F(2),F(-3)),(F(1,7),F(3,5))]
for t,u in fixtures:
    # Three bosonic and two fermionic auxiliary states: rectangular index+1.
    A=[[F(1),F(0),t],[F(0),F(1),u]]
    Q=[[F(0) for _ in range(5)] for _ in range(5)]
    for i in range(2):
        for j in range(3): Q[3+i][j]=A[i][j]
    Qd=transpose(Q)
    assert mm(Q,Q)==[[0]*5 for _ in range(5)]
    H0=add(mm(Qd,Q),mm(Q,Qd))
    ground=[-t,-u,F(1),F(0),F(0)]
    assert mv(H0,ground)==[0]*5
    fermion=mm(A,transpose(A))
    assert fermion[0][0]*fermion[1][1]-fermion[0][1]*fermion[1][0]==1+t*t+u*u>0
    # Paired positive spectrum; index is1, not lifted by these deformations.
    power=[[F(int(i==j)) for j in range(5)] for i in range(5)]
    for degree in range(5):
        supertrace=sum(power[i][i]*(1 if i<3 else -1) for i in range(5))
        assert supertrace==(1 if degree==0 else 0)
        power=mm(power,H0)
    for z in (F(1),F(N),F(1944)):
        H=[[H0[i][j]+(abs(z) if i==j else 0) for j in range(5)] for i in range(5)]
        assert mv(H,ground)==[abs(z)*x for x in ground]
# Two integral central-charge assignments preserve all prior charge constraints.
# k is the collective integer, e the elementary one; physical Q=k-e.
def central(k,e,state_weight=1):
    internal=sum(1 if s[1][0]=='arrow' else state_weight for s in slots)
    return internal*k+e
assert central(1,0)==1836 and central(0,1)==1
assert central(1,0,2)==1944 and central(0,1,2)==1
# If the index+1 auxiliary system is supplied in EVERY sector, the single real
# central charge gives charged zero-energy states, an unwanted extra spectrum.
k,e=1,-N
assert central(k,e)==0 and k-e==N+1
# Also in the second assignment; protection does not remove the kernel lattice.
assert central(1,-1944,2)==0 and 1-(-1944)==1945
# The existing source incidence graph has its own canonical two-term complex,
# unlike the auxiliary3-to2 complex above. Do not discard its cycle modes.
path=prior['prior']['previous']['prior']
edge_count=len(path['source_links'])
assert len(path['components'](N,path['source_links']))==1
b0=1; b1=edge_count-N+1
assert (b0,b1,N-edge_count)==(1,13339,-13338)
result={
 'status':'passed','classification':'index_protects_assigned_energy_bound_not_1836_selection',
 'auxiliary_bosonic_dimension':3,'auxiliary_fermionic_dimension':2,'protected_index':1,
 'exact_supercharge_deformations_checked':len(fixtures),
 'source_graph_complex':{'degree_zero_cohomology':b0,'degree_one_cohomology':b1,'graded_index':N-edge_count},
 'equally_protected_collective_energy_ratios':[1836,1944],
 'unwanted_zero_bound_sector':{'collective_integer':k,'elementary_integer':e,'external_charge':k-e},
 'checks':{'prior_sector_chain_fresh':True,'nilpotent_supercharge':True,
           'exact_surviving_bosonic_zero_mode':True,'positive_spectrum_pairing':True,
           'central_charge_assignment_not_selected':True,
           'all_sector_index_predicts_charged_zero_energy_state':True},
 'conclusion':'A nonzero index can protect saturation of a declared energy bound against auxiliary deformations. It protects1836 or1944 equally, depending on the supplied central-charge functional. Extending the same index to every charge sector also produces an unwanted charged zero-energy sector. The actual source graph complex has one degree-zero and13339 degree-one zero modes; it does not supply the trial index+1 spectrum or central-charge assignment.',
 'next_falsifier':'Derive admissible higher cells and a sector-dependent central-charge pairing for the actual source graph complex. Arbitrarily discarding its cycle modes or assigning a bound does not select a particle spectrum.'}
out=HERE.parent/'results/mass-index-protected-bound.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
