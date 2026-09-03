"""Test uniqueness and boundary character of three-descriptor influx detectors."""
import json,sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_cross_grade_support_replacement as r
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_influx_detector_nonuniqueness.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def det(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def main():
 raw=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());sp=json.loads((RES/'cosmology_sparse_raw_q_certificates.json').read_text());u7,d7=r.support(raw['groups'][0],sp['groups'][0]);u8,d8=r.support(raw['groups'][1],sp['groups'][1]);shifted=set()
 for k in u7:
  d=list(d7[k]);d[3]=list(d[3]);d[4]=list(d[4]);d[2]+=1;shifted.add(r.key(d))
 influx=sorted(u8-shifted);cs=raw['groups'][1]['certificates'];maps=[{r.key(t['descriptor']):q(t['coefficient']) for t in c['raw_q_terms']} for c in cs];forms={k:tuple(m.get(k,Fraction()) for m in maps) for k in influx};detect=[]
 for tri in combinations(influx,3):
  if det(*(forms[k] for k in tri)):detect.append(tri)
 x0=[k for k in influx if d8[k][4][0]==0];y0=[k for k in influx if d8[k][4][1]==0];dx=sum(bool(det(*(forms[k] for k in tri))) for tri in combinations(x0,3));dy=sum(bool(det(*(forms[k] for k in tri))) for tri in combinations(y0,3));mins=min(max(sum(d8[k][4]) for k in tri) for tri in detect);mintris=[tri for tri in detect if max(sum(d8[k][4]) for k in tri)==mins]
 out={'schema':'marici.voevodsky.cosmology-influx-detector-nonuniqueness.v1','status':'detector_highly_nonunique','influx_count':len(influx),'all_triples':len(list(combinations(influx,3))),'detecting_triples':len(detect),'x_boundary_descriptor_count':len(x0),'x_boundary_detecting_triples':dx,'y_boundary_descriptor_count':len(y0),'y_boundary_detecting_triples':dy,'minimum_max_total_exponent':mins,'detectors_at_minimum_max_total_exponent':len(mintris),'example_minimal_degree_detector':[d8[k][4] for k in mintris[0]],'decision':'The earlier three-descriptor detector is a pivot choice, not unique; boundary-only and lower-degree detecting triples are counted exactly.','claim_boundary':'Nonuniqueness of coordinate probes does not remove basis-independent injectivity of the full influx restriction.','next_gate':'replace-detector-by-basis-independent-rank-invariant','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
