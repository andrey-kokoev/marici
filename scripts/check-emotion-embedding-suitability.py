"""Predeclared suitability checks, not a model leaderboard or native join proof.

uv run --python 3.12 --with numpy --with sentence-transformers==5.1.2 python scripts/check-emotion-embedding-suitability.py
"""
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import sys
import time
import zipfile

import numpy as np

HERE = Path(__file__).resolve().parent
CACHE = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / ".cache"))) / "marici" / "embeddings"
OUTPUT = HERE.parent / "tmp" / "emotion-word-join" / "suitability"
MODELS = [
    {"name": "fasttext-wiki-news-300d-subword", "kind": "static", "url": "https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M-subword.vec.zip", "adapter": "Exact word lookup; for sentences, lowercase tokenization and mean of unnormalized token vectors followed by L2 normalization. Not contextual."},
    {"name": "fasttext-wiki-news-300d-no-subword", "kind": "static", "url": "https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip", "adapter": "Exact word lookup; for sentences, lowercase tokenization and mean of unnormalized token vectors followed by L2 normalization. Not contextual."},
    {"name": "sentence-transformers/all-MiniLM-L6-v2", "kind": "contextual", "revision": "1110a243fdf4706b3f48f1d95db1a4f5529b4d41", "adapter": "Official SentenceTransformer.encode on each full input, default pooling, normalize_embeddings=True, CPU, no prompt."},
    {"name": "sentence-transformers/all-mpnet-base-v2", "kind": "contextual", "revision": "e8c3b32edf5434bc2275fc9bab85f82640a19130", "adapter": "Official SentenceTransformer.encode on each full input, default pooling, normalize_embeddings=True, CPU, no prompt."},
]


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(8 * 1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def static_embeddings(spec, texts):
    module_spec = importlib.util.spec_from_file_location("word_join_download", HERE / "explore-emotion-word-join.py")
    helper = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(helper)
    archive = CACHE / spec["url"].rsplit("/", 1)[1]
    helper.download(archive, spec["url"])
    tokens = {text: re.findall(r"[a-z]+(?:-[a-z]+)*", text.lower()) for text in texts}
    wanted = {token for parts in tokens.values() for token in parts}
    vectors = {}
    with zipfile.ZipFile(archive) as z:
        member, = [name for name in z.namelist() if name.endswith(".vec")]
        with z.open(member) as source:
            total, dims = map(int, source.readline().split())
            parsed = 0
            for line in source:
                parsed += 1
                token, _, values = line.partition(b" ")
                word = token.decode("utf-8")
                if word not in wanted:
                    continue
                vector = np.fromstring(values.decode("ascii"), sep=" ", dtype=np.float32)
                if len(vector) != dims or not np.isfinite(vector).all():
                    raise RuntimeError(f"Invalid vector: {word}")
                vectors[word] = vector
            if parsed != total:
                raise RuntimeError(f"Expected {total} vectors, read {parsed}")
    missing = sorted(wanted - vectors.keys())
    if missing:
        raise RuntimeError(f"Missing exact tokens: {missing}. No substitutions or silent omissions.")
    embeddings = np.stack([np.mean([vectors[token] for token in tokens[text]], axis=0) for text in texts])
    embeddings /= np.linalg.norm(embeddings, axis=1, keepdims=True)
    return embeddings, {"archive_sha256": sha256_file(archive), "member": member, "dimensions": dims, "vectors_read": parsed, "tokens_requested": len(wanted), "missing_tokens": missing, "license": "CC BY-SA 3.0"}


def contextual_embeddings(spec, texts):
    import torch
    from sentence_transformers import SentenceTransformer
    torch.set_num_threads(4)
    model = SentenceTransformer(spec["name"], revision=spec["revision"], device="cpu", cache_folder=str(CACHE / "huggingface"), trust_remote_code=False)
    vectors = model.encode(texts, batch_size=16, normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False)
    return vectors, {"revision": spec["revision"], "dimensions": vectors.shape[1], "max_seq_length": model.max_seq_length, "modules": str(model)}


def main():
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    case_path = HERE / "emotion-embedding-suitability-cases.json"
    case_bytes = case_path.read_bytes()
    suite = json.loads(case_bytes)
    case_hash = hashlib.sha256(case_bytes).hexdigest()
    protocol = {"suite_sha256": case_hash, "suite": suite, "models": MODELS, "numeric_tolerance": 0.000001}
    protocol_bytes = (json.dumps(protocol, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    protocol_hash = hashlib.sha256(protocol_bytes).hexdigest()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    frozen = OUTPUT / f"protocol-{protocol_hash}.json"
    if frozen.exists() and frozen.read_bytes() != protocol_bytes:
        raise RuntimeError("Frozen protocol differs")
    frozen.write_bytes(protocol_bytes)
    print(f"Frozen protocol: {protocol_hash}", flush=True)
    cases = suite["cases"]
    if len({case["id"] for case in cases}) != len(cases):
        raise RuntimeError("Duplicate case identifiers")
    texts = list(dict.fromkeys(case[key] for case in cases for key in ("query", "positive", "negative")))
    index = {text: i for i, text in enumerate(texts)}
    versions = {}
    for package in ("numpy", "sentence-transformers", "transformers", "torch", "huggingface-hub"):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    report = {"protocol_sha256": protocol_hash, "protocol_path": str(frozen), "python": platform.python_version(), "package_versions": versions, "case_count": len(cases), "threshold": 0.000001, "results": [], "scope": suite["status"]}
    result_path = OUTPUT / "results.json"

    def save():
        result_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    save()
    for spec in MODELS:
        print(f"Testing: {spec['name']}", flush=True)
        started = time.monotonic()
        try:
            embeddings, provenance = (static_embeddings if spec["kind"] == "static" else contextual_embeddings)(spec, texts)
            if not np.isfinite(embeddings).all():
                raise RuntimeError("Nonfinite embeddings")
            results = []
            groups = {}
            for case in cases:
                query, positive, negative = (embeddings[index[case[key]]] for key in ("query", "positive", "negative"))
                pos, neg = float(query @ positive), float(query @ negative)
                passed = pos - neg > report["threshold"]
                results.append({**case, "positive_cosine": pos, "negative_cosine": neg, "margin": pos - neg, "pass": passed})
                group = groups.setdefault(case["group"], {"passed": 0, "total": 0, "minimum_margin": float("inf")})
                group["passed"] += int(passed)
                group["total"] += 1
                group["minimum_margin"] = min(group["minimum_margin"], pos - neg)
            for group in groups.values():
                group["pass"] = group["passed"] == group["total"]
            result = {"model": spec, "status": "evaluated", "seconds": time.monotonic() - started, "provenance": provenance, "groups": groups, "all_cases_pass": all(case["pass"] for case in results), "cases": results}
            print(json.dumps({"model": spec["name"], "groups": groups, "failures": [case for case in results if not case["pass"]]}, indent=2), flush=True)
        except Exception as error:
            result = {"model": spec, "status": "not-evaluated", "error_type": type(error).__name__, "error": str(error), "seconds": time.monotonic() - started}
            print(json.dumps(result, indent=2), flush=True)
        report["results"].append(result)
        save()
    print(f"Report: {result_path}", flush=True)
    if any(result["status"] != "evaluated" for result in report["results"]):
        sys.exit(2)


if __name__ == "__main__":
    main()
