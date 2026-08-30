"""Test the labelled D -> D+step cutoff inclusion as a GM adapter."""

from __future__ import annotations

import hashlib
import json
import os
import struct
import subprocess
from itertools import product
from pathlib import Path

import check_rank26_total_energy_source_word_rees as source


P=source.P
SMALL=int(os.environ.get("MARICI_SMALL_AMBIENT","8"))
STEP=int(os.environ.get("MARICI_AMBIENT_STEP","2"))
BIG=SMALL+STEP
SMALL_K_OVERRIDE=os.environ.get("MARICI_SMALL_K_DEPTH")
SMALL_Q_OVERRIDE=os.environ.get("MARICI_SMALL_Q_DEPTHS")
BIG_K_DELTA=int(os.environ.get("MARICI_BIG_K_DEPTH_DELTA","0"))
BIG_Q_DELTA=int(os.environ.get("MARICI_BIG_Q_DEPTH_DELTA","0"))
BIG_Q_OCCURRENCE=os.environ.get("MARICI_BIG_Q_OCCURRENCE")
POINT=tuple(int(value) for value in os.environ.get("MARICI_JET_POINT","2,3,-4").split(","))
AXIS=int(os.environ.get("MARICI_DERIVATIVE_AXIS","2"))
ENGINE=source.ROOT/".narada"/"runtime"/"benincasa"/"sparse_modular_submodule_closure_stream.exe"


def packet(ambient,k_depth,q_depths):
    low_monomials=source.rees.base.monomials_at_most(source.rees.CUTOFF)
    low_labels=[(0,*levels,monomial) for levels in product(range(1,2),repeat=len(source.rees.NAMES)) for monomial in low_monomials]
    low_set=set(low_labels);ambient_monomials=source.rees.base.monomials_at_most(ambient+4);ordered=list(low_labels)
    for k_pole in range(k_depth+1):
        for levels in product(*(range(1,depth+1) for depth in q_depths)):
            ordered.extend(label for monomial in ambient_monomials if (label:=(k_pole,*levels,monomial)) not in low_set)
    return low_labels,{label:index for index,label in enumerate(ordered)}


def relations(point,columns,ambient,k_depth,q_depths):
    k,all_q=source.rees.base.fiber_data(*point);q=[all_q[name] for name in source.rees.NAMES]
    kd=[source.rees.base.derivative(k,axis) for axis in range(2)]
    qd=[[source.rees.base.derivative(poly,axis) for axis in range(2)] for poly in q]
    rows=[]
    for k_pole in range(k_depth):
      for levels in product(*(range(1,depth+1) for depth in q_depths)):
        if any(levels[i]==q_depths[i] for i in range(len(levels))):continue
        for axis in range(2):
          for exponent in source.rees.base.monomials_at_most(ambient):
            row={}
            if exponent[axis]:
              derived=list(exponent);derived[axis]-=1;source.rees.add(row,columns[(k_pole,*levels,tuple(derived))],exponent[axis])
            for term,value in kd[axis].items():source.rees.add(row,columns[(k_pole+1,*levels,source.rees.base.shifted(exponent,term))],(source.rees.charts.GAMMA-k_pole)*value)
            for qi,q_pole in enumerate(levels):
              raised=list(levels);raised[qi]+=1
              for term,value in qd[qi][axis].items():source.rees.add(row,columns[(k_pole,*raised,source.rees.base.shifted(exponent,term))],-q_pole*value)
            rows.append(row)
    for k_pole in range(k_depth):
      for levels in product(*(range(1,depth+1) for depth in q_depths)):
        for exponent in source.rees.base.monomials_at_most(ambient-4):
          row={columns[(k_pole,*levels,exponent)]:1}
          for term,value in source.rees.base.multiply_monomial(k,exponent,-1):source.rees.add(row,columns[(k_pole+1,*levels,term)],value)
          rows.append(row)
    for qi,qpoly in enumerate(q):
      for k_pole in range(k_depth+1):
        for levels in product(*(range(1,depth+1) for depth in q_depths)):
          if levels[qi]==q_depths[qi]:continue
          raised=list(levels);raised[qi]+=1
          for exponent in source.rees.base.monomials_at_most(ambient-1):
            row={columns[(k_pole,*levels,exponent)]:1}
            for term,value in source.rees.base.multiply_monomial(qpoly,exponent,-1):source.rees.add(row,columns[(k_pole,*raised,term)],value)
            rows.append(row)
    return rows


def raw_connection_depths(row,axis,ordered,columns,derivatives,k_depth,q_depths):
    kd,qd=derivatives[axis];result={}
    for column,coefficient in row.items():
      k_pole,*rest=ordered[column];exponent=rest.pop();levels=rest
      if k_pole<k_depth:
        for term,value in kd.items():
          target=(k_pole+1,*levels,source.rees.base.shifted(exponent,term))
          if target in columns:source.row_add(result,columns[target],source.jet_scale(source.jet_multiply(coefficient,value),source.rees.charts.GAMMA-k_pole))
      for qi,level in enumerate(levels):
        if level>=q_depths[qi]:continue
        raised=list(levels);raised[qi]+=1
        for term,value in qd[source.rees.NAMES[qi]].items():
          target=(k_pole,*raised,source.rees.base.shifted(exponent,term))
          if target in columns:source.row_add(result,columns[target],source.jet_scale(source.jet_multiply(coefficient,value),-level))
    return result


