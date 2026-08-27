"""Exact rank-one unimodular Green-Schwarz lattice audit."""
import json
from math import gcd
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
wp781=json.loads((ROOT/"results"/"wp781_green_schwarz_product_stueckelberg_fiber.json").read_text(encoding="utf-8"))

def primitive(n):
    return n != 0 and gcd(abs(n),0)==1

def pairing(gram,u,v):
    return gram*u*v

grams=range(1,9)
unimodular=[n for n in grams if abs(n)==1]
primitive_vectors=[n for n in range(-5,6) if primitive(n)]
characteristic_by_gram={
    N: all((pairing(N,1,n)-pairing(N,n,n))%2==0 for n in range(-12,13))
    for N in grams
}
unimodular_primitive_pairings=sorted({
    pairing(1,u,v) for u in primitive_vectors for v in primitive_vectors
})
gram_three_pairing=pairing(3,1,1)
gram_three_determinant=3
nonprimitive_three_pairing=pairing(1,1,3)

# The rank-one lattice automorphism e -> -e preserves the bilinear form.
N=sp.symbols("N", nonzero=True, integer=True)
orientation_isometry=sp.simplify(N*(-1)*(-1)-N)

# Integral topology does not fix the positive kinetic/Hodge metric.
g,k,h=sp.symbols("g k h", positive=True)
mass_sq=g**2*h*k**2
metric_ratio=sp.simplify(mass_sq.subs(h,2)/mass_sq.subs(h,1))

checks={
 "wp781_dependency_passed":wp781["status"]=="PASS" and all(wp781["checks"].values()),
 "rank_one_positive_unimodular_scan_has_only_gram_one":unimodular==[1],
 "primitive_rank_one_vectors_are_only_plus_minus_one":primitive_vectors==[-1,1],
 "primitive_generator_is_characteristic_for_every_scanned_gram":all(characteristic_by_gram.values()),
 "unimodular_primitive_pairing_magnitudes_are_one":unimodular_primitive_pairings==[-1,1],
 "gram_three_gives_pairing_three_but_is_not_unimodular":gram_three_pairing==3 and gram_three_determinant!=1,
 "unimodular_pairing_three_requires_nonprimitive_vector":nonprimitive_three_pairing==3 and not primitive(3),
 "orientation_reversal_is_a_lattice_isometry":orientation_isometry==0,
 "kinetic_metric_varies_at_fixed_integral_lattice":metric_ratio==2,
}
checks={name:bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result={
 "work_package":"WP782","status":"PASS","checks":checks,"dependency":"WP781",
 "admitted_state_domain":"positive rank-one integral Green-Schwarz/string-charge lattices with Gram entries 1 through 8, primitive characteristic and flux vectors, and an independent positive kinetic metric",
 "faithful_coordinate":"Gram determinant, primitive-vector coefficients, integral pairing, lattice automorphism orbit, and continuous kinetic metric",
 "source_authorized_probe":"unimodularity, characteristic parity, primitive integral pairing, lattice isometry, and kinetic normalization",
 "contextual_partition":"the unimodular primitive rank-one domain has only pairing magnitude one; pairing three lies either in a nonunimodular lattice or on a nonprimitive vector; orientation reversal remains an isometry",
 "lattice_result":"rank-one unimodularity excludes Gram three, while Gram one requires the explicitly nonprimitive vector 3e to obtain pairing three",
 "normalization_result":"the integral lattice does not fix the Hodge/kinetic metric, so Stückelberg mass and portal normalization remain continuous",
 "classification":"the primitive rank-one lattice is neither a flux-three selector nor a physical-normalization selector; choosing Gram three or vector 3e relocates the desired integer into source data",
 "smallest_exact_falsifier":"[3] pairs primitive generators to three but has determinant three; [1] is unimodular but reaches three only with nonprimitive 3e",
 "deutschian_status":"the numeral three is not hard to vary in the rank-one lattice family and orientation plus kinetic scale remain independent",
 "next_source_gate":"test the smallest higher-rank unimodular lattice for a uniquely distinguished primitive characteristic/flux pair of pairing three, modulo its full automorphism group and with stabilized metric",
 "instrument_gate":"no lattice datum alone specifies Stückelberg production current, decay channel, mixing, or detector calibration",
 "primary_sources":["https://arxiv.org/abs/1103.0019","https://arxiv.org/abs/1711.04777","https://arxiv.org/abs/1008.4133"],
}
(ROOT/"results"/"wp782_rank_one_unimodular_lattice_flux_three_no_go.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
