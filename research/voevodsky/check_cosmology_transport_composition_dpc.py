"""DPC audit: does canonical DAG closure define compositional word transport?"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_transport_composition_dpc.json'
def main():
 closure=json.loads((RES/'cosmology_transported_source_dag_closure.json').read_text());records=closure['records'];assert len(records)==780
 required=('input_source_basis_digest','input_word_digest','linear_generator_map_digest','predecessor_transport_id')
 missing={k:sum(k not in r for r in records) for k in required};assert all(n==780 for n in missing.values())
 a16=sum(r.get('target_ambient')==16 for r in records);composition=sum('composition_residual' in r for r in records);assert a16==composition==0
 out={'schema':'marici.voevodsky.cosmology-transport-composition-dpc.v1','problem':'Do pivot-canonical A14 DAG closures define a compositional transport of source words?','bold_conjecture':'Canonical DAG closure is a path-independent source-word transport from A12 through A14 to A16.','named_rivals':['endpoint-normalized exact section depending only on target descriptor','naive identity coefficient transport','shifted-basis exact re-solving without total span'],'risky_consequences':['each output binds the input basis and word','a linear generator map is serialized','A12-A14-A16 predecessor links exist','iterated and direct A16 words have an exact comparison residual'],'strongest_falsification':{'records_tested':780,'missing_field_counts':missing,'A16_records':a16,'composition_witnesses':composition,'exact_residual':'780/780 closures omit the input word and any linear generator map; zero A16 or composition records exist.'},'disposition':{'status':'conjecture_rejected_at_first_missing_typed_map','surviving_scope':'All 780 A14 targets admit exact pivot-canonical endpoint words with zero equation residual.','withheld':'No source-word transport, composition, path independence, or arbitrary-even functor follows.','first_missing_typed_object':'A linear map on labelled source-generator modules whose application to each A12 word yields the A14 word.','acceptance_test':'Serialize the generator map on every T/S_K/Q basis descriptor; verify linearity, exact row commutation, and equality of direct versus iterated A16 images for x4, x2y2 along both orders, and y4.'},'next_gate':'construct-linear-generator-transport-matrix','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
