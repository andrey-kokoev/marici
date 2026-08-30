import json
from decimal import Decimal,getcontext
from pathlib import Path

getcontext().prec=50
sqrt5=Decimal(5).sqrt()
x2=(Decimal(7)-sqrt5)/2
x5=(sqrt5-Decimal(1))/2
d2=2*x2-7
d5=2*x5+1
assert abs(d2+sqrt5)<Decimal('1e-48')
assert abs(d5-sqrt5)<Decimal('1e-48')
assert d2!=0 and d5!=0

packet={
 'schema':'marici.five_site_region_pair_active_soft_zero_transversality.v1',
 'records':[
   {'endpoint':'y2=0','root':'(7-sqrt(5))/2','tangential_derivative':'-sqrt(5)','simple_zero':True},
   {'endpoint':'y5=0','root':'(sqrt(5)-1)/2','tangential_derivative':'sqrt(5)','simple_zero':True},
 ],
 'cyclic_simple_zero_occurrences':10,
 'tangential_statement':'the second-Rees coefficient vanishes to first order transverse to each coefficient-zero ray in shape space',
 'normal_rees_statement':'undetermined: tangential simplicity does not imply that the next nonanalytic normal term is third Rees order',
 'required_for_next_normal_order':'full endpoint integrand expansion one order beyond the delta^2 log(delta) coefficient with the zero-ray equation imposed',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-active-soft-zero-transversality.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
