#!/usr/bin/env python3
"""Disclosed exception route (nativeShellException): minimal MCP stdio
JSON-RPC client for the marici epistemic-graph surface.

Why this exists: the agent-side emission of mcp_loader_call_* tool
shapes collapsed to mcp_loader_attach_surface 14 times in one session
(a generation fault, persisting across a carrier restart). The loader
binding remains the canonical route; this client spawns the exact
command/args declared in the site fabric
(.ai/mcp/narada-marici-epistemic-graph-mcp.json) and speaks MCP stdio
directly. Use ONLY when the loader route is demonstrably unavailable,
and disclose each use in the ledger entry it serves.

Usage:
  python tools/mcp_stdio_client.py <tool_name> '<json_arguments>'
"""
import json
import subprocess
import sys

PROXY = ("C:/Users/andrey/src/mcp-surfaces/packages/shared/mcp-runtime-proxy/"
         "dist/native/versions/850c89b963a0910e639b243746eaa0d7608b75f64a68243dd5d404225b1fcae0/"
         "narada-mcp-runtime.exe")
MANIFEST = ("C:/Users/andrey/src/mcp-surfaces/.ai/runtime/"
            "workspace-artifact-manifest.json")


def _manifest_child():
    """Resolve the ledger-domain child from the workspace artifact manifest.

    The proxy preflight refuses any entrypoint absent from the manifest, so
    the client must track the manifest-listed build rather than a pinned
    version directory (the d040aefe pin went stale on 2026-08-23 when the
    workspace was re-materialized to 68c9e7e7).
    """
    with open(MANIFEST) as fh:
        manifest = json.load(fh)
    for artifact in manifest.get('artifacts', []):
        path = artifact.get('path', '')
        if path.endswith('narada-ledger-domain.exe'):
            return path
    raise RuntimeError('narada-ledger-domain.exe not in artifact manifest')


CHILD = _manifest_child()
DOMAIN = ("C:\\Users\\andrey\\src\\mcp-surfaces\\packages/shared/"
          "ledger-domain-epistemic/domain.json")
SITE_ROOT = "C:\\Users\\andrey\\src\\marici"

CMD = [PROXY, "proxy",
       "--surface-id", "epistemic-graph",
       "--child-command", CHILD,
       "--artifact-manifest", MANIFEST,
       "--runtime-contract-version", "8",
       "--entrypoint", CHILD,
       "--child-invocation-kind", "native_entrypoint",
       "--",
       "--domain", DOMAIN,
       "--site-root", SITE_ROOT]


def read_message(stream):
    """Read one newline-delimited JSON-RPC message."""
    line = stream.readline()
    if not line:
        return None
    line = line.strip()
    if not line:
        return read_message(stream)
    return json.loads(line)


def send(stream, msg):
    stream.write(json.dumps(msg) + "\n")
    stream.flush()


def main():
    tool_name = sys.argv[1]
    raw = sys.argv[2] if len(sys.argv) > 2 else "{}"
    if raw.startswith("@"):
        with open(raw[1:], "r", encoding="utf-8") as fh:
            raw = fh.read()
    arguments = json.loads(raw)
    proc = subprocess.Popen(
        CMD,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )
    try:
        send(proc.stdin, {
            "jsonrpc": "2.0", "id": 1, "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "marici-fig-stdio-exception",
                               "version": "0.1.0"},
            },
        })
        init = read_message(proc.stdout)
        if not init or "result" not in init:
            print(json.dumps({"error": "initialize failed", "got": init}))
            return 2
        send(proc.stdin, {"jsonrpc": "2.0",
                          "method": "notifications/initialized"})
        if tool_name == "__list__":
            send(proc.stdin, {"jsonrpc": "2.0", "id": 2, "method": "tools/list",
                              "params": {}})
        else:
            send(proc.stdin, {
                "jsonrpc": "2.0", "id": 2, "method": "tools/call",
                "params": {"name": tool_name, "arguments": arguments},
            })
        while True:
            msg = read_message(proc.stdout)
            if msg is None:
                print(json.dumps({"error": "server closed stream"}))
                return 3
            if msg.get("id") == 2:
                print(json.dumps(msg, indent=1))
                return 0
    finally:
        try:
            proc.stdin.close()
        except Exception:
            pass
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except Exception:
            proc.kill()


if __name__ == "__main__":
    sys.exit(main())
