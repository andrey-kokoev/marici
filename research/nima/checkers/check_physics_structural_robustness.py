"""Exact rational parameter-region controls; no measurements or full-node closure."""
import argparse
import copy
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import check_physics_geometric_candidate as G
import check_physics_observation_resource_interface as O

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-structural-robustness.v1.json'


def box(c,key):return tuple(map(F,c[key]))
def grid(lo,hi):return tuple(lo+(hi-lo)*F(i,8) for i in range(9))
def gap(eta,gamma,r):return eta*(1-gamma)*(1-r)/(1-eta*r)
def derivative(eta,gamma,r):return (1-eta)*(1-gamma)/(1-eta*r)**2


def validate(c):
    G.require(c['decision']=='constructed_partial_parameter_region_witness' and c['empirical_exclusions']==[],'scope promotion')
    b=c['detector_box'];G.require(box(b,'eta')==(F(1,4),F(1,2)) and box(b,'gamma')==(F(1,4),F(1,2))
                                and box(b,'prior_readiness')==(F(1,4),F(3,4)),'detector regime drift')
    G.require(all(box(c['optical_box'],k)==(F(1,3),F(2,3)) for k in ('t1_squared','a_squared','r2_squared')),'optical regime drift')
    G.require(F(c['discrepancy_allowance'])==F(1,100) and len(c['limitations'])==4,'budget/limitations')


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);validate(c);paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    b=c['detector_box'];el,eh=box(b,'eta');gl,gh=box(b,'gamma');rl,rh=box(b,'prior_readiness')
    bounds={'reset_CC':el*el,'reset_CNC':el*el*(1-gh),'no_click_continuation':gap(el,gh,rh),
            'dark_return_occupation':F(1,27),'environment_norm_defect':F(1,27)}
    G.require(bounds['reset_CC']==F(1,16) and bounds['reset_CNC']==F(1,32)
              and bounds['no_click_continuation']==F(1,26),'lower bound values')
    G.require(all(v>2*F(c['discrepancy_allowance']) for v in bounds.values()),'separation margin')
    floor_n=1-eh*rh;floor_c=el*rl;lip=derivative(eh,gl,rh)
    G.require(floor_n==F(5,8) and floor_c==F(1,16) and lip==F(24,25),'conditioning bounds')
    # At worst r=rh, derivative in eta has sign 2*rh-1-rh*eta, positive on eta box.
    G.require(2*rh-1-rh*eh>0,'one-step derivative extremum argument')
    etas=grid(el,eh);gammas=grid(gl,gh);readies=grid(rl,rh)
    cases=0
    for eta,gamma,r in itertools.product(etas,gammas,readies):
        posterior,likelihood=O.filter_step(1,'N',r,eta,gamma)
        G.require(likelihood>=floor_n and eta*r>=floor_c,'likelihood floor')
        G.require(eta*(1-posterior)==gap(eta,gamma,r),'predictive gap identity')
        G.require(F(1,26)<=gap(eta,gamma,r)<=F(9,28),'gap enclosure')
        G.require(0<=derivative(eta,gamma,r)<=lip,'one-step derivative enclosure')
        G.require(eta**2>=bounds['reset_CC'] and eta**2*(1-gamma)>=bounds['reset_CNC'],'reset enclosures')
        cases+=1
    lipschitz_cases=0
    for eta,gamma,r1,r2 in itertools.product(etas,gammas,readies,readies):
        p1=O.filter_step(1,'N',r1,eta,gamma)[0];p2=O.filter_step(1,'N',r2,eta,gamma)[0]
        G.require(abs(p1-p2)<=lip*abs(r1-r2),'prior perturbation bound')
        lipschitz_cases+=1
    optical_cases=0
    for t,a,r2 in itertools.product(grid(F(1,3),F(2,3)),repeat=3):
        dark=t*a*r2;environment=(1-a)*r2*(1-t)
        G.require(F(1,27)<=dark<=F(8,27) and F(1,27)<=environment<=F(8,27),'optical parameter bounds')
        optical_cases+=1
    # Explicit failure/alias regions; mathematical controls only.
    G.require(gap(F(1,2),F(1),F(1,2))==0 and gap(F(1,2),F(1,2),F(1))==0,'boundary aliases')
    G.require(F(1,1000)**2<2*F(c['discrepancy_allowance']),'small-efficiency separation collapse')
    for n,y,r,eta in ((1,'C',F(0),F(1,2)),(1,'N',F(1),F(1))):
        try:O.filter_step(n,y,r,eta)
        except ValueError:pass
        else:raise AssertionError('zero-likelihood posterior accepted')
    G.require(F(1,4)*1==F(1,2)*F(1,2),'eta/readiness alias')
    # Same-parameter separation is NOT full independently fitted nuisance-set separation.
    cnc_reference=F(1,2)**2*F(1,4);cnc_reset=F(1,4)**2
    G.require(cnc_reference==cnc_reset==F(1,16),'CNC cross-parameter alias')
    escaped=O.filter_step(1,'N',rh,el,gh)[0]
    G.require(escaped==F(11,13)>rh,'box non-invariance control')
    rejected=[]
    for name in ('inflated-regime','empirical-promotion','lost-limitations'):
        bad=copy.deepcopy(c)
        if name=='inflated-regime':bad['detector_box']['eta'][0]='1/1000'
        elif name=='empirical-promotion':bad['empirical_exclusions']=['reset-ready']
        else:bad['limitations']=[]
        try:validate(bad)
        except ValueError:rejected.append(name)
        else:raise AssertionError('accepted '+name)
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','disposition':c['decision'],
         'common_parameter_gap_lower_bounds':{k:str(v) for k,v in bounds.items()},
         'likelihood_floors':{'N':str(floor_n),'C':str(floor_c)},'one_step_prior_lipschitz':str(lip),
         'detector_rational_controls':cases,'prior_perturbation_controls':lipschitz_cases,'optical_squared_parameter_controls':optical_cases,
         'CNC_independently_fitted_alias':str(cnc_reference),'readiness_box_not_invariant':str(escaped),
         'full_identifiability_node_closed':False,'empirical_exclusions':[],
         'rejected_corruptions':rejected,'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
