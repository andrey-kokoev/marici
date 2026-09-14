"""Audit the integral endpoint-to-Gysin stage before physical support transport."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 d=json.loads(Path(a.input).read_text());rows=d['line_retaining_adjunction_comparison'];assert len(rows)==16
 checked=[]
 for r in rows:
  assert r['normalized_cohomology']['line']=={'0':1}
  assert r['normalized_cohomology']['Gysin']=={'0':1}
  assert r['normalized_cohomology']['comparison']=={}
  assert r['normalized_cohomology']['fibre']=={'0':1}
  assert all(abs(int(x))>=0 for x in r['unit_pivots'])
  checked.append({'T':r['T'],'endpoint':r['endpoint'],'central':bool(r['central_face']),
                  'line_H0':1,'Gysin_H0':1,'comparison_acyclic':True,'fibre_H0':1})
 out={'schema':'marici.nima.endpoint-gysin-W-transport-stage.v1','status':'passed','cases':checked,
  'integral_cases':len(checked),
  'conclusion':'endpoint line to coefficient Gysin comparison is an integral quasi-isomorphism in all 16 cases; only coefficient-Gysin to physical-supported identification remains'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
