"""Executable PDF-ensemble reach audit for the WP462 production portal."""

import hashlib
import json
import os
import tarfile
import tempfile
import urllib.request
from pathlib import Path

import numpy as np
import sympy as sp
from parton import PLumi, mkPDF


root = Path(__file__).resolve().parents[1]
wp461 = json.loads(
    (root / "results" / "wp461_kaon_conditioned_pole_width_reach.json").read_text(
        encoding="utf-8"
    )
)
wp462 = json.loads(
    (root / "results" / "wp462_positive_production_rate_portal.json").read_text(
        encoding="utf-8"
    )
)

pdf_set = "NNPDF23_lo_as_0130_qed"
pdf_url = f"https://lhapdfsets.web.cern.ch/current/{pdf_set}.tar.gz"
pdf_sha256 = "60d3c1df1c31e5840f91f4217163ae30a256b9291a5adc894882e86607ef5d63"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def prepare_pdf_root():
    supplied = os.environ.get("WP463_PDF_ROOT")
    if supplied:
        pdf_root = Path(supplied)
        archive = pdf_root / f"{pdf_set}.tar.gz"
        if sha256(archive) != pdf_sha256:
            raise RuntimeError("Supplied PDF archive digest mismatch")
        return pdf_root, None

    temporary = tempfile.TemporaryDirectory(prefix="wp463-pdfs-")
    pdf_root = Path(temporary.name)
    archive = pdf_root / f"{pdf_set}.tar.gz"
    urllib.request.urlretrieve(pdf_url, archive)
    if sha256(archive) != pdf_sha256:
        raise RuntimeError("Downloaded PDF archive digest mismatch")
    with tarfile.open(archive, "r:gz") as bundle:
        bundle.extractall(pdf_root, filter="data")
    return pdf_root, temporary


pdf_root, temporary_owner = prepare_pdf_root()
m_gev = 5000.0
sqrt_s_gev = 13000.0
tau = (m_gev / sqrt_s_gev) ** 2
ordered_channels = [(1, -3), (-3, 1), (3, -1), (-1, 3)]

luminosities = []
for member in range(101):
    pdf = mkPDF(pdf_set, member, pdfdir=pdf_root)
    luminosity = PLumi(pdf, Q2=m_gev**2)
    luminosities.append(
        sum(float(luminosity.L(p1, p2, tau)) for p1, p2 in ordered_channels)
    )
luminosities = np.asarray(luminosities)

central_luminosity = float(luminosities[0])
replica_mean = float(np.mean(luminosities[1:]))
replica_standard_deviation = float(np.std(luminosities[1:], ddof=1))
replica_minimum = float(np.min(luminosities[1:]))
replica_maximum = float(np.max(luminosities[1:]))

g_squared_max = sp.sympify(
    wp461["conditional_working_limits"]["g_F_max"]
) ** 2
gev_squared_to_pb = sp.Float("389379365.6")
integrated_luminosity_fb = sp.Integer(139)
hadronic_s_gev_squared = sp.Integer(13000) ** 2


def cross_section_fb(luminosity):
    return sp.N(
        sp.pi
        * g_squared_max
        * sp.Float(str(luminosity))
        / (4 * hadronic_s_gev_squared)
        * gev_squared_to_pb
        * 1000,
        18,
    )


central_cross_section_fb = cross_section_fb(central_luminosity)
maximum_cross_section_fb = cross_section_fb(replica_maximum)
central_events = sp.N(central_cross_section_fb * integrated_luminosity_fb, 18)
maximum_events = sp.N(maximum_cross_section_fb * integrated_luminosity_fb, 18)
optimistic_atlas_limit_fb = sp.Rational(8, 100)
limit_gap = sp.N(optimistic_atlas_limit_fb / maximum_cross_section_fb, 18)

checks = {
    "wp461_dependency_passed": wp461["passed"],
    "wp462_dependency_passed": wp462["passed"],
    "pdf_archive_digest_verified": sha256(pdf_root / f"{pdf_set}.tar.gz")
    == pdf_sha256,
    "all_101_pdf_members_evaluated": len(luminosities) == 101,
    "all_source_channel_luminosities_positive": bool(np.all(luminosities > 0)),
    "central_luminosity_deterministic": abs(
        central_luminosity - 0.0011785691192713744
    )
    < 1e-15,
    "maximum_replica_luminosity_deterministic": abs(
        replica_maximum - 0.006117350025077182
    )
    < 1e-15,
    "maximum_replica_event_ceiling_below_one": maximum_events < 1,
    "maximum_replica_event_ceiling_below_two_thousandths": maximum_events
    < sp.Rational(2, 1000),
    "source_rate_below_optimistic_atlas_limit": maximum_cross_section_fb
    < optimistic_atlas_limit_fb,
    "rate_gap_exceeds_eight_thousand": limit_gap > 8000,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP463",
    "runtime": {
        "parton": "0.2.2",
        "pdf_set": pdf_set,
        "archive_url": pdf_url,
        "archive_sha256": pdf_sha256,
        "members": 101,
    },
    "collider_domain": {
        "sqrt_s_GeV": sqrt_s_gev,
        "m_triplet_GeV": m_gev,
        "tau": tau,
        "factorization_scale_GeV": m_gev,
        "ordered_PDG_channels": ordered_channels,
        "integrated_luminosity_fb^-1": int(integrated_luminosity_fb),
        "acceptance_ceiling": 1,
    },
    "pdf_luminosity": {
        "central": central_luminosity,
        "replica_mean": replica_mean,
        "replica_standard_deviation": replica_standard_deviation,
        "replica_minimum": replica_minimum,
        "replica_maximum": replica_maximum,
    },
    "unit_acceptance_rate_ceiling": {
        "central_cross_section_fb": float(central_cross_section_fb),
        "maximum_replica_cross_section_fb": float(maximum_cross_section_fb),
        "central_produced_events": float(central_events),
        "maximum_replica_produced_events": float(maximum_events),
        "optimistic_ATLAS_generic_limit_fb": float(optimistic_atlas_limit_fb),
        "limit_to_source_rate_gap": float(limit_gap),
    },
    "contextual_partition": "The mathematical rate map separates positive g_F, but all kaon-allowed points are operationally background-only in the Run-2 finite-count domain.",
    "classification": "Negative Run-2 production-rate reach; neither selector nor rigidifier.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "instrument": "ATLAS inclusive dijet generic-rate class with official NNPDF2.3 LO source channels; source yield is far below one event before acceptance.",
    "smallest_exact_falsifier": "Any official PDF replica raises the unit-acceptance source yield to one event or the source cross section above 0.08 fb.",
    "remaining_gate": "A higher-energy/luminosity flavor-tagged collider with a source-specific likelihood; current Run-2 rate cannot identify g_F.",
    "sources": [
        "https://arxiv.org/abs/1910.08447",
        "https://lhapdfsets.web.cern.ch/current/NNPDF23_lo_as_0130_qed.tar.gz",
    ],
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp463_run2_production_rate_reach.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
