"""Replay cited Flavor source checkers before a DPC gate consumes their results.

A DPC gate may use a prior result only after that result's checker has been
replayed successfully in the current environment.  During one audit session a
caller may set FLAVOR_DPC_REPLAY_SESSION; the helper then memoizes successful
replays by checker and result digest so nested gates do not repeatedly replay
the same unchanged source.  Sympy-backed historical checkers use the
repository-local ephemeral dependency target .ai/tmp/flavor-dpc-python-deps
when present.
"""

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

CHECKERS = Path(__file__).resolve().parent
FLAVOR = CHECKERS.parent
REPO = FLAVOR.parents[1]
DEP_TARGET = REPO / ".ai" / "tmp" / "flavor-dpc-python-deps"
_ACTIVE = set()


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _checker_for(number: int) -> Path:
    matches = sorted(CHECKERS.glob(f"wp{number}_*.py"))
    if not matches:
        raise AssertionError(f"missing source checker for WP{number}")
    return matches[0]


def _result_for(number: int) -> Path:
    matches = sorted((FLAVOR / "results").glob(f"wp{number}_*.json"))
    if not matches:
        raise AssertionError(f"missing source result for WP{number}")
    return matches[0]


def _result_passed(path: Path) -> bool:
    data = json.loads(path.read_text())
    return (
        data.get("status") == "PASS"
        or data.get("all_pass") is True
        or (data.get("summary") or {}).get("all_passed") is True
    )


def _session_cache() -> tuple[Path | None, dict]:
    raw = os.environ.get("FLAVOR_DPC_REPLAY_SESSION", "")
    if not raw:
        return None, {}
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", raw)
    path = REPO / ".ai" / "tmp" / f"flavor-dpc-replay-{safe}.json"
    if path.exists():
        return path, json.loads(path.read_text())
    return path, {}


def _write_cache(path: Path | None, cache: dict) -> None:
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n")


def replay_source_checkers(*numbers: int) -> list[dict]:
    """Replay each cited checker and return durable replay records."""
    records = []
    env = os.environ.copy()
    if DEP_TARGET.exists():
        env["PYTHONPATH"] = str(DEP_TARGET) + os.pathsep + env.get("PYTHONPATH", "")
    cache_path, cache = _session_cache()
    for number in numbers:
        if number in _ACTIVE:
            raise AssertionError(f"cyclic source replay at WP{number}")
        checker = _checker_for(number)
        result_path = _result_for(number)
        checker_digest = _sha256(checker)
        result_digest = _sha256(result_path)
        key = str(number)
        cached = cache.get(key)
        if (
            cached
            and cached.get("checker_sha256") == checker_digest
            and cached.get("result_sha256") == result_digest
            and _result_passed(result_path)
        ):
            records.append({**cached, "status": "session_replayed"})
            continue
        _ACTIVE.add(number)
        try:
            completed = subprocess.run(
                [sys.executable, str(checker)],
                cwd=REPO,
                env=env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=180,
                check=False,
            )
        finally:
            _ACTIVE.remove(number)
        ok = completed.returncode == 0 and (
            "PASS" in completed.stdout or _result_passed(result_path)
        )
        if not ok:
            tail = completed.stdout[-2000:]
            raise AssertionError(
                f"source replay failed for WP{number} ({checker.name}): {tail}"
            )
        record = {
            "work_package": f"WP{number}",
            "checker": str(checker.relative_to(REPO)),
            "result": str(result_path.relative_to(REPO)),
            "status": "replayed",
            "checker_sha256": checker_digest,
            "result_sha256": _sha256(result_path),
        }
        cache[key] = record
        _write_cache(cache_path, cache)
        records.append(record)
    return records
