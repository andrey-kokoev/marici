"""Bounded primary-literature census for the WP522 H_0 instrument."""

import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp511 = load("wp511_neutral_b_current_instrument.json")
wp522 = load("wp522_six_resolvent_bilocal_basis.json")

# Frozen primary-source abstract census.  The classification records only what
# each cited source explicitly advertises in its abstract; it is not an
# inference that the wider literature contains no other construction.
sources = [
    {
        "arxiv": "1907.01025",
        "url": "https://arxiv.org/abs/1907.01025",
        "title": "Neutral B-meson mixing from full lattice QCD at the physical point",
        "meson": "B",
        "operator_scope": "local",
        "reported_object": "bag parameters for five local mixing operators",
        "calibrated_h0": False,
    },
    {
        "arxiv": "1602.03560",
        "url": "https://arxiv.org/abs/1602.03560",
        "title": "B0_(s)-mixing matrix elements from lattice QCD for the Standard Model and beyond",
        "meson": "B",
        "operator_scope": "local",
        "reported_object": "matrix elements and correlations for five local operators",
        "calibrated_h0": False,
    },
    {
        "arxiv": "1311.6820",
        "url": "https://arxiv.org/abs/1311.6820",
        "title": "Matrix Elements for D- and B-Mixing from 2+1 Flavor Lattice QCD",
        "meson": "B",
        "operator_scope": "local",
        "reported_object": "complete five-local-operator B-mixing basis",
        "calibrated_h0": False,
    },
    {
        "arxiv": "2111.11287",
        "url": "https://arxiv.org/abs/2111.11287",
        "title": "BSM B-Bbar mixing on JLQCD and RBC/UKQCD ensembles",
        "meson": "B",
        "operator_scope": "local",
        "reported_object": "bag parameters from the five-operator basis",
        "calibrated_h0": False,
    },
    {
        "arxiv": "1012.6034",
        "url": "https://arxiv.org/abs/1012.6034",
        "title": "Long-distance contributions to weak amplitudes",
        "meson": "K",
        "operator_scope": "bilocal",
        "reported_object": "space-time integrated product of two DeltaS=1 weak operators",
        "calibrated_h0": False,
    },
    {
        "arxiv": "1201.2065",
        "url": "https://arxiv.org/abs/1201.2065",
        "title": "Computing the long-distance contribution to epsilon_K",
        "meson": "K",
        "operator_scope": "bilocal",
        "reported_object": "lattice method for long-distance kaon mixing",
        "calibrated_h0": False,
    },
]

b_sources = [source for source in sources if source["meson"] == "B"]
k_bilocal_sources = [
    source
    for source in sources
    if source["meson"] == "K" and source["operator_scope"] == "bilocal"
]
h0_sources = [source for source in sources if source["calibrated_h0"]]
urls = [source["url"] for source in sources]

checks = {
    "wp511_dependency_passed": bool(wp511["passed"]),
    "wp522_dependency_passed": bool(wp522["passed"]),
    "census_contains_at_least_four_primary_b_sources": len(b_sources) >= 4,
    "every_b_source_in_census_is_local_operator_scope": bool(
        all(source["operator_scope"] == "local" for source in b_sources)
    ),
    "census_contains_bilocal_kaon_precedent": len(k_bilocal_sources) >= 2,
    "no_censused_source_reports_calibrated_wp522_h0": len(h0_sources) == 0,
    "all_primary_urls_are_unique_arxiv_records": bool(
        len(urls) == len(set(urls))
        and all(url.startswith("https://arxiv.org/abs/") for url in urls)
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP523",
    "search_scope": {
        "date": "2026-08-26",
        "sources": "Primary arXiv records returned by bounded searches for neutral-B bilocal mixing, light-mediator mixing, and lattice bilocal meson methods.",
        "authority_limit": "This is a bounded census, not a proof that no H_0 calculation exists anywhere.",
    },
    "primary_source_census": sources,
    "classification": "Existing censused neutral-B lattice instruments are local-operator instruments. Bilocal lattice methods exist in kaon mixing, so methodology is transferable in principle, but no censused source supplies the calibrated WP522 H_0 B_s matrix element.",
    "selector": False,
    "rigidifier": False,
    "instrument": "WP511 plus local lattice bag parameters remains valid on the local WET packet. The WP522 H_0 source packet has no realized instrument in this bounded census.",
    "smallest_exact_falsifier": "One primary neutral-B source in the frozen census explicitly reports the resolvent-weighted H_0 matrix element with its normalization, renormalization, continuum limit, and covariance.",
    "remaining_gate": "Adapt the established bilocal integrated-correlator lattice methodology to B_s with the exact WP522 kernel D^-1, then provide renormalization, threshold matching, continuum/volume limits, and a covariance usable by the DeltaM_s likelihood.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp523_h0_instrument_census.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
