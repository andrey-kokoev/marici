#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';rows=[]
for m in range(21,33):
 p=root/f'gate3_prime_residual_streamed_block_m{m}_extra0.json'
 if not p.exists():p=root/f'gate3_prime_residual_streamed_block_m{m}.json'
 rows.append(json.loads(p.read_text()))
peak=max(rows,key=lambda x:x['m_times_smooth']);out={'schema':'marici.voevodsky.gate3-prime-smooth-blocks-21-to32.v1','rows':[{'m':x['m'],'m_times_smooth':x['m_times_smooth']} for x in rows],'maximum_observed':peak['m_times_smooth'],'maximum_at_m':peak['m'],'target':.02,'all_pass_scout':all(x['passed_scout'] for x in rows),'passed':False,'scope':'floating exact-degree Gauss','rh_proved':False};p=root/'gate3_prime_smooth_blocks_21_to32.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['all_pass_scout']
