"""Local artifact verification and explicitly bounded replayable operations.

Verifies reference inventory and freshly replayed native reader incidence,
NOT physical truth, upstream extraction, or a spatial isotope construction.
"""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote

from rdflib import Graph, Literal, Namespace, RDF, URIRef

ISO = Namespace("urn:marici:isotope:")
BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
REFERENCE = "research/matter/isotope-reference.resource.json"
OPERATION = ISO.ReferenceNuclearInventoryV1
DESCRIPTION = "Replayed nuclear-count projection from a pinned repository reference; no electrons, geometry, or physical certification."
MAX_BYTES = 4 * 1024 * 1024
MAX_CONSTITUENTS = 1000  # execution budget, not a physical limit


class SourceError(ValueError):
    def __init__(self, code, detail, source=None):
        super().__init__(f"{code}: {detail}")
        self.code, self.source = code, source


def read_artifact(root, reference):
    parts = reference.split("/")
    if (not reference or len(reference) > 4096 or "\\" in reference or ":" in reference
            or any(part in ("", ".", "..") for part in parts)):
        raise SourceError("unsafe-reference", "Expected a canonical repository-relative POSIX file path")
    root = Path(root).resolve()
    try:
        path = root.joinpath(*parts).resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise SourceError("missing-artifact", reference) from error
    if not path.is_relative_to(root):
        raise SourceError("outside-root", reference)
    if not path.is_file():
        raise SourceError("not-a-file", reference)
    try:
        with path.open("rb") as stream:
            raw = stream.read(MAX_BYTES + 1)
    except OSError as error:
        raise SourceError("artifact-unreadable", reference) from error
    if len(raw) > MAX_BYTES:
        raise SourceError("artifact-size-limit", reference)
    return raw, hashlib.sha256(raw).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise SourceError("duplicate-json-key", str(key))
        result[key] = value
    return result


def selected_record(raw, key):
    try:
        resource = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SourceError("invalid-json", "Input is not valid UTF-8 JSON") from error
    if not isinstance(resource, dict) or resource.get("profile") != "tabular-data-resource" or resource.get("name") != "isotope-reference":
        raise SourceError("unsupported-resource", "Expected the repository isotope-reference tabular resource")
    schema = resource.get("schema")
    if not isinstance(schema, dict) or not isinstance(schema.get("fields"), list):
        raise SourceError("invalid-resource-schema", "Missing field descriptors")
    fields = schema["fields"]
    if any(not isinstance(f, dict) or not isinstance(f.get("name"), str) for f in fields):
        raise SourceError("invalid-resource-schema", "Invalid field descriptor")
    names = [f["name"] for f in fields]
    if len(set(names)) != len(names) or not {"isotope", "protons", "neutrons"}.issubset(names):
        raise SourceError("invalid-resource-schema", "Fields must be unique and include isotope, protons, neutrons")
    rows = resource.get("data")
    if not isinstance(rows, list) or any(not isinstance(row, list) or len(row) != len(names) for row in rows):
        raise SourceError("invalid-resource-rows", "Rows must match declared field width")
    matches = [(i, dict(zip(names, row))) for i, row in enumerate(rows) if row[names.index("isotope")] == key]
    if len(matches) != 1:
        raise SourceError("record-selection", f"Expected one record for {key!r}, found {len(matches)}")
    row_index, record = matches[0]
    z, n = record["protons"], record["neutrons"]
    if type(z) is not int or type(n) is not int or z < 1 or n < 0:
        raise SourceError("invalid-counts", "Protons and neutrons must be integer counts with Z >= 1, N >= 0")
    if z + n > MAX_CONSTITUENTS:
        raise SourceError("count-budget", "Selected record exceeds this operation's allocation budget")
    match = re.fullmatch(r"[A-Za-z]+-([1-9][0-9]*)", key)
    if match is None or int(match.group(1)) != z + n:
        raise SourceError("mass-label-mismatch", "Selected isotope label must agree with Z + N")
    return row_index, record


