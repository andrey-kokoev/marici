"""Compare canonical q-lift descriptor coefficients across ambient degrees 12, 14, 16."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_K_q_canonical_ambient_compatibility.json'
def main():
 packets={a:json.loads((RES/f'cosmology_rank26_p_normal_K_q_canonical_signature_a{a}.json').read_text()) for a in (12,14,16)}
 hashes={k:{str(a):packets[a]['signatures'][k]['descriptor_coefficient_sha256'] for a in packets} for k in ('k0','k1')}; rows={k:{str(a):packets[a]['signatures'][k]['q_rows'] for a in packets} for k in ('k0','k1')}
 assert all(len(set(v.values()))==1 for v in hashes.values()); assert all(len(set(v.values()))==1 for v in rows.values())
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-K-q-canonical-ambient-compatibility.v1','status':'canonical_q_lifts_descriptor_identical_across_A12_A14_A16','degrees':[12,14,16],'descriptor_coefficient_hashes':hashes,'q_row_counts':rows,'decision':'The pole-0 and pole-1 canonical lift coefficient lists are exactly compatible under ambient inclusion across all tested degrees.','limitations':['single prime','three finite degrees','compatibility of a pivot-selected representative does not alone prove source-natural uniqueness'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
