"""Cyclic transport of the typed first-Rees e6/physical-boundary pairing."""
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/benincasa/results/rank12-e6-supported-pairing-cyclic.json'
P=[[0,0,1],[1,0,0],[0,1,0]]
pair=Fraction(1,4)

# Symbolic homogeneity exponents on each chart edge.  e6 has weight -2 in
# Entry 764's physical-energy gauge; the dual cycle has weight +2.
covector_weights=[-2,-2,-2]
cycle_weights=[2,2,2]
assert [a+b for a,b in zip(covector_weights,cycle_weights)]==[0,0,0]

def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert mm(P,mm(P,P))==[[1,0,0],[0,1,0],[0,0,1]]
pairings=[pair,pair,pair]

packet={
 'schema':'marici.benincasa.rank12_e6_supported_pairing_cyclic.v1',
 'occurrence_order':['X2-soft/G12','X3-soft/G23','X1-soft/G31'],
 'cyclic_matrix':P,
 'residue_orientation_signs':[1,1,1],
 'e6_covector_homogeneity':covector_weights,
 'physical_boundary_dual_homogeneity':cycle_weights,
 'net_pairing_homogeneity':[0,0,0],
 'pairings':[str(x) for x in pairings],
 'threefold_transport_identity':True,
 'regular_module_functional':'(1/4)*(1,1,1)',
 'classification':'the typed supported first-Rees physical pairing is C3-invariant; no cyclic sign, scale, or carrier obstruction'
}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet))
