"""Filter a tagged triangle-wall packet to a selected marked-family subset."""

import argparse
import struct
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("input", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("--marked-mask", type=lambda value: int(value, 0), required=True)
args = parser.parse_args()
if not 0 <= args.marked_mask < 32:
    raise ValueError("marked mask must be between 0 and 31")

data = args.input.read_bytes()
if data[:8] != b"MRCIDR03":
    raise ValueError("input must be a tagged MRCIDR03 packet")
prime, ambient, columns, row_count, _ = struct.unpack_from("<IIIII", data, 8)
cursor = 28
records = []
for _ in range(row_count):
    start = cursor
    family = struct.unpack_from("<I", data, cursor)[0]
    cursor += 4
    for _ in range(3):
        term_count = struct.unpack_from("<I", data, cursor)[0]
        cursor += 4 + 8 * term_count
    if family < 2 or args.marked_mask & (1 << (family - 2)):
        records.append(data[start:cursor])
if cursor != len(data):
    raise ValueError("packet has trailing bytes")

with args.output.open("wb") as stream:
    stream.write(b"MRCIDR03")
    stream.write(struct.pack("<IIIII", prime, ambient, columns, len(records), 0))
    for record in records:
        stream.write(record)

print(f"mask={args.marked_mask:#04x} rows={len(records)} output={args.output}")
