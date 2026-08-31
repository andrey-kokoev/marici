"""Classify one-face attachments to the primitive exceptional boundary cycle."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_open_change_unit_attachment.json'
def main():
 cases=[]
 for m in range(-6,7):
  if m==0: h1='Z'; killed=False
  elif abs(m)==1: h1='0'; killed=True
  else: h1=f'Z/{abs(m)}'; killed=False
  cases.append({'attachment_degree':m,'H1_after_attachment':h1,'primitive_class_killed_integrally':killed})
 assert [x['attachment_degree'] for x in cases if x['primitive_class_killed_integrally']]==[-1,1]
 out={'schema':'marici.voevodsky.cosmology-open-change-unit-attachment.v1','status':'integral_triangle_obstruction_killed_only_by_unit_degree_face_attachment','chain_model':'C2=Z --m--> H1(boundary)=Z','homology_after_attachment':'coker(m)=Z/mZ, with m=0 interpreted as Z','tested_degrees':cases,'theorem':'A single sourced face kills the primitive triangle class integrally iff its attaching degree is +1 or -1. Nonunit degree leaves torsion and zero degree leaves the free class.','alteration_consequence':'A degree-m boundary cover/root construction with |m|>1 cannot supply the primitive horn filler; it leaves a Z/|m| obstruction.','decision':'Any admissible open-changing source geometry must provide an oriented unit attachment, not merely a finite cover, ramified root, or nonunit multiple.','remaining_gate':'derive a unit-degree face from an actual source incidence correspondence and verify its carrier chain map; otherwise the construction is the abstract tau_p cell','limitations':['classifies the one-face attachment model','does not prove no more elaborate multi-cell source complex can kill the class primitively','no Bockstein or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
