"""Faithful incidence projection of freshly replayed native reader records.

Reader states are NOT spatial vertices; transitions are NOT colored arrows.
Permutations, geometry and construction prefixes remain in the pinned input,
checked by the constructor replay but not projected into this incidence view.
"""
import hashlib
import json
import math
from pathlib import Path
import subprocess
from rdflib import Graph, Literal, RDF, URIRef
from provenance import BASE, ROOT, ISO, SourceError, read_artifact, unique_object

NATIVE_OPERATION = ISO.NativeReaderIncidenceV1
NATIVE_REFERENCE = "research/strominger/results/reference-ne22-search/D4-verification.json"
NATIVE_MANIFEST = "research/strominger/results/reference-ne22-search/verification.json"
KEY = "Neon-22-D4"
DESCRIPTION = "Freshly replayed native Ne-22 finite-reader incidence projection; not spatial vertices, colored arrows, physical certification or a complete isotope diagram."


def replay_native(root, reference, raw, dependency_raw):
    try:
        result = subprocess.run(["node", str(BASE / "native_replay.mjs"), str(Path(root).resolve() / reference)],
                                cwd=ROOT, capture_output=True, text=True, timeout=180, check=False)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SourceError("native-runtime-unavailable", str(error)) from error
    try:
        receipt = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise SourceError("native-runtime-error", result.stderr[-1000:]) from error
    if result.returncode or receipt.get("status") != "native-generator-replayed":
        raise SourceError("native-replay-failed", json.dumps(receipt))
    if receipt["witnessSha256"] != hashlib.sha256(raw).hexdigest() or receipt["manifestSha256"] != hashlib.sha256(dependency_raw).hexdigest():
        raise SourceError("native-input-disagreement", "Replay bytes differ from pinned artifacts")
    return receipt


def build_native(raw, reference, dependency_raw, key=KEY, output=None, source=None, artifact=None, dependency=None):
    if key != KEY:
        raise SourceError("unsupported-native-selector", key)
    try:
        witness = json.loads(raw, object_pairs_hook=unique_object)["witness"]
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SourceError("invalid-native-json", "Expected valid UTF-8 JSON") from error
    # JSON's numeric spelling is not identity: the JS constructor treats 0 and
    # 0.0 as the same integer. Canonicalize only integral projected fields.
    for rows, fields in [(witness["packets"], ("id", "origin", "chart")),
                         (witness["charts"], ("cell",)), (witness["bodies"], ("cell",)),
                         (witness["operations"], ("id", "source", "target", "phaseDelta"))]:
        for row in rows:
            for field in fields:
                value = row[field]
                if type(value) not in (int, float) or (type(value) is float and not math.isfinite(value)) or int(value) != value:
                    raise SourceError("native-field-type", f"Expected integral {field}")
                row[field] = int(value)
    output = output or URIRef("urn:marici:native-reader:Neon-22:D4")
    source = source or URIRef(f"{output}:source")
    artifact = artifact or URIRef(f"{output}:artifact")
    dependency = dependency or URIRef(f"{output}:dependencies")
    graph = Graph()
    graph.bind("iso", ISO)
    def add(s, p, o):
        graph.add((s, p, o))
    def record(node, kind):
        add(node, RDF.type, kind); add(node, ISO.source, source)
    for node, path, content in [(artifact, reference, raw), (dependency, NATIVE_MANIFEST, dependency_raw)]:
        add(node, RDF.type, ISO.InputArtifact)
        add(node, ISO.artifactPath, Literal(path))
        add(node, ISO.sha256, Literal(hashlib.sha256(content).hexdigest()))
    add(source, RDF.type, ISO.Source)
    for predicate, value in [(ISO.sourceKind, Literal("derived-input")), (ISO.reference, Literal(reference)),
                             (ISO.description, Literal(DESCRIPTION)), (ISO.operation, NATIVE_OPERATION),
                             (ISO.inputArtifact, artifact), (ISO.dependencyArtifact, dependency),
                             (ISO.recordKey, Literal(key)), (ISO.outputStructure, output)]:
        add(source, predicate, value)
    record(output, ISO.IsotopeStructure)
    add(output, ISO.isotopeName, Literal("Neon-22"))
    add(output, ISO.profile, ISO.PartialStructureProfile)
    add(output, ISO.bindingScope, ISO.TotalBindings)
    nucleus, electronic = URIRef(f"{output}:nucleus"), URIRef(f"{output}:electrons")
    record(nucleus, ISO.Nucleus); record(electronic, ISO.ElectronicState)
    add(output, ISO.nucleus, nucleus); add(output, ISO.electronicState, electronic)
    bodies = {}
    for body in witness["bodies"]:
        node = URIRef(f"{output}:body:{body['cell']}")
        bodies[body["cell"]] = node
        record(node, ISO[body["species"].capitalize()])
        add(electronic if body["species"] == "electron" else nucleus, ISO[body["species"]], node)
    charts = {chart["id"]: chart for chart in witness["charts"]}
    for packet in witness["packets"]:
        state = URIRef(f"{output}:reader:{packet['id']}")
        chart = charts[f"chart-{packet['chart']}"]
        body = bodies[chart["cell"]]
        record(state, ISO.ReaderState); add(output, ISO.readerState, state)
        for predicate, value in [(ISO.nativeId, Literal(packet["id"])), (ISO.readerChart, Literal(chart["id"])),
                                 (ISO.origin, Literal(packet["origin"])), (ISO.readerBody, body)]:
            add(state, predicate, value)
        binding = URIRef(f"{output}:binding:{packet['id']}")
        record(binding, ISO.Interpretation); add(output, ISO.interpretation, binding)
        add(binding, ISO.particle, body); add(binding, ISO.role, state)
    for operation in witness["operations"]:
        transition = URIRef(f"{output}:transition:{operation['id']}")
        record(transition, ISO.ReaderTransition); add(output, ISO.readerTransition, transition)
        for predicate, value in [(ISO.nativeId, Literal(operation["id"])), (ISO.transitionKind, Literal(operation["kind"])),
                                 (ISO.phaseDelta, Literal(operation["phaseDelta"])),
                                 (ISO.fromReader, URIRef(f"{output}:reader:{operation['source']}")),
                                 (ISO.toReader, URIRef(f"{output}:reader:{operation['target']}"))]:
            add(transition, predicate, value)
    return graph


def import_native(root=ROOT):
    raw, _ = read_artifact(root, NATIVE_REFERENCE)
    dependencies, _ = read_artifact(root, NATIVE_MANIFEST)
    receipt = replay_native(root, NATIVE_REFERENCE, raw, dependencies)
    return build_native(raw, NATIVE_REFERENCE, dependencies), receipt
