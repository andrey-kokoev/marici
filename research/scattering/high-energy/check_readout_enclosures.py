"""H6 Arb readout intervals for stored binary data; no solver-error certification."""
import argparse
import json
from pathlib import Path
import numpy as np
from flint import acb,arb,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches

CASE=ROOT/'.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33'
PEAK=HOME/'results/peak-enclosure.v1.json'
REVIEW=HOME/'results/quadrature-review.v1.json'
NOTE=HOME/'READOUT-ENCLOSURES.md'
RESULT=HOME/'results/readout-enclosures.v1.json'


def outward(x):
    return [float(np.nextafter(float(x.lower()),-np.inf)),float(np.nextafter(float(x.upper()),np.inf))]


def absolute_upper(x):return abs(x).upper()


def absolute_lower(x):
    if x.lower()>0:return x.lower()
    if x.upper()<0:return -x.upper()
    return arb(0)


def audit():
    historical_validate();ctx.prec=128
    peak=json.loads(PEAK.read_text(encoding='utf-8'));review=json.loads(REVIEW.read_text(encoding='utf-8'))
    for receipt in (peak,review):
        for path,value in receipt['source_sha256'].items():assert digest(ROOT/path)==value
    with np.load(CASE/'metadata.npz',allow_pickle=False) as md:K=md['K']
    with np.load(CASE/'packet_kernels.npz',allow_pickle=False) as z:G=z['G'];B=z['Gb']
    collection=json.loads((CASE/'collection.json').read_text(encoding='utf-8'))
    results=[];intervals=[]
    for packet,preparation,stride in zip(peak['packets'],review['independently_reconstructed_packets'],(2,1)):
        ix=np.arange(0,33,stride);k=K[ix];coeff=packet['binary_coefficients'];n=len(k)
        t=arb(float(packet['reference_time']))
        radius=max(abs(arb(float(packet['peak_bracket'][0]))-t),abs(arb(float(packet['peak_bracket'][1]))-t))
        def peak_bound(kernel):
            value=arb(0);derivative=arb(0);curvature=arb(0)
            for i in range(n):
                for j in range(n):
                    a=arb(float(coeff[i]))*arb(float(coeff[j]))*acb(complex(kernel[ix[i],ix[j]]))
                    frequency=arb(float(k[j]))-arb(float(k[i]))
                    phase=acb(0,-frequency*t).exp()
                    value+=(a*phase).real
                    derivative+=(a*phase*acb(0,-frequency)).real
                    curvature+=abs(a)*frequency*frequency
            variation=abs(derivative)*radius+curvature*radius*radius/2
            enclosure=value+arb(0,variation.upper())
            return enclosure,variation
        occupation,pvar=peak_bound(G);current,jvar=peak_bound(B)
        assert occupation.lower()>0
        transport=current/occupation
        weights=preparation['moment_matched_weights']
        occupation_integral=arb(0);current_integral=arb(0);product=arb(0)
        for i,index in enumerate(ix):
            weight=arb(float(weights[i]))
            occupation_integral+=weight*arb(float(G[index,index].real))
            current_integral+=weight*arb(float(B[index,index].real))
            product+=weight*arb(float(collection['rows'][int(index)]['product_probability']))
        assert occupation_integral.lower()>0
        values={'peak_transport':transport,'whole_packet_transport':current_integral/occupation_integral,'product_probability':product}
        intervals.append(values)
        results.append({'energy_nodes':n,'readout_enclosures':{name:outward(value) for name,value in values.items()},
                        'readout_balls':{name:str(value) for name,value in values.items()},
                        'peak_occupation_variation_upper':float(pvar.upper()),'peak_current_variation_upper':float(jvar.upper()),
                        'peak_occupation_lower':float(occupation.lower())})
    comparisons={}
    for key in intervals[0]:
        old=intervals[0][key];new=intervals[1][key]
        difference=absolute_upper(new-old);baseline=absolute_lower(old)
        margin=arb(1)/100*baseline-difference
        passes=bool(margin.lower()>0)
        assert passes,'stored-readout inequality not enclosed: '+key
        comparisons[key]={'maximum_absolute_difference':float(np.nextafter(float(difference),np.inf)),
                          'minimum_absolute_17_readout':float(np.nextafter(float(baseline),-np.inf)),
                          'remaining_absolute_error_budget':float(np.nextafter(float(margin.lower()),-np.inf)),
                          'relative_change_upper':float(np.nextafter(float((difference/baseline).upper()),np.inf)),
                          'stored_readout_inequality_certified':passes,
                          'sufficient_remaining_error_condition':'epsilon33 + 1.01 epsilon17 <= remaining_absolute_error_budget'}
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',PEAK,REVIEW,CASE/'metadata.npz',CASE/'packet_kernels.npz',CASE/'collection.json']
    return {'schema':'marici.scattering.readout-enclosures.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'packets':results,'comparisons':comparisons,
            'all_three_stored_binary_readout_inequalities_certified':True,
            'reference':'exact binary kernels/energies/coherent coefficients, packet weights and saved product probabilities; peak ratios at every time in certified brackets',
            'stationary_solver_error_certified':False,'exact_preparation_certified':False,
            'H6_disposition':'open; stored-readout comparisons enclosed including peak-bracket uncertainty, exact model/preparation errors remain'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','relative_change_upper':{k:v['relative_change_upper'] for k,v in result['comparisons'].items()},'H6':result['H6_disposition']}))


if __name__=='__main__':main()
