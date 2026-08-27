"""Exact rank-two unimodular characteristic/flux orbit audit."""
import itertools
import json
from math import gcd
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp782=json.loads((ROOT/"results"/"wp782_rank_one_unimodular_lattice_flux_three_no_go.json").read_text(encoding="utf-8"))
J=sp.Matrix([[1,0],[0,-1]])
U=sp.Matrix([[0,1],[1,0]])

def primitive(v):
    return gcd(abs(int(v[0])),abs(int(v[1])))==1

def dot(G,u,v):
    return int((sp.Matrix(u).T*G*sp.Matrix(v))[0])

def characteristic(G,b,bound=5):
    return all((dot(G,b,x)-dot(G,x,x))%2==0
               for x in itertools.product(range(-bound,bound+1),repeat=2))

isometries={}
for name,G in (("odd",J),("even",U)):
    mats=[]
    for entries in itertools.product(range(-3,4),repeat=4):
        A=sp.Matrix(2,2,entries)
        if abs(A.det())==1 and A.T*G*A==G:
            mats.append(tuple(entries))
    isometries[name]=sorted(mats)

even_primitive_characteristics=[
    v for v in itertools.product(range(-5,6),repeat=2)
    if primitive(v) and characteristic(U,v)
]
odd_b=(1,1)
odd_b_is_characteristic=characteristic(J,odd_b)
pairing_three_fluxes=[
    v for v in itertools.product(range(-6,7),repeat=2)
    if primitive(v) and dot(J,odd_b,v)==3
]
flux_norms={v:dot(J,v,v) for v in pairing_three_fluxes}
stabilizer_b=[]
for entries in isometries["odd"]:
    A=sp.Matrix(2,2,entries)
    if tuple(A*sp.Matrix(odd_b))==odd_b:
        stabilizer_b.append(entries)

f1=(2,-1)
f2=(4,1)

# Two positive generalized metrics compatible with J.
H0=sp.eye(2)
H1=sp.Matrix([[sp.Rational(5,4),sp.Rational(3,4)],
              [sp.Rational(3,4),sp.Rational(5,4)]])
compat0=sp.simplify(H0*J*H0-J)
compat1=sp.simplify(H1*J*H1-J)
energy0=(sp.Matrix(f1).T*H0*sp.Matrix(f1))[0]
energy1=(sp.Matrix(f1).T*H1*sp.Matrix(f1))[0]

checks={
 "wp782_dependency_passed":wp782["status"]=="PASS" and all(wp782["checks"].values()),
 "odd_and_even_forms_are_unimodular":abs(J.det())==1 and abs(U.det())==1,
 "bounded_integral_isometry_groups_have_four_elements_each":len(isometries["odd"])==4 and len(isometries["even"])==4,
 "even_hyperbolic_plane_has_no_primitive_characteristic_vector":even_primitive_characteristics==[],
 "odd_null_vector_is_primitive_characteristic":primitive(odd_b) and odd_b_is_characteristic,
 "bounded_pairing_three_fiber_has_multiple_primitive_points":len(pairing_three_fluxes)>=2,
 "hostile_pair_has_same_pairing_three":dot(J,odd_b,f1)==3 and dot(J,odd_b,f2)==3,
 "hostile_pair_has_distinct_isometry_invariant_norms":flux_norms[f1]==3 and flux_norms[f2]==15,
 "fixed_characteristic_stabilizer_is_trivial":len(stabilizer_b)==1,
 "compatible_kinetic_metrics_give_different_flux_energy":compat0==sp.zeros(2) and compat1==sp.zeros(2) and energy0==5 and energy1==sp.Rational(13,4),
}
checks={name:bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result={
 "work_package":"WP783","status":"PASS","checks":checks,"dependency":"WP782",
 "admitted_state_domain":"the even hyperbolic plane U and odd lattice I_(1,1), primitive vectors in [-6,6]^2, integral isometries with entries in [-3,3], and two exact compatible positive kinetic metrics",
 "faithful_coordinate":"lattice parity, primitive characteristic vector, pairing, flux norm, joint isometry orbit, and generalized kinetic metric",
 "source_authorized_probe":"unimodularity, characteristic parity, integral isometry action, invariant norm, and flux kinetic energy",
 "contextual_partition":"the even lattice has no primitive characteristic sector; the odd lattice pairing-three fiber splits into multiple norm-distinguished orbits",
 "orbit_result":"for b=(1,1), f=(2,-1) and f=(4,1) are primitive, both pair to three, but have norms 3 and 15 and cannot be isometric",
 "normalization_result":"two exact J-compatible positive metrics give energies 5 and 13/4 for the same flux vector, so the integral source does not fix threshold normalization",
 "classification":"rank two permits primitive pairing three but does not select a unique physical flux orbit or kinetic scale",
 "smallest_exact_falsifier":"the norm-distinguished hostile pair f=(2,-1) and f=(4,1) has identical pairing-three readout",
 "search_scope":"primitive vectors in [-6,6]^2 and isometry matrices in [-3,3]^4; the hostile pair is exact and sufficient independently of exhaustiveness beyond the box",
 "deutschian_status":"pairing three is too weak: it leaves physically inequivalent flux constructors and a continuous metric fiber",
 "next_source_gate":"add a source-derived secondary invariant or potential that uniquely selects one pairing-three orbit and stabilizes the tensor metric, then test orientation and the Stückelberg instrument",
 "instrument_gate":"the lattice and metric candidates still do not name production currents, decay channels, kinetic mixing, or calibrated physical16 response",
 "primary_sources":["https://arxiv.org/abs/1103.0019","https://arxiv.org/abs/1808.01334"],
}
(ROOT/"results"/"wp783_rank_two_unimodular_pairing_three_fiber.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
