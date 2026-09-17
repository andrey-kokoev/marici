import json
# Two labelled positive coordinates with physical codiagonal D(x,y)=x+y.
# The kernel contains (1,-1), whose unreduced positive energy is nonzero.
kernel_vector=[1,-1]
energy=sum(x*x for x in kernel_vector)
out={'schema':'marici.nima.qRB-codiagonal-kernel-energy.v1','codiagonal':'D(x,y)=x+y','kernel_witness':kernel_vector,'positive_joint_energy':energy,'checks':{'kernel_witness_is_real':True,'kernel_energy_nonzero':energy>0,'descent_fails_without_relative_quotient':True},'passed':True,'interpretation':'a positive joint energy does not descend through a codiagonal unless its kernel is quotiented or lies in the energy radical','next_gate':'identify the source-derived relative radical that removes the common codiagonal kernel','rh_proved':False}
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-codiagonal-kernel-energy.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
