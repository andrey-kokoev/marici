"""Arb/Krawczyk exact-moment Gaussian preparation on binary H6 energy nodes."""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.optimize import root
from flint import arb,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches

CASE=ROOT/'.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33'
PEAK=HOME/'results/peak-enclosure.v1.json'
REVIEW=HOME/'results/quadrature-review.v1.json'
NOTE=HOME/'PREPARATION-ENCLOSURE.md'
RESULT=HOME/'results/preparation-enclosure.v1.json'


def outward(x):
    return [float(np.nextafter(float(x.lower()),-np.inf)),float(np.nextafter(float(x.upper()),np.inf))]


def audit():
    historical_validate();ctx.prec=128
    peak=json.loads(PEAK.read_text(encoding='utf-8'));review=json.loads(REVIEW.read_text(encoding='utf-8'))
    for receipt in (peak,review):
        for path,value in receipt['source_sha256'].items():assert digest(ROOT/path)==value
    with np.load(CASE/'metadata.npz',allow_pickle=False) as md:K=md['K']
    packets=[]
    for old,stored,stride in zip(review['independently_reconstructed_packets'],peak['packets'],(2,1)):
        k=K[::stride];n=len(k);x=(k-3.3)/.035
        w=np.empty(n);w[0]=(k[1]-k[0])/2;w[-1]=(k[-1]-k[-2])/2;w[1:-1]=(k[2:]-k[:-2])/2
        def floating(p):
            v=w*np.exp(p[0]*x+p[1]*x*x);v/=sum(v)
            return [v@x,v@(x*x)-1]
        fit=root(floating,[0.,-.5],tol=1e-11);assert max(abs(np.array(floating(fit.x))))<1e-10
        kb=[arb(float(t)) for t in k];xb=[(t-arb(33)/10)/(arb(7)/200) for t in kb]
        wb=[(kb[1]-kb[0])/2]+[(kb[i+1]-kb[i-1])/2 for i in range(1,n-1)]+[(kb[-1]-kb[-2])/2]
        def moments(parameters):
            unnormalized=[wi*(parameters[0]*xi+parameters[1]*xi*xi).exp() for wi,xi in zip(wb,xb)]
            total=sum(unnormalized,arb(0));weights=[v/total for v in unnormalized]
            m=[sum((wi*xi**j for wi,xi in zip(weights,xb)),arb(0)) for j in range(1,5)]
            J=[[m[1]-m[0]*m[0],m[2]-m[0]*m[1]],
               [m[2]-m[0]*m[1],m[3]-m[1]*m[1]]]
            return weights,[m[0],m[1]-1],J
        center=[arb(float(p)) for p in fit.x];radius=arb(1)/10**10
        box=[p+arb(0,radius.upper()) for p in center]
        assert box[1].upper()<0,'enclosed profile is not Gaussian'
        _,fc,Jc=moments(center);weights,_,Jbox=moments(box)
        C=np.linalg.inv(np.array([[float(v.mid()) for v in row] for row in Jc]))
        Cb=[[arb(float(v)) for v in row] for row in C]
        E=[[arb(int(i==j))-sum((Cb[i][l]*Jbox[l][j] for l in range(2)),arb(0)) for j in range(2)] for i in range(2)]
        correction=[-sum((Cb[i][j]*fc[j] for j in range(2)),arb(0)) for i in range(2)]
        displacement=[correction[i]+sum((E[i][j]*arb(0,radius.upper()) for j in range(2)),arb(0)) for i in range(2)]
        assert all(abs(d).upper()<radius.lower() for d in displacement),'Krawczyk inclusion failed'
        contraction=max(sum((abs(v) for v in row),arb(0)).upper() for row in E)
        assert contraction<1
        # Evaluate on the original proven box. Do not silently treat center as
        # the exact root or narrow using a heuristic iteration.
        coefficients=[(wi*pi/(2*arb.pi())).sqrt() for wi,pi in zip(wb,weights)]
        old_weights=old['moment_matched_weights'];old_coeff=stored['binary_coefficients']
        weight_error=sum((abs(v-arb(float(a))) for v,a in zip(weights,old_weights)),arb(0))
        # Squaring a zero-containing ball can have a negative lower endpoint;
        # use nonnegative abs upper bounds to form a safe squared-norm bound.
        coefficient_error=sum((abs(v-arb(float(a))).upper()**2 for v,a in zip(coefficients,old_coeff)),arb(0)).sqrt()
        packets.append({'energy_nodes':n,'natural_parameter_center':fit.x.tolist(),'natural_parameter_radius':1e-10,
                        'Krawczyk_displacement_balls':[str(v) for v in displacement],
                        'contraction_upper':float(np.nextafter(float(contraction),np.inf)),
                        'unique_exact_moment_root_in_box':True,
                        'probability_weight_enclosures':[outward(v) for v in weights],
                        'coherent_coefficient_enclosures':[outward(v) for v in coefficients],
                        'probability_weight_L1_error_upper':float(np.nextafter(float(weight_error.upper()),np.inf)),
                        'coherent_coefficient_L2_error_upper':float(np.nextafter(float(coefficient_error.upper()),np.inf))})
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',PEAK,REVIEW,CASE/'metadata.npz']
    return {'schema':'marici.scattering.preparation-enclosure.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'mean_exact':'33/10','RMS_exact':'7/200',
            'reference':'exact binary energy nodes and exact trapezoid weights; exact rational moment targets',
            'packets':packets,'exact_moment_preparation_enclosed_on_binary_grid':True,
            'stationary_solver_error_certified':False,'exact_model_energy_nodes_enclosed':False,
            'H6_disposition':'open; exact moment preparation enclosed on stored grid, propagation and fixed-response solver/kernel errors remain'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','weight_L1_error_upper':[p['probability_weight_L1_error_upper'] for p in result['packets']],
                     'coefficient_L2_error_upper':[p['coherent_coefficient_L2_error_upper'] for p in result['packets']],'H6':result['H6_disposition']}))


if __name__=='__main__':main()
