"""Validate all registered grammar fragments, tests and optional source-bound proof receipts."""
import argparse
import copy
import hashlib
import json
import check_native_grammar as native
import check_semantic_grammar as semantic
import check_grammar_completion as completion
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "research/nima/generating-grammar"
REGISTRY = DIRECTORY / "registry.json"
TABLE = DIRECTORY / "TABLE.md"
REPORT = DIRECTORY / "verification.json"
ROLES = {"constructor", "derived", "conditional", "candidate"}
EVIDENCE = {
    "source_reported_induction", "source_reported_construction",
    "source_reported_checked", "selected_architecture",
    "source_reported_conditional", "candidate_protocol", "separate_model_choice",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value):
    return isinstance(value, list) and bool(value) and all(map(nonempty, value))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_path(source):
    path = (ROOT / source["path"]).resolve()
    require(path.is_relative_to(ROOT.resolve()), "source escapes repository")
    require(path.is_file(), "missing source: " + source["path"])
    return path


def contract_items(data):
    text = source_path(data["sources"]["contract"]).read_text(encoding="utf-8")
    section = text.split("## State and operation ledger", 1)[1].split("\n## ", 1)[0]
    items = []
    for line in section.splitlines():
        if not line.startswith("| "):
            continue
        cell = line.split("|")[1].strip()
        if cell != "Operation":
            items.append(cell)
    require(bool(items), "source contract table is empty")
    return items


def validate(data):
    require(data["schema_version"] == 4, "unsupported schema")
    require(data["completions_and_policies"] == completion.MANIFEST.relative_to(ROOT).as_posix(), "unexpected completion manifest")
    completed = json.loads(source_path({"path": data["completions_and_policies"]}).read_text(encoding="utf-8"))
    completion_counts = completion.validate(completed, completion.source_text(completed))
    require(data["semantic_extensions"] == semantic.MANIFEST.relative_to(ROOT).as_posix(), "unexpected semantic extensions")
    extensions = json.loads(source_path({"path": data["semantic_extensions"]}).read_text(encoding="utf-8"))
    extension_counts = semantic.validate(extensions, semantic.load_sources(extensions))
    require(data["native_core"] == str(native.MANIFEST.relative_to(ROOT)).replace('\\', '/'), "unexpected native core")
    core = json.loads(source_path({"path": data["native_core"]}).read_text(encoding="utf-8"))
    core_counts = native.validate(core, native.sources(core))
    require(nonempty(data["catalogue_role"]), "missing catalogue role")
    require(type(data["revision"]) is int and data["revision"] > 0, "invalid revision")
    require(data["completeness"] == "open", "closure requires a reviewed schema revision")
    for field in ("title", "maintainer", "authority", "scope"):
        require(nonempty(data[field]), "empty " + field)
    require(data["source_basis"]["status"] == "unresolved", "source basis promotion needs schema review")
    for field in ("description", "acceptance"):
        require(nonempty(data["source_basis"][field]), "empty source basis " + field)
    require(bool(data["sources"]), "no sources")
    for source in data["sources"].values():
        source_path(source)
        require(nonempty(source["section"]), "missing source locator")
    sorts = data["sorts"]
    require(bool(sorts) and all(map(nonempty, sorts.values())), "invalid sorts")
    seed_ids = [s["id"] for s in data["seeds"]]
    require(bool(seed_ids) and len(seed_ids) == len(set(seed_ids)), "missing or duplicate seeds")
    for seed in data["seeds"]:
        require(seed["codomain"] in sorts, "unknown seed sort")
        require(nonempty(seed["rule"]) and strings(seed["requires"]), "invalid seed")
        require(seed["source"] in data["sources"], "unknown seed source")
    unsupported_ids = [u["id"] for u in data["unsupported_families"]]
    require(len(unsupported_ids) == len(set(unsupported_ids)), "duplicate unsupported family")
    for family in data["unsupported_families"]:
        source_path({"path": family["source_path"]})
        require(nonempty(family["reason"]), "unsupported family lacks reason")
    operations = data["operations"]
    require(bool(operations), "no operations")
    ids = [op["id"] for op in operations]
    require(len(ids) == len(set(ids)), "duplicate operation id")
    index = {op["id"]: op for op in operations}
    for op in operations:
        for field in ("id", "name", "codomain", "rule", "gap"):
            require(nonempty(op[field]), "empty operation " + field)
        for field in ("domain", "requires", "retains", "sources"):
            require(strings(op[field]), "empty or invalid " + field + " in " + op["id"])
        require(all(t in sorts for t in op["domain"] + [op["codomain"]]), "unknown sort")
        require(op["role"] in ROLES, "unknown role")
        require(op["evidence"] in EVIDENCE, "unknown evidence strength")
        require(op["s4_status"] == "unassessed", "S4 promotion requires frozen source and schema review")
        require(all(s in data["sources"] for s in op["sources"]), "unknown source")
        deps = op["depends_on"]
        require(isinstance(deps, list) and all(map(nonempty, deps)), "invalid dependencies")
        require(len(deps) == len(set(deps)), "duplicate dependency")
        require(all(d in index for d in deps), "unknown dependency")
        require(op["role"] != "derived" or bool(deps), "derived rule lacks dependencies")
    visited, active = set(), set()

    def visit(key):
        require(key not in active, "dependency cycle")
        if key in visited:
            return
        active.add(key)
        for dep in index[key]["depends_on"]:
            visit(dep)
        active.remove(key)
        visited.add(key)

    for key in ids:
        visit(key)
    seen = set()
    for row in data["coverage"]:
        require(row["source"] in data["sources"], "unknown coverage source")
        require(nonempty(row["item"]), "empty coverage item")
        key = (row["source"], row["item"])
        require(key not in seen, "duplicate coverage item")
        seen.add(key)
        require(strings(row["operations"]), "empty coverage mapping")
        for op_id in row["operations"]:
            require(op_id in index, "unknown covered operation")
            require(row["source"] in index[op_id]["sources"], "coverage/source mismatch")
    expected = contract_items(data)
    actual = [r["item"] for r in data["coverage"] if r["source"] == "contract"]
    require(len(actual) == len(expected) and set(actual) == set(expected), "source contract coverage drift")
    relation_ids = set()
    for relation in data["relations"]:
        require(relation["id"] not in relation_ids, "duplicate relation id")
        relation_ids.add(relation["id"])
        require(nonempty(relation["statement"]), "empty relation")
        require(relation["source"] in data["sources"], "unknown relation source")
        require(strings(relation["operations"]), "empty relation operations")
        require(all(x in index for x in relation["operations"]), "unknown relation operation")
    gap_ids = [g["id"] for g in data["gaps"]]
    require(bool(gap_ids) and len(gap_ids) == len(set(gap_ids)), "missing or duplicate gaps")
    require(all(nonempty(g["acceptance"]) for g in data["gaps"]), "gap lacks acceptance test")
    retired = [g["id"] for g in data["retired_gaps"]]
    require(len(retired) == len(set(retired)) and not (set(retired) & set(gap_ids)), "retired/current gap collision")
    require(all(nonempty(g["reason"]) for g in data["retired_gaps"]), "missing gap retirement reason")
    return {"operations": len(ids), "contract_rows_covered": len(actual), "relations": len(relation_ids), "native_core": core_counts, "semantic_extensions": extension_counts, "completions_and_policies": completion_counts}


