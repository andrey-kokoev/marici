import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/nima/results/reciprocal-bivector-complete-current-normalization-no-go.json'

def packet(s,lam,D=F(1)):
 return {
  'E':D/(2*lam*(lam-s)**2),
  'B':D/(lam-s)**2,
  'F':D/(2*lam*(lam-s))
 }

def main():
 # Exact off-seam fixture with both reciprocal tails decaying.
 s=F(1,3); sr=1-s; lam=F(2)
 p=packet(s,lam); r=packet(sr,lam)
 # Any scalar normalization multiplies E,B,F together; F/B is invariant.
 checks={
  'both_sheets_decay':lam>s and lam>sr,
  'different_forcing_to_boundary_ratio':p['F']/p['B'] != r['F']/r['B'],
  'ratio_difference_equals_seam_defect':p['F']/p['B']-r['F']/r['B']==(1-2*s)/(2*lam),
  'boundary_matching_forces_energy_matching':p['E']/p['B']==r['E']/r['B']==F(1,2*lam),
  'complete_packet_scalar_normalization_impossible':p['F']/p['B'] != r['F']/r['B']
 }
 assert all(checks.values()),checks
 out={
  'schema':'marici.nima.reciprocal-bivector-complete-current-normalization-no-go.v1',
  'classification':'off_seam_scalar_sheet_normalization_cannot_identify_complete_bivector_green_packets',
  'fixture':{'s':str(s),'reciprocal_s':str(sr),'lambda':str(lam),'direct':{k:str(v) for k,v in p.items()},'reciprocal':{k:str(v) for k,v in r.items()}},
  'checks':checks,
  'identity':'F_s/B_s=(lambda-s)/(2 lambda), so F_s/B_s-F_(1-s)/B_(1-s)=(1-2s)/(2 lambda).',
  'consequence':'A scalar rescaling can match boundary and energy coordinates, but cannot also match forcing unless s=1/2. Complete-current reciprocal sewing requires an additional source channel or a non-scalar current-valued mate.',
  'next_constructor':'Represent the forcing-ratio defect as a typed relative current and test whether primitive, square, seam, connected, or archimedean incidence supplies it before scalar aggregation.',
  'passed':True
 }
 OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
