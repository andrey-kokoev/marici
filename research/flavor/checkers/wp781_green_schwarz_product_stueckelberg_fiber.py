"""Exact minimal Green-Schwarz product and Stückelberg-fiber audit."""
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp780=json.loads((ROOT/"results"/"wp780_added_matter_u1_completion_spectral_no_go.json").read_text(encoding="utf-8"))

A,k,c,rho,gF,fa,m,q=sp.symbols("A k c rho gF fa m q", nonzero=True, real=True)
anomaly_residual=A-k*c
rescaled_residual=sp.simplify(anomaly_residual.subs({k:rho*k,c:c/rho}))
stueckelberg_mass_sq=gF**2*fa**2*k**2
rescaled_mass_sq=sp.simplify(stueckelberg_mass_sq.subs(k,rho*k))
low_energy_exchange=sp.simplify(gF**2/stueckelberg_mass_sq)
rescaled_exchange=sp.simplify(low_energy_exchange.subs(k,rho*k))

# Charge reversal reverses an odd Abelian anomaly coefficient. Reversing the
# axion shift coefficient restores cancellation while leaving the mass fixed.
reversed_residual=sp.expand((-A)-(-k)*c)
reversed_mass_sq=sp.expand(stueckelberg_mass_sq.subs(k,-k))
index=q*m
paired_reversed_index=sp.expand(index.subs({q:-q,m:-m}, simultaneous=True))

checks={
 "wp780_dependency_passed":wp780["status"]=="PASS" and all(wp780["checks"].values()),
 "green_schwarz_cancellation_fixes_only_product":sp.solve(sp.Eq(anomaly_residual,0),c)==[A/k],
 "inverse_rescaling_preserves_anomaly_cancellation":sp.simplify(rescaled_residual-anomaly_residual)==0,
 "stueckelberg_mass_changes_along_product_fiber":sp.simplify(rescaled_mass_sq/stueckelberg_mass_sq)==rho**2,
 "low_energy_exchange_changes_along_product_fiber":sp.simplify(rescaled_exchange/low_energy_exchange)==rho**-2,
 "charge_and_axion_orientation_reverse_preserves_cancellation":reversed_residual==-anomaly_residual,
 "stueckelberg_mass_is_orientation_blind":reversed_mass_sq==stueckelberg_mass_sq,
 "paired_charge_flux_reversal_preserves_chiral_index":paired_reversed_index==index,
 "flux_integer_absent_from_local_cancellation_equation":m not in anomaly_residual.free_symbols,
}
checks={name:bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result={
 "work_package":"WP781","status":"PASS","checks":checks,"dependency":"WP780",
 "admitted_state_domain":"minimal four-dimensional Green-Schwarz effective theory with one anomalous U(1)_F, one shifting axion, one Wess-Zumino coefficient, one Stückelberg scale, and integer magnetic flux sectors",
 "faithful_coordinate":"(A,k,c,g_F,f_a,m,q) together with anomaly residual A-kc, Stückelberg mass squared, low-energy exchange, and chiral index qm",
 "source_authorized_probe":"gauge variation of the fermion determinant plus axion Wess-Zumino variation and the Stückelberg quadratic action",
 "contextual_partition":"A=kc identifies the continuous fiber (k,c)~(rho k,c/rho); simultaneous charge/axion/flux reversal preserves cancellation, mass, and chiral index",
 "anomaly_result":"Green-Schwarz cancellation fixes the product kc=A but neither factor separately",
 "threshold_result":"the Stückelberg mass scales as rho^2 along the allowed product fiber while low-energy exchange scales as rho^-2, so threshold survival and physical magnitude are not fixed",
 "orientation_result":"charge reversal accompanied by axion-shift and flux reversal is equally consistent and preserves the chiral index",
 "flux_result":"the integer flux does not appear in the local Green-Schwarz cancellation equation and is not selected",
 "classification":"the minimal Green-Schwarz constructor cancels an anomaly and rigidifies its gauge variation, but is neither an oriented-flux selector nor a physical portal-magnitude selector",
 "smallest_exact_falsifier":"(k,c) and (2k,c/2) cancel the same anomaly, yet their Stückelberg masses differ by four and their low-energy exchanges differ by one quarter",
 "deutschian_status":"a geometric completion must quantize k, c, f_a, and the flux in one common orientation-sensitive object; the effective Green-Schwarz relation alone is too easy to vary",
 "next_source_gate":"identify a concrete compactification intersection lattice whose primitive characteristic vector simultaneously fixes the Green-Schwarz coefficients and an oriented tadpole m=3, then calculate its mass and detector coupling",
 "instrument_gate":"the anomalous U(1)_F is massive; an executable port requires independently fixed Stückelberg mass, kinetic mixing, production current, decay channel, and detector calibration",
 "primary_sources":["https://arxiv.org/abs/1210.6034","https://arxiv.org/abs/hep-ph/0703127"],
}
(ROOT/"results"/"wp781_green_schwarz_product_stueckelberg_fiber.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
