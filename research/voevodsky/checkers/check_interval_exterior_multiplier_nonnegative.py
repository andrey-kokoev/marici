from __future__ import annotations
import json
from pathlib import Path
import flint
from flint import arb,acb

flint.ctx.prec=160
START=100;STOP=10000;WIDTH=10

def main():
 log2=arb(2).log();prime_bound=log2/arb(2).sqrt();logpi=arb.pi().log();minimum=None;worst=None;fail=[]
 for a in range(START,STOP,WIDTH):
  b=min(a+WIDTH,STOP);u=arb(str((a+b)/2),arb(str((b-a)/2)))
  gamma=(acb(arb('0.25'),u/2).digamma().real-logpi)/2
  margin=gamma-prime_bound;lo=float(margin.lower())
  if minimum is None or lo<minimum:minimum=lo;worst=[a,b,str(margin)]
  if lo<=0:fail.append([a,b,str(margin)])
 result={'schema':'marici.voevodsky.interval-exterior-multiplier-nonnegative.v1',
  'checked_domain':'100 <= |u| <= 10000','cell_width':WIDTH,'cell_count':(STOP-START)//WIDTH,
  'prime_oscillation_absolute_bound':str(prime_bound),'minimum_margin_lower':minimum,
  'worst_cell':worst,'failure_count':len(fail),'first_failures':fail[:3],
  'beyond_10000_source':'binets-digamma-integral-certifies-the-safe-cutoff.md',
  'all_frequencies_beyond_100_certified_nonnegative':not fail,'passed':not fail}
 rendered=json.dumps(result,indent=2,sort_keys=True)
 Path('research/voevodsky/results/interval_exterior_multiplier_nonnegative.json').write_text(rendered+'\n',encoding='utf-8')
 print(rendered)
if __name__=='__main__':main()
