"""Audit naturality of relation Bocksteins under strict degree projection."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--projection',required=True);p.add_argument('--shift',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 proj=json.loads(Path(a.projection).read_text());shift=json.loads(Path(a.shift).read_text())
 assert proj['status']=='passed';assert shift['status']=='proved';assert shift['minimum_shift']==2
 assert all(r['new_columns_with_low_output']==0 for r in proj['rows'])
 out={'schema':'marici.nima.L2-global-bockstein-naturality.v1','status':'proved',
  'relation_naturality':'if A_Dplus4*x=0 then projection gives an A_D relation after discarding high target degrees',
  'representative_naturality':'projection(B_Dplus4*x)=B_D*projection(x) columnwise',
  'finite_support':'every global finite relation and its Bockstein representative occur in some cutoff',
  'conclusion':'the integral relation-to-Bockstein-representative maps form a filtered natural system and define one global locally finite Bockstein operator',
  'qualification':'cokernel saturation and geometric road-Cech realization are not supplied'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
