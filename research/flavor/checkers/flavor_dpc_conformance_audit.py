import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
CONTRACT=ROOT/"contracts"/"flavor-interaction-net-state.v1.json"
INDEX=ROOT/"flavor-programme-index.md"
NET_MD=ROOT/"flavor-interaction-net-state.md"
WORK_PACKAGES=list(range(1177,1187))
REQUIRED_TOP_LEVEL={
    "schema","status","question","dpc","classification","remaining_gate",
    "hostile_gate","claim_boundary","disposition"
}
REQUIRED_DPC={
    "conjecture","rivals","risky_consequences","falsification_attempt",
    "residual","disposition"
}
net=json.loads(CONTRACT.read_text())
net_nodes={node["id"]:node for node in net["nodes"]}
index_text=INDEX.read_text()
net_text=NET_MD.read_text()
records=[]
for number in WORK_PACKAGES:
    checker=next((ROOT/"checkers").glob(f"wp{number}_*.py"),None)
    result_path=next((ROOT/"results").glob(f"wp{number}_*.json"),None)
    assert checker is not None, f"missing checker for WP{number}"
    assert result_path is not None, f"missing result for WP{number}"
    node_id=checker.stem
    node=net_nodes.get(node_id)
    assert node is not None, f"missing net node {node_id}"
    locator=REPO/node["locator"]
    assert locator.exists(), f"missing locator {locator}"
    result=json.loads(result_path.read_text())
    missing_top=sorted(REQUIRED_TOP_LEVEL-result.keys())
    assert not missing_top, f"WP{number} missing {missing_top}"
    assert result["status"]=="PASS", f"WP{number} status {result['status']}"
    missing_dpc=sorted(REQUIRED_DPC-result["dpc"].keys())
    assert not missing_dpc, f"WP{number} DPC missing {missing_dpc}"
    assert result["dpc"]["rivals"], f"WP{number} has no rivals"
    assert result["dpc"]["risky_consequences"], f"WP{number} has no risky consequences"
    markdown=locator.read_text()
    assert "## DPC resolution" in markdown, f"WP{number} markdown lacks DPC section"
    assert "\\boxed" not in markdown, f"WP{number} markdown uses boxed notation"
    assert f"WP{number}" in index_text, f"WP{number} absent from programme index"
    assert f"WP{number}" in net_text, f"WP{number} absent from net narrative"
    completed=subprocess.run(
        [sys.executable,str(checker)],cwd=REPO,text=True,
        stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=120,check=True
    )
    assert "PASS" in completed.stdout, f"WP{number} replay did not pass: {completed.stdout[-500:]}"
    records.append({
        "work_package":f"WP{number}",
        "checker":str(checker.relative_to(REPO)),
        "result":str(result_path.relative_to(REPO)),
        "locator":node["locator"],
        "net_node":node_id,
        "replay":completed.stdout.strip().splitlines()[-1]
    })
net_replay=subprocess.run(
    [sys.executable,str(ROOT/"checkers"/"wp1043_flavor_interaction_net_state.py")],
    cwd=REPO,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
    timeout=120,check=True
)
assert "WP1043 PASS: 150 5" in net_replay.stdout
constructed=sum(1 for node in net["nodes"] if node.get("status")=="constructed")
assert constructed==150
assert len(net["hostile_fixtures"])==148
assert "\\boxed" not in net_text
output={
    "schema":"marici.flavor.dpc-conformance-audit.v1",
    "status":"PASS",
    "work_packages_checked":[f"WP{n}" for n in WORK_PACKAGES],
    "work_package_count":len(WORK_PACKAGES),
    "required_top_level":sorted(REQUIRED_TOP_LEVEL),
    "required_dpc":sorted(REQUIRED_DPC),
    "constructed_nodes":constructed,
    "hostile_fixtures":len(net["hostile_fixtures"]),
    "net_replay":net_replay.stdout.strip(),
    "records":records,
    "checks":{
        "artifacts_exist":True,
        "dpc_fields_complete":True,
        "rivals_nonempty":True,
        "risky_consequences_nonempty":True,
        "markdown_dpc_sections":True,
        "programme_index_entries":True,
        "net_narrative_entries":True,
        "checker_replays":True,
        "boxed_notation_absent":True,
        "interaction_net_counts":True
    }
}
(ROOT/"results"/"flavor_dpc_conformance_audit.json").write_text(json.dumps(output,indent=2)+"\n")
print(f"DPC CONFORMANCE PASS: {len(WORK_PACKAGES)} work packages, {constructed} nodes, {len(net['hostile_fixtures'])} fixtures")
