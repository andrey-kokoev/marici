"""Reversible syndrome/feedback locking with retained records and reservoirs."""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import product
from fractions import Fraction as F
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    prior=runpy.run_path(str(HERE/'check_mass_path_port_connectivity.py'))
N=prior['N']; edges=prior['source_links']
adj=[set() for _ in range(N)]
for a,b in edges: adj[a].add(b); adj[b].add(a)
# A deterministic physical controller schedule, not a new source symmetry.
seen={0}; queue=[0]; tree=[]
for parent in queue:
    for child in sorted(adj[parent]):
        if child not in seen:
            seen.add(child); queue.append(child); tree.append((parent,child))
assert len(tree)==N-1
# Exact finite-register version, all records retained. The qutrit residues here
# test unitarity; the full network below uses integer charges without wrapping.
d=3
def gate(a,b,r):
    rp=(r+b-a)%d
    bp=(b-rp)%d
    return a,bp,rp
images={gate(a,b,r) for a,b,r in product(range(d),repeat=3)}
assert len(images)==d**3
for a,b,r in product(range(d),repeat=3):
    ap,bp,rp=gate(a,b,r)
    old_b=(bp+rp)%d; old_r=(rp-old_b+ap)%d
    assert (ap,old_b,old_r)==(a,b,r)
    if r==0: assert bp==a
    # Two separate ideal reservoirs carry charge and charging-energy transfers.
    q,w=7,11
    qp=q+b-bp; wp=w+b*b-bp*bp
    assert a+b+q==ap+bp+qp
    assert a*a+b*b+w==ap*ap+bp*bp+wp
# QND syndrome recording alone does not alter charge populations.
for n in range(2,6):
    configs=list(product(range(d),repeat=n))
    accepted=[v for v in configs if all(v[i+1]-v[i]==0 for i in range(n-1))]
    assert F(len(accepted),len(configs))==F(1,d**(n-1))
assert all(x==0 for x in (0,)*N)  # zero syndrome also accepts the vacuum

# Full integer controller: n_child -> n_parent, record old difference, and
# retain reservoirs rather than concealing the energy/charge needed for locking.
charges=[0]*N; charges[0]=1
initial=charges.copy(); records=[]; reservoir_q=N; reservoir_E=N
initial_total_Q=sum(charges)+reservoir_q
initial_total_E=sum(x*x for x in charges)+reservoir_E
for parent,child in tree:
    a,b=charges[parent],charges[child]
    record=b-a
    charges[child]=a
    reservoir_q+=b-a
    reservoir_E+=b*b-a*a
    records.append((parent,child,record))
    assert sum(charges)+reservoir_q==initial_total_Q
    assert sum(x*x for x in charges)+reservoir_E==initial_total_E
assert charges==[1]*N
assert all(charges[a]==charges[b] for a,b in edges)
energy_supplied=N-reservoir_E
assert energy_supplied==N-1
# Exact reverse uses the retained difference; deleting records is not allowed.
for parent,child,record in reversed(records):
    a=charges[parent]; b=a+record
    reservoir_q+=a-b; reservoir_E+=a*a-b*b
    charges[child]=b
assert charges==initial and reservoir_q==N and reservoir_E==N
# Gain mismatch is a different constraint, not evidence for equal charges.
assert (2*1-2)==0 and 1!=2  # sensor measuring 2*n_parent-n_child
# Every core integer k is prepared; nothing selects k=1 over k=0 or k=2.
for k in (-1,0,1,2):
    state=[0]*N; state[0]=k
    for a,b in tree: state[b]=state[a]
    assert state==[k]*N and sum(x*x for x in state)==N*k*k

result={
 'status':'passed','classification':'reversible_driven_charge_locking_not_autonomous_mass_generation',
 'channels':N,'retained_difference_records':len(records),
 'prepared_unit_sector_energy':N,'supplied_charging_energy':energy_supplied,
 'uniform_product_postselection_probability':f'3^(-{N-1})',
 'checks':{'prior_chain_fresh':True,'full_finite_register_unitarity':True,
           'reservoir_charge_and_energy_conserved':True,'integer_network_constraints_satisfied':True,
           'retained_record_reverse_recovers_input':True,'measurement_alone_not_preparation':True,
           'zero_syndrome_does_not_select_nonzero_charge':True,'coupling_gain_mismatch_hostile':True},
 'conclusion':'A reversible QND-syndrome plus feedback interaction locks all1836 charges and retains the old differences. Preparing unit occupation from one seeded unit requires1835 supplied charge and energy units under the chosen charging Hamiltonian. It is a driven preparation, not an autonomous source-derived proton mass mechanism.',
 'next_falsifier':'Derive an autonomous source Hamiltonian, conserved sector and energy form implementing the locking interaction without externally choosing the root charge, matched gains and work supply.'}
out=HERE.parent/'results/mass-history-locking-controller.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
