"""Join existing independent verifiers through an explicit fixture identification."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import hashlib
import json
import sys

HERE=Path(__file__).resolve().parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


t=load('numerical_square',HERE/'verify_diagonal_transition.py');v=t.v


def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def row(raw):
    v.array(raw,5);return [v.q(x) for x in raw]


def row_times(a,b):return [sum((a[k]*F(b[k][j]) for k in range(5)),F(0)) for j in range(5)]


def verify_bridge(structural,numerical,link,structural_verifier):
    v.fields(link,('version','kind','scope','structural_sha256','numerical_sha256',
                   'normalized_error_bound','identifications'))
    v.require(type(link['version']) is int and link['version']==1,'Wrong bridge version')
    v.require(link['kind']=='fixture-private-row-gain-bridge-v1','Wrong bridge kind')
    v.require(link['scope']=='finite-structural-fixture-only','Physical identification not supplied')
    v.require(link['structural_sha256']==digest(structural) and link['numerical_sha256']==digest(numerical),'Bridge digest mismatch')
    checker=load('structural_square',Path(structural_verifier))
    checker.verify(structural)
    t.verify_square(numerical)
    keys=('00','10','01','11');v.fields(link['identifications'],keys)
    error=v.q(link['normalized_error_bound']);v.require(error>=0,'Negative error')
    gains={}
    for key in keys:
        ident=link['identifications'][key]
        v.fields(ident,('source_witness','raw_row','normalized_row','raw_factor','raw_center','raw_radius'))
        v.require(ident['source_witness']==['1'],'Source generator is not fixed')
        node=structural['nodes'][key];p=numerical['nodes'][key]
        raw=row(ident['raw_row']);normalized=row(ident['normalized_row'])
        v.require(raw==[F(0),F(0),F(0),F(1),F(0)],'Raw coordinate must be the declared l coordinate')
        v.require(normalized==list(map(v.q,node['private'][0])),'Normalized row is not the structural private row')
        factor=v.q(ident['raw_factor']);v.require(factor>0,'Nonpositive row factor')
        gains[key]=factor
        # Equality on the whole E, not merely agreement on f(1).
        v.require(raw==[factor*x for x in normalized],'Raw/normalized row identity fails')
        f=[v.q(r[0]) for r in node['f']]
        v.require(sum(x*y for x,y in zip(normalized,f))==1,'Source witness normalization fails')
        v.require(sum(x*y for x,y in zip(raw,f))==factor,'Wrong raw source response')
        v.require(len(p['rows'])==1 and p['rows'][0]['weight']=='1','Wrong fixture source norm')
        v.require(list(map(v.q,p['rows'][0]['calibration']))==[factor,factor],'Numerical calibration is not structural response')
        v.require(p['target']['coefficients']==['1'],'Task is not the normalized source coefficient')
        center=v.q(ident['raw_center']);radius=v.q(ident['raw_radius'])
        v.require(radius>=0 and list(map(v.q,p['rows'][0]['data']))==[center-radius,center+radius],'Reading/noise mismatch')
        v.require(radius/factor<=error,'Normalized error budget exceeded')
    for start,end in (('00','10'),('00','01'),('10','11'),('01','11')):
        edge=structural['edges'][start+'-'+end];ne=numerical['edges'][start+'->'+end]
        ratio=gains[end]/gains[start]
        v.require(ne['source_scale']==['1'] and ne['target_scale']=='1','Source/task comparison is not identity')
        v.require(list(map(v.q,ne['observation_scale']))==[ratio],'Observer gain not identified')
        old=link['identifications'][start];new=link['identifications'][end]
        v.require(row_times(row(new['normalized_row']),edge['upper'])==row(old['normalized_row']),'Normalized row does not intertwine')
        v.require(row_times(row(new['raw_row']),edge['upper'])==[ratio*x for x in row(old['raw_row'])],'Raw row does not intertwine')
    return True


if __name__=='__main__':
    structural,numerical,link=[v.strict_load(path) for path in sys.argv[1:4]]
    verify_bridge(structural,numerical,link,sys.argv[4])
    print('VALID fixture-level structural/numerical bridge; no physical observer identification claimed')
