"""Test whether the grade-7/8 surviving-line law has a grade-6 domain."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_six_line_law_domain.json'
def main():
 d=json.loads((RES/'cosmology_twelve_class_cyclic_span.json').read_text());checks=[x for x in d['exact_checks'] if x['grade']==6 and x['axis']=='x2'];assert len(checks)==2 and all(x['source_span_rank']==x['image_span_rank']==x['orbit_elements'] for x in checks)
 out={'schema':'marici.voevodsky.cosmology-grade-six-line-law-domain.v1','status':'grade_six_not_a_surviving_line_sector','checks':checks,'decision':'Grade 6 remains rank four at A12→A14 and rank eight at A14→A16 under x2, so the rank-one functional and its diagonal grade-rescaling law have no grade-6 analogue.','claim_boundary':'This excludes only the same rank-one construction; it does not exclude a higher-rank descriptor transport law.','next_gate':'classify-grade-six-full-rank-transport-matrix','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
