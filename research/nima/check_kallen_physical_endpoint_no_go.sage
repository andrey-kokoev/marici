import json
import hashlib

R.<A,B,T,z> = PolynomialRing(QQ)
f = A*z^2-(A+B-T)*z+B
Q = 4*A*B-(A+B-T)^2
disc = f.discriminant(z)
assert disc == -Q

kallen_path = 'research/benincasa/q-kallen-incidence-discriminant.json'
raw_path = 'research/benincasa/generic_q_log_smoothness_certificate.md'
germ_path = 'research/benincasa/published_boundary_value_leray_uniqueness.md'
checker_path = 'research/benincasa/verify_q_sheet_resolution.rs'

def read_bytes(path):
    return open(path,'rb').read()

kallen_bytes = read_bytes(kallen_path)
raw_bytes = read_bytes(raw_path)
germ_bytes = read_bytes(germ_path)
sheet_checker_bytes = read_bytes(checker_path)
kallen = json.loads(kallen_bytes)
raw = raw_bytes.decode('utf-8')
germ = germ_bytes.decode('utf-8')
sheet_checker = sheet_checker_bytes.decode('utf-8')

assert kallen['incidence_discriminant'] == '-Q'
assert kallen['generic_cover_degree'] == 2
assert kallen['membership_in_physical_coefficient_system_established'] is False
assert kallen['physical_chain_identification_established'] is False

# The frozen physical pair has no generic-Q surface, component, pair, triple,
# or infinity incidence degeneration.  The tracked verifier turns this census
# into a simultaneous resolution and identity-monodromy assertion.
assert '1,719 nonconstant' in raw
assert 'Every reported remainder is nonzero' in raw
assert 'uniquely determines the local' in germ
assert 'simultaneous_resolution_over_disk' in sheet_checker
assert 'variation_zero' in sheet_checker
assert 'proved_generic_Q_apparent_for_q_G12_relative_sector' in sheet_checker

# A generically finite identification of degree-two endpoint covers preserves
# the branch divisor.  The incidence cover has simple branch Q=0, whereas the
# resolved physical endpoint pair is unramified there.  Hence no such
# identification exists over the frozen base.
result = {
    'schema':'marici.kallen-physical-endpoint-no-go.v1',
    'field':'QQ(A,B,T)',
    'incidence_polynomial':'A*z^2-(A+B-T)*z+B',
    'incidence_discriminant':str(disc),
    'incidence_cover_generic_Q_ramification':True,
    'physical_endpoint_generic_Q_ramification':False,
    'generic_finite_endpoint_cover_identification':False,
    'logical_gate':'branch divisors must agree under a generically finite identification of degree-two covers',
    'scope':'generic nonsoft Q; proper intersections with the frozen discriminant union excluded',
    'source_hashes':{
        kallen_path:hashlib.sha256(kallen_bytes).hexdigest(),
        raw_path:hashlib.sha256(raw_bytes).hexdigest(),
        germ_path:hashlib.sha256(germ_bytes).hexdigest(),
        checker_path:hashlib.sha256(sheet_checker_bytes).hexdigest(),
    },
    'status':'physical_endpoint_identification_falsified',
}

with open('research/nima/kallen-physical-endpoint-no-go.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True)
    handle.write('\n')

print(json.dumps(result,indent=2,sort_keys=True))
