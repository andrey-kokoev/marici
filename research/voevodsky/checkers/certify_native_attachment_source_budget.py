"""Arb bounds carrying the finite witness from source norms to response noise."""
from pathlib import Path
import json
from flint import arb,ctx
ctx.prec=160
one=arb(1)
Ctail=2/arb(3).sqrt()
kappa=2*Ctail
D=(kappa+1)/(kappa-1)
H4=D*(kappa**4-1)
assert 4<=8*arb.pi()-7
assert 2*kappa<5
assert H4<70
# Supplied piecewise-H1 gamma regulator estimate, using gamma_E<1.
d0=1-(-arb(2)).exp()
Cinf=arb.pi().log()+1+9/d0+(4*(-one/2).exp()+(-arb(2)).exp())/d0
assert Cinf<20
sig=arb(5)/2
prime_majorant=arb(2).log()*arb(2)**(-sig)+arb(2)**(1-sig)*(arb(2).log()/(sig-1)+1/(sig-1)**2)
assert prime_majorant<1
CA=arb(22)
Cbeta=(one/5+one/3).sqrt()
M=2*CA+Cbeta+1
assert M<46
# Actual weighted forcing includes (1+x), which controls the moment trace.
# The previous certificate gives |L(7/2)|<1.
assert arb(5).sqrt()+arb(2).sqrt()<4
Cresponse=arb(46)*4
Cjoint=16*Cresponse
assert Cjoint==2944
# Factors lambda and sqrt(w_seam) cancel in the dimensionless checks.
# n=4: native multiplier=4800 lambda^2; inherited at R=5=150000 lambda.
native_multiplier=arb(4800)
inherited_multiplier=arb(150000)
source_error_inherited=Cjoint*70/inherited_multiplier*arb('1e-23')
source_error_native=Cjoint/native_multiplier*arb('1e-22')
extra_measurement=arb('2e-23')
assert source_error_inherited+extra_measurement<arb('1e-22')
assert source_error_native+extra_measurement<arb('1e-22')
result={'passed':True,'parameters':{'forcing_beta':4,'spectral_point':'3i',
 'receiver_gamma':2,'event_length':4,'retained_features':1,
 'graph_control_s':1,'native_path_radius':1,'inherited_path_radius':5,
 'physical_weights':'lambda>0 and w_seam>0 retained symbolically'},
 'rigorous_balls':{k:str(v) for k,v in {'theta_tail_constant':Ctail,
 'four_event_tuple_lift_bound':H4,'gamma_graph_bound':Cinf,
 'prime_majorant':prime_majorant,'response_map_bound':M,
 'inherited_source_output_error':source_error_inherited,
 'native_source_output_error':source_error_native}.items()},
 'certified_budgets':{'inherited_source_norm':'1e-23 * lambda * sqrt(w_seam)',
 'native_tuple_presentation_norm':'1e-22 * lambda^2 * sqrt(w_seam)',
 'additional_per_feature_response_noise':'2e-23',
 'total_per_feature_response_error_below':'1e-22'},
 'scope':'Four-event, one-feature homogeneous packet; admissible ideal/presentation perturbations only. The selected-sector normalization is vacuum concatenation. The actual lift and balancing identities are checked by the owning source checkers; the analytic constants and physical-weight bookkeeping are proved in the companion note.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/native-attachment-source-budget.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
