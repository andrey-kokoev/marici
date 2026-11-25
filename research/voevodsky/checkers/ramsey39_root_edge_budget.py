"""Check the local edge-budget obstruction for a putative (3,9;36) graph.
Input assumption: McKay's catalogue of (3,8;27) graphs is exhaustive.
"""
from collections import Counter
import gzip
from pathlib import Path

path = Path(__file__).resolve().parents[2] / 'chatgpt/ramsey/pauli-realization-catalogues/r38_27.g6.gz'
hist = Counter()
with gzip.open(path, 'rb') as records:
    for record in records:
        header, *payload = record.rstrip(b'\r\n')
        assert header - 63 == 27 and len(payload) == 59
        assert (payload[-1] - 63) % 8 == 0  # 351 edgeslots + 3 zero padding bits
        hist[sum((c - 63).bit_count() for c in payload)] += 1
need = 36 * 8 // 2 - 8 * 8
print('parents:', hist.total(), 'required edges:', need, 'observed:', sorted(hist.items()))
assert hist.total() == 477142 and min(hist) == 85 and need == 80