def render(data):
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ")

    lines = ["# Supplementary operation catalogue", "",
             "The implemented grammar is [NATIVE-CORE.md](NATIVE-CORE.md); source-defined computational extensions are in [SEMANTIC-EXTENSIONS.md](SEMANTIC-EXTENSIONS.md). This table records policy and experimental operations whose relation to that core must be established separately.", "",
             "Generated from `registry.json`; do not edit. See `README.md` for scope and maintenance.", "",
             f"Revision: {data['revision']}. Completeness: **open**. S4 source signature: **unresolved**.", "",
             "Evidence is source-reported. Rule IDs are local to this audit, not a claim of minimal generators.", "",
             "Seeds: " + "; ".join(f"`{s['id']}`: {s['rule']}" for s in data["seeds"]), "",
             "Existing record/map packages are conditional inputs, not generated from the experimental seed by assumption.", "",
             "| ID | Input → output | Rule | Role / evidence | Required inputs | Source |",
             "|---|---|---|---|---|---|"]
    for op in data["operations"]:
        source_links = []
        for key in op["sources"]:
            source_links.append(f"[{key}](../../../{data['sources'][key]['path']})")
        row = [f"`{op['id']}`", ", ".join(op["domain"]) + " → " + op["codomain"],
               op["rule"], op["role"] + " / " + op["evidence"],
               "; ".join(op["requires"]), ", ".join(source_links)]
        lines.append("| " + " | ".join(map(cell, row)) + " |")
    lines += ["", "## Unresolved derivations", "",
              "Every registered S4 derivation is unassessed. These are missing bridges, not no-go results.", "",
              "| Rule | Retained data | Local dependencies | Missing bridge or limitation |",
              "|---|---|---|---|"]
    for op in data["operations"]:
        row = [f"`{op['id']}`", "; ".join(op["retains"]),
               ", ".join(op["depends_on"]) or "None declared", op["gap"]]
        lines.append("| " + " | ".join(map(cell, row)) + " |")
    lines += ["", "## Operational interpretation gaps", "",
              "Completed arithmetic and all nine policy assessments are in [COMPLETIONS-AND-POLICIES.md](COMPLETIONS-AND-POLICIES.md).", ""]
    for family in data["unsupported_families"]:
        lines.append(f"- [{family['id']}](../../../{family['source_path']}): {family['reason']}")
    lines += ["", "## Coverage gates", ""]
    lines += [f"- **{g['id']}**: {g['acceptance']}" for g in data["gaps"]]
    return "\n".join(lines) + "\n"


