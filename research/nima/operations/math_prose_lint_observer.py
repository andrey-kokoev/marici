from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SITE_ROOT = Path(r"C:\Users\andrey\src\marici")
STATE_PATH = SITE_ROOT / ".narada" / ".ai" / "format-lint" / "state.json"
DOMAIN_PATH = Path(r"C:\Users\andrey\src\mcp-surfaces\packages\shared\ledger-domain-epistemic\domain.json")
EXECUTABLE_ROOT = Path(r"C:\Users\andrey\src\mcp-surfaces\packages\ledger-domain-mcp\dist\native\versions")

OWNER_IDS = {
    "nima": ("marici.Nima", "team_member:aa2834674c8559a5dee0"),
    "benincasa": ("marici.Benincasa", "team_member:bc28f30924d7df1af02a"),
    "flavor": ("marici.Figueiredo", "team_member:7f11641564913e4417ff"),
    "strominger": ("marici.Strominger", "team_member:4561aedd7f948b5ddee5"),
    "grothendieck": ("marici.Grothendieck", "team_member:7283d8c22c912c41664b"),
    "buzzard": ("marici.Buzzard", "team_member:81a83d48cea75aaf3336"),
    "kitaev": ("marici.Kitaev", "team_member:2ec122bc41a1fea3b5ab"),
    "sontag": ("marici.Sontag", "team_member:139d753e7403768d1d2b"),
    "aspect": ("marici.Aspect", "team_member:ae219c2b8562ec798ba1"),
}
IDENTITY_TO_OWNER = {identity: (identity, member_id) for identity, member_id in OWNER_IDS.values()}
IDENTITY_TO_OWNER.update({member_id: (identity, member_id) for identity, member_id in OWNER_IDS.values()})

TEXT_COMMAND = re.compile(r"\\text\{([^{}]*)\}")
BOXED_COMMAND = re.compile(r"\\boxed(?:\s*\{|\b)")
WORD = re.compile(r"[A-Za-z]{2,}")
INLINE_CODE = re.compile(r"`[^`]*`")
ERROR_ALREADY_EXISTS = 183


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    code: str
    excerpt: str
    owner: str
    owner_member_id: str

    @property
    def fingerprint(self) -> str:
        raw = f"{self.path}\0{self.line}\0{self.code}\0{self.excerpt}".encode("utf-8")
        return hashlib.sha256(raw).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def owner_for(relative: str, text: str) -> tuple[str, str] | None:
    parts = Path(relative).parts
    if len(parts) >= 2 and parts[0].lower() == "research":
        return OWNER_IDS.get(parts[1].lower())
    if len(parts) >= 2 and parts[0].lower() == "src" and parts[1].lower() == "ledger":
        match = re.search(r"(?m)^author:\s*(marici\.[A-Za-z]+)\s*$", text)
        if match:
            identity = match.group(1)
            for value in OWNER_IDS.values():
                if value[0] == identity:
                    return value
        return OWNER_IDS["nima"]
    if relative == "AGENTS.md":
        return OWNER_IDS["nima"]
    return None


def scan_text(relative: str, text: str) -> list[Finding]:
    owner = owner_for(relative, text)
    if owner is None:
        return []
    findings: list[Finding] = []
    in_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        authored = INLINE_CODE.sub("", line)
        if BOXED_COMMAND.search(authored):
            findings.append(Finding(relative, number, "forbidden_boxed", authored.strip()[:240], *owner))
        for match in TEXT_COMMAND.finditer(authored):
            content = match.group(1).strip()
            words = WORD.findall(content)
            if any(character.isspace() for character in content) or len(words) >= 3:
                findings.append(Finding(relative, number, "prose_in_math_text_command", line.strip()[:240], *owner))
    return findings


def scan_graph_body(entity_id: str, sender: str, body: str) -> list[Finding]:
    owner = IDENTITY_TO_OWNER.get(sender)
    if owner is None:
        return []
    source = f"graph:{entity_id}"
    findings: list[Finding] = []
    for number, line in enumerate(body.splitlines(), start=1):
        if BOXED_COMMAND.search(line):
            findings.append(Finding(source, number, "forbidden_boxed_in_graph_message", line.strip()[:240], *owner))
        for match in TEXT_COMMAND.finditer(line):
            content = match.group(1).strip()
            words = WORD.findall(content)
            if any(character.isspace() for character in content) or len(words) >= 3:
                findings.append(Finding(source, number, "prose_in_graph_math_text_command", line.strip()[:240], *owner))
    return findings


