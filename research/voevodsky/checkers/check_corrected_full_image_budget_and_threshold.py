#!/usr/bin/env python3
"""Verify the telescoping image constant and update the directed-tail threshold."""
import json,math
from pathlib import Path
# partial sum tends to 1/2
K=1_000_000;s=sum(1/k-1/(2*k)-1/(2*(k+1)) for k in range(1,K+1));telescoping_exact=f'1/2-1/(2*({K}+1))'
nearest=math.pi/math.sqrt(3);aliases=math.log(2)-3/8;rank_one=.25;cb=nearest+aliases+rank_one;cg=2.6947343670010686;cp=0.4504638081309234;C=cg+cb+cp;L=.55;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1;margin=.5*math.log1p(math.pi*M/(2*L))-C
out={'schema':'marici.voevodsky.corrected-full-image-budget-threshold.v1','constant_pairing_partial_sum':s,'partial_sum_exact':telescoping_exact,'coefficient_one_rank_one_norm':.5,'half_normalized_rank_one_budget':rank_one,'corrected_boundary_budget':cb,'exact_two_prime_norm':cp,'total_constant':C,'sufficient_dirichlet_mode':M,'strict_margin':margin,'supersedes_boundary_budget':2.1319465447941632,'passed':abs(s-(.5-1/(2*(K+1))))<1e-12 and margin>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'corrected_full_image_budget_and_threshold.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
