from __future__ import annotations
import json,math
from fractions import Fraction

def main():
    # Source spectral coefficient d/(4*pi), while F=sqrt(2*pi)*F_unitary.
    # Hence the multiplier relative to the unitary Fourier L2 norm is d/2.
    source_scale="1/(4*pi)"; unitary_scale="1/2"
    # Binet at z=1/4+50i: remainder <=1/300 and Re(1/(2z))<1/20000.
    d_lower=Fraction(39,10)-Fraction(23,20)-Fraction(1,300)-Fraction(1,20000)
    gamma_lower=d_lower/2
    required_upper=Fraction(547,1000)
    assert gamma_lower>required_upper
    L=.35; R=100.; delta=.05; p=2*math.pi/math.log(2)
    c=math.log(2)/math.sqrt(2)
    c_low=(0.5772156649015329+math.pi/2+3*math.log(2)+math.log(math.pi))/2
    cminus=c_low+c; eta=delta/(delta+cminus)
    N=math.ceil(2*R/p)+1; W=2*R; K=max(1,math.floor(N/(2*math.pi)+.5))
    H=sum(1/(k-.5) for k in range(1,K+1))
    D=1+2*math.log(N)+8*L*p*N/math.pi**2*H+4*L*p*N/math.pi**2
    trace=L*W/math.pi; M=math.ceil(trace+D/eta)
    result={"schema":"marici.voevodsky.unitary-gamma-tail-scale-check.v1",
      "status":"two_pi_scale_defect_repaired","source_spectral_scale":source_scale,
      "unitary_state_multiplier_scale":unitary_scale,"safe_R":100,
      "m_gamma_lower":str(gamma_lower),"required_level_upper":str(required_upper),
      "component_upper":N,"measure_upper":W,"transition_bound":D,"trace_upper":trace,
      "sufficient_M_diagnostic":M,"prior_R_10000_chain_valid":False,
      "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