def markdown_files() -> list[Path]:
    files = [SITE_ROOT / "AGENTS.md"]
    for root in (SITE_ROOT / "research", SITE_ROOT / "src" / "ledger"):
        if root.exists():
            files.extend(root.rglob("*.md"))
    return sorted({path.resolve() for path in files if path.is_file()})


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {"schema": "marici.math-prose-lint-state.v1", "files": {}, "active": {}}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = STATE_PATH.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(STATE_PATH)


def latest_graph_executable() -> Path:
    candidates = list(EXECUTABLE_ROOT.glob("*/narada-ledger-domain.exe"))
    if not candidates:
        raise RuntimeError(f"epistemic graph executable not found below {EXECUTABLE_ROOT}")
    return max(candidates, key=lambda path: path.stat().st_mtime_ns)


class McpClient:
    def __init__(self) -> None:
        command = latest_graph_executable()
        self.process = subprocess.Popen(
            [str(command), "--domain", str(DOMAIN_PATH), "--site-root", str(SITE_ROOT)],
            cwd=SITE_ROOT,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        self.next_id = 1
        self.request("initialize", {"protocolVersion": "2024-11-05"})

    def request(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        if self.process.stdin is None or self.process.stdout is None:
            raise RuntimeError("MCP pipes are unavailable")
        request_id = self.next_id
        self.next_id += 1
        wire = {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params}
        self.process.stdin.write(json.dumps(wire, separators=(",", ":")) + "\n")
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        if not line:
            stderr = self.process.stderr.read()[-2000:] if self.process.stderr else ""
            raise RuntimeError(f"MCP process closed without response: {stderr}")
        response = json.loads(line)
        if "error" in response:
            raise RuntimeError(json.dumps(response["error"], sort_keys=True))
        return response["result"]

    def call(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        return self.request("tools/call", {"name": name, "arguments": arguments})

    def close(self) -> None:
        if self.process.stdin and not self.process.stdin.closed:
            self.process.stdin.close()
        try:
            self.process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            self.process.terminate()


def scan_graph_since(client: McpClient, after_sequence: int) -> tuple[list[Finding], int]:
    findings: list[Finding] = []
    largest_sequence = after_sequence
    for identity, _member_id in OWNER_IDS.values():
        result = client.call(
            "epistemic_graph_query",
            {
                "template": "epistemic:inbox",
                "recipient": identity,
                "viewer": identity,
                "direction": "incoming",
                "read_state": "all",
                "after_sequence": after_sequence,
                "include_body": True,
                "limit": 100,
                "max_datoms": 200000,
                "timeout_ms": 10000,
            },
        )
        content = result.get("structuredContent", {})
        if content.get("has_more"):
            raise RuntimeError(f"graph message scan exceeded one bounded page for {identity}")
        for item in content.get("items", []):
            sequence = int(item.get("event_sequence", 0))
            largest_sequence = max(largest_sequence, sequence)
            body = item.get("body", "")
            # The observer must quote exact evidence in its own obligations. Those
            # typed audit messages are not authored presentation and must not
            # recursively generate obligations about their quoted evidence.
            if body.startswith("Automated formatting repair obligation.") or body.startswith("Automated rescan no longer finds violation"):
                continue
            findings.extend(scan_graph_body(item["entity_id"], item.get("sender", ""), body))
    return findings, largest_sequence


def obligation_operations(finding: Finding) -> list[dict[str, Any]]:
    short = finding.fingerprint[:20]
    obligation_id = f"marici:repair_obligation:math-prose-{short}"
    local = f"obligation_{short}"
    message = f"message_{short}"
    body = (
        f"Automated formatting repair obligation. {finding.code} at {finding.path}:{finding.line}. "
        f"Evidence: {finding.excerpt!r}. Replace prose math-typesetting with ordinary prose; retain only actual "
        "mathematical notation in math delimiters. Repair only your own locus and verify the finding disappears. "
        f"Fingerprint: {finding.fingerprint}."
    )
    return [
        {
            "op": "entity.declare",
            "entity_id": obligation_id,
            "local_ref": local,
            "kind": "marici:repair_obligation",
            "title": f"Repair prohibited math prose at {finding.path}:{finding.line}",
            "assignee": finding.owner,
            "status": "open",
            "source_path": finding.path,
            "source_line": finding.line,
            "violation_code": finding.code,
            "violation_fingerprint": finding.fingerprint,
            "acceptance_criterion": "A subsequent scan finds no matching violation at this source location.",
        },
        {
            "op": "entity.declare",
            "local_ref": message,
            "kind": "narada.epistemic:communication",
            "title": f"Automated math-prose repair obligation: {finding.path}:{finding.line}",
            "sender": "marici.Nima",
            "recipient": finding.owner,
            "intent": "request",
            "sent_at": utc_now(),
            "body": body,
        },
        {"op": "relation.declare", "relation_type": "narada.epistemic:sent_by", "source_ref": message, "target_id": OWNER_IDS["nima"][1]},
        {"op": "relation.declare", "relation_type": "narada.epistemic:addressed_to", "source_ref": message, "target_id": finding.owner_member_id},
        {"op": "relation.declare", "relation_type": "requests", "source_ref": message, "target_ref": local},
        {"op": "relation.declare", "relation_type": "marici:assigned_to", "source_ref": local, "target_id": finding.owner_member_id},
    ]


def resolution_operations(record: dict[str, Any]) -> list[dict[str, Any]]:
    fingerprint = record["fingerprint"]
    short = fingerprint[:20]
    obligation_id = f"marici:repair_obligation:math-prose-{short}"
    resolution = f"resolution_{short}"
    message = f"resolution_message_{short}"
    owner = record["owner"]
    member_id = record["owner_member_id"]
    return [
        {
            "op": "entity.declare",
            "local_ref": resolution,
            "kind": "marici:repair_resolution",
            "title": f"Resolved math-prose finding at {record['path']}:{record['line']}",
            "violation_fingerprint": fingerprint,
            "resolved_at": utc_now(),
        },
        {"op": "relation.declare", "relation_type": "marici:resolves", "source_ref": resolution, "target_id": obligation_id},
        {
            "op": "entity.declare",
            "local_ref": message,
            "kind": "narada.epistemic:communication",
            "title": f"Automated math-prose repair verified: {record['path']}:{record['line']}",
            "sender": "marici.Nima",
            "recipient": owner,
            "intent": "acknowledgment",
            "sent_at": utc_now(),
            "body": f"Automated rescan no longer finds violation {fingerprint} at {record['path']}:{record['line']}. The repair obligation has a resolution record.",
        },
        {"op": "relation.declare", "relation_type": "narada.epistemic:sent_by", "source_ref": message, "target_id": OWNER_IDS["nima"][1]},
        {"op": "relation.declare", "relation_type": "narada.epistemic:addressed_to", "source_ref": message, "target_id": member_id},
        {"op": "relation.declare", "relation_type": "acknowledges", "source_ref": message, "target_ref": resolution},
    ]


def admit(operations: list[dict[str, Any]]) -> None:
    client = McpClient()
    try:
        for start in range(0, len(operations), 180):
            batch = operations[start : start + 180]
            result = client.call(
                "epistemic_graph_submit_review_admit",
                {
                    "actor": "marici.Nima",
                    "authority_basis": {
                        "kind": "operator_direct_instruction",
                        "summary": "Operator authorized a one-minute automated math-prose scanner with assigned graph repair obligations.",
                    },
                    "operations": batch,
                },
            )
            content = result.get("structuredContent", {})
            if content.get("status") != "admitted":
                raise RuntimeError(f"graph admission failed: {json.dumps(result, sort_keys=True)}")
    finally:
        client.close()


def self_test() -> None:
    bad = "[\\n  \\text{ordinary prose belongs outside math}\\n]"
    findings = scan_text("research/nima/example.md", bad)
    assert len(findings) == 1
    assert findings[0].code == "prose_in_math_text_command"
    assert scan_text("research/nima/example.md", r"The map \\operatorname{Spec}(A) is typed.") == []
    boxed = scan_text("research/nima/example.md", r"\\boxed{x+y}")
    assert len(boxed) == 1 and boxed[0].code == "forbidden_boxed"
    graph = scan_graph_body("message:test", "marici.Grothendieck", r"\\text{ordinary prose in math}")
    assert len(graph) == 1 and graph[0].owner == "marici.Grothendieck"
    documented = "Use `\\boxed` nowhere.\n```text\n\\text{quoted bad fixture}\n```"
    assert scan_text("research/nima/example.md", documented) == []
    print(json.dumps({"status": "pass", "tests": 5}))


def acquire_watch_mutex() -> int | None:
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateMutexW.argtypes = [ctypes.c_void_p, ctypes.c_bool, ctypes.c_wchar_p]
    kernel32.CreateMutexW.restype = ctypes.c_void_p
    kernel32.CloseHandle.argtypes = [ctypes.c_void_p]
    kernel32.CloseHandle.restype = ctypes.c_bool
    handle = kernel32.CreateMutexW(None, False, "Local\\MariciMathProseLintObserver")
    if not handle:
        raise ctypes.WinError(ctypes.get_last_error())
    if ctypes.get_last_error() == ERROR_ALREADY_EXISTS:
        kernel32.CloseHandle(handle)
        return None
    return int(handle)


def run(baseline: bool, dry_run: bool) -> None:
    state = load_state()
    previous_files: dict[str, str] = state.get("files", {})
    previous_active: dict[str, dict[str, Any]] = state.get("active", {})
    current_files: dict[str, str] = {}
    current_active = dict(previous_active)
    for key, record in list(current_active.items()):
        if record.get("path", "").startswith("graph:") and record.get("excerpt", "").startswith("Automated formatting repair obligation."):
            current_active.pop(key, None)
    new_findings: list[Finding] = []

    for path in markdown_files():
        relative = path.relative_to(SITE_ROOT).as_posix()
        data = path.read_bytes()
        file_digest = digest(data)
        current_files[relative] = file_digest
        if baseline or previous_files.get(relative) == file_digest:
            continue
        text = data.decode("utf-8", errors="replace")
        for finding in scan_text(relative, text):
            if finding.fingerprint not in previous_active:
                new_findings.append(finding)
            current_active[finding.fingerprint] = {
                "fingerprint": finding.fingerprint,
                "path": finding.path,
                "line": finding.line,
                "code": finding.code,
                "excerpt": finding.excerpt,
                "owner": finding.owner,
                "owner_member_id": finding.owner_member_id,
            }

        old_for_file = [key for key, value in previous_active.items() if value["path"] == relative]
        new_for_file = {finding.fingerprint for finding in scan_text(relative, text)}
        for key in old_for_file:
            if key not in new_for_file:
                current_active.pop(key, None)

    removed_files = set(previous_files) - set(current_files)
    for key, record in list(current_active.items()):
        if record["path"] in removed_files:
            current_active.pop(key, None)

    resolved = [record for key, record in previous_active.items() if key not in current_active]

    graph_after_sequence = int(state.get("graph_after_sequence", 0))
    client: McpClient | None = None
    if baseline:
        client = McpClient()
        status = client.call("epistemic_graph_status", {}).get("structuredContent", {})
        graph_after_sequence = int(status.get("event_count", graph_after_sequence))
    else:
        client = McpClient()
        graph_findings, graph_after_sequence = scan_graph_since(client, graph_after_sequence)
        for finding in graph_findings:
            if finding.fingerprint not in previous_active:
                new_findings.append(finding)
            current_active[finding.fingerprint] = {
                "fingerprint": finding.fingerprint,
                "path": finding.path,
                "line": finding.line,
                "code": finding.code,
                "excerpt": finding.excerpt,
                "owner": finding.owner,
                "owner_member_id": finding.owner_member_id,
            }
    operations: list[dict[str, Any]] = []
    for finding in new_findings:
        operations.extend(obligation_operations(finding))
    for record in resolved:
        operations.extend(resolution_operations(record))

    report = {
        "schema": "marici.math-prose-lint-run.v1",
        "baseline": baseline,
        "files_seen": len(current_files),
        "new_findings": len(new_findings),
        "resolved_findings": len(resolved),
        "active_findings": len(current_active),
        "graph_operation_count": len(operations),
        "dry_run": dry_run,
    }
    print(json.dumps(report, sort_keys=True))
    if operations and not dry_run:
        if client is not None:
            client.close()
            client = None
        admit(operations)
    if not dry_run:
        state = {
            "schema": "marici.math-prose-lint-state.v1",
            "updated_at": utc_now(),
            "graph_after_sequence": graph_after_sequence,
            "files": current_files,
            "active": current_active,
        }
        save_state(state)
    if client is not None:
        client.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--watch", action="store_true")
    arguments = parser.parse_args()
    if arguments.self_test:
        self_test()
    elif arguments.watch:
        mutex = acquire_watch_mutex()
        if mutex is None:
            print(json.dumps({"status": "already_running"}))
            return
        while True:
            try:
                run(False, False)
            except Exception as error:
                STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
                with (STATE_PATH.parent / "watch-errors.log").open("a", encoding="utf-8") as stream:
                    stream.write(f"{utc_now()} {error}\n")
            time.sleep(60)
    else:
        run(arguments.baseline, arguments.dry_run)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(json.dumps({"status": "error", "error": str(error)}), file=sys.stderr)
        raise