def self_test(data):
    mutations = [
        ("duplicate operation id", lambda d: d["operations"].append(copy.deepcopy(d["operations"][0]))),
        ("unknown sort", lambda d: d["operations"][0].update(codomain="Missing")),
        ("unknown source", lambda d: d["operations"][0].update(sources=["missing"])),
        ("unknown dependency", lambda d: d["operations"][0].update(depends_on=["missing"])),
        ("dependency cycle", lambda d: d["operations"][0].update(depends_on=["type.pp"])),
        ("source contract coverage drift", lambda d: d["coverage"].pop()),
        ("S4 promotion requires frozen source and schema review", lambda d: d["operations"][0].update(s4_status="derived")),
        ("source basis promotion needs schema review", lambda d: d["source_basis"].update(status="resolved")),
        ("closure requires a reviewed schema revision", lambda d: d.update(completeness="closed")),
    ]
    rejected = []
    for expected, mutate in mutations:
        bad = copy.deepcopy(data)
        mutate(bad)
        try:
            validate(bad)
        except ValueError as exc:
            require(str(exc) == expected, f"wrong rejection: {exc}; expected {expected}")
            rejected.append(expected)
        else:
            raise ValueError("accepted malformed registry: " + expected)
    return rejected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="regenerate table and validation receipt")
    parser.add_argument("--self-test", action="store_true", help="run all fragment hostiles and path execution tests")
    parser.add_argument("--require-formal", action="store_true", help="validate current source-bound core, arithmetic and macro receipts")
    args = parser.parse_args()
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    counts = validate(data)
    rejections = self_test(data) if args.self_test else []
    core = json.loads(native.MANIFEST.read_text(encoding="utf-8"))
    extensions = json.loads(semantic.MANIFEST.read_text(encoding="utf-8"))
    completed = json.loads(completion.MANIFEST.read_text(encoding="utf-8"))
    component_tests = {}
    path_execution = {"status": "not_requested"}
    if args.self_test:
        component_tests = {
            "native": native.rejection_tests(core, native.sources(core)),
            "semantic": semantic.census_hostiles(extensions, semantic.load_sources(extensions)),
            "completion": completion.hostiles(completed, completion.source_text(completed)),
        }
        path_execution = semantic.path_tests()
    formal = {"status": "not_requested"}
    if args.require_formal:
        core_formal = native.formal_receipts(core)
        require(core_formal["mathematical_verification"], "native core formal evidence unavailable")
        formal = {"native_core": core_formal, "natural_arithmetic": semantic.arithmetic_receipt(),
                  "completion_and_macros": completion.formal_evidence()}
    views = [(TABLE, render(data)), (native.TABLE, native.render(core)),
             (semantic.TABLE, semantic.render(extensions)), (completion.TABLE, completion.render(completed))]
    for target, table in views:
        if args.write:
            target.write_text(table, encoding="utf-8")
        else:
            require(target.is_file() and target.read_text(encoding="utf-8") == table,
                    "generated table is stale: " + target.name + "; run --write")
    report = {
        "schema": "marici.generating_grammar.validation.v1", "revision": data["revision"],
        "status": "passed", "checked_at": datetime.now(timezone.utc).isoformat(),
        "scope": "All registered fragment source censuses, generated views and requested hostiles/execution/proof-receipt checks; no global generation theorem",
        "counts": counts, "rejection_tests": rejections, "component_tests": component_tests,
        "path_execution": path_execution, "formal_evidence": formal,
        "registry_sha256": digest(REGISTRY), "table_sha256": digest(TABLE),
        "native_core_sha256": digest(ROOT / data["native_core"]),
        "semantic_extensions_sha256": digest(ROOT / data["semantic_extensions"]),
        "completions_and_policies_sha256": digest(ROOT / data["completions_and_policies"]),
        "generated_views": {target.name: digest(target) for target, _ in views},
        "checker_sha256": digest(Path(__file__)),
        "sources": {key: {"path": value["path"], "sha256": digest(source_path(value))}
                    for key, value in data["sources"].items()},
        "mathematical_proofs_rerun": False, "global_completeness": "open", "s4_derivation": "unassessed",
    }
    if args.write:
        REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
