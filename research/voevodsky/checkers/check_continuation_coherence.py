"""Two-refinement coherence, with retained authority explicitly outside summary."""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
from uuid import uuid4
import json
from atomic_fine_restoration import Vault
from verify_fine_successor import expected_archive
from continuation_coherence import root,semantic,make_path,verify_path,compare,point_query,digest,transport_defect
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def main():
 f={'normal':['0','0','1'],'upper':'1/2'}
 g={'normal':['0','0','-1'],'upper':'-1/4'}
 vault=Vault();cases=[];rejections=[]
 def reject(name,call):
  try:call()
  except (AssertionError,PermissionError,ValueError,KeyError):rejections.append(name)
  else:raise AssertionError(name+' accepted')
 for history in ('A','B'):
  event=uuid4().hex;context=digest({'family':'owning-m4-moment-curve-two-history-v1','n':18,'public_retirement':'shared'})
  token=vault._admit(event,context,18,history)
  # Explicit trusted-owner gate. A proof-path digest alone is not authority.
  grant=vault._authorize(token,event,context,digest({'operations':[f,g]}));archive=grant['archive']
  binding=root(archive,event,context)
  direct=make_path(archive,binding,[[f,g]])
  staged=make_path(archive,binding,[[f],[g]])
  reversed_path=make_path(archive,binding,[[g],[f]])
  comparison=compare(archive,binding,[[f,g]],direct,[[f],[g]],staged)
  permutation=compare(archive,binding,[[f],[g]],staged,[[g],[f]],reversed_path)
  assert not comparison['proof_paths_identical'] and not permutation['proof_paths_identical']
  base=semantic(archive,[]);parent=digest(base)
  defect={'binding':binding,'tip':parent,'retained_archive':archive}
  d1=transport_defect(defect,binding,parent,[f]);d2=transport_defect(d1,binding,d1['tip'],[g])
  assert d2['retained_archive']==archive and d2['binding']==binding
  after=verify_path(archive,binding,[[f],[g]],staged)
  answers=[]
  for p in (['1','1'],['1/18','1/324'],['1/2','1/4']):
   a=point_query(after,p);assert a==point_query(direct['edges'][-1]['successor'],p)
   if a['admitted']:
    t=tuple(map(Q,a['source_lift']));h=(t[0]-50)*128**4
    assert Q(1,4)<=h<=Q(1,2) and t[1]==51
    assert all(sum(x*y for x,y in zip(map(Q,r['normal']),(Q(p[0]),Q(p[1]),h)))<=Q(r['upper']) for r in after['fine_rows'])
   answers.append({'point':p,'answer':a})
  assert answers[0]['answer']['admitted']==(history=='B')
  assert answers[1]['answer']['admitted']==(history=='A')
  bad=deepcopy(staged);bad['edges'][1]['successor']['fine_rows'].pop()
  reject('missing-refined-row',lambda:verify_path(archive,binding,[[f],[g]],bad))
  reject('omitted-earlier-operation',lambda:compare(archive,binding,[[f,g]],direct,[[g]],make_path(archive,binding,[[g]])))
  bad=deepcopy(staged);bad['edges'][1]['parent']='foreign-parent'
  reject('broken-path-binding',lambda:verify_path(archive,binding,[[f],[g]],bad))
  foreign=expected_archive(18,'B' if history=='A' else 'A')
  reject('history-switch',lambda:verify_path(foreign,binding,[[f],[g]],staged))
  altered=deepcopy(defect);altered['retained_archive']=foreign
  reject('defect-archive-substitution',lambda:transport_defect(altered,binding,parent,[f]))
  reject('self-asserted-authority',lambda:vault._authorize({'history':history},event,context,'request'))
  cases.append({'history':history,'binding':binding,'direct':direct,'staged':staged,
   'comparison':comparison,'permuted_comparison':permutation,'point_controls':answers,
   'transported_defect_archive_digest':digest(d2['retained_archive'])})
 result={'passed':True,'cases':cases,'rejections':rejections,'archive_vault_encoded_bytes':vault.bytes(),
 'theorem_scope':'Conjunction-based fine refinement; equal canonical fine rows prove whole-domain semantic equality. Authority root remains fixed. Proof paths are compared, not identified.',
 'not_claimed':'Minimal defect, residue jet, general 4-simplex/5-cone realization, arbitrary polyhedral equivalence, simultaneous live checkpoint forks.'}
 (OUT/'continuation-coherence.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':True,'histories':2,'semantic_comparisons':4,'rejections':len(rejections)},indent=2))
if __name__=='__main__':main()
