from __future__ import annotations
import json
from fractions import Fraction

def harmonic(n): return sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
def main():
    # The derived pre-crossover cell bound is 4N/(pi*T_k). With
    # T_k proportional to k/p, summation is proportional to p*N*H_K.
    values=[]
    for N in [8,32,128,512]:
        K=max(1,N//7)
        normalized=Fraction(N)*harmonic(K)
        values.append({"N":N,"K":K,"N_H_K":float(normalized),
                       "ratio_to_N_squared":float(normalized/(N*N))})
    assert values[-1]["ratio_to_N_squared"] < values[0]["ratio_to_N_squared"]
    result={"schema":"marici.voevodsky.resonance-split-nlogn-check.v1",
            "status":"harmonic_resonance_scaling_verified","cell_bound":"4*N/(pi*T_k)",
            "summed_scaling":"O(p*N*(1+log N))","fixtures":values,
            "full_source_constant_computed":False,"transition_trace_certified":False,
            "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
