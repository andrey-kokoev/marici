"""Hostile numerical scan of F' on the unit t-circle."""
import json,cmath,math
from pathlib import Path
from reduced_source_pick_hostile_scan import reduced_F

def derivative(t,depth,h):return (reduced_F(t+h,depth)-reduced_F(t-h,depth))/(2*h)
angles=[2*math.pi*k/96 for k in range(96)]
baseline=[];control=[]
for theta in angles:
    t=cmath.exp(1j*theta)
    baseline.append((abs(derivative(t,52,1e-5)),theta))
    control.append((abs(derivative(t,48,5e-6)),theta))
maximum=max(baseline);control_maximum=max(control)
discrepancy=max(abs(a[0]-b[0]) for a,b in zip(baseline,control))
result={'circle_radius':1,'sample_count':len(angles),'maximum_baseline_F_prime_modulus':maximum[0],
        'maximum_baseline_angle':maximum[1],'maximum_control_F_prime_modulus':control_maximum[0],
        'maximum_control_angle':control_maximum[1],'maximum_pointwise_control_discrepancy':discrepancy,
        'proposed_bound_20_safety_factor':20/max(maximum[0],control_maximum[0]),
        'all_samples_below_20':maximum[0]<20 and control_maximum[0]<20,
        'interval_certified':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'reduced-source-F-prime-unit-circle-scan.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
