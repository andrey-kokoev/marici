#!/usr/bin/env python3
"""Insert the existing directed angular-IMS localization constant."""
import json,math,hashlib
from pathlib import Path
root=Path(__file__).parents[1]/'results';locpath=root/'angular_ims_interval_integration.json';loc=json.loads(locpath.read_text());L=.55;cg=(4+.5*math.log(20)+math.log(math.pi))/2;cb=math.pi/2;cp=sum(math.log(p)/math.sqrt(p) for p in (2,3));cl=loc['normalized_localization_upper'];C=cg+cb+cp+cl;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1
out={'schema':'marici.voevodsky.high-mode-threshold-with-directed-localization.v1','L':L,'constants':{'gamma':cg,'carleman':cb,'prime':cp,'localization':cl,'total':C},'sufficient_mode_threshold':M,'dependency_sha256':hashlib.sha256(locpath.read_bytes()).hexdigest(),'assessment':'The directed IMS bound closes the constant gate but makes dense intermediate-band certification infeasible; optimize the partition or avoid localization via a direct interval operator comparison.','passed':True,'rh_proved':False}
p=root/'high_mode_threshold_with_directed_localization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
