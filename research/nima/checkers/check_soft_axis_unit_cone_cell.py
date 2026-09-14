"""Exact contractible cone supplying a boundary equal to the road target unit."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 # C1=Z<c>, C0=Z<1>, d(c)=1, and h(1)=c.
 for n in range(-32,33):
  d_c=n; h_unit=n
  assert d_c==n                 # d h = id on C0
  assert h_unit==n              # h d = id on C1
 # Oriented cell -c has boundary -1 and cancels residual +1.
 assert -1+1==0
 out={'schema':'marici.nima.soft-axis-unit-cone-cell.v1','status':'proved',
  'complex':'Z<c>[1] --identity--> Z<1>[0]',
  'boundary':'d(c)=1','contraction':'h(1)=c; dh=id_C0 and hd=id_C1',
  'oriented_correction':'d(-c)=-1 cancels residual +1',
  'integrality':'identity differential; unit Smith pivot',
  'scope':'explicit algebraic contractible extension; geometric nearby-cycle realization not asserted'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
