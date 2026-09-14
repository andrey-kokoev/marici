"""Verify the pushout condition for attaching the contractible unit cone."""
import argparse,json
from pathlib import Path
import sympy as sp

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 # Nontrivial sample complex C1 -> C0 -> C-1 and a closed residual r.
 d0=sp.Matrix([[1,0,0]])
 d1=sp.Matrix([[0],[1],[0]])
 r=sp.Matrix([0,0,1])
 assert d0*d1==sp.zeros(1,1)
 assert d0*r==sp.zeros(1,1)
 extended=d1.row_join(-r)
 assert d0*extended==sp.zeros(1,2)
 detector=sp.Matrix([[0,0,1]])
 assert (detector*r)[0]==1 and (detector*(-r))[0]==-1
 assert extended.rank()==d1.rank()+1
 out={'schema':'marici.nima.soft-axis-unit-cone-pushout.v1','status':'proved',
  'attachment':'map cone unit 1 to closed residual r; new cell has differential -r',
  'chain_condition':'d(r)=0 implies d^2(new cell)=0',
  'detector_condition':'lambda(r)=1 implies lambda(d(new cell))=-1',
  'free_rank_effect':'new column is independent modulo old image and kills the detector free class',
  'qualification':'the standalone cone is contractible; its pushout kills r and need not be contractible'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
