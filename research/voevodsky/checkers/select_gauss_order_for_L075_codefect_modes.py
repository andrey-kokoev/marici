#!/usr/bin/env python3
"""Select a unit-panel Gauss order resolving the L=.75 near-unit co-defect block."""
import json,math
from pathlib import Path
rho=1.477032961426901;base_order=48;base_entry=2.544e-13;dimension=1000;absolute_margin=6.613795188441013e-16;target=absolute_margin/4
rows=[]
for q in range(48,97,4):
 entry=base_entry*rho**(-2*(q-base_order));spectral=dimension*entry;rows.append({'order':q,'entry_remainder':entry,'full_dimension_spectral_remainder':spectral,'below_quarter_margin':spectral<target})
chosen=next(r for r in rows if r['below_quarter_margin']);out={'schema':'marici.voevodsky.L075-codefect-gauss-order-selection.v1','bernstein_rho':rho,'base_order':base_order,'base_entry_remainder':base_entry,'absolute_margin_scout':absolute_margin,'target_quarter_margin':target,'candidates':rows,'selected_order':chosen['order'],'selected_spectral_remainder':chosen['full_dimension_spectral_remainder'],'passed':True,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'L075_codefect_gauss_order_selection.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
