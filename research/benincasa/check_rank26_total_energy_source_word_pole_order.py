"""Normal pole-order audit for the primitive source-word lattice."""

from __future__ import annotations

import hashlib
import json
import os
import struct
import subprocess

import check_rank26_total_energy_source_word_closure as closure


source = closure.source
P = source.P
AMBIENT = int(os.environ.get("MARICI_AMBIENT", "12"))
ENGINE = source.ROOT / ".narada" / "runtime" / "benincasa" / "sparse_modular_submodule_pole_stream.exe"


def main():
    assert ENGINE.exists()
    checks = source.validate_parameter_jets()
    _, columns = source.rees.column_packet()
    width = len(columns)
    ordered = [None] * width
    for label, column in columns.items(): ordered[column] = label
    x, y, z0 = source.rees.POINT
    z = (z0 % P, 1, 0)
    derivatives = [source.derivative_jet_data(x, y, z, axis) for axis in range(3)]
    source_rows = source.source_word_jets(columns)
    normal_rows = [closure.normal_covariant_derivative(row, ordered, columns, derivatives) for row in source_rows]

    process = subprocess.Popen([str(ENGINE)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert process.stdin is not None
    process.stdin.write(struct.pack("<I", P))
    # Complete relation modules through E^3.
    points = [(x, y, z0 + offset) for offset in source.rees.OFFSETS]
    generators = [source.rees.raw_relations(point, columns) for point in points]
    check = source.rees.raw_relations((x, y, z0 + source.rees.CHECK_OFFSET), columns)
    weights = [source.rees.interpolation_weights(degree) for degree in range(3)]
    for all_rows in zip(*generators, check, strict=True):
        samples, check_row = all_rows[:-1], all_rows[-1]
        assert source.rees.combine((source.rees.combine(samples, source.rees.evaluation_weights(source.rees.CHECK_OFFSET)), check_row), (1,-1)) == {}
        jets = [source.rees.combine(samples, weight) for weight in weights]
        for order in range(1, 4):
            for shift in range(order):
                terms = [{}] * shift + jets[:order-shift]
                source.write_numeric_row(process.stdin, order - 1, source.rees.assemble(tuple(terms), width))
    # Declared lattice through E^3.
    for order in range(1, 4):
        for row in source_rows:
            for shift in range(order):
                source.write_numeric_row(process.stdin, order + 2, source.source_row_at_order(row, width, order, shift))
    # Test nabla, E*nabla, E^2*nabla in independent families.
    for multiplier in range(3):
        for order in range(1, 4):
            for row in normal_rows:
                shifted = (
                    {}
                    if multiplier >= order
                    else source.source_row_at_order(row, width, order, multiplier)
                )
                source.write_numeric_row(process.stdin, 6 + 3 * multiplier + order - 1, shifted)
    process.stdin.close()
    assert process.stdout is not None and process.stderr is not None
    stdout, stderr = process.stdout.read(), process.stderr.read()
    if process.wait(): raise RuntimeError(stderr.decode("utf-8", errors="replace"))
    engine = json.loads(stdout)
    result = {
        "schema":"marici.benincasa.rank26-total-energy-source-word-pole-order.v1",
        "field":P,"point":list(source.rees.POINT),"ambient_relation_degree":AMBIENT,
        "parameter_jet_checks":checks,"source_image_ranks":engine["source_image_ranks"],
        "normal_multiplier_extension_ranks":{
            "1":engine["test_extension_ranks"][0],
            "E_T":engine["test_extension_ranks"][1],
            "E_T^2":engine["test_extension_ranks"][2],
        },
        "rank_engine":{"source":"research/benincasa/sparse_modular_submodule_pole_stream.rs","executable_sha256":hashlib.sha256(ENGINE.read_bytes()).hexdigest().upper(),"result":engine},
    }
    output=source.HERE / f"rank26-total-energy-source-word-pole-order-a{AMBIENT}-p{P}.json"
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__": main()
