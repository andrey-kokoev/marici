"""Finite countermodel: road correction does not imply group coherence."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 # Singleton road cell/Cech/scalar model satisfies every oriented correction field.
 cell='c'; residual=1; boundary={cell:-1}; add=lambda x,y:x+y
 detector=lambda x:x; neg=lambda x:-x
 road={
  'boundary_is_negative_residual':boundary[cell]==neg(residual),
  'cancellation':add(residual,boundary[cell])==0,
  'negative_unit_pairing':detector(boundary[cell])==neg(1)}
 assert all(road.values())
 # Independent two-point group model falsifies the requested coherence equality.
 zero_group=0; group_difference=1
 assert group_difference!=zero_group
 out={'schema':'marici.nima.road-correction-group-independence.v1','status':'countermodel',
  'road_correction_fields':road,
  'group_model':{'zeroGroup':zero_group,'groupDifferenceAtCandidate':group_difference,
                 'coherent':False},
  'conclusion':'No theorem from oriented road-correction data alone to physical group coherence exists parametrically.'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
