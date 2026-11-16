"""Cross-root evidence isolation and source-owned output regression tests."""
import json
from collections import Counter

from rdflib import Graph, Literal, RDF, URIRef
from provenance import ROOT, REFERENCE, import_reference, verify_sources, read_artifact
from validation_tests import EX, ISO, SH


def run(check, shapes, base, derive_readouts):
    tests = []
    candidate_path = "research/strominger/results/reference-ne22-search/D4-verification.json"
    raw, digest = read_artifact(ROOT, candidate_path)
    witness = json.loads(raw)["witness"]
    counts = dict(Counter(body["species"] for body in witness["bodies"]))
    packet_ids = {packet["id"] for packet in witness["packets"]}
    endpoints_resolve = all(op["source"] in packet_ids and op["target"] in packet_ids for op in witness["operations"])
    inspection = {"reference": candidate_path, "sha256": digest,
                  "status": "inspected-not-generator-replayed", "body_counts": counts,
                  "packet_count": len(packet_ids), "operation_count": len(witness["operations"]),
                  "operation_endpoints_resolve": endpoints_resolve,
                  "operation_kinds": sorted({op["kind"] for op in witness["operations"]}),
                  "operations_with_color": sum("color" in op for op in witness["operations"]),
                  "scope": "Saved Ne-22 finite-reader candidate, not the Ne-20 drawing. Packet IDs are reader states, not spatial vertices. No constructor, source dependency pins, or physical claims revalidated."}
    (base / "results" / "native-source-inspection.json").write_text(json.dumps(inspection, indent=2) + "\n", encoding="utf-8")
    tests.append({"name": "actual saved native candidate has resolvable packet endpoints and explicit body species",
                  "pass": counts == {"proton": 10, "neutron": 12, "electron": 10}
                  and len(packet_ids) == len(witness["packets"]) and endpoints_resolve})
    native, mapping = import_reference(ROOT, REFERENCE, "Neon-20")
    output = URIRef(mapping["output"])
    source = native.value(output, ISO.source)
    nucleus = native.value(output, ISO.nucleus)

    def copy():
        graph = Graph()
        for triple in native:
            graph.add(triple)
        return graph

    def reject(name, graph):
        before = set(graph)
        conforms, report, _ = check(graph, shapes)
        codes = set(report.objects(None, ISO.sourceErrorCode)) if report is not None else set()
        tests.append({"name": name, "pass": not conforms and Literal("replay-mismatch") in codes and before == set(graph)})

    graph = copy()
    graph.add((EX.extra, RDF.type, ISO.Vertex))
    graph.add((EX.extra, ISO.source, source))
    reject("unlisted source-owned record cannot hide outside the replayed root", graph)

    graph = copy()
    fixture_source = EX.wrapperSource
    attribution = [
        (fixture_source, RDF.type, ISO.Source), (fixture_source, ISO.sourceKind, Literal("fixture")),
        (fixture_source, ISO.description, Literal("Authored wrapper for a cross-root evidence test; not a derived output.")),
        (fixture_source, ISO.reference, Literal("research/strominger/isotope-schema/fixtures/inventory.ttl")),
    ]
    for triple in attribution:
        graph.add(triple)
    proton = next(graph.objects(nucleus, ISO.proton))
    graph.set((proton, ISO.source, fixture_source))
    reject("reassigning a derived child's source cannot remove it from replay scope", graph)

    # Sharing an existing nucleus adds only incoming links to native output.
    # It is an authored wrapper, not another result of the native operation.
    graph = copy()
    for triple in attribution + [
        (EX.wrapper, RDF.type, ISO.IsotopeStructure), (EX.wrapper, ISO.source, fixture_source),
        (EX.wrapper, ISO.profile, ISO.InventoryProfile), (EX.wrapper, ISO.bindingScope, ISO.NoBindings),
        (EX.wrapper, ISO.nucleus, nucleus),
    ]:
        graph.add(triple)
    before = set(graph)
    conforms, _, _ = check(graph, shapes)
    receipt = verify_sources(graph)
    scopes = {item["structure"]: item for item in receipt["structures"]}
    own, wrapper = scopes[str(output)], scopes[str(EX.wrapper)]
    tests.append({"name": "mixed-root replay evidence stays attached to the exact operation output",
                  "pass": bool(conforms) and own["root_evidence"] == "operation-replayed"
                  and wrapper["root_evidence"] == "attribution-only" and wrapper["root_source"] == str(fixture_source)
                  and len(receipt["replayed_outputs"]) == 1 and before == set(graph)})
    tests.append({"name": "shared records are disclosed without inventing exclusive ownership",
                  "pass": own["shared_records"] == wrapper["shared_records"]
                  and str(nucleus) in own["shared_records"] and len(own["shared_records"]) == 21
                  and len(wrapper["record_sources"]) == 2})
    readouts = derive_readouts(graph, shapes)
    tests.append({"name": "mixed-root readouts enumerate both roots without certifying the wrapper",
                  "pass": len(readouts) == 2 and readouts[str(output)] == readouts[str(EX.wrapper)]
                  and readouts[str(output)]["Z"] == 10 and readouts[str(output)]["N"] == 10})

    # Taking over the native output's namespace must fail even if the count is
    # unchanged and the replacement uses a separately resolvable attribution.
    graph.set((output, ISO.source, fixture_source))
    reject("reassigning the output root cannot evade replay through incoming metadata", graph)
    return tests
