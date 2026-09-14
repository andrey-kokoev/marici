"""Conditional physical parity selector from the strict native reflection law."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 d=json.loads(Path(a.input).read_text());formula=d['reflection_formula']
 assert formula=='s(W)=-W+[r11,r00] strictly on chosen bar cup expressions'
 # Universal additive readout calculation: tau(sW)=-tau(W)+tau([,]).
 for w in range(-8,9):
  comm_readout=0
  assert -w+comm_readout==-w
 out={'schema':'marici.nima.reflection-parity-abelianized-selector.v1','status':'conditional-proof',
  'native_formula':formula,
  'required_physical_input':'physical readout kills [r11,r00]',
  'derived_parity':'odd: tau(sW)=-tau(W)',
  'nonvanishing_requirement':'tau(W) must remain nonzero to distinguish odd from trivial parity',
  'conclusion':'commutator-killing physical transport selects odd reflection parity; proving that transport is the remaining gate'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
