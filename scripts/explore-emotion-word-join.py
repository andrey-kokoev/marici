"""Exploratory lexical search, not a native Marici join implementation.

Run: uv run --python 3.12 --with numpy python scripts/explore-emotion-word-join.py
Downloads fastText to the user's cache, not the repository. Retains two cosine
scores; reports independent neighbors and the Pareto frontier without averaging.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import time
import urllib.request
import zipfile

import numpy as np

URL = "https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M-subword.vec.zip"
LICENSE = "https://creativecommons.org/licenses/by-sa/3.0/"


def download(path, url=URL):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_suffix(path.suffix + ".partial")
    start = partial.stat().st_size if partial.exists() else 0
    request = urllib.request.Request(url, headers={"Range": f"bytes={start}-"} if start else {})
    with urllib.request.urlopen(request, timeout=90) as response:
        if start and response.status != 206:
            start = 0
        expected = int(response.headers["Content-Length"])
        received = 0
        tick = time.monotonic()
        with partial.open("ab" if start else "wb") as output:
            while chunk := response.read(4 * 1024 * 1024):
                output.write(chunk)
                received += len(chunk)
                if time.monotonic() - tick > 10:
                    print(f"Download: {(start + received) / 1e6:.1f} MB", flush=True)
                    tick = time.monotonic()
        if received != expected:
            raise RuntimeError(f"Incomplete download: {received} != {expected}")
    # Opening the directory validates ZIP structure; streaming below verifies CRC.
    with zipfile.ZipFile(partial):
        pass
    partial.replace(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--left", default="pissed")
    parser.add_argument("--right", default="disheartened")
    parser.add_argument("--output", default="tmp/emotion-word-join/results.json")
    args = parser.parse_args()
    cache = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / ".cache"))) / "marici" / "embeddings"
    archive = cache / URL.rsplit("/", 1)[1]
    download(archive)
    print(f"Cache: {archive}", flush=True)
    digest = hashlib.sha256()
    with archive.open("rb") as source:
        while chunk := source.read(8 * 1024 * 1024):
            digest.update(chunk)

    anchors = {}
    with zipfile.ZipFile(archive) as z:
        members = [name for name in z.namelist() if name.endswith(".vec")]
        if len(members) != 1:
            raise RuntimeError(f"Unexpected vector members: {members}")
        member = members[0]
        with z.open(member) as source:
            total, dims = map(int, source.readline().split())
            for line in source:
                token, _, values = line.partition(b" ")
                word = token.decode("utf-8")
                if word in (args.left, args.right):
                    vector = np.fromstring(values.decode("ascii"), sep=" ", dtype=np.float32)
                    if len(vector) != dims or not np.isfinite(vector).all() or np.linalg.norm(vector) == 0:
                        raise RuntimeError(f"Invalid anchor: {word}")
                    anchors[word] = vector / np.linalg.norm(vector)
                    print(f"Found anchor: {word}", flush=True)
                if len(anchors) == len(set((args.left, args.right))):
                    break
        if args.left not in anchors or args.right not in anchors:
            raise RuntimeError(f"Missing exact anchor(s); found {list(anchors)}. No substitution performed.")
        matrix = np.stack([anchors[args.left], anchors[args.right]], axis=1)
        words, score_batches, batch = [], [], []
        eligible = re.compile(r"[a-z]+(?:-[a-z]+)*\Z")
        parsed = 0
        invalid = 0

        def flush():
            if not batch:
                return
            vectors = np.stack(batch)
            vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
            score_batches.append(vectors @ matrix)
            batch.clear()

        with z.open(member) as source:
            source.readline()
            for line in source:
                parsed += 1
                token, _, values = line.partition(b" ")
                word = token.decode("utf-8")
                if not eligible.fullmatch(word):
                    continue
                vector = np.fromstring(values.decode("ascii"), sep=" ", dtype=np.float32)
                if len(vector) != dims or not np.isfinite(vector).all() or np.linalg.norm(vector) == 0:
                    invalid += 1
                    continue
                words.append(word)
                batch.append(vector)
                if len(batch) >= 4096:
                    flush()
                if parsed % 100000 == 0:
                    print(f"Read {parsed}/{total} vectors", flush=True)
            flush()
        if parsed != total:
            raise RuntimeError(f"Vector count mismatch: {parsed} != {total}")
    scores = np.concatenate(score_batches)
    candidates = np.array([i for i, word in enumerate(words) if word not in anchors], dtype=np.int64)
    # A candidate is dominated if another is at least as close to both anchors
    # and strictly closer to one. Equal score pairs are retained as separate words.
    order = candidates[np.lexsort((-scores[candidates, 1], -scores[candidates, 0]))]
    frontier = []
    best_right = -np.inf
    previous_frontier_pair = None
    for i in order:
        pair = tuple(float(v) for v in scores[i])
        if pair[1] > best_right or pair == previous_frontier_pair:
            frontier.append(int(i))
            best_right = pair[1]
            previous_frontier_pair = pair

    def record(i):
        return {"word": words[i], "cosine_left": float(scores[i, 0]), "cosine_right": float(scores[i, 1])}

    report = {
        "status": "exploratory-not-a-native-witnessed-join",
        "source": {"url": URL, "license": LICENSE, "archive_sha256": digest.hexdigest(), "archive_path": str(archive), "member": member, "dimensions": dims, "vectors_read": parsed},
        "inputs": {"left": args.left, "right": args.right, "shared_reference": "Both descriptions refer to the same breakdown in the user's work; context retained here but not encoded by these static vectors."},
        "method": {"metric": "cosine on L2-normalized float32 word vectors", "candidate_filter": "lowercase ASCII words, optionally hyphenated; exclude exact inputs; no emotion or POS filtering", "valid_filtered_vocabulary": len(words), "invalid_filtered_vectors": invalid, "selection": "Independent nearest neighbors and Pareto-nondominated score pairs; no summed embedding or aggregate score", "limitation": "Similarity is association, not evidence that a candidate expresses both emotions. Static vectors conflate word senses."},
        "input_cosine": float(anchors[args.left] @ anchors[args.right]),
        "nearest_left": [record(int(i)) for i in candidates[np.argsort(-scores[candidates, 0], kind="stable")[:30]]],
        "nearest_right": [record(int(i)) for i in candidates[np.argsort(-scores[candidates, 1], kind="stable")[:30]]],
        "pareto_frontier": [record(i) for i in frontier],
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"input_cosine": report["input_cosine"], "pareto_frontier": report["pareto_frontier"], "nearest_left": report["nearest_left"][:10], "nearest_right": report["nearest_right"][:10]}, indent=2), flush=True)
    print(f"Report: {output.resolve()}", flush=True)


if __name__ == "__main__":
    main()