def coefficient(row,degree):return {column:jet[degree] for column,jet in row.items() if jet[degree]}


def shifted_point(point,axis,offset):
    result=list(point);result[axis]+=offset;return tuple(result)


def main():
    small_q=source.rees.charts.Q_DEPTH
    small_k=source.rees.charts.K_DEPTH if SMALL_K_OVERRIDE is None else int(SMALL_K_OVERRIDE)
    small_q_depths=([small_q]*len(source.rees.NAMES) if SMALL_Q_OVERRIDE is None else [int(value) for value in SMALL_Q_OVERRIDE.split(",")])
    assert len(small_q_depths)==len(source.rees.NAMES)
    big_q_depths=[depth+BIG_Q_DELTA for depth in small_q_depths]
    selected_occurrences=[] if not BIG_Q_OCCURRENCE else BIG_Q_OCCURRENCE.split(",")
    if selected_occurrences:
        for name in selected_occurrences:big_q_depths[source.rees.NAMES.index(name)]+=1
    big_k=small_k+BIG_K_DELTA
    _,small_columns=packet(SMALL,small_k,small_q_depths);_,big_columns=packet(BIG,big_k,big_q_depths)
    small_ordered=[None]*len(small_columns);big_ordered=[None]*len(big_columns)
    for label,column in small_columns.items():small_ordered[column]=label
    for label,column in big_columns.items():big_ordered[column]=label
    assert all(label in big_columns for label in small_columns)
    assert AXIS in (0,1,2)
    x,y,z0=POINT;z=(z0%P,0,0)
    derivatives=[source.derivative_jet_data(x,y,z,axis) for axis in range(3)]
    offsets=source.rees.OFFSETS
    small_samples=[relations(shifted_point(POINT,AXIS,offset),small_columns,SMALL,small_k,small_q_depths) for offset in offsets]
    check=relations(shifted_point(POINT,AXIS,source.rees.CHECK_OFFSET),small_columns,SMALL,small_k,small_q_depths)
    first=source.rees.interpolation_weights(1);evaluation=source.rees.evaluation_weights(source.rees.CHECK_OFFSET)
    tests=[]
    for all_rows in zip(*small_samples,check,strict=True):
        samples,check_row=all_rows[:-1],all_rows[-1]
        assert source.rees.combine((source.rees.combine(samples,evaluation),check_row),(1,-1))=={}
        r0=dict(samples[offsets.index(0)]);r1=source.rees.combine(samples,first)
        embedded0={big_columns[small_ordered[column]]:value for column,value in r0.items()}
        embedded1={big_columns[small_ordered[column]]:value for column,value in r1.items()}
        jet_row={column:(value,0,0) for column,value in embedded0.items()}
        connection=coefficient(raw_connection_depths(jet_row,AXIS,big_ordered,big_columns,derivatives,big_k,big_q_depths),0)
        covariant=dict(embedded1)
        for column,value in connection.items():
            next_value=(covariant.get(column,0)+value)%P
            if next_value:covariant[column]=next_value
            else:covariant.pop(column,None)
        tests.append(covariant)
    big_relations=relations(POINT,big_columns,BIG,big_k,big_q_depths)
    process=subprocess.Popen([str(ENGINE)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    assert process.stdin is not None
    process.stdin.write(struct.pack("<I",P))
    relation_count=0
    for row in big_relations:
        relation_count+=1;source.write_numeric_row(process.stdin,0,row)
    for row in tests:source.write_numeric_row(process.stdin,4,row)
    process.stdin.close();assert process.stdout is not None and process.stderr is not None
    stdout,stderr=process.stdout.read(),process.stderr.read()
    if process.wait():raise RuntimeError(stderr.decode("utf-8",errors="replace"))
    engine=json.loads(stdout)
    result={
      "schema":"marici.benincasa.cutoff-inclusion-gauss-manin-adapter.v1",
      "field":P,"point":list(POINT),"derivative_axis":AXIS,"small_ambient":SMALL,"big_ambient":BIG,
      "small_K_depth":small_k,"big_K_depth":big_k,"small_q_depths":small_q_depths,"big_q_depths":big_q_depths,
      "small_column_count":len(small_columns),"big_column_count":len(big_columns),
      "small_relation_test_count":len(tests),"big_relation_count":relation_count,
      "adapter_cone_rank":engine["test_extension_ranks"][0],
      "gauss_manin_compatible":engine["test_extension_ranks"][0]==0,
      "rank_engine":{"executable_sha256":hashlib.sha256(ENGINE.read_bytes()).hexdigest().upper(),"result":engine},
      "convention":f"literal label inclusion; derivative and A_{AXIS} evaluated in the big presentation",
    }
    suffix="-".join(f"m{-v}" if v<0 else str(v) for v in POINT)
    occurrence_suffix="" if not selected_occurrences else "-"+"-".join(selected_occurrences)+"plus1"
    depth_suffix=(f"-kplus{BIG_K_DELTA}-qplus{BIG_Q_DELTA}" if BIG_K_DELTA or BIG_Q_DELTA else "")+occurrence_suffix
    axis_suffix="" if AXIS==2 else f"-axis{AXIS}"
    output=Path(__file__).with_name(f"cutoff-inclusion-gauss-manin-adapter-a{SMALL}-to-a{BIG}{depth_suffix}{axis_suffix}-p{P}-point-{suffix}.json")
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":main()