def build_inventory(raw, reference, key, output=None, source=None, artifact=None):
    row_index, record = selected_record(raw, key)
    output = output or URIRef("urn:marici:isotope-reference:" + quote(key, safe=""))
    source = source or URIRef(str(output) + ":source")
    artifact = artifact or URIRef(str(output) + ":artifact")
    nucleus = URIRef(str(output) + ":nucleus")
    digest = hashlib.sha256(raw).hexdigest()
    graph = Graph()
    graph.bind("iso", ISO)
    triples = [
        (artifact, RDF.type, ISO.InputArtifact), (artifact, ISO.artifactPath, Literal(reference)),
        (artifact, ISO.sha256, Literal(digest)), (source, RDF.type, ISO.Source),
        (source, ISO.sourceKind, Literal("derived-input")), (source, ISO.reference, Literal(reference)),
        (source, ISO.description, Literal(DESCRIPTION)), (source, ISO.operation, OPERATION),
        (source, ISO.inputArtifact, artifact), (source, ISO.outputStructure, output), (source, ISO.recordKey, Literal(key)),
        (output, RDF.type, ISO.IsotopeStructure), (output, ISO.source, source), (output, ISO.isotopeName, Literal(key)),
        (output, ISO.profile, ISO.InventoryProfile), (output, ISO.bindingScope, ISO.NoBindings), (output, ISO.nucleus, nucleus),
        (nucleus, RDF.type, ISO.Nucleus), (nucleus, ISO.source, source),
    ]
    mapping = {}
    for kind, count in (("proton", record["protons"]), ("neutron", record["neutrons"])):
        nodes = [URIRef(f"{output}:{kind}:{i}") for i in range(count)]
        mapping[kind] = [str(node) for node in nodes]
        for node in nodes:
            triples.extend([(nucleus, ISO[kind], node), (node, RDF.type, ISO[kind.capitalize()]), (node, ISO.source, source)])
    for triple in triples:
        graph.add(triple)
    return graph, {"key": key, "row_index": row_index, "projected_fields": ["isotope", "protons", "neutrons"],
                   "Z": record["protons"], "N": record["neutrons"], "input_sha256": digest,
                   "output": str(output), "operation": str(OPERATION), "constituent_slots": mapping,
                   "scope": "Count expansion into nominal inventory slots; no physical particle identities, electronic state or topology inferred."}


def import_reference(root, reference, key):
    raw, _ = read_artifact(root, reference)
    return build_inventory(raw, reference, key)


def one(graph, subject, predicate):
    values = list(graph.objects(subject, predicate))
    if len(values) != 1:
        raise SourceError("source-cardinality", f"{subject} needs one {predicate}", subject)
    return values[0]


def structure_evidence(data, replayed):
    """Report evidence per root, without treating shared records as derivations.

    Follow record-valued outgoing links, not source/artifact metadata. Sharing
    is disclosed rather than forbidden: an incoming link is not a new output
    of an operation and does not inherit that operation's root evidence.
    """
    roots = sorted(set(data.subjects(RDF.type, ISO.IsotopeStructure)), key=str)
    records = set(data.subjects(ISO.source, None))
    closures = {}
    for root in roots:
        visited, pending = set(), [root]
        while pending:
            subject = pending.pop()
            if subject in visited:
                continue
            visited.add(subject)
            pending.extend(obj for obj in data.objects(subject, None) if obj in records and obj not in visited)
        closures[root] = visited
    replay_roots = {item["output"]: item["source"] for item in replayed}
    reports = []
    for root in roots:
        source = one(data, root, ISO.source)
        members = closures[root]
        shared = members & set().union(*(v for r, v in closures.items() if r != root))
        sources = {}
        for member in members:
            member_source = str(one(data, member, ISO.source))
            sources[member_source] = sources.get(member_source, 0) + 1
        reports.append({"structure": str(root), "profile": str(one(data, root, ISO.profile)),
                        "root_source": str(source),
                        "root_evidence": "operation-replayed" if replay_roots.get(str(root)) == str(source) else "attribution-only",
                        "record_count": len(members), "record_sources": dict(sorted(sources.items())),
                        "shared_records": sorted(map(str, shared))})
    return reports


