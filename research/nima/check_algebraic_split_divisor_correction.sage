import json

R.<u,v> = PolynomialRing(QQ)
p = ZZ(2305843009213693951)

y = (u+v)/2-1
P6 = 1-u-v+v^2/4+u*v/2-7*u^2/4+u^2*v+u^3-u^3*v+u^4
D1 = (v-u)*(y-u^2)*(y+u^2)
Ptop = u*(u-2)*(v-2)

with open('research/benincasa/marici-gm/algebraic-split.json') as handle:
    split = json.load(handle)

h = R.zero()
for i,j,c in split['numerator_terms']:
    h += QQ(ZZ(c).rational_reconstruction(p))*u^i*v^j

expected_h = u*(u+v)*(u+v-4)*P6/4
assert h == expected_h
assert P6 != D1
assert split['denominator_powers'] == {'D1':0, 'P6':0, 'Q':0}

result = {
    'schema':'marici.algebraic-split-divisor-correction.v1',
    'entry_865_symbol_correction':'D in the e6 calculation is P6, not quotient divisor D1',
    'P6':str(P6),
    'D1':str(D1),
    'top_to_quotient_gauge':'1/(Ptop*D1)',
    'finite_field_split_status':split['status'],
    'reconstructed_h':str(factor(h)),
    'characteristic_zero_split_pde':'pending exact source substitution',
}

with open('research/nima/algebraic-split-divisor-correction.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True)
    handle.write('\n')

print(json.dumps(result,indent=2,sort_keys=True))
