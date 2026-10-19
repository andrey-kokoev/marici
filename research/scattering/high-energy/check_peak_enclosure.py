"""Ball/Taylor global peak localization for exact binary H6 kernel readouts."""
import argparse
import json
from pathlib import Path
import numpy as np
from flint import acb,arb,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches

CASE=ROOT/'.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33'
REVIEW=HOME/'results/quadrature-review.v1.json'
NOTE=HOME/'PEAK-ENCLOSURE.md'
RESULT=HOME/'results/peak-enclosure.v1.json'


def audit():
    historical_validate();ctx.prec=128
    review=json.loads(REVIEW.read_text(encoding='utf-8'))
    for path,value in review['source_sha256'].items():assert digest(ROOT/path)==value
    with np.load(CASE/'metadata.npz',allow_pickle=False) as md:K=md['K']
    with np.load(CASE/'packet_kernels.npz',allow_pickle=False) as z:G=z['G']
    packets=[]
    for packet,stride in zip(review['independently_reconstructed_packets'],(2,1)):
        ix=np.arange(0,33,stride);k=K[ix];g=G[np.ix_(ix,ix)];n=len(k)
        w=np.empty(n);w[0]=(k[1]-k[0])/2;w[-1]=(k[-1]-k[-2])/2;w[1:-1]=(k[2:]-k[:-2])/2
        ew=np.array(packet['moment_matched_weights']);coeff=np.sqrt(w*ew/(2*np.pi))
        step=arb(float(k[1]-k[0]));series={d:acb(0) for d in range(-n+1,n)}
        frequency_error=arb(0);derivative_error=arb(0);M2=arb(0)
        for i in range(n):
            for j in range(n):
                a=arb(float(coeff[i]))*arb(float(coeff[j]))*acb(complex(g[i,j]))
                d=j-i;freq=arb(float(k[j]))-arb(float(k[i]));delta=abs(freq-d*step)
                series[d]+=a
                frequency_error+=abs(a)*delta*100
                derivative_error+=abs(a)*delta*(1+abs(d*step)*100)
                M2+=abs(a)*freq*freq
        positive=[(d*step,series[d]+series[-d].conjugate()) for d in range(1,n)]
        constant=series[0].real
        def evaluate(t):
            p=constant;der=arb(0)
            for f,a in positive:
                sn,cs=(f*t).sin_cos()
                p+=a.real*cs+a.imag*sn
                der+=f*(-a.real*sn+a.imag*cs)
            return p,der
        center=float(packet['peak_time']);lo=center-.001;hi=center+.001
        assert -100<lo<hi<100
        p0,_=evaluate(arb(center));reference=(p0-frequency_error).lower()
        # Cells entirely outside this bracket are excluded by a certified Taylor
        # upper bound. The retained bracket need not have a unique maximizer.
        stack=[(-100.,lo,0),(hi,100.,0)];leaves=0;visited=0;max_depth=0
        while stack:
            left,right,depth=stack.pop();visited+=1;max_depth=max(max_depth,depth)
            assert visited<=200000 and depth<=60,'bounded peak enclosure did not close'
            mid=(left+right)/2
            # Use exact endpoint differences, not a rounded half-width.
            rad=max(abs(arb(mid)-arb(left)),abs(arb(right)-arb(mid)))
            p,der=evaluate(arb(mid))
            upper=p+frequency_error+(abs(der)+derivative_error)*rad+M2*rad*rad/2
            if upper.upper()<reference:leaves+=1
            else:
                assert left<mid<right,'float subdivision exhausted'
                stack.extend([(left,mid,depth+1),(mid,right,depth+1)])
        packets.append({'energy_nodes':n,'binary_coefficients':coeff.tolist(),'peak_bracket':[lo,hi],
                        'reference_time':center,'reference_occupation_lower_ball':str(reference),
                        'frequency_grouping_uniform_value_error_ball':str(frequency_error),
                        'frequency_grouping_uniform_derivative_error_ball':str(derivative_error),
                        'global_second_derivative_upper_ball':str(M2.upper()),
                        'excluded_leaf_intervals':leaves,'visited_intervals':visited,'maximum_depth':max_depth,
                        'global_maximum_in_bracket_for_binary_kernel':True})
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',REVIEW,CASE/'packet_kernels.npz',CASE/'metadata.npz']
    return {'schema':'marici.scattering.peak-enclosure.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'search_window':[-100.,100.],
            'reference':'real occupation quadratic form of exact binary stored kernels, energies and reconstructed binary coefficients',
            'packets':packets,'binary_kernel_global_peak_localized':True,
            'stationary_solver_error_certified':False,'exact_moment_weights_certified':False,
            'H6_disposition':'open; stored binary readout peak localized, solver and exact preparation/readout margins remain'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','peak_brackets':[p['peak_bracket'] for p in result['packets']],
                      'visited_intervals':[p['visited_intervals'] for p in result['packets']],'H6':result['H6_disposition']}))


if __name__=='__main__':main()
