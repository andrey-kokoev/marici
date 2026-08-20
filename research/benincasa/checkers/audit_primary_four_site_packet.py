"""Audit whether arXiv:2408.16386 freezes an explicit four-site integrand packet."""
import hashlib
import io
import json
import tarfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/primary-four-site-packet-audit.json"
URL = "https://export.arxiv.org/e-print/2408.16386"

archive = urllib.request.urlopen(URL, timeout=30).read()
with tarfile.open(fileobj=io.BytesIO(archive), mode="r:*") as tf:
    tex = {}
    for member in tf.getmembers():
        if member.isfile() and member.name.endswith(".tex"):
            handle = tf.extractfile(member)
            if handle is not None:
                tex[member.name] = handle.read().decode("utf-8", errors="replace")

applications = tex["sections/applications.tex"]
cosmological = tex["sections/cosmologicalintegrals.tex"]

assert "One-loop two-site graph" in applications
assert "One-loop three-site graph" in applications
assert "One-loop four-site graph" not in applications
assert "four-site" not in applications.lower()
assert "for each subgraph" in cosmological
assert "q_{\\mathfrak{g}}" in cosmological
assert "canonical function" in cosmological.lower()

packet = {
    "schema": "marici.benincasa.primary_four_site_packet_audit.v1",
    "source": "arXiv:2408.16386",
    "source_archive_sha256": hashlib.sha256(archive).hexdigest(),
    "explicit_application_sections": ["one-loop two-site", "one-loop three-site"],
    "explicit_four_site_application": False,
    "general_source_objects_present": [
        "one linear q_g for each subgraph",
        "canonical-function numerator and facet arrangement",
        "signed-triangulation formalism",
    ],
    "missing_frozen_datum": "an explicit four-site signed triangulation term and its simultaneous labelled denominator subset",
    "upstream_primary_sources": [
        "arXiv:1709.02813 (cosmological-polytope canonical function)",
        "arXiv:2112.09028 (physical/adjoint triangulations)",
        "arXiv:2005.03612 (polytope subdivisions/covariant forms)",
    ],
    "classification": "carrier arrangement derivable; physical four-site term not frozen by the target paper",
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
