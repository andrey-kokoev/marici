"""Classify integral killing of the primitive triangle cycle by multiple sourced cells."""
from __future__ import annotations
import json
from math import gcd
from functools import reduce
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_multi_cell_Bezout_gate.json'
def egcd(a,b):
 if b==0:return (abs(a),1 if a>=0 else -1,0)
 g,x1,y1=egcd(b,a%b);return g,y1,x1-(a//b)*y1
def bezout(vals):
 coeff=[1];g=vals[0]
 for v in vals[1:]:
  ng,x,y=egcd(g,v);coeff=[x*c for c in coeff]+[y];g=ng
 return g,coeff
def case(vals):
 g,cs=bezout(vals);assert sum(a*b for a,b in zip(vals,cs))==g
 return {'degrees':vals,'gcd':g,'bezout_coefficients':cs,'primitive_killed':g==1,'H1_after':('0' if g==1 else f'Z/{g}' if g else 'Z')}
def main():
 examples=[case([2,3]),case([2,4]),case([6,10,15]),case([0,5]),case([1,7])]
 assert examples[0]['primitive_killed'] and not examples[1]['primitive_killed'] and examples[2]['primitive_killed']
 out={'schema':'marici.voevodsky.cosmology-multi-cell-Bezout-gate.v1','status':'multi_cell_primitive_killing_iff_attachment_degrees_generate_unit_ideal','chain_model':'Z^k --[m1,...,mk]--> Z<triangle cycle>','theorem':'The residual group is Z/gZ for g=gcd(m1,...,mk). The primitive class is killed integrally iff the attaching degrees generate the unit ideal.','examples':examples,'correction_to_single_cell_gate':'A unit individual face is sufficient but not necessary. Several nonunit sourced faces can kill the primitive class when their degrees are coprime, for example degrees 2 and 3.','representative_status':'A Bezout filler word is generally nonunique; different coefficient vectors differ by the kernel of the attachment row, while the quotient filler class is canonical when g=1.','next_gate':'inventory all independently sourced candidate face degrees and chain maps; formal coprime integers without source cells do not authorize a filler','limitations':['one target-cycle row; additional compatibility differentials must still be checked','no sourced face inventory, horn, Bockstein, or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
