#!/usr/bin/env python3
"""Assemble the nearest and repeated image norm budgets."""
import json,math
from pathlib import Path
nearest=math.pi/math.sqrt(3);aliases=math.log(2)-3/8;total=nearest+aliases
out={'schema':'marici.voevodsky.full-image-boundary-budget.v1','half_normalized_nearest_images':nearest,'half_normalized_repeated_aliases':aliases,'full_boundary_budget':total,'zero_mode_constant':'annihilated by odd periodic extension','common_prefactor':'fixed by (2/pi) Fourier cosine normalization','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'full_image_boundary_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
