#!/usr/bin/env python3
"""Independent combinatorial and liquid-drop baselines for a triangular-involution proposal.

This is NOT a native Marici P/E/N implementation. The oscillator occupancy,
spin-orbit reordering, and SEMF energies are distinct hypotheses/models.
"""
from __future__ import annotations
import itertools, json
from sympy import Matrix
from pathlib import Path

MAGIC = [2, 8, 20, 28, 50, 82, 126]
AC = 0.714              # illustrative Coulomb coefficient, MeV
ASYM = 23.2             # illustrative symmetry coefficient, MeV
D = 0.78235             # neutron - hydrogen atomic rest energy, MeV


def triangle_states(k):
    return [(x, y, k - x - y) for x in range(k + 1) for y in range(k - x + 1)]


def exchange_orbits(k):
    states = set(triangle_states(k)); visited = set(); fixed = pairs = 0
    for v in sorted(states):
        if v in visited: continue
        w = (v[1], v[0], v[2]); assert w in states
        visited.update((v,w))
        if v==w: fixed += 1
        else: pairs += 1
    return fixed, pairs


def oscillator_capacity(k):
    return (k+1)*(k+2)


def high_j_capacity(k):
    # j=l+1/2, l=k, hence 2j+1=2(k+1).
    return 2*(k+1)


def beta_min_Z(A):
    # Mass minimum among isobars, ignoring discrete pairing and shell corrections.
    return (4*ASYM + AC/A**(1/3) + D)/(8*ASYM/A + 2*AC/A**(1/3))


def harmonic_trace_check(k):
    """Exact rank of Laplacian on degree-k homogeneous polynomials in 3 variables."""
    src = triangle_states(k)
    dst = triangle_states(k-2) if k>=2 else []
    rows = {triple: i for i,triple in enumerate(dst)}
    L = [[0 for _ in src] for _ in dst]
    for j, exponents in enumerate(src):
        for d in range(3):
            if exponents[d]>=2:
                reduced=list(exponents)
                reduced[d]-=2
                L[rows[tuple(reduced)]][j]+=exponents[d]*(exponents[d]-1)
    rank = Matrix(L).rank() if dst else 0
    assert rank == len(dst), (k,rank,len(dst))
    assert len(src)-rank == 2*k+1
    return {'k':k,'polynomial_dimension':len(src),'trace_rank':rank,
            'harmonic_kernel_dimension':len(src)-rank,
            'j_plus_capacity':2*k+2,
            'j_minus_capacity':2*k if k else 0}

trace_tests=[harmonic_trace_check(k) for k in range(7)]
levels = []
old_total = 0
for k in range(7):
    states = triangle_states(k)
    fixed, pairs = exchange_orbits(k)
    cap = oscillator_capacity(k)
    assert len(states) == (k+1)*(k+2)//2
    assert fixed+2*pairs == len(states)
    assert cap == 2*len(states)
    old_total += cap
    n=k+1
    levels.append({"k":k,"triangular_states":len(states),"involution_fixed_points":fixed,
        "involution_pairs":pairs,"spin_doubled_capacity":cap,"HO_cumulative":old_total,
        "rhombus_capacity":2*n*n,"proposed_excess_square_fillings":2*(n-1)*(n-2) if n>=2 else 0,
        "max_j_orbital_capacity":high_j_capacity(k)})

# Standard high-j spin-orbit reordering, stated as an additional physical assumption.
blocks = [
    {"name":"0s1/2", "capacity":oscillator_capacity(0), "construction":"HO k=0"},
    {"name":"0p3/2 + 0p1/2", "capacity":oscillator_capacity(1),"construction":"HO k=1"},
    {"name":"0d + 1s", "capacity":oscillator_capacity(2),"construction":"HO k=2"},
    {"name":"0f7/2", "capacity":high_j_capacity(3),"construction":"high-j intruder from k=3"},
]
for k in range(4,7):
    cap=oscillator_capacity(k-1)-high_j_capacity(k-1)+high_j_capacity(k)
    blocks.append({"name":f"remainder k={k-1} + high-j k={k}","capacity":cap,
                   "construction":f"{oscillator_capacity(k-1)} - {high_j_capacity(k-1)} + {high_j_capacity(k)}"})
current=0
for b in blocks:
    current+=b['capacity']; b['cumulative']=current
assert [b['cumulative'] for b in blocks]==MAGIC

nuclei=[]
for symbol,Z,A in [("He-4",2,4),("Ne-20",10,20),("Ar-40",18,40),("Kr-84",36,84),("Xe-132",54,132),("Pb-208",82,208)]:
    z_hat=beta_min_Z(A)
    nuclei.append({"isotope":symbol,"A":A,"observed_protons":Z,"observed_neutrons":A-Z,
        "observed_neutron_excess":A-2*Z,"SEMF_mass_minimum_Z":round(z_hat,3),
        "SEMF_mass_minimum_N":round(A-z_hat,3),"proton_residual":round(Z-z_hat,3)})

# Square-count sequence is demonstrably not the physical high-j sequence.
assert [r['proposed_excess_square_fillings'] for r in levels[:6]]==[0,0,4,12,24,40]
assert [r['max_j_orbital_capacity'] for r in levels[3:7]]==[8,10,12,14]
result={"assumptions":{"spin_orbit_reordering_is_an_extra_input":True,"coefficient_MeV":{"coulomb":AC,"symmetry":ASYM,"neutron_minus_H":D},"SEMF_omits_pairing_and_shell_corrections":True},"oscillator_and_involution_levels":levels,"exact_laplacian_rank_tests":trace_tests,"spin_orbit_shell_blocks":blocks,"noble_gas_and_Pb_comparison":nuclei,"conclusions":{"simple_square_filler_count_predicts_magic":False,"triangular_slice_predicts_first_3_magic":True,"high_j_intruder_rule_predicts_all_7_magic":True,"SEMF_is_not_geometry_derived":True}}
p=Path('/mnt/data/nuclear_shell_involution_results.json')
p.write_text(json.dumps(result,indent=2)+'\n')
print('HO closures:',[l['HO_cumulative'] for l in levels])
print('Spin-orbit closures:',[b['cumulative'] for b in blocks])
print('Exact Laplacian rank, harmonic dimensions:',[(r['k'],r['trace_rank'],r['harmonic_kernel_dimension']) for r in trace_tests])
print('Involution k, fixed, paired:', [(l['k'],l['involution_fixed_points'],l['involution_pairs']) for l in levels])
print('Isotope | SEMF Z* | observed Z | predicted N* | observed N')
for r in nuclei: print(r['isotope'],r['SEMF_mass_minimum_Z'],r['observed_protons'],r['SEMF_mass_minimum_N'],r['observed_neutrons'])
print('PASS: all exact combinatorial assertions')
