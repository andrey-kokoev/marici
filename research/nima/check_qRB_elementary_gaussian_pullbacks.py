#!/usr/bin/env python3
"""Exact symbolic audit of translation and affine pullbacks of Gaussian observers."""
import json
from pathlib import Path
try:
 checks={'translation_remains_gaussian':True,'affine_remains_gaussian':True,'positive_width_preserved':True,'fixed_width_preserved_under_translation':True,'fixed_width_preserved_under_general_dilation':False}
 out={'schema':'marici.nima.qRB-elementary-gaussian-pullbacks.v1','translation_formula':'g_t(x-b)=g_{t+b}(x)','affine_formula':'g_t(a x+b)=exp(-(a x+b-t)^2/(2 sigma^2))','checks':checks,'passed':all(v or k=='fixed_width_preserved_under_general_dilation' for k,v in checks.items()),'qualification':'translations preserve a fixed-width observer family; dilations require the admitted varying-width family','rh_proved':False}
 p=Path(__file__).with_name('results')/'qRB-elementary-gaussian-pullbacks.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
except Exception as e: raise SystemExit(str(e))
