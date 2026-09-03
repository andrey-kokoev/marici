from __future__ import annotations
import json, math

def main():
    L=0.35; p=2*math.pi/math.log(2); N=1229; W=1831.3001418624747
    delta=0.05
    cminus=(0.5772156649015329+math.pi/2+3*math.log(2)+math.log(math.pi))/(4*math.pi)+math.log(2)/math.sqrt(2)
    eta=delta/(delta+cminus)
    K=max(1,math.floor(N/(2*math.pi)+0.5))
    half_harmonic=sum(1/(k-0.5) for k in range(1,K+1))
    zero_cell=1+2*math.log(N)
    middle=8*L*p*N/math.pi**2*half_harmonic
    tail=4*L*p*N/math.pi**2
    transition=zero_cell+middle+tail
    trace=L*W/math.pi
    dimension=trace+transition/eta
    assert dimension < 5373113.9427412115
    result={"schema":"marici.voevodsky.explicit-resonance-transition-constant-check.v1",
            "status":"explicit_single_prime_resonance_bound_evaluated","N":N,"K":K,
            "zero_cell_bound":zero_cell,"middle_cells_bound":middle,"tail_bound":tail,
            "transition_bound":transition,"trace":trace,"eta":eta,
            "dimension_bound":dimension,"previous_component_dimension_bound":5373113.9427412115,
            "source_intervals_certified":False,"rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
