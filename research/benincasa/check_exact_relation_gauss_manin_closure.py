"""Test whether the frozen exact relation image is Gauss--Manin stable."""

from __future__ import annotations

import hashlib
import json
import os
import struct
import subprocess
from pathlib import Path

import check_rank26_total_energy_source_word_rees as source
import derive_rank26_source_word_basis as basis


P=source.P
AMBIENT=int(os.environ.get("MARICI_AMBIENT","8"))
POINT=tuple(int(value) for value in os.environ.get("MARICI_JET_POINT","2,3,-4").split(","))
SAFE_INTERIOR=os.environ.get("MARICI_SAFE_INTERIOR","0")=="1"
ENGINE=source.ROOT/".narada"/"runtime"/"benincasa"/"sparse_modular_submodule_closure_stream.exe"


def coefficient(row,degree): return {column:jet[degree] for column,jet in row.items() if jet[degree]}


def interior(row,ordered):
    for column in row:
        k_pole,*rest=ordered[column]; exponent=rest.pop(); levels=rest
        if k_pole>=source.rees.charts.K_DEPTH:return False
        if any(level>=source.rees.charts.Q_DEPTH for level in levels):return False
        if sum(exponent)>=AMBIENT:return False
    return True


def main():
    assert ENGINE.exists()
    _,columns=source.rees.column_packet(); width=len(columns)
    ordered=[None]*width
    for label,column in columns.items(): ordered[column]=label
    x,y,z0=POINT; z=(z0%P,1,0)
    derivatives=[source.derivative_jet_data(x,y,z,axis) for axis in range(3)]
    points=[(x,y,z0+offset) for offset in source.rees.OFFSETS]
    generators=[source.rees.raw_relations(point,columns) for point in points]
    check=source.rees.raw_relations((x,y,z0+source.rees.CHECK_OFFSET),columns)
    first=source.rees.interpolation_weights(1)
    evaluation=source.rees.evaluation_weights(source.rees.CHECK_OFFSET)
    relations=[]; derivatives_rows=[]; test_provenance=[]
    for generator_index,all_rows in enumerate(zip(*generators,check,strict=True)):
        samples,check_row=all_rows[:-1],all_rows[-1]
        assert source.rees.combine((source.rees.combine(samples,evaluation),check_row),(1,-1))=={}
        r0=dict(samples[source.rees.OFFSETS.index(0)])
        relations.append(r0)
        if SAFE_INTERIOR and not interior(r0,ordered):
            continue
        r1=source.rees.combine(samples,first)
        jet_row={column:(value,0,0) for column,value in r0.items()}
        connection=coefficient(source.raw_connection(jet_row,2,ordered,columns,derivatives),0)
        covariant=dict(r1)
        for column,value in connection.items():
            next_value=(covariant.get(column,0)+value)%P
            if next_value: covariant[column]=next_value
            else: covariant.pop(column,None)
        derivatives_rows.append(covariant)
        test_provenance.append({"generator_index":generator_index,"source_labels":[list(ordered[column]) for column in sorted(r0)]})
    process=subprocess.Popen([str(ENGINE)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    assert process.stdin is not None
    process.stdin.write(struct.pack("<I",P))
    for row in relations: source.write_numeric_row(process.stdin,0,row)
    for row in derivatives_rows: source.write_numeric_row(process.stdin,4,row)
    process.stdin.close();assert process.stdout is not None and process.stderr is not None
    stdout,stderr=process.stdout.read(),process.stderr.read()
    if process.wait():raise RuntimeError(stderr.decode("utf-8",errors="replace"))
    engine=json.loads(stdout)
    residual_records=[]
    if SAFE_INTERIOR:
        old_ambient=basis.AMBIENT;basis.AMBIENT=AMBIENT
        try:pres=basis.presentation(POINT)
        finally:basis.AMBIENT=old_ambient
        assert len(pres["pivots"])==engine["relation_ranks"][0]
        for provenance,row in zip(test_provenance,derivatives_rows,strict=True):
            residual=source.rees.base.reduce_row(row,pres["pivots"])
            if residual:
                residual_records.append({**provenance,"residual_support":len(residual),"residual_labels":[list(ordered[column]) for column in sorted(residual)]})
    result={
      "schema":"marici.benincasa.exact-relation-gauss-manin-closure.v1",
      "field":P,"point":list(POINT),"ambient_relation_degree":AMBIENT,
      "relation_count":len(relations),"relation_rank":engine["relation_ranks"][0],
      "covariant_test_count":len(derivatives_rows),
      "safe_interior_only":SAFE_INTERIOR,
      "covariant_relation_extension_rank":engine["test_extension_ranks"][0],
      "gauss_manin_stable":engine["test_extension_ranks"][0]==0,
      "normal_operator":"partial_z+A_z",
      "nonzero_residual_records":residual_records,
      "rank_engine":{"executable_sha256":hashlib.sha256(ENGINE.read_bytes()).hexdigest().upper(),"result":engine},
    }
    suffix="-".join(f"m{-v}" if v<0 else str(v) for v in POINT)
    mode="-interior" if SAFE_INTERIOR else ""
    output=Path(__file__).with_name(f"exact-relation-gauss-manin-closure{mode}-a{AMBIENT}-p{P}-point-{suffix}.json")
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":main()
