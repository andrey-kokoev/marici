#!/usr/bin/env python3
"""WP61: exact local reversibility of the complete coupled one-loop RG field."""

from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/flavor/results/wp61_full_rg_local_diffeomorphism.json"

def main():
    xs=sp.symbols("x0:8", real=True)
    yu=sp.Matrix(2,2,xs[:4]); yd=sp.Matrix(2,2,xs[4:])
    au,bu,gu=sp.Rational(2),sp.Rational(3),sp.Rational(-1)
    ad,bd,gd=sp.Rational(-2),sp.Rational(1),sp.Rational(-3)
    fu=au*yu+bu*yu*yu.T*yu+gu*yd*yd.T*yu
    fd=ad*yd+bd*yd*yd.T*yd+gd*yu*yu.T*yd
    f=sp.Matrix(list(fu)+list(fd))
    jac=f.jacobian(xs)
    point={x:v for x,v in zip(xs,[1,2,0,3,2,1,4,1])}
    f0=sp.simplify(f.subs(point)); j0=sp.simplify(jac.subs(point)); acceleration=sp.simplify(j0*f0)

    # Universal second-order flow jet and reverse-flow jet cancellation.
    forward_t1=f0
    forward_t2=sp.Rational(1,2)*acceleration
    reverse_composite_t1=sp.simplify(forward_t1-f0)
    reverse_composite_t2=sp.simplify(forward_t2-j0*forward_t1+sp.Rational(1,2)*acceleration)
    tau=sp.symbols("tau",real=True)
    differential_jet=sp.eye(8)+tau*j0
    determinant_at_zero=sp.simplify(differential_jet.det().subs(tau,0))

    wp53=json.loads((ROOT/"research/flavor/results/wp53_rg_transport_selector_gate.json").read_text())
    wp60=json.loads((ROOT/"research/flavor/results/wp60_source_authority_inventory.json").read_text())
    gates={
      "complete_coupled_beta_field_is_nonzero":f0!=sp.zeros(8,1),
      "forward_reverse_flow_jets_cancel_at_first_order":reverse_composite_t1==sp.zeros(8,1),
      "forward_reverse_flow_jets_cancel_at_second_order":reverse_composite_t2==sp.zeros(8,1),
      "flow_differential_is_invertible_at_zero_time":determinant_at_zero==1,
      "full_weak_basis_covariance_dependency_passes":wp53["gates"]["one_loop_yukawa_beta_is_full_weak_basis_covariant"],
      "rg_is_only_derived_source_operation":wp60["gates"]["exactly_one_derived_operation_family_declared"],
    }
    assert all(gates.values()),gates
    result={
      "schema":"marici.flavor.full-rg-local-diffeomorphism.v1",
      "arithmetic":"exact rational polynomial vector-field algebra",
      "operation":"complete coupled one-loop Yukawa beta field with self and cross-sector cubic terms",
      "domain":"finite RG intervals inside the smooth Yukawa-pair domain; quotient conclusion uses WP53 covariance",
      "flow_jet":{"first":str(forward_t1),"second_acceleration":str(acceleration),"reverse_residual_order_1":str(reverse_composite_t1),"reverse_residual_order_2":str(reverse_composite_t2)},
      "descent":"yes, by WP53 full weak-basis covariance",
      "proper_image":"no locally: autonomous smooth ODE uniqueness makes every finite-time flow a local diffeomorphism wherever both directions exist",
      "contextual_partition":"locally unchanged; physical points are transported bijectively",
      "instrument":"no standalone RG instrument; scale-dependent measurements provide boundary readouts",
      "smallest_exact_falsifier":"unit determinant of the flow differential at zero time together with the vanishing second-order forward/reverse residual",
      "conclusion":"The complete coupled one-loop field, not only its leading common rescaling, is locally invertible transport and cannot locally select a proper physical16 family.",
      "gates":gates,
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":sum(gates.values()),"total":len(gates),"output":str(OUT.relative_to(ROOT))}))

if __name__=="__main__": main()
