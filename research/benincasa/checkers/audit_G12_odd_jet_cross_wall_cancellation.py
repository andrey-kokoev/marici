#!/usr/bin/env python3
"""Test exact divisor cancellations in the G12 exchange-odd cleared second jet."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text())
a,b,c=s.symbols('a b c');locals_={'a':a,'b':b,'c':c}
N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=locals_)
N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=locals_)
odd=s.expand(N23-N31);even=s.expand(N23+N31)
K0=s.sympify(data['K0'],locals=locals_)
walls={'exchange_fixed':a-b,'B12':c+3,'g1':b+c+1,'g2':c+a+1,'g3':a+b+1,'s23':b+c+2,'s31':c+a+2,'K0':K0}
def divisible(poly,q):return s.rem(s.Poly(poly,a,b,c),s.Poly(q,a,b,c))==0
vals={k:divisible(odd,q) for k,q in walls.items()}
quot=s.cancel(odd/(a-b))
checks={'source_packet_passes':data['all_checks_pass'],'odd_nonzero':odd!=0,'odd_under_exchange':s.expand(odd.xreplace({a:b,b:a})+odd)==0,'even_under_exchange':s.expand(even.xreplace({a:b,b:a})-even)==0,'fixed_locus_factor':vals['exchange_fixed'],'quotient_polynomial':s.denom(quot)==1,'no_B12_cancellation':not vals['B12'],'no_K0_cancellation':not vals['K0'],'no_individual_source_wall_cancellation':not any(vals[k] for k in ('g1','g2','g3','s23','s31'))}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-odd-jet-cross-wall-cancellation.v1','combination':'G12_g23 second jet minus G12_g31 second jet','cleared_odd_degree':s.Poly(odd,a,b,c).total_degree(),'cleared_odd_monomial_count':len(s.Poly(odd,a,b,c).terms()),'divisibility':vals,'exchange_factor':'a-b','exchange_quotient_degree':s.Poly(quot,a,b,c).total_degree(),'result':'Antisymmetry supplies exactly the expected exchange-fixed-locus factor a-b, but cancels none of B12, K0, g1, g2, g3, s23, or s31. Therefore it does not by itself prevent cross-wall cycling in iterative IBP.','VA0_consequence':'A global termination filtration must weight the coupled divisor set; a one-wall pole order is insufficient.','next_task':'Construct a multigraded monomial order and verify every tangential remainder from H_q strictly decreases it, or exhibit a two-wall cycle as a no-go.','checks':checks,'passed':True}
d=ROOT/'research/benincasa/results/G12_odd_jet_cross_wall_cancellation.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'degree':out['cleared_odd_degree'],'divisibility':vals,'result':out['result']}))
