"""Test exact and quotient column membership for decorated boundaries."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_bigraded_boundary_column_lattice.json'
def aggregate(cols,a):
 return (sum(x*c['n'] for x,c in zip(a,cols)),sum(x*c['r'] for x,c in zip(a,cols)),tuple(sum((x%2)*c['s'][i] for x,c in zip(a,cols))%2 for i in range(3)))
def parity(s):return sum(s)%2
def main():
 target=(1,-1,(0,0,1));bad=[{'n':1,'r':-1,'s':(1,0,0)}];assert aggregate(bad,[1])!=target
 repair=bad+[{'n':0,'r':0,'s':(1,0,1)}];assert aggregate(repair,[1,1])==target
 assert parity(aggregate(bad,[1])[2])==parity(target[2])
 out={'schema':'marici.voevodsky.cosmology-bigraded-boundary-column-lattice.v2','status':'three_exact_sign_equations_one_quotient_parity_equation','exact_target':'(1,-1,(0,0,1),0,...)','exact_conditions':['free Xi equation','free sigma equation','three mod-two sign equations','all residual equations'],'quotient_condition':'After explicitly adjoining diagonal boundaries spanning the even-parity plane, only sign parity remains.','counterexample':'A column with sign (1,0,0) passes quotient parity but fails exact membership; adding the diagonal boundary (1,0,1) repairs it.','decision':'Exact and quotient membership are now separated.','next_gate':'torsion-corrected-single-generator remains exact; use the free-plus-hyperplane synthesis for cohomological obstruction claims','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
