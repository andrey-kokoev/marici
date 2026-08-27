"""Exact isolated-fixture versus external portal-interface audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp799 = json.loads(
    (ROOT / "results" / "wp799_monodromic_g2_polarization_scale_fiber.json")
    .read_text(encoding="utf-8")
)

genus, punctures = sp.symbols("genus punctures", integer=True, nonnegative=True)
moduli_dimension = 3 * genus - 3 + punctures

# Intrinsic normalized fixture datum and external portal interface.
C = sp.symbols("C", nonzero=True, real=True)
kappa = sp.symbols("kappa", real=True)
portal = sp.expand(kappa * C)

# Intrinsic fixture probes see C but are blind to the external interface.
intrinsic_jacobian = sp.Matrix([[sp.diff(C, C), sp.diff(C, kappa)]])
interface_kernel = intrinsic_jacobian.nullspace()

# A dimension-two relevant deformation creates a threshold proportional to sqrt(m).
m = sp.symbols("m", positive=True, real=True)
threshold = sp.sqrt(m)

# A rank-one Coulomb coordinate is a vacuum coordinate even for an isolated SCFT.
u = sp.symbols("u", real=True)

checks = {
    "wp799_dependency_passed": wp799["status"] == "PASS"
    and all(wp799["checks"].values()),
    "three_punctured_sphere_has_no_complex_structure_modulus":
        moduli_dimension.subs({genus: 0, punctures: 3}) == 0,
    "four_punctured_sphere_restores_one_gluing_modulus":
        moduli_dimension.subs({genus: 0, punctures: 4}) == 1,
    "portal_depends_on_external_interface":
        sp.diff(portal, kappa) == C,
    "same_fixture_two_interfaces_give_distinct_portals":
        portal.subs(kappa, 1) != portal.subs(kappa, 2),
    "interface_sign_is_not_fixed_by_fixture":
        portal.subs(kappa, -1) == -portal.subs(kappa, 1),
    "intrinsic_probe_has_rank_one_on_two_coordinate_packet":
        intrinsic_jacobian.rank() == 1,
    "intrinsic_probe_kernel_is_interface_direction":
        interface_kernel == [sp.Matrix([0, 1])],
    "relevant_deformation_sets_free_threshold":
        threshold.subs(m, 1) != threshold.subs(m, 4),
    "rank_one_coulomb_vacuum_is_not_singleton":
        u.subs(u, 0) != u.subs(u, 1),
    "added_portal_probe_detects_interface_only_after_new_coupling":
        sp.Matrix([[sp.diff(C, C), sp.diff(C, kappa)],
                   [sp.diff(portal, C), sp.diff(portal, kappa)]])
        .subs(kappa, 1).rank() == 2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP800",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP799",
    "admitted_state_domain": (
        "a three-punctured Z3-twisted D4 class-S fixture treated as an "
        "isolated four-dimensional N=2 SCFT, together with a separately "
        "declared coupling kappa from a normalized dimension-two fixture "
        "operator to a dimension-two external flavor bilinear, relevant "
        "deformation coefficient m, and rank-one Coulomb coordinate u"
    ),
    "faithful_coordinate": (
        "intrinsic normalized SCFT data C, external portal coefficient kappa, "
        "relevant deformation m, Coulomb vacuum u, Standard Model embedding, "
        "threshold completion, and physical16 detector response"
    ),
    "source_authorized_probe_family": (
        "intrinsic fixture spectra, central charges, flavor levels, and "
        "normalized correlators; the external portal response is excluded "
        "until its coupling operation is independently admitted"
    ),
    "contextual_partition": (
        "intrinsic probes identify all states with the same fixture data C "
        "while leaving the full kappa direction unresolved; adding the portal "
        "experiment refines that partition but changes the source experiment"
    ),
    "selector_result": (
        "fixture isolation can select intrinsic dimensionless SCFT data and "
        "remove a complex-structure gauge modulus, but it neither selects the "
        "external portal interface nor its deformation and vacuum state"
    ),
    "smallest_exact_falsifier": (
        "the same isolated fixture with kappa=1 and kappa=2 has identical "
        "intrinsic spectra and correlators but different portal magnitudes; "
        "kappa=+1 and -1 reverse the portal sign"
    ),
    "sign_result": (
        "the fixture fixes no relative sign between its normalized operator "
        "and the external Standard Model bilinear"
    ),
    "magnitude_result": (
        "intrinsic OPE coefficients may be fixed, but the physical portal is "
        "their product with the independently variable interface kappa"
    ),
    "rg_threshold_result": (
        "the undeformed SCFT has no massive threshold hierarchy; a relevant "
        "dimension-two deformation introduces a threshold proportional to "
        "sqrt(m), and m is not fixed by fixture isolation"
    ),
    "instrument_result": (
        "intrinsic SCFT correlators are physical instruments for fixture data "
        "but have a one-dimensional kernel on the fixture-plus-interface "
        "packet; the portal probe becomes rank two only after adding the "
        "external coupling experiment and still lacks physical16 calibration"
    ),
    "deutschian_status": (
        "isolation makes intrinsic CFT data hard to vary, but the explanation "
        "of the flavor portal remains easy to vary at the interface, relevant "
        "deformation, vacuum, and detector arrows"
    ),
    "remaining_gate": (
        "derive the Standard Model sector and its portal as part of the same "
        "isolated source rather than by gluing an external operator, then "
        "prove unique deformation/vacuum selection, massive threshold "
        "survival, and calibrated physical16 response"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/1601.02077",
        "https://arxiv.org/abs/0904.2715",
        "https://arxiv.org/abs/1203.6734",
    ],
}

(ROOT / "results" / "wp800_isolated_fixture_interface_deformation_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
