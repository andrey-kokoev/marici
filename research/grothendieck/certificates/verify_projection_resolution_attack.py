"""Portable exact refutation of the fixed-theta projection-resolution conjecture.

Analytical validity of the supplied enclosures is external. This verifies the
Cartesian mass-box obstruction and the two frozen middle-task certificates.
Needs sibling verify_source_task_transition.py; no flint or producer imports.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,sys
s=importlib.util.spec_from_file_location('task',Path(__file__).with_name('verify_source_task_transition.py'))
v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
def interval(x):return v.box([x['lower'],x['upper']])
def mass_floor(report):
    C=interval(report['C_after']);H=interval(report['h']);L=interval(report['L'])
    xa=interval(report['windows']['A1']['X']);xb=interval(report['windows']['B1']['X'])
    ma=interval(report['windows']['A1']['mu']);mb=interval(report['windows']['B1']['mu'])
    v.require(min(C+H+xa+xb)>0 and ma[0]>L[1] and mb[0]>L[1],'Monotonicity hypotheses fail')
    # Hold every other quantity exact anywhere in its declared interval.
    # Low X endpoints, but the MOST favorable remaining factors:
    lower_max=2*xa[0]*xb[0]*(C[1]+H[1]*(ma[1]-L[0]))*(C[1]+H[1]*(mb[1]-L[0]))
    # High X endpoints, but the LEAST favorable remaining factors:
    upper_min=2*xa[1]*xb[1]*(C[0]+H[0]*(ma[0]-L[1]))*(C[0]+H[0]*(mb[0]-L[1]))
    threshold=v.q(report['threshold'])
    v.require(lower_max<threshold<upper_min,'Mass-box floor not proved')
    # Check that the reported calibrated gain contains the entire Cartesian box.
    lower=2*xa[0]*xb[0]*(C[0]+H[0]*(ma[0]-L[1]))*(C[0]+H[0]*(mb[0]-L[1]))
    upper=2*xa[1]*xb[1]*(C[1]+H[1]*(ma[1]-L[0]))*(C[1]+H[1]*(mb[1]-L[0]))
    gl,gu=interval(report['gain_after'])
    v.require(gl<=lower<=upper<=gu,'Gain omits a Cartesian corner')
    return lower_max,upper_min

def verify(bundle):
    v.fields(bundle,('schema','report','source_tasks','scope'))
    v.require(bundle['schema']=='projection272-fixed-theta-refutation-v1','Wrong schema')
    v.require(bundle['scope']=='Cartesian enclosure obstruction, not physical ambiguity or impossibility of further calibration','Wrong scope')
    r=bundle['report'];mass_floor(r)
    v.require(r['verdict']=='refuted_for_this_declared_method_and_precision','Wrong verdict')
    before=v.box(r['C_before']);after=interval(r['C_after'])
    v.require(before[0]<after[0]<after[1]<before[1],'No strict pairing refinement')
    v.require(v.q(r['C_width_reduction'])==(before[1]-before[0])/(after[1]-after[0]),'Wrong width ratio')
    v.fields(bundle['source_tasks'],('private','reuse'))
    for mode,task in bundle['source_tasks'].items():
        v.fields(task,('problem','certificate'));p=task['problem'];c=task['certificate'];v.node(p,c)
        raw,gains,sigma,D,M,outer,weights,lower=v.problem(p)
        v.require(p['mode']==mode and c['status']=='UNRESOLVED','Wrong middle status/mode')
        v.require(raw['vacuum']==(Q(1,100),Q(1,100)) and raw['crossed']==(Q(0),Q(0)),'Wrong source slice')
        threshold=raw['positive'][0]/((M-weights['vacuum']*Q(1,100))/weights['positive'])
        v.require(threshold==v.q(r['threshold']),'Threshold detached from source task')
        v.require(gains['positive']==interval(r['gain_after']),'Gain mismatch')
        v.require(p['evidence']['calibration']==r['calibration_sha256'],'Calibration evidence mismatch')
    return True
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Usage: python verify_projection_resolution_attack.py BUNDLE.json')
    verify(v.load(sys.argv[1]))
    print('VALID refutation: frozen theta-mass boxes straddle the task threshold even with exact remaining factors; analytical enclosure premises external')