def verify_sources(data, root=ROOT):
    # The application enumerates explicit records, never inferred subclasses.
    # Refuse untyped references even when this helper is called without SHACL.
    referenced = set(data.objects(None, ISO.source))
    declared = set(data.subjects(RDF.type, ISO.Source))
    if referenced - declared:
        source = sorted(referenced - declared, key=str)[0]
        raise SourceError("untyped-source-reference", str(source), source)
    artifacts = {}
    for artifact in sorted(data.subjects(RDF.type, ISO.InputArtifact), key=str):
        reference = str(one(data, artifact, ISO.artifactPath))
        pin = str(one(data, artifact, ISO.sha256))
        try:
            raw, digest = read_artifact(root, reference)
        except SourceError as error:
            error.source = artifact
            raise
        if not re.fullmatch(r"[0-9a-f]{64}", pin) or pin != digest:
            raise SourceError("digest-mismatch", reference, artifact)
        artifacts[artifact] = (reference, raw, digest)
    resolved, replayed = [], []
    for source in sorted(data.subjects(RDF.type, ISO.Source), key=str):
        kind = str(one(data, source, ISO.sourceKind))
        reference = str(one(data, source, ISO.reference))
        if kind in ("fixture", "operator-input"):
            try:
                _, digest = read_artifact(root, reference)
            except SourceError as error:
                error.source = source
                raise
            resolved.append({"source": str(source), "reference": reference, "observed_sha256": digest,
                             "status": "reference-resolved-not-derived"})
            continue
        if kind != "derived-input":
            raise SourceError("unsupported-source-kind", kind, source)
        operation = one(data, source, ISO.operation)
        if operation not in (OPERATION, ISO.NativeReaderIncidenceV1):
            raise SourceError("unsupported-operation", str(operation), source)
        artifact = one(data, source, ISO.inputArtifact)
        if artifact not in artifacts:
            raise SourceError("missing-input-artifact", str(artifact), source)
        input_reference, raw, digest = artifacts[artifact]
        if reference != input_reference:
            raise SourceError("reference-disagreement", reference, source)
        key = str(one(data, source, ISO.recordKey))
        output = one(data, source, ISO.outputStructure)
        try:
            if operation == OPERATION:
                expected, receipt = build_inventory(raw, reference, key, output, source, artifact)
            else:
                from native_projection import NATIVE_MANIFEST, build_native, replay_native
                dependency = one(data, source, ISO.dependencyArtifact)
                if dependency not in artifacts or artifacts[dependency][0] != NATIVE_MANIFEST:
                    raise SourceError("native-dependency-artifact", "Missing native dependency manifest", source)
                dependency_raw = artifacts[dependency][1]
                native_receipt = replay_native(root, reference, raw, dependency_raw)
                expected = build_native(raw, reference, dependency_raw, key, output, source, artifact, dependency)
                receipt = {"key": key, "output": str(output), "operation": str(operation),
                           "input_sha256": digest, "native_replay": native_receipt,
                           "scope": "Native finite-reader incidence and body assignment only; not spatial vertices, colored arrows or complete geometry."}
        except SourceError as error:
            error.source = source
            raise
        expected_subjects = set(expected.subjects())
        actual_subjects = set(data.subjects(ISO.source, source)) | {source, artifact}
        # Include expected subjects even if the output's source link was removed
        # or reassigned. Compare every outgoing triple, not just particle counts.
        subjects = expected_subjects | actual_subjects
        actual = {triple for subject in subjects for triple in data.triples((subject, None, None))}
        if actual != set(expected):
            raise SourceError("replay-mismatch", f"{output}: missing {len(set(expected) - actual)} triples, extra {len(actual - set(expected))}", source)
        replayed.append({**receipt, "source": str(source), "reference": reference,
                         "status": "operation-replayed", "output_triples": len(expected)})
    return {"resolved_attributions": resolved, "replayed_outputs": replayed,
            "structures": structure_evidence(data, replayed),
            "scope": "Local file resolution and explicitly supported operation replay only; no upstream extraction or physical truth certification."}
