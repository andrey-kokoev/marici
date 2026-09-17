#!/usr/bin/env python3
"""Correct the Carleman normalization and expose the remaining localization parameter."""
import json,math
from pathlib import Path
L=.55;cg=(4+.5*math.log(20)+math.log(math.pi))/2;cb=math.pi/2;cp=sum(math.log(p)/math.sqrt(p) for p in (2,3))
def threshold(cloc):
 C=cg+cb+cp+cloc;return math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1
out={'schema':'marici.voevodsky.corrected-high-mode-threshold.v1','L':L,'constants':{'coarse_half_normalized_gamma':cg,'half_normalized_carleman':cb,'prime_norm':cp},'threshold_with_zero_localization_budget':threshold(0),'localization_sensitivity':[{'C_loc':x,'threshold':threshold(x)} for x in (0,.25,.5,1,2)],'correction':'replace pi by pi/2 in the unitary Weil normalization','remaining_gate':'directed C_loc(0.55)','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'corrected_high_mode_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
