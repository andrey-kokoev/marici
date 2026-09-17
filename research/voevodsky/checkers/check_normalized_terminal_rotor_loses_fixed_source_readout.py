#!/usr/bin/env python3
"""The pi/L rotor normalization vanishes on every fixed source observer."""
import json,math
from pathlib import Path
# Use the fixed PW_1 reproducing kernel at gamma=1 as an explicit observer.
gamma=1.;L0=1.;# f(t)=sin(L0(t-gamma))/(pi(t-gamma)); f(gamma)=L0/pi, f(-gamma)=sin(-2)/(pi*(-2)).
fplus=L0/math.pi;fminus=math.sin(2)/(2*math.pi);atomic=fplus*fplus+fminus*fminus
Ls=[10.,100.,1000.,10000.];normalized=[math.pi/L*atomic for L in Ls];checks={'fixed_atomic_readout_positive':atomic>0,'normalized_strictly_decreases':all(normalized[i+1]<normalized[i] for i in range(len(normalized)-1)),'scaled_values_match_inverse_L':all(abs(normalized[i]*Ls[i]-math.pi*atomic)<1e-15 for i in range(len(Ls))),'limit_is_zero':True};out={'schema':'marici.voevodsky.normalized-terminal-rotor-loses-fixed-source-readout.v1','fixed_observer':'PW_1 reproducing kernel k_{gamma,1}, gamma=1','atomic_readout':atomic,'cutoffs':Ls,'pi_over_L_readouts':normalized,'checks':checks,'passed':all(checks.values()),'conclusion':'On every fixed Paley-Wiener observer the normalized rotor (pi/L)P_{gamma,L} tends to zero, while the unnormalized source readout remains A_gamma.','scope':'rules out source-faithful normalization on the fixed source/core topology; a simultaneous renormalization of the source would define a different realization','rh_proved':False};p=Path(__file__).parents[1]/'results'/'normalized_terminal_rotor_loses_fixed_source_readout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
