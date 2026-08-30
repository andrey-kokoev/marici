"""Depth census of the true multivariate covariant source-jet closure."""

from __future__ import annotations

import contextlib
import importlib
import io
import json
import os
from pathlib import Path

import derive_rank26_source_word_basis as basis


with contextlib.redirect_stdout(io.StringIO()):
    source = importlib.import_module("check_rank26_total_energy_source_word_rees")

P=source.P
DEPTH=int(os.environ.get("MARICI_JET_DEPTH","4"))
AMBIENT=int(os.environ.get("MARICI_AMBIENT","12"))
ZERO=(0,0,0)


def jclean(value): return {key:coefficient%P for key,coefficient in value.items() if coefficient%P}
def jconstant(value): return {} if value%P==0 else {ZERO:value%P}
def jadd(left,right,scale=1):
    result=dict(left)
    for key,value in right.items():
        next_value=(result.get(key,0)+scale*value)%P
        if next_value: result[key]=next_value
        else: result.pop(key,None)
    return result
def jscale(value,scale): return jclean({key:scale*coefficient for key,coefficient in value.items()})
def jmul(left,right):
    result={}
    for a,av in left.items():
        for b,bv in right.items():
            key=tuple(a[i]+b[i] for i in range(3))
            if sum(key)<=DEPTH:
                result[key]=(result.get(key,0)+av*bv)%P
    return jclean(result)
def jsquare(value): return jmul(value,value)
def jderivative(value,axis):
    result={}
    for key,coefficient in value.items():
        if key[axis]:
            target=list(key); factor=target[axis]; target[axis]-=1
            result[tuple(target)]=(result.get(tuple(target),0)+factor*coefficient)%P
    return jclean(result)


def parameter(value,axis):
    result=jconstant(value); key=[0,0,0]; key[axis]=1; result[tuple(key)]=1
    return result


def fiber_data(point):
    x,y,z=(parameter(point[i],i) for i in range(3))
    energy=jadd(jadd(x,y),z)
    x2,y2,z2,c2=map(jsquare,(x,y,z,energy))
    xm=jadd(x2,jadd(y2,z2),-1); ym=jadd(y2,jadd(x2,z2),-1); zm=jadd(z2,jadd(x2,y2),-1)
    k={
      (4,0):x2,
      (2,2):jscale(jadd(jadd(x2,y2),z2,-1),-1),
      (0,4):y2,
      (2,0):jadd(jmul(x2,xm),jmul(c2,jadd(y2,jadd(x2,z2),-1))),
      (0,2):jadd(jmul(y2,ym),jmul(c2,jadd(x2,jadd(y2,z2),-1))),
      (0,0):jadd(jadd(jmul(z2,jsquare(c2)),jmul(jmul(c2,z2),zm)),jmul(jmul(z2,x2),y2)),
    }
    q={
      "g1":{(0,1):jconstant(1),(0,0):jscale(jadd(y,z),-1)},
      "g2":{(1,0):jconstant(1),(0,0):jscale(jadd(x,z),-1)},
      "g3":{(1,0):jconstant(1),(0,1):jconstant(1),(0,0):z},
      "g23":{(0,1):jconstant(1),(0,0):jscale(x,-1)},
      "g31":{(1,0):jconstant(1),(0,0):jscale(y,-1)},
    }
    return k,q


def padd(target,source_poly,scale=1):
    for exponent,value in source_poly.items():
        target[exponent]=jadd(target.get(exponent,{}),value,scale)
        if not target[exponent]: target.pop(exponent)


def row_add(target,column,value):
    target[column]=jadd(target.get(column,{}),value)
    if not target[column]: target.pop(column)


def raw_source(columns,q):
    numerator=dict(q["g23"]); padd(numerator,q["g31"])
    prefix=(0,1,1,1,1,1)
    return {columns[prefix+(exponent,)]:value for exponent,value in numerator.items()}


