"""Associative concatenation only inside one source-generation scope."""
from pathlib import Path
import json
def atom(a,b,source='rows-A',generation=1):return {'start':a,'end':b,'scope':(source,generation),'edges':((a,b,'bound-weakening@1'),)}
def compose(p,q):
 if p['end']!=q['start']:raise ValueError('MIDDLE_ID_MISMATCH')
 if p['scope']!=q['scope']:raise ValueError('SOURCE_SCOPE_MISMATCH')
 return {'start':p['start'],'end':q['end'],'scope':p['scope'],'edges':p['edges']+q['edges']}
a,b,c=atom('P','Q'),atom('Q','R'),atom('R','S')
left=compose(compose(a,b),c);right=compose(a,compose(b,c))
assert left==right and left['edges']==a['edges']+b['edges']+c['edges'] and len(left['edges'])==3
stale=atom('Q','R','rows-B',2)
for x,y in ((a,stale),(stale,c)):
 try:compose(x,y)
 except ValueError as err:assert str(err)=='SOURCE_SCOPE_MISMATCH'
 else:raise AssertionError('cross-source composition accepted')
report={'passed':True,'three_same_source_edges':'both bracketings equal ordered three-edge sequence','mixed_source_middle':'rejected before either associativity claim','scope':'Synthetic path structure only, not valid Farkas proof, observed event, issuer or analytic map.'}
out=Path(__file__).resolve().parents[1]/'results/scoped-path-associativity.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
