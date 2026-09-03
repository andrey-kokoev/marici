"""Attach exact grade-rescaling weights to source target descriptors."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_grade_weight_descriptors.json'
def main():
 c=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());r=json.loads((RES/'cosmology_grade_functional_rescaling.json').read_text());rows=sorted([x for x in c['A12_classes'] if x['grade']==7],key=lambda x:x['target_id']);weights=[x['numerator']//x['denominator'] for x in r['diagonal_weights']];attached=[{'target_id':x['target_id'],'descriptor':x['descriptor'],'weight':w} for x,w in zip(rows,weights)];out={'schema':'marici.voevodsky.cosmology-grade-weight-descriptors.v1','status':'weights_attached_to_exact_descriptors','attachments':attached,'distinct_absolute_weights':sorted({abs(w) for w in weights}),'decision':'The four diagonal weights are now attached to exact q-target descriptors; no formula from descriptor entries alone is certified by four samples.','claim_boundary':'Attachment is source-labelled finite data, not a canonical grading operator.','next_gate':'test-weight-law-on-grade-six-or-new-targets','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
