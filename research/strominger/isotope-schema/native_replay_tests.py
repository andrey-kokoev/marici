"""Fresh native constructor replay, kept separate from RDF conformance."""
import hashlib
import json
import contextlib
import io
from unittest.mock import patch
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

from provenance import ROOT, ISO, verify_sources
from native_projection import import_native, build_native, NATIVE_REFERENCE, NATIVE_MANIFEST
from rdflib import Graph, Literal, RDF
from validation_tests import expectation, matches, SH, EX
from organization_tests import complete_fixture


def run(check, shapes, base, derive_readouts, cli_main):
    script = base / "native_replay.mjs"
    native = ROOT / "research/strominger/results/reference-ne22-search"
    protected = [native / name for name in ("verification.json", "D4-verification.json", "D4-input.json", "replay-verification.json")]
    before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}

    def replay(witness=None):
        result = subprocess.run(["node", str(script), *([] if witness is None else [str(witness)])],
                                cwd=ROOT, capture_output=True, text=True, timeout=180, check=False)
        try:
            receipt = json.loads(result.stdout)
        except json.JSONDecodeError:
            receipt = {"status": "runtime-error", "stderr": result.stderr[-2000:], "stdout": result.stdout[-2000:]}
        return result.returncode, receipt

    code, receipt = replay()
    (base / "results" / "native-constructor-replay.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    tests = [{"name": "fresh native Ne-22 constructor replay verifies declared pins and retained witness",
              "actual_status": receipt.get("status"), "stage": receipt.get("stage"),
              "pass": code == 0 and receipt.get("status") == "native-generator-replayed"
              and receipt.get("counts") == {"proton": 10, "neutron": 12, "electron": 10}}]
    with TemporaryDirectory(prefix="marici-native-replay-") as temporary:
        value = json.loads((native / "D4-verification.json").read_bytes())
        value["witness"]["operations"][0]["target"] = -1
        path = Path(temporary) / "tampered.json"
        path.write_text(json.dumps(value), encoding="utf-8")
        code, rejection = replay(path)
        tests.append({"name": "native replay rejects changed transition endpoints independently of saved pass flags",
                      "actual_status": rejection.get("status"), "stage": rejection.get("stage"),
                      "pass": code == 1 and rejection.get("status") == "rejected" and rejection.get("stage") == "constructor-replay"})
        numeric = json.loads((native / "D4-verification.json").read_bytes())
        for section, fields in [("packets", ("id", "chart", "origin")), ("charts", ("cell",)),
                                ("bodies", ("cell",)), ("operations", ("id", "source", "target", "phaseDelta"))]:
            for field in fields:
                numeric["witness"][section][0][field] = float(numeric["witness"][section][0][field])
        numeric_raw = json.dumps(numeric).encode("utf-8")
        path.write_bytes(numeric_raw)
        numeric_code, numeric_receipt = replay(path)
        numeric_graph = build_native(numeric_raw, NATIVE_REFERENCE, (native / "verification.json").read_bytes())
    data, _ = import_native()
    original = set(data)
    tests.append({"name": "integral JSON numeric spellings preserve native projection payload, not artifact pins",
                  "pass": numeric_code == 0 and numeric_receipt.get("status") == "native-generator-replayed"
                  and {t for t in numeric_graph if t[1] != ISO.sha256} == {t for t in original if t[1] != ISO.sha256}
                  and set(numeric_graph) != original})
    output = next(data.subjects(RDF.type, ISO.IsotopeStructure))
    conforms, _, text = check(data, shapes)
    tests.append({"name": "actual native reader incidence imports as a validated totally bound partial structure",
                  "pass": bool(conforms) and not any(data.objects(output, ISO.vertex))
                  and not any(data.objects(output, ISO.arrow)) and set(data) == original})
    if not conforms:
        print(text)
        return tests
    witness = json.loads((native / "D4-verification.json").read_bytes())["witness"]
    expected_edges = {(op["id"], op["source"], op["target"], op["kind"], op["phaseDelta"]) for op in witness["operations"]}
    actual_edges = {(int(data.value(t, ISO.nativeId)), int(data.value(data.value(t, ISO.fromReader), ISO.nativeId)),
                     int(data.value(data.value(t, ISO.toReader), ISO.nativeId)), str(data.value(t, ISO.transitionKind)),
                     int(data.value(t, ISO.phaseDelta))) for t in data.objects(output, ISO.readerTransition)}
    tests.append({"name": "independent source-row oracle verifies every projected native transition", "pass": actual_edges == expected_edges})
    chart_cells = {int(c["id"].rsplit("-", 1)[1]): c["cell"] for c in witness["charts"]}
    expected_states = {(p["id"], p["origin"], p["chart"], chart_cells[p["chart"]]) for p in witness["packets"]}
    actual_states = {(int(data.value(s, ISO.nativeId)), int(data.value(s, ISO.origin)),
                      int(str(data.value(s, ISO.readerChart)).rsplit("-", 1)[1]),
                      int(str(data.value(s, ISO.readerBody)).rsplit(":", 1)[1])) for s in data.objects(output, ISO.readerState)}
    tests.append({"name": "independent source-row oracle verifies reader origins, chart links and body assignments", "pass": actual_states == expected_states})
    readouts = derive_readouts(data, shapes)
    tests.append({"name": "native body readouts are computed from imported constituents",
                  "pass": readouts[str(output)] == {"Z": 10, "N": 12, "A": 22, "electrons": 10, "charge_e": 0}})
    path = base / "results" / "native-ne22-readers.ttl"
    path.write_bytes(data.serialize(format="turtle", encoding="utf-8"))
    parsed = Graph().parse(path, format="turtle")
    conforms, _, _ = check(parsed, shapes)
    tests.append({"name": "native reader Turtle roundtrip preserves all projected triples and replays",
                  "pass": bool(conforms) and set(parsed) == original})
    evidence = verify_sources(parsed)
    (base / "results" / "native-ne22-source-replay.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    transition = next(parsed.objects(output, ISO.readerTransition))
    parsed.set((transition, ISO.transitionKind, Literal("invented-transition")))
    conforms, report, _ = check(parsed, shapes)
    tests.append({"name": "native projection rejects changed transition payload with unchanged counts",
                  "pass": not conforms and Literal("replay-mismatch") in set(report.objects(None, ISO.sourceErrorCode))})
    for profile, scope, constraint in [
        (ISO.InventoryProfile, ISO.NoBindings, ISO.InventoryHasNoStructureConstraint),
        (ISO.CompleteStructureProfile, ISO.TotalBindings, ISO.CompleteMembersConstraint),
    ]:
        graph = Graph()
        for triple in original:
            graph.add(triple)
        graph.set((output, ISO.profile, profile)); graph.set((output, ISO.bindingScope, scope))
        conforms, report, _ = check(graph, shapes)
        shape = "ProfileShape" if profile == ISO.InventoryProfile else "CompletenessShape"
        tests.append({"name": f"native reader projection cannot be relabeled {profile}",
                      "pass": not conforms and matches(report, shapes, output, expectation("SPARQL", shape, constraint=constraint))})
    def original_graph():
        result = Graph()
        for triple in original:
            result.add(triple)
        return result
    graph = original_graph()
    state = graph.value(transition, ISO.fromReader)
    graph.remove((output, ISO.readerState, state))
    conforms, report, _ = check(graph, shapes)
    tests.append({"name": "native transition endpoint must remain in its root's reader inventory",
                  "pass": not conforms and matches(report, shapes, output, expectation("SPARQL", "ReaderMembershipShape", constraint=ISO.ReaderMembershipConstraint))})
    graph = original_graph()
    graph.add((state, RDF.type, ISO.Vertex))
    conforms, report, _ = check(graph, shapes)
    tests.append({"name": "native reader state cannot masquerade as a spatial vertex",
                  "pass": not conforms and matches(report, shapes, state, expectation("Xone", "RecordIdentityShape"))})
    graph = original_graph()
    source = graph.value(output, ISO.source)
    dependency = graph.value(source, ISO.dependencyArtifact)
    graph.set((dependency, ISO.sha256, Literal("0" * 64)))
    conforms, report, _ = check(graph, shapes)
    tests.append({"name": "native dependency manifest pin is checked before projection replay",
                  "pass": not conforms and any(report.value(r, ISO.sourceErrorCode) == Literal("digest-mismatch")
                    for r in report.subjects(SH.focusNode, dependency))})
    # Node replaces invalid UTF-8 in ignored metadata; the Python projection
    # must fail with a source diagnostic, not crash after a successful replay.
    with TemporaryDirectory(prefix="marici-native-encoding-") as temporary:
        root_path = Path(temporary)
        value = json.loads((native / "D4-verification.json").read_bytes())
        value["encodingProbe"] = "BAD_UTF8_MARKER"
        raw = json.dumps(value).encode("utf-8").replace(b"BAD_UTF8_MARKER", b"\xff")
        witness_path = root_path / NATIVE_REFERENCE
        witness_path.parent.mkdir(parents=True)
        witness_path.write_bytes(raw)
        (root_path / NATIVE_MANIFEST).write_bytes((native / "verification.json").read_bytes())
        graph = original_graph()
        artifact = graph.value(source, ISO.inputArtifact)
        graph.set((artifact, ISO.sha256, Literal(hashlib.sha256(raw).hexdigest())))
        conforms, report, _ = check(graph, shapes, repository_root=root_path)
        tests.append({"name": "cross-runtime malformed UTF-8 fails with a source diagnostic rather than crashing",
                      "pass": not conforms and Literal("invalid-native-json") in set(report.objects(None, ISO.sourceErrorCode))})
    graph = complete_fixture(base)
    root = EX.structure
    body = next(graph.objects(graph.value(root, ISO.nucleus), ISO.proton))
    state = EX.readerOnlyRole
    for triple in [(state, RDF.type, ISO.ReaderState), (state, ISO.source, graph.value(root, ISO.source)),
                   (state, ISO.nativeId, Literal(0)), (state, ISO.origin, Literal(0)),
                   (state, ISO.readerChart, Literal("fixture-chart")), (state, ISO.readerBody, body),
                   (root, ISO.readerState, state)]:
        graph.add(triple)
    conforms, _, _ = check(graph, shapes)
    tests.append({"name": "an added reader layer preserves complete fixture conformance while spatial bindings remain", "pass": bool(conforms)})
    for binding in list(graph.objects(root, ISO.interpretation)):
        if graph.value(binding, ISO.particle) == body:
            graph.remove((binding, ISO.role, None)); graph.add((binding, ISO.role, state))
    conforms, report, _ = check(graph, shapes)
    spec = expectation("SPARQL", "BindingCoverageShape", constraint=ISO.ConstituentCoverageConstraint)
    spec["value"] = body
    tests.append({"name": "reader-only roles cannot discharge complete spatial binding coverage",
                  "pass": not conforms and matches(report, shapes, root, spec)})
    stream = io.StringIO()
    with patch("sys.argv", ["check.py", "--import-native-reader"]), contextlib.redirect_stdout(stream):
        cli_main()
    cli_graph = Graph().parse(data=stream.getvalue(), format="turtle")
    tests.append({"name": "native import CLI emits exactly the checked reader projection", "pass": set(cli_graph) == original})
    tests.append({"name": "native replay and import leave original inputs and native receipt untouched",
                  "pass": before == {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}})
    return tests
