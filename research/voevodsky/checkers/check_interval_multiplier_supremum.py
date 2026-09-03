from __future__ import annotations
import json
from pathlib import Path
import flint
from flint import arb,acb

flint.ctx.prec=160
U=arb(250);N=25000

def main():
    width=U/N;half=width/2;log2=arb(2).log();c=log2/arb(2).sqrt();logpi=arb.pi().log()
    maximum=0.;minimum_lower=float('inf');worst_cell=None
    for k in range(N):
        center=(arb(k)+arb('0.5'))*width;u=arb(center,half)
        z=acb(arb('0.25'),u/2)
        symbol=(z.digamma().real-logpi)/2-c*(u*log2).cos()
        lo=float(symbol.lower());hi=float(symbol.upper())
        absolute=max(abs(lo),abs(hi))
        if absolute>maximum: maximum=absolute;worst_cell=k
        minimum_lower=min(minimum_lower,lo)
    result={'schema':'marici.voevodsky.interval-multiplier-supremum.v1',
      'domain':'[-250,250]','even_symmetry_used':True,'cell_count_on_nonnegative_half':N,
      'cell_width':float(width),'maximum_absolute_upper':maximum,'below_10':maximum<10,
      'minimum_symbol_lower':minimum_lower,'worst_cell_index':worst_cell,
      'minimum_above_minus_129_over_40':minimum_lower>-129/40,
      'pointwise_localization_inequality':'s(u) >= 1/40 - (130/40) 1_{|u|<=100}',
      'arb_precision_bits':flint.ctx.prec,'passed':maximum<10 and minimum_lower>-129/40}
    rendered=json.dumps(result,indent=2,sort_keys=True)
    Path('research/voevodsky/results/interval_multiplier_supremum.json').write_text(rendered+'\n',encoding='utf-8')
    print(rendered)
if __name__=='__main__':main()
