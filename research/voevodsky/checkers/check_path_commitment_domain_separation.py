"""Empty residual bytes must not alias original identity and reduced-view claims."""
from hashlib import sha256
from pathlib import Path
import json
def H(x):return sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
identity={'kind':'original-identity@1','endpoint':'A','edges':[],'origin':None,'lineage':[]}
reduced={'kind':'derived-reduction@1','endpoint':'A','edges':[],'origin':H([('A','B','e1'),('B','A','e2')]),'lineage':[{'removed':['e1','e2']}]}
assert H(identity['edges'])==H(reduced['edges'])
assert H(identity)!=H(reduced)
def accept(payload,expected_kind):return 'KIND_MISMATCH' if payload['kind']!=expected_kind else 'STRUCTURAL_MATCH_NOT_OBSERVED'
assert accept(reduced,'original-identity@1')=='KIND_MISMATCH'
assert accept(identity,'original-identity@1')=='STRUCTURAL_MATCH_NOT_OBSERVED'
report={'passed':True,'empty_edge_digest':'same for identity and derived reduction','complete_domain_separated_digest':'different','mislabelled_derived_view_as_identity':'KIND_MISMATCH','scope':'Synthetic commitments only; hash distinction is not observed event evidence, issuer grant or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/path-commitment-domain-separation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
