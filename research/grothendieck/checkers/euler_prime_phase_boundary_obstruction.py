"""Cutoff diagnostic for the raw Euler prime phase near the critical line."""
import json,math
from pathlib import Path

cutoffs=[1000,10_000,100_000];maximum=max(cutoffs)
sieve=bytearray(b'\x01')*(maximum+1);sieve[:2]=b'\x00\x00'
for p in range(2,int(maximum**.5)+1):
    if sieve[p]:sieve[p*p:maximum+1:p]=b'\x00'*(((maximum-p*p)//p)+1)
primes=[p for p in range(2,maximum+1) if sieve[p]]
T=14.0;sigmas=[1.2,1.05,0.8,0.5]
values={}
for sigma in sigmas:
    row=[]
    for cutoff in cutoffs:
        phase=0.0
        for p in primes:
            if p>cutoff:break
            m=1
            while p**m<=cutoff:
                phase-=p**(-m*sigma)*math.sin(m*T*math.log(p))/m;m+=1
        row.append(phase)
    values[str(sigma)]=row
drifts={key:[row[i+1]-row[i] for i in range(2)] for key,row in values.items()}
result={'test_height':T,'prime_power_cutoffs':cutoffs,'raw_euler_phase_values':values,
        'successive_cutoff_drifts':drifts,'absolute_convergence_domain':'sigma > 1',
        'critical_line_value_source_defined_by_raw_sum':False,
        'diagnostic_not_a_proof_of_nonexistence_of_regularized_boundary':True,'zero_locations_used':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'euler-prime-phase-boundary-obstruction.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
