#!/usr/bin/env python3
"""Debit the directed fifth-derivative jump tail from the shifted completion reserve."""
import json,re
from decimal import Decimal,getcontext
from pathlib import Path
getcontext().prec=50;ROOT=Path(__file__).resolve().parents[2];N=ROOT/'research/nima/results';base=json.loads((N/'L075-shifted-tail-through-fourth-derivative.json').read_text());fifth=json.loads((N/'L075-directed-fifth-derivative-jump-tail-from1500.json').read_text())
def upper(s):m=re.fullmatch(r'\[([^ ]+) \+/- ([^\]]+)\]',s);return Decimal(m.group(1))+Decimal(m.group(2))
before=Decimal(base['reserve_for_C5_and_analytic_rows']);b5=upper(fifth['total_bound']);after=before-b5
out={'schema':'marici.nima.L075-shifted-tail-through-fifth-derivative.v1','reserve_before_fifth':str(before),'fifth_derivative_jump_bound':str(b5),'reserve_for_orders_6_through_149_and_analytic_rows':str(after),'fifth_component_fits':after>0,'prime_boundary_series_terminates_after_order':149,'full_tail_passed':False,'next_obligation':'assemble orders 6 through 149 as one coupled boundary-jet vector, then bound analytic gamma and endpoint rows','rh_proved':False,'passed':after>0};p=N/'L075-shifted-tail-through-fifth-derivative.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
