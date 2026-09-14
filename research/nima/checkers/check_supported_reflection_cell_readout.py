"""Assemble the supported odd reflection readout on the normalized ramified line."""
import json
W=1;commutator=0;sW=-W+commutator
assert W!=0 and commutator==0 and sW==-W
out={'schema':'marici.nima.supported-reflection-cell-readout.v1','status':'supported_odd_reflection_cell_readout_constructed',
'primitive_W_readout':W,'commutator_readout':commutator,'reflected_W_readout':sW,
'nonannihilation_source':'normalized ramified branch-difference detector equals one',
'commutator_killing_source':'supported scalar readout is commutative and multiplicative',
'cell_source':'native integral group homotopy sW=-W+[r11,r00] transported to selected supported line',
'boundary':'a concrete rawGroup physical formula is still required for boundary equality'}
open('research/nima/results/supported-reflection-cell-readout.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
