"""Exact-moment preparation propagated through stored kernels and global peaks."""
import argparse
import json
from pathlib import Path
import numpy as np
from flint import arb,acb,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches

CASE=ROOT/'.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33'
PREPARATION=HOME/'results/preparation-enclosure.v1.json'
PEAK=HOME/'results/peak-enclosure.v1.json'
NOTE=HOME/'PREPARED-READOUT-ENCLOSURES.md'
RESULT=HOME/'results/prepared-readouts.v1.json'


def ball(bounds):
    lo,hi=map(arb,bounds)
    return (lo+hi)/2+arb(0,((hi-lo)/2).upper())


def outward(x):
    return [float(np.nextafter(float(x.lower()),-np.inf)),float(np.nextafter(float(x.upper()),np.inf))]


def audit():
    historical_validate();ctx.prec=128
    preparation=json.loads(PREPARATION.read_text(encoding='utf-8'));peak=json.loads(PEAK.read_text(encoding='utf-8'))
    for receipt in (preparation,peak):
        for path,value in receipt['source_sha256'].items():assert digest(ROOT/path)==value
    with np.load(CASE/'metadata.npz',allow_pickle=False) as md:K=md['K']
    with np.load(CASE/'packet_kernels.npz',allow_pickle=False) as z:G=z['G'];B=z['Gb']
    collection=json.loads((CASE/'collection.json').read_text(encoding='utf-8'))
    packets=[];intervals=[]
    for prep,old_peak,stride in zip(preparation['packets'],peak['packets'],(2,1)):
        ix=np.arange(0,33,stride);k=K[ix];n=len(k)
        coefficients=[ball(v) for v in prep['coherent_coefficient_enclosures']]
        weights=[ball(v) for v in prep['probability_weight_enclosures']]
        step=arb(float(k[1]-k[0]));series={d:acb(0) for d in range(-n+1,n)}
        error=arb(0);derivative_error=arb(0);curvature=arb(0)
        for i in range(n):
            for j in range(n):
                a=coefficients[i]*coefficients[j]*acb(complex(G[ix[i],ix[j]]))
                d=j-i;f=arb(float(k[j]))-arb(float(k[i]));delta=abs(f-d*step)
                series[d]+=a;error+=abs(a)*delta*100
                derivative_error+=abs(a)*delta*(1+abs(d*step)*100);curvature+=abs(a)*f*f
        harmonics=[(d*step,series[d]+series[-d].conjugate()) for d in range(1,n)]
        def evaluate(t):
            value=series[0].real;derivative=arb(0)
            for f,a in harmonics:
                sn,cs=(f*t).sin_cos()
                value+=a.real*cs+a.imag*sn
                derivative+=f*(-a.real*sn+a.imag*cs)
            return value,derivative
        center=float(old_peak['reference_time']);lo=center-.002;hi=center+.002
        pcenter,_=evaluate(arb(center));lower=(pcenter-error).lower()
        stack=[(-100.,lo,0),(hi,100.,0)];visited=0;leaves=0;depth_max=0
        while stack:
            left,right,depth=stack.pop();visited+=1;depth_max=max(depth_max,depth)
            assert visited<=200000 and depth<=60,'prepared peak enclosure did not close'
            mid=(left+right)/2;rad=max(abs(arb(mid)-arb(left)),abs(arb(right)-arb(mid)))
            value,derivative=evaluate(arb(mid))
            upper=value+error+(abs(derivative)+derivative_error)*rad+curvature*rad*rad/2
            if upper.upper()<lower:leaves+=1
            else:
                assert left<mid<right
                stack.extend([(left,mid,depth+1),(mid,right,depth+1)])
        radius=max(abs(arb(center)-arb(lo)),abs(arb(hi)-arb(center)))
        def ratio_component(kernel):
            value=arb(0);derivative=arb(0);M2=arb(0)
            for i in range(n):
                for j in range(n):
                    a=coefficients[i]*coefficients[j]*acb(complex(kernel[ix[i],ix[j]]))
                    f=arb(float(k[j]))-arb(float(k[i]));phase=acb(0,-f*arb(center)).exp()
                    value+=(a*phase).real;derivative+=(a*phase*acb(0,-f)).real;M2+=abs(a)*f*f
            variation=abs(derivative)*radius+M2*radius*radius/2
            return value+arb(0,variation.upper())
        occupation=ratio_component(G);current=ratio_component(B);assert occupation.lower()>0
        whole_occupation=arb(0);whole_current=arb(0);probability=arb(0)
        for i,index in enumerate(ix):
            whole_occupation+=weights[i]*arb(float(G[index,index].real))
            whole_current+=weights[i]*arb(float(B[index,index].real))
            probability+=weights[i]*arb(float(collection['rows'][int(index)]['product_probability']))
        assert whole_occupation.lower()>0
        values={'peak_transport':current/occupation,'whole_packet_transport':whole_current/whole_occupation,'product_probability':probability}
        intervals.append(values)
        packets.append({'energy_nodes':n,'prepared_global_peak_bracket':[lo,hi],
                        'all_enclosed_preparations_have_global_peak_in_bracket':True,
                        'visited_intervals':visited,'excluded_leaves':leaves,'maximum_depth':depth_max,
                        'readout_enclosures':{name:outward(value) for name,value in values.items()},
                        'readout_balls':{name:str(value) for name,value in values.items()}})
    comparisons={}
    for key in intervals[0]:
        old,new=intervals[0][key],intervals[1][key];assert old.lower()>0
        difference=abs(new-old).upper();baseline=old.lower();margin=baseline/100-difference
        assert margin.lower()>0,'prepared comparison did not close: '+key
        comparisons[key]={'relative_change_upper':float(np.nextafter(float((difference/baseline).upper()),np.inf)),
                          'remaining_absolute_error_budget':float(np.nextafter(float(margin.lower()),-np.inf)),
                          'prepared_stored_kernel_inequality_certified':True,
                          'sufficient_remaining_error_condition':'epsilon33 + 1.01 epsilon17 <= remaining_absolute_error_budget'}
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',PREPARATION,PEAK,CASE/'metadata.npz',CASE/'packet_kernels.npz',CASE/'collection.json']
    return {'schema':'marici.scattering.prepared-readouts.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'search_window':[-100.,100.],'packets':packets,'comparisons':comparisons,
            'exact_moment_preparation_propagated_on_binary_grid':True,
            'all_three_prepared_stored_kernel_inequalities_certified':True,
            'stationary_solver_error_certified':False,'exact_model_energy_reference_certified':False,
            'H6_disposition':'open; exact-moment preparation and peak uncertainty propagated on stored grid/kernels, solver/kernel/reference errors remain'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','relative_change_upper':{k:v['relative_change_upper'] for k,v in result['comparisons'].items()},
                     'peak_intervals_visited':[p['visited_intervals'] for p in result['packets']],'H6':result['H6_disposition']}))


if __name__=='__main__':main()
