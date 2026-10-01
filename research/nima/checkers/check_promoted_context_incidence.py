"""Derive leaf-pair coefficients of a promoted-value composition probe.

Uses the actual endpoint keys and two horizontal candidates of the rung fixture.
Product coefficients follow from multiplying family means, not a claim about
physical statistical independence. Choosing this probe is explicit.
"""
from collections import defaultdict
from contextlib import redirect_stdout
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import io
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
with redirect_stdout(io.StringIO()):
    model=runpy.run_path(str(Path(__file__).with_name('check_rung_transport_diagram.py')))
add,scale,mul=(model[k] for k in ('add','scale','mul'))
Z=model['m']['Z']; r=scale(F(1,2),model['I']); d=model['physical_reference'].value
assert mul(d,r)==mul(r,d)==model['I']
mean,leaves,indexed,unindex=(model[k] for k in ('mean','leaves','indexed','unindex'))
promotion=model['incoming_promotion']


def bridge(b,a): return mul(mul(b,r),a)
def total(items):
    out=Z
    for item in items: out=add(out,item)
    return out


def promote(rows,policy):
    return promotion(promotion(rows,1,policy),2,policy)


def leaf_law(row):
    if not row.members: return {row.label:F(1)}
    assert row.mass==sum(child.mass for child in row.members)
    result=defaultdict(F)
    for child in row.members:
        for label,p in leaf_law(child).items():
            result[label]+=F(child.mass,row.mass)*p
    assert sum(result.values())==1
    return dict(result)


def incidence(families,staged=False):
    """Choose one family by mass; expand its two operand occurrences."""
    mass=sum(f.mass for f in families); pi=defaultdict(F)
    for family in families:
        law=leaf_law(family) if staged else {x.label:F(x.mass,family.mass) for x in leaves((family,))}
        for right,p in law.items():
            for left,q in law.items(): pi[right,left]+=F(family.mass,mass)*p*q
    return dict(pi)


def paired_value(pi,rows):
    by_label={row.label:row.value for row in rows}
    return total(scale(weight,bridge(by_label[right],by_label[left]))
                 for (right,left),weight in pi.items())


reports=[]
for weighted in (False,True):
    rows=tuple(replace(row,mass=i+1) if weighted else row for i,row in enumerate(model['source']))
    mass=sum(row.mass for row in rows)
    first=promotion(rows,1,'inherited')
    assert len(first)==32
    if not weighted:
        assert sorted(len(leaves((f,))) for f in first)==[1]*16+[4]+[6]*6+[9]*9
    by_policy={}; signatures={}
    for policy in ('inherited','common'):
        final=promote(rows,policy)
        pi=incidence(final)
        assert pi==incidence(final,staged=True)
        assert leaves(final)==rows and mean(final)==mean(rows)
        assert sum(pi.values())==1 and all(value>0 for value in pi.values())
        right_mass=defaultdict(F); left_mass=defaultdict(F)
        for (right,left),weight in pi.items():
            right_mass[right]+=weight; left_mass[left]+=weight
        expected={row.label:F(row.mass,mass) for row in rows}
        assert dict(right_mass)==dict(left_mass)==expected
        # Passive retained indexing cannot change this leaf-labelled incidence.
        for field in ('source','target'):
            assert incidence(promote(unindex(indexed(rows,field)),policy))==pi
        expanded=paired_value(pi,rows)
        direct=total(scale(F(f.mass,mass),bridge(f.value,f.value)) for f in final)
        assert expanded==direct
        signatures[policy]=direct
        by_policy[policy]={'families':len(final),'supported_leaf_pairs':len(pi)}
    assert by_policy=={'inherited':{'families':32,'supported_leaf_pairs':977},
                       'common':{'families':1,'supported_leaf_pairs':18769}}
    assert signatures['inherited']!=signatures['common']
    assert signatures['common']==bridge(mean(rows),mean(rows))
    # The difference is exactly the between-family ordered covariance.
    mu=mean(rows)
    between=total(scale(F(f.mass,mass),bridge(add(f.value,scale(-1,mu)),
                                              add(f.value,scale(-1,mu)))) for f in first)
    difference=add(signatures['inherited'],scale(-1,signatures['common']))
    assert difference==between!=Z
    diagonal={(row.label,row.label):F(row.mass,mass) for row in rows}
    diagonal_value=paired_value(diagonal,rows)
    within=total(scale(F(row.mass,mass),bridge(add(row.value,scale(-1,f.value)),
                                                add(row.value,scale(-1,f.value))))
                 for f in first for row in leaves((f,)))
    assert add(diagonal_value,scale(-1,signatures['inherited']))==within
    assert within!=Z
    # Reference subtraction is common to all policies and cannot erase the gap.
    assert add(signatures['inherited'],scale(-1,d))!=add(signatures['common'],scale(-1,d))
    reports.append({'weights':'positive nonuniform' if weighted else 'unit leaf masses',
                    'profiles':by_policy,
                    'between_family_difference':[[str(x) for x in row] for row in difference],
                    'within_family_difference':[[str(x) for x in row] for row in within]})

result={
    'status':'passed',
    'classification':'promoted_value_composition_derives_leaf_incidence_and_separates_endpoint_policies',
    'obligation':'source-operation realization and route/coherencer compatibility',
    'stratum':'Actual137-slot rung fixture; declared promoted-value self-composition; fixed invertible reference; two endpoint policies',
    'checks':{'staged_leaf_disintegration':True,'presentation_covariance':True,
              'marginals_and_family_masses':True,'matrix_expansion':True,
              'first_moment_agreement':True,'second_order_policy_separation':True,
              'within_between_covariance_accounting':True},
    'reports':reports,
    'unsupported':['selection of the intended next-level endpoints',
                   'selection of promoted-value versus full-member composition',
                   'interpretation as physical statistical independence',
                   'physical metric and reference normalization'],
    'next_constructor':'Specify which retained family ports the intended generator composes and whether it acts on member records or promoted matrix values.'
}
output=ROOT/'research/nima/results/promoted-context-incidence.json'
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
