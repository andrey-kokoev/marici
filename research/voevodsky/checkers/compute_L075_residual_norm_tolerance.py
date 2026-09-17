#!/usr/bin/env python3
"""Residual-norm tolerance left by the directed L=.75 critical candidate."""
import json,math
from pathlib import Path
candidate=3.40628e-15-2.19e-21;alpha=.022276778741280565;observed=7.59387617969497e-9;maximum=math.sqrt(alpha*candidate);allow=maximum-observed;out={'schema':'marici.voevodsky.L075-residual-norm-tolerance.v1','directed_candidate_lower':candidate,'complement_floor':alpha,'maximum_residual_norm_for_positivity':maximum,'observed_residual_norm':observed,'allowable_absolute_residual_norm_error':allow,'relative_reserve':allow/observed,'passed':allow>0,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'L075_residual_norm_tolerance.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