def raw_connection(row,axis,ordered,columns,k,q):
    kd={exponent:jderivative(value,axis) for exponent,value in k.items()}
    qd={name:{exponent:jderivative(value,axis) for exponent,value in poly.items()} for name,poly in q.items()}
    result={}
    for column,coefficient in row.items():
        k_pole,*rest=ordered[column]; exponent=rest.pop(); levels=rest
        if k_pole<source.rees.charts.K_DEPTH:
            for term,value in kd.items():
                target=(k_pole+1,*levels,source.rees.base.shifted(exponent,term))
                if target in columns: row_add(result,columns[target],jscale(jmul(coefficient,value),source.rees.charts.GAMMA-k_pole))
        for qi,level in enumerate(levels):
            if level>=source.rees.charts.Q_DEPTH: continue
            raised=list(levels); raised[qi]+=1
            for term,value in qd[source.rees.NAMES[qi]].items():
                target=(k_pole,*raised,source.rees.base.shifted(exponent,term))
                if target in columns: row_add(result,columns[target],jscale(jmul(coefficient,value),-level))
    return result


def covariant(row,axis,ordered,columns,k,q):
    result={column:jderivative(value,axis) for column,value in row.items()}
    result={column:value for column,value in result.items() if value}
    connection=raw_connection(row,axis,ordered,columns,k,q)
    for column,value in connection.items(): row_add(result,column,value)
    return result


def center(row): return {column:value[ZERO] for column,value in row.items() if ZERO in value}
def polynomial_center(poly): return {exponent:value[ZERO] for exponent,value in poly.items() if ZERO in value}


def main():
    point=tuple(int(value) for value in os.environ.get("MARICI_JET_POINT","2,3,-4").split(","))
    old_ambient=basis.AMBIENT; basis.AMBIENT=AMBIENT
    try: pres=basis.presentation(point)
    finally: basis.AMBIENT=old_ambient
    ordered=pres["ordered_columns"]; columns=pres["columns"]
    k,q=fiber_data(point)
    numeric_k,numeric_q=source.rees.base.fiber_data(*point)
    assert polynomial_center(k)==numeric_k
    assert all(polynomial_center(q[name])==numeric_q[name] for name in source.rees.NAMES)
    derivative_checks=0
    for axis in range(3):
        expected_k,expected_q=source.audit.parameter_derivative_data(source.rees.base.fiber_data,point,axis)
        assert {exponent:value for exponent,jet in k.items() if (value:=jderivative(jet,axis).get(ZERO,0))}==expected_k
        derivative_checks+=1
        for name in source.rees.NAMES:
            observed={exponent:value for exponent,jet in q[name].items() if (value:=jderivative(jet,axis).get(ZERO,0))}
            assert observed==expected_q[name]
            derivative_checks+=1
    roots=[raw_source(columns,q)]
    span={}; ranks=[]; word_counts=[]; frontier=roots
    for depth in range(DEPTH+1):
        for row in frontier:
            quotient=source.rees.base.reduce_row(center(row),pres["pivots"])
            source.rees.base.add_pivot(dict(quotient),span)
        ranks.append(len(span)); word_counts.append(len(frontier))
        if depth<DEPTH:
            frontier=[covariant(row,axis,ordered,columns,k,q) for row in frontier for axis in range(3)]
    result={
      "schema":"marici.benincasa.true-covariant-source-jet-closure.v1",
      "field":P,"point":list(point),"ambient_relation_degree":AMBIENT,
      "maximum_jet_depth":DEPTH,"words_per_exact_depth":word_counts,
      "fiber_center_checks":6,"parameter_derivative_checks":derivative_checks,
      "cumulative_covariant_ranks":ranks,
      "convention":"all 3^d true covariant words retained; no dependent intermediate word is pruned",
    }
    suffix="-".join(f"m{-v}" if v<0 else str(v) for v in point)
    output=Path(__file__).with_name(f"true-covariant-source-jet-closure-d{DEPTH}-a{AMBIENT}-p{P}-point-{suffix}.json")
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__": main()
