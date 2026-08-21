"""Finite diagnostics and falsifiers for the compact-Jacobi Sommerfeld attack."""
import json,math
from pathlib import Path
root=Path(__file__).parents[1]/'results'
a=json.loads((root/'quarter-point-jacobi-diagonal.json').read_text())['jacobi_diagonal_a0_through_a4'];b=json.loads((root/'quarter-point-jacobi-coefficients.json').read_text())['jacobi_off_diagonal_squares_b1_through_b4'];mom=json.loads((root/'quarter-point-order-four-interval.json').read_text())['moments_A0_through_A9']
a=[sum(map(float,x))/2 for x in a];b=[sum(map(float,x))/2 for x in b];A0=sum(map(float,mom[0]))/2
partial_trace=[];s=0
for x in a:s+=x;partial_trace.append(s)
result={'jacobi_diagonal_midpoints':a,'off_diagonal_squares_midpoints':b,
        'off_diagonal_midpoints':[math.sqrt(x) for x in b],
        'partial_diagonal_trace':partial_trace,'source_mass_A0':A0,
        'five_step_trace_fraction':partial_trace[-1]/A0,
        'post_transient_a_decreases':all(a[i]>a[i+1] for i in range(1,4)),
        'observed_b_strictly_decreases':all(b[i]>b[i+1] for i in range(3)),
        'constant_nonzero_tail_candidate':'incompatible with required compact pure-point spectrum',
        'finite_data_proves_compactness':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=root/'sommerfeld-jacobi-attack.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
