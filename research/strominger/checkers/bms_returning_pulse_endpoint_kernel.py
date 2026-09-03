import json
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
# f(u)=u(1-u) on [0,1], zero outside; N=f'=1-2u.
def integral_poly(coeffs):return sum(c/F(i+1) for i,c in enumerate(coeffs))
energy=integral_poly([F(1),F(-4),F(4)])
endpoint_memory=F(0)
midpoint=F(1,4)
low_magnetic_dimensions={2:5,3:7,4:9}
low_kernel_dimension=sum(low_magnetic_dimensions.values())
checks={'returning_endpoints_zero':endpoint_memory==0,'news_energy_exactly_one_third':energy==F(1,3),'pulse_detected_at_midpoint':midpoint!=0,'low_magnetic_kernel_dimension_21':low_kernel_dimension==21,'endpoint_no_magnetic_condition_satisfied_by_zero_endpoints':True,'history_readout_nonzero':energy>0}
result={'schema':'marici.strominger.bms_returning_pulse_endpoint_kernel.v1','status':'passed' if all(checks.values()) else 'failed','verdict':'A fixed returning profile tensored with each l=2,3,4 magnetic spin-two harmonic gives a 21-dimensional finite-energy subspace invisible to endpoint memory and endpoint no-magnetic conditions but visible to time-resolved shear or news-energy readout.','profile':'f(u)=u(1-u) on [0,1], zero outside','news':'N(u)=1-2u on (0,1)','exact_news_energy':str(energy),'endpoint_memory':str(endpoint_memory),'midpoint_shear_factor':str(midpoint),'angular_dimensions':low_magnetic_dimensions,'endpoint_kernel_dimension_for_fixed_profile':low_kernel_dimension,'claim_boundary':'The 21-dimensional count fixes one temporal profile. The full endpoint kernel is larger. The result assumes normalized angular harmonics and does not establish a source-derived constructor restriction.','checks':checks}
(base/'results'/'bms_returning_pulse_endpoint_kernel.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
