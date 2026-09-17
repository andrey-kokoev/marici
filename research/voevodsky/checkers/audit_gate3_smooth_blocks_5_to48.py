#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';rows=[]
for m in range(5,49):
 if m<=7:d=json.loads((root/f'continuum_residual_jump_smooth_L06495_{m}000_{m}999.json').read_text());v=d['m_times_smooth_norm']
 else:
  p=root/f'gate3_prime_residual_streamed_block_m{m}_extra0.json'
  if not p.exists():p=root/f'gate3_prime_residual_streamed_block_m{m}.json'
  d=json.loads(p.read_text());v=d['m_times_smooth']
 rows.append({'m':m,'m_times_smooth':v})
peak=max(rows,key=lambda x:x['m_times_smooth']);target=.06;out={'schema':'marici.voevodsky.gate3-smooth-blocks-5-to48.v1','block_count':len(rows),'rows':rows,'maximum':peak['m_times_smooth'],'maximum_at_m':peak['m'],'analytic_target':target,'reserve':target-peak['m_times_smooth'],'reserve_factor':target/peak['m_times_smooth'],'all_finite_scouts_pass':all(x['m_times_smooth']<target for x in rows),'passed':False,'remaining':'directed floating/source error promotion for m=5..48 and analytic recurrence tail for m>=49','rh_proved':False};p=root/'gate3_smooth_blocks_5_to48.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['all_finite_scouts_pass']
