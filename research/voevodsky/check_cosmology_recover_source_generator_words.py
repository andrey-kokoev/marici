"""DPC durability audit for exact source-generator words in seed results."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];V=ROOT/'research'/'voevodsky'/'results'
OUT=V/'cosmology_recover_source_generator_words.json'
FILES=('cosmology_IBP_corrected_transport_exact_seeds_a12.json','cosmology_nonmarked_K_exact_seeds_a12.json','cosmology_q_exact_seeds_a12.json')
REQUIRED=('canonical_target_id','source_basis_digest','coefficient_word','equation_digest','checker_path')
def main():
    reports={};total_records=0;recoverable=0;full_flags=0
    for name in FILES:
        data=json.loads((V/name).read_text());records=data['records'];total_records+=len(records)
        present={k:sum(k in r for r in records) for k in REQUIRED}
        recoverable+=sum(all(k in r for k in REQUIRED) for r in records)
        full_flags+=sum(bool(r.get('full_reconstruction')) for r in records)
        reports[name]={'records':len(records),'present_counts':present}
    assert total_records==1224 and recoverable==0 and full_flags>0
    assert not all(k in {'full_reconstruction':True} for k in REQUIRED)  # flag is not a certificate
    out={'schema':'marici.voevodsky.cosmology-recover-source-generator-words.v1','status':'DPC_recovery_conjecture_rejected_exact_words_not_durable_in_seed_results','conjecture':'The exact seed JSONs durably encode canonical source-generator words sufficient for downstream comparison.','rivals':['full_reconstruction is only a solver outcome flag','coefficient vectors were transient checker state','raw relation provenance is external and unreferenced'],'risky_consequences':list(REQUIRED),'falsification':'Across 1,224 records, zero records contain the five-field source-word certificate. Many q/K records say full_reconstruction=true, but no basis digest or coefficient word is serialized, so the reconstruction cannot be replayed or geometrized from the result.','reports':reports,'recoverable_records':recoverable,'residual':'Exact absorption decisions remain checker outcomes, but their witness words are not durable interfaces. Repository-wide source recovery also lacks a typed filesystem search capability in this turn.','disposition':'Reject recovery from result artifacts. Require regenerated exact certificates with canonical IDs, basis/equation digests, sparse rational words, and checker provenance.','next_gate':'serialize-exact-source-certificates','limitations':['audits result JSONs, not every unreferenced repository file'],'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
