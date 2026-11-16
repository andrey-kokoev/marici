"""Validate the Ne-20 Turtle artifact and generate the editor's offline snapshot.

Run with pinned pySHACL/RDFLib dependencies. This does not edit any drawing.
The Node embedder/publisher checks byte freshness; it does not run SHACL.
"""
import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "research/strominger/isotope-schema"
sys.path.insert(0, str(SCHEMA))
from check import check, derive_readouts, load
from shape_bundle import load_shapes
from provenance import ISO, REFERENCE, OPERATION, verify_sources
from rdflib import RDF, URIRef

ARTIFACT = SCHEMA / "results/neon-20-inventory.ttl"
DESTINATION = ROOT / "examples/isotope-wiring/core/ne20-inventory.json"


def snapshot():
    data, shapes = load(ARTIFACT), load_shapes()
    conforms, _, report = check(data, shapes)
    if not conforms:
        raise ValueError(report)
    subject = URIRef("urn:marici:isotope-reference:Neon-20")
    if set(data.subjects(RDF.type, ISO.IsotopeStructure)) != {subject} or data.value(subject, ISO.profile) != ISO.InventoryProfile:
        raise ValueError("Expected only the Ne-20 inventory root")
    evidence = verify_sources(data)
    if len(evidence["replayed_outputs"]) != 1 or evidence["resolved_attributions"]:
        raise ValueError("Expected one replayed output, not attribution-only evidence")
    replay = evidence["replayed_outputs"][0]
    if replay["operation"] != str(OPERATION) or replay["key"] != "Neon-20" or replay["reference"] != REFERENCE:
        raise ValueError("Unexpected source operation or selector")
    counts = derive_readouts(data, shapes)[str(subject)]
    if counts != {"Z": 10, "N": 10, "A": 20, "electrons": None, "charge_e": None}:
        raise ValueError("Unexpected Ne-20 inventory readouts")
    paths = [*SCHEMA.glob("*.py"), *SCHEMA.glob("*.ttl"), ARTIFACT, ROOT / REFERENCE, Path(__file__).resolve()]
    inputs = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}
    raw = ARTIFACT.read_bytes()
    return {"schema": "marici.editor-turtle-inventory.v1", "definitionId": "Ne20", "subject": str(subject),
            "readouts": counts, "validation": "SHACL-and-source-replay-at-build-time",
            "versions": {p: importlib.metadata.version(p) for p in ("pyshacl", "rdflib")},
            "artifactPath": ARTIFACT.relative_to(ROOT).as_posix(), "turtleSha256": hashlib.sha256(raw).hexdigest(),
            "source": {"path": REFERENCE, "sha256": replay["input_sha256"], "operation": replay["operation"]},
            "inputs": inputs, "turtle": raw.decode("utf-8"),
            "scope": "Nuclear inventory only. Electronic state and charge unspecified; no drawing, placement or physical certification."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = json.dumps(snapshot(), ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    if args.check:
        if not DESTINATION.exists() or DESTINATION.read_bytes() != output.encode("utf-8"):
            raise SystemExit("Validated Turtle snapshot is stale; regenerate it")
    else:
        DESTINATION.write_bytes(output.encode("utf-8"))
    print("Validated Ne-20 inventory snapshot " + ("checked" if args.check else "generated"))
