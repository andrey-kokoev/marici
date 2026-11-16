"""Actual reference imports and source/output tampering controls."""
import copy
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from rdflib import Graph, Literal, RDF, URIRef
from provenance import ROOT, REFERENCE, OPERATION, SourceError, build_inventory, import_reference, read_artifact, verify_sources
from validation_tests import EX, ISO, SH, expectation, matches


def clone(graph):
    result = Graph()
    for triple in graph:
        result.add(triple)
    return result


def run(check, shapes, base, derive_readouts):
    tests = []
    for key, z, n in [("Hydrogen-1", 1, 0), ("Neon-20", 10, 10), ("Calcium-46", 20, 26)]:
        data, mapping = import_reference(ROOT, REFERENCE, key)
        before = set(data)
        conforms, _, text = check(data, shapes)
        output = URIRef(mapping["output"])
        nucleus = data.value(output, ISO.nucleus)
        actual = {"Z": len(set(data.objects(nucleus, ISO.proton))), "N": len(set(data.objects(nucleus, ISO.neutron)))}
        no_invented_structure = not any(data.objects(output, ISO.vertex)) and not any(data.objects(output, ISO.electronicState))
        readout = derive_readouts(data, shapes)[str(output)] if conforms else None
        expected = {"Z": z, "N": n, "A": z + n, "electrons": None, "charge_e": None}
        passed = conforms and actual == {"Z": z, "N": n} and readout == expected and no_invented_structure and before == set(data)
        tests.append({"name": f"actual reference import and replay: {key}", "expected": expected,
                      "actual": readout, "input_sha256": mapping["input_sha256"], "pass": bool(passed)})
        if not passed:
            print(text)
        if key == "Neon-20" and passed:
            output_dir = base / "results"
            output_dir.mkdir(exist_ok=True)
            ttl = output_dir / "neon-20-inventory.ttl"
            ttl.write_bytes(data.serialize(format="turtle", encoding="utf-8"))
            receipt = verify_sources(data)
            receipt["serialized_output_sha256"] = hashlib.sha256(ttl.read_bytes()).hexdigest()
            (output_dir / "neon-20-source-replay.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
            parsed = Graph().parse(ttl, format="turtle")
            conforms_again, _, _ = check(parsed, shapes)
            tests.append({"name": "actual imported Turtle roundtrip preserves every triple and replays", "pass": conforms_again and set(parsed) == set(data)})

    # Deliberately relabel the old attribution-only fixture as derived. It must
    # fail the declared metadata constraint before attempting any operation.
    data = Graph().parse(base / "fixtures" / "valid.ttl", format="turtle")
    data.set((EX.source, ISO.sourceKind, Literal("derived-input")))
    conforms, report, _ = check(data, shapes)
    spec = expectation("SPARQL", "SourcePayloadShape", constraint=ISO.SourceDerivationPayloadConstraint)
    tests.append({"name": "derived label plus arbitrary reference is not a derivation",
                  "pass": not conforms and matches(report, shapes, EX.source, spec)})

    raw, _ = read_artifact(ROOT, REFERENCE)
    resource = json.loads(raw)
    with TemporaryDirectory(prefix="marici-isotope-provenance-") as temporary:
        root = Path(temporary)
        file = root / "reference.json"
        file.write_bytes(raw)
        baseline, mapping = build_inventory(raw, "reference.json", "Neon-20")
        output = URIRef(mapping["output"])
        source = baseline.value(output, ISO.source)
        artifact = baseline.value(source, ISO.inputArtifact)
        nucleus = baseline.value(output, ISO.nucleus)

        def rejection(name, code, edit=None, input_bytes=raw):
            file.write_bytes(input_bytes)
            data = clone(baseline)
            if edit:
                edit(data)
            before, before_shapes = set(data), set(shapes)
            conforms, report, text = check(data, shapes, repository_root=root)
            found = report is not None and any(report.subjects(ISO.sourceErrorCode, Literal(code)))
            passed = not conforms and found and set(data) == before and set(shapes) == before_shapes
            tests.append({"name": name, "expected_source_error": code, "pass": bool(passed)})
            if not passed:
                print(text)

        rejection("changed input bytes invalidate the pinned artifact", "digest-mismatch", input_bytes=raw + b"\n")
        rejection("wrong digest is rejected", "digest-mismatch", lambda g: g.set((artifact, ISO.sha256, Literal("0" * 64))))
        rejection("unknown operation is not executed", "unsupported-operation", lambda g: g.set((source, ISO.operation, EX.UnknownOperation)))
        rejection("missing selector row is rejected", "record-selection", lambda g: g.set((source, ISO.recordKey, Literal("Missing-20"))))
        rejection("source and artifact paths must agree", "reference-disagreement", lambda g: g.set((source, ISO.reference, Literal("different.json"))))
        rejection("missing artifact fails closed", "missing-artifact", lambda g: file.unlink())
        rejection("path traversal is rejected", "unsafe-reference", lambda g: g.set((artifact, ISO.artifactPath, Literal("../outside.json"))))
        rejection("remote references are not fetched", "unsafe-reference", lambda g: g.set((artifact, ISO.artifactPath, Literal("https://example.test/reference.json"))))
        rejection("renamed output label fails replay", "replay-mismatch", lambda g: g.set((output, ISO.isotopeName, Literal("Neon-21"))))
        rejection("deleted neutron cannot hide behind otherwise valid SHACL", "replay-mismatch",
                  lambda g: g.remove((nucleus, ISO.neutron, URIRef(str(output) + ":neutron:0"))))

        def rename_slot(g):
            old = URIRef(str(output) + ":proton:0")
            for triple in list(g):
                if old in triple:
                    g.remove(triple)
                    g.add(tuple(EX.renamedSlot if term == old else term for term in triple))
        rejection("equal counts with altered occurrence identity fail replay", "replay-mismatch", rename_slot)
        rejection("extra source-owned output cannot be ignored", "replay-mismatch",
                  lambda g: (g.add((EX.extra, RDF.type, ISO.Vertex)), g.add((EX.extra, ISO.source, source))))
        changed = copy.deepcopy(resource)
        fields = [f["name"] for f in changed["schema"]["fields"]]
        row = next(row for row in changed["data"] if row[fields.index("isotope")] == "Neon-20")
        row[fields.index("protons")], row[fields.index("neutrons")] = 11, 9
        changed_raw = json.dumps(changed).encode()
        rejection("updated digest alone cannot certify old output against changed counts", "replay-mismatch",
                  lambda g: g.set((artifact, ISO.sha256, Literal(hashlib.sha256(changed_raw).hexdigest()))), changed_raw)

        # Matching counts may legitimately import after a new source projection;
        # columns are resolved by names rather than hardcoded positions.
        reordered = copy.deepcopy(resource)
        reordered["schema"]["fields"].reverse()
        for row in reordered["data"]:
            row.reverse()
        reordered_raw = json.dumps(reordered).encode()
        file.write_bytes(reordered_raw)
        graph, map_ = build_inventory(reordered_raw, "reference.json", "Calcium-46")
        conforms, _, _ = check(graph, shapes, repository_root=root)
        tests.append({"name": "reordered source columns are resolved by field names",
                      "pass": conforms and map_["Z"] == 20 and map_["N"] == 26})

        variants = []
        duplicate = copy.deepcopy(resource)
        duplicate["data"].append(next(row for row in duplicate["data"] if row[0] == "Neon-20"))
        variants.append(("duplicate selected source row", duplicate, "record-selection"))
        invalid = copy.deepcopy(resource)
        next(row for row in invalid["data"] if row[0] == "Neon-20")[1] = True
        variants.append(("boolean is not a proton count", invalid, "invalid-counts"))
        inconsistent = copy.deepcopy(resource)
        next(row for row in inconsistent["data"] if row[0] == "Neon-20")[2] = 11
        variants.append(("mass label disagreement", inconsistent, "mass-label-mismatch"))
        for name, variant, code in variants:
            try:
                build_inventory(json.dumps(variant).encode(), "reference.json", "Neon-20")
            except SourceError as error:
                passed = error.code == code
            else:
                passed = False
            tests.append({"name": name, "expected_source_error": code, "pass": passed})

    # Attribution resolution is weaker than replay and is reported as such.
    data = Graph().parse(base / "fixtures" / "inventory.ttl", format="turtle")
    receipt = verify_sources(data)
    tests.append({"name": "resolved fixture attribution is not called a replayed derivation",
                  "pass": len(receipt["resolved_attributions"]) == 1 and receipt["replayed_outputs"] == []})
    data.set((EX.source, ISO.reference, Literal("research/strominger/isotope-schema/missing-source.json")))
    conforms, report, _ = check(data, shapes)
    tests.append({"name": "nonexistent attribution source is rejected",
                  "pass": not conforms and any(report.subjects(ISO.sourceErrorCode, Literal("missing-artifact")))})
    return tests
