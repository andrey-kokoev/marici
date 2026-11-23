"""Check receipt coverage only. Values can disagree; unavailable observations do not pass."""
import itertools,json,sys
corners='I X Y XY YX'.split()
required={'frozen':'carrier marks X Y readout compare'.split(),'readings':corners+['XX','YY'],'comparisons':[':'.join(p) for p in itertools.combinations(corners,2)]+['I:XX','I:YY'],'comparison_of_comparisons':['I:X vs Y:YX','I:Y vs X:XY']}
def template():return {k:{i:{'status':'missing','result':None,'evidence':''} for i in v} for k,v in required.items()}
def gaps(r):
 for k,items in required.items():
  for i in items:
   v=r.get(k,{}).get(i,{})
   if not isinstance(v,dict) or v.get('status')!='recorded' or v.get('result') in (None,'',{},[]) or not str(v.get('evidence') or '').strip():yield f'{k}/{i}'
if __name__=='__main__':
 if sys.argv[1:]==['--template']:print(json.dumps(template(),indent=2));sys.exit(0)
 if len(sys.argv)!=2:sys.exit('usage: two_perspective_gate.py --template | receipt.json')
 with open(sys.argv[1],encoding='utf-8') as f:missing=list(gaps(json.load(f)))
 print('PARTIAL: '+', '.join(missing) if missing else 'Complete records; mathematical verdict requires review.');sys.exit(bool(missing))
