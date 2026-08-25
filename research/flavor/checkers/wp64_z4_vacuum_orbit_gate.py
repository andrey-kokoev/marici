#!/usr/bin/env python3
"""WP64: exact Z4 angular-vacuum orbit and missing quotient-map audit."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp64_z4_vacuum_orbit_gate.json"

def main():
    theta,kappa=sp.symbols("theta kappa",real=True)
    r=sp.symbols("r",positive=True)
    n=4
    vang=2*kappa*r**n*sp.cos(n*theta)
    d1=sp.diff(vang,theta); d2=sp.diff(vang,theta,2)
    stationary=[sp.Rational(j,4)*sp.pi for j in range(8)]
    hessians=[sp.simplify(d2.subs(theta,t)) for t in stationary]
    # kappa<0: even j are minima (real/imaginary axes); kappa>0: odd j.
    kmag=sp.symbols("K",positive=True)
    hneg=[sp.simplify(h.subs(kappa,-kmag)) for h in hessians]
    hpos=[sp.simplify(h.subs(kappa,kmag)) for h in hessians]
    minima_neg=[j for j,h in enumerate(hneg) if h.is_positive]
    minima_pos=[j for j,h in enumerate(hpos) if h.is_positive]
    authority=json.loads((ROOT/"research/flavor/results/wp60_source_authority_inventory.json").read_text())
    gates={
      "angular_stationarity_is_sin_4theta_zero":sp.simplify(d1/(-8*kappa*r**4)-sp.sin(4*theta))==0,
      "negative_kappa_selects_real_imaginary_axes":minima_neg==[0,2,4,6],
      "positive_kappa_selects_pi_over_4_shifted_axes":minima_pos==[1,3,5,7],
      "coefficient_sign_changes_vacuum_orbit":minima_neg!=minima_pos,
      "source_marks_z4_picture_illustrative_deferred":authority["markers"]["z4_modal"]["unique"] and authority["markers"]["uv_deferred"]["unique"],
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.z4-vacuum-orbit-gate.v1",
      "arithmetic":"exact symbolic angular-potential calculus",
      "candidate_potential":"V_ang=2 kappa r^4 cos(4 theta)",
      "stationary_set":"theta=j*pi/4",
      "vacuum_orbits":{"kappa_negative":"theta=0,pi/2,pi,3pi/2 (real/imaginary)","kappa_positive":"theta=pi/4,3pi/4,5pi/4,7pi/4"},
      "independent_normalization":"missing: source does not specify kappa sign, radial potential, flavon-Yukawa map, or vacuum-selection history",
      "descent":"not established to physical16; theta is a flavon/chart datum until a covariant Yukawa coupling map is declared",
      "classification":{"vacuum_rigidifier_given_sign":True,"physical_selector":False,"instrument":"none declared"},
      "smallest_exact_falsifier":"changing only sign(kappa) shifts every minimum by pi/4 while preserving Z4 symmetry",
      "minimal_added_structure":"complete potential with coefficient signs, selected vacuum orbit, covariant spurion-to-Yukawa map, and ensemble-tested physical prediction",
      "conclusion":"Z4 symmetry alone does not select the real/imaginary orbit; the potential sign does, and that datum plus the quotient map is absent.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()
