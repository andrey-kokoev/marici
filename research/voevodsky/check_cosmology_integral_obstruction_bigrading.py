"""Separate the full decorated boundary group from the monomial-symbol image constraint."""
from __future__ import annotations
import json
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_integral_obstruction_bigrading.json'
def parity(s):return sum(s)%2
def main():
 signs=list(product((0,1),repeat=3));E=[s for s in signs if parity(s)==0];assert len(signs)==8 and len(E)==4
 isolated=(0,(0,0,1));assert parity(isolated[1])!=isolated[0]%2
 target=(1,(0,0,1));assert parity(target[1])==1
 cosets={parity(s) for s in signs};assert cosets=={0,1}
 out={'schema':'marici.voevodsky.cosmology-integral-obstruction-bigrading.v2','status':'full_boundary_group_separated_from_monomial_image_and_cohomology_quotient','chain_group':'D=Z x (Z/2)^3','monomial_image_constraint':'B={(n,s): parity(s)=n mod 2}; valid for monomial Milnor boundaries only','counterexample_to_full_fiber_product':'the Gersten cycle (0,(0,0,1)) represents H*(-1) and lies in D but not B','diagonal_boundary_plane':[list(s) for s in E],'cohomology_quotient':'O=D/(0 x E)=Z x Z/2','target':{'chain':[1,[0,0,1]],'cohomology':[1,1]},'decision':'Use D for exact boundary equations, B only for monomial-symbol image tests, and O for the free plus hyperplane-sign obstruction class.','next_gate':'bigraded-boundary-column-lattice correction: impose three chain-level sign equations or one quotient parity equation only when diagonal boundaries are admitted','limitations':['three-line constant-sign sector','other K1 unit data remain separate'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
