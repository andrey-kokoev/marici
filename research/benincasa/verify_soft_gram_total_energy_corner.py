#!/usr/bin/env python3
"""Exact cross-check of the nine-master soft--Gram--total-energy corner."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

HERE=Path(__file__).parent
modes=("total","gram","corner")

def mat(rows):
    return sp.Matrix([[sp.Rational(x) for x in row] for row in rows])

packets={}
for mode in modes:
    p=HERE/f"soft_gram_total_energy_corner_{mode}.json"
    o=json.loads(p.read_text(encoding="utf-8"))
    assert o["schema"]=="marici.benincasa.soft_gram_total_energy_corner_connection.v1"
    assert o["normal_connection"]["logarithmic"]
    assert o["normal_connection"]["higher_poles"]==[]
    R=mat(o["normal_connection"]["residue_matrix"])
    Rf=R[5:9,5:9]
    Ra=mat(o["normal_connection"]["algebraic_plane_residue"])
    Re=mat(o["normal_connection"]["elliptic_boundary_residue"])
    assert Re.rank()==1 and Re**2==sp.zeros(2)
    if mode in ("total","gram"):
        assert Ra==sp.zeros(2)
        assert Rf.rank()==1 and Rf**2==sp.zeros(4)
        semisimple=sp.zeros(4)
        nilpotent=Rf
        excess_nilpotent_rank=Rf.rank()-Re.rank()
    else:
        assert Ra==sp.diag(0,1)
        semisimple=Rf**2
        nilpotent=sp.simplify(Rf-semisimple)
        assert semisimple**2==semisimple
        assert nilpotent**2==sp.zeros(4)
        assert semisimple*nilpotent==sp.zeros(4)
        assert nilpotent*semisimple==sp.zeros(4)
        assert semisimple.rank()==Ra.rank()==1
        assert nilpotent.rank()==Re.rank()==1
        excess_nilpotent_rank=nilpotent.rank()-Re.rank()
    assert excess_nilpotent_rank==0
    packets[mode]={
        "full_final_residue_rank":Rf.rank(),
        "algebraic_residue_rank":Ra.rank(),
        "elliptic_nilpotent_rank":Re.rank(),
        "elliptic_N_squared_zero":Re**2==sp.zeros(2),
        "full_nilpotent_rank":nilpotent.rank(),
        "full_N_squared_zero":nilpotent**2==sp.zeros(4),
        "excess_nilpotent_rank":excess_nilpotent_rank,
        "semisimple_rank":semisimple.rank(),
    }

# Frozen ordinary/Rees expansion of the published algebraic quartic.
E,s,p,x=sp.symbols("E s p x")
Q=-16*p**2-8*p*E**2+8*s*E**3-5*E**4
assert sp.expand(Q).coeff(E,1)==0
assert sp.expand(Q).coeff(E,2)==-8*p
corner_second=sp.expand((-8*p).subs(p,-x**2))
assert corner_second==8*x**2

# The signed-energy boundary factor is already an SNC product.
u,v=sp.symbols("u v")
B=u*v
assert sp.Poly(B,u,v).terms()==[((1,1),sp.Integer(1))]

result={
 "schema":"marici.benincasa.soft_gram_total_energy_corner_verification.v1",
 "status":"pass",
 "frozen_normals":{"u":"ell4=E_T","v":"ell3","site_soft_corner":"u=v=0 => X3=0 and X2=-X1","B":"u*v"},
 "mode_certificates":packets,
 "residue_conclusion":{
   "total_energy":"rank-one nodal elliptic N only",
   "gram":"rank-one nodal elliptic N only in the nine-master quotient; physical orientation Kummer is an independent sign line",
   "radial_corner":"one algebraic integral semisimple grade plus the same rank-one elliptic N",
   "excess_kernel_to_elliptic_nilpotent_rank":0,
   "new_extension_coupling_detected":False
 },
 "physical_gram_kummer":{"T_s":-1,"T_u":1,"N":0},
 "combined_with_elliptic_nearby_cycles":{"T_s":-1,"rank_N":1,"N_squared_zero":True},
 "second_rees":{
   "Q_gr1_E":0,
   "Q_gr2_E":"-8*p",
   "corner_p":"-x^2",
   "corner_Q_gr2_E":"8*x^2",
   "generic_nonzero":True,
   "classification":"regular second-normal coefficient datum; Q itself is a unit at the corner"
 },
 "classification":"existing energy/Gram/soft SNC carrier plus algebraic Tate, orientation Kummer, and nodal Legendre coefficient data",
 "new_carrier_datum":False,
 "scope_boundary":"Exact on three source-fixed one-parameter tests of the nine-master q_G12 residue module; this does not prove the full multivariate logarithmic extension or integral physical-chain compatibility."
}
out=HERE/"soft_gram_total_energy_corner_verification.json"
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print("SOFT-GRAM-TOTAL-ENERGY CORNER PASS")
print(json.dumps(result["residue_conclusion"],indent=2))
print(out)
