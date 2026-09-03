"""Test transport of the abstract four-target collapse space through A16."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_collapse_space_transport.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def main():
 d=json.loads((RES/'cosmology_surviving_line_transport.json').read_text());groups=[]
 for g in d['groups']:
  a=[q(x['scalar']) for x in g['A12_to_A14_x2_multipliers']];b=[q(x['scalar']) for x in g['A14_to_A16_x2_multipliers'] if x['source_path']=='x2'];assert a==b and len(a)==4;groups.append({'grade':g['grade'],'normalized_functional_equal':True,'coefficient_space_dimension':4,'image_rank':1,'relation_space_dimension':3})
 out={'schema':'marici.voevodsky.cosmology-collapse-space-transport.v1','status':'abstract_relation_space_transports_identically','groups':groups,'decision':'For each grade, equality of the normalized four-component image functional makes its three-dimensional coefficient-relation kernel identical at A14 and on x-generated A16 paths.','claim_boundary':'This transports the abstract coefficient kernel only; persistence of the raw-q probes 1,y,x requires a fresh A16 relation certificate.','next_gate':'construct-A16-raw-q-detector-certificate','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
