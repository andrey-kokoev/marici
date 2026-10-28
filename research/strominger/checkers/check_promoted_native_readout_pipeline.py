"""Exact executable composition controls for the proven native readout schema.
Python syntax mirrors the native amplitude tree; it is not extracted Agda code.
"""
from dataclasses import replace
from itertools import product
from pathlib import Path
import copy
import hashlib
import json
import sympy as s
from check_oscillator_retained_cone import API, Row, build, triangle_decode
from check_oscillator_fcc_representation import encode, decode

ROOT=Path(__file__).resolve().parents[3]


def factor(k): return ('factor',k)
def mul(a,b): return ('product',a,b)
def add(a,b): return ('sum',a,b)


def compile_expr(expr, fields):
    if expr[0]=='factor':
        k=expr[1]
        # Marked local factor seed. No answer seed is admitted.
        return ('factor-seed',k,fields[k])
    if expr[0]=='one': return ('one-seed',s.Integer(1))
    if expr[0] not in ('sum','product'): raise ValueError('Unknown operation')
    return ('Pi',('operator-seed',expr[0]),compile_expr(expr[1],fields),compile_expr(expr[2],fields))


def run(tree):
    if tree[0]=='factor-seed': return tree[2]
    if tree[0]=='one-seed': return tree[1]
    if tree[0]!='Pi' or tree[1][0]!='operator-seed': raise ValueError('Malformed native schema')
    left,right=run(tree[2]),run(tree[3])
    return left+right if tree[1][1]=='sum' else left*right


def pipeline(packet,expr):
    # Only the retained output is an input; no original source is captured.
    standalone=copy.deepcopy(encode(build(packet),(3,0,2,1)))
    recovered=triangle_decode(decode(standalone)[1:])
    fields={r.label[1]:r.value for r in API['leaves'](recovered)}
    tree=compile_expr(expr,fields)
    return s.simplify(run(tree)),tree


def promote(fields,policy):
    rows=tuple(Row(('field',key),('record',),('port',key),value) for key,value in sorted(fields.items()))
    first=API['incoming_promotion'](rows,1,policy)
    return API['incoming_promotion'](first,2,policy)


def main():
    g,h=s.symbols('g h',positive=True,real=True)
    delta=s.symbols('delta',real=True)
    chi=1/((g*g+h*h)/2-s.I*delta)
    oscillator={'external':g*chi,'bath':h*chi,'return':-g}
    reflection=add(('one',),mul(factor('return'),factor('external')))
    noise=mul(factor('return'),factor('bath'))
    current=mul(mul(factor('level'),factor('normal')),factor('sign'))
    frames=[s.Matrix([1,0]),s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,s.I])/s.sqrt(2)]
    matrices=[v*v.conjugate().T for v in frames]
    berry={f'{v}{a}{b}':matrices[v][a,b] for v,a,b in product(range(3),range(2),range(2))}
    terms=[mul(mul(factor(f'0{a}{b}'),factor(f'1{b}{c}')),factor(f'2{c}{a}')) for a,b,c in product(range(2),repeat=3)]
    contraction=terms[0]
    for term in terms[1:]: contraction=add(contraction,term)
    reports={}
    for policy in ('inherited','common'):
        p=promote(oscillator,policy)
        rr,rt=pipeline(p,reflection); qq,qt=pipeline(p,noise)
        assert s.simplify(rr-(1-g*g*chi))==0
        assert s.simplify(qq+g*h*chi)==0
        def erase(row):
            if row.members: return replace(row,members=tuple(erase(c) for c in row.members))
            return replace(row,value=s.Integer(0)) if row.label==('field','bath') else row
        bad=tuple(erase(row) for row in p)
        badq,badt=pipeline(bad,noise)
        assert badq==0 and badt!=qt
        plus,pt=pipeline(promote({'level':s.Integer(3),'normal':s.Integer(1),'sign':s.Integer(1)},policy),current)
        minus,mt=pipeline(promote({'level':s.Integer(3),'normal':s.Integer(-1),'sign':s.Integer(-1)},policy),current)
        assert plus==minus==3 and pt!=mt
        b,bt=pipeline(promote(berry,policy),contraction)
        assert s.simplify(b-s.trace(matrices[0]*matrices[1]*matrices[2]))==0
        assert b==(1+s.I)/4
        reports[policy]={'symbolic_oscillator_matches':True,'nested_bath_change_reaches_native_tree':True,
                         'mirror_equal_current_distinct_histories':True,'berry_contraction':str(b)}
    paths=['research/nima/agda/PromotedPhysicalReadoutComposition.agda','research/nima/agda/PhysicalDomainNativeReadouts.agda','research/nima/agda/NativeAmplitudeResolution.agda','research/nima/checkers/check_rung_transport_diagram.py','research/strominger/checkers/check_oscillator_retained_cone.py','research/strominger/checkers/check_oscillator_fcc_representation.py',str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','policies':reports,
            'scope':'Actual adapter/cone/chart pipeline with a finite interpreter of the native amplitude schema; formal theorem separately compiled, no Python-to-Agda equivalence asserted.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/strominger/results/promoted-native-readout-pipeline/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
