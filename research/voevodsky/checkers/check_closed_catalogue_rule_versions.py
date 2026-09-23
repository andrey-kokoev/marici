"""Reject unknown, ambiguous, and unversioned edge rules before evaluating endpoints."""
from pathlib import Path
import json
rules={'comparison@1','bound-weakening@1'}
def dispatch(edge):
 label=edge.get('rule')
 if not isinstance(label,str) or label not in rules:return 'UNKNOWN_OR_AMBIGUOUS_RULE_VERSION'
 if label=='comparison@1':return 'CHECK_SAME_EXACT_TARGET'
 return 'CHECK_SAME_NORMAL_WEIGHTS_AND_SURPLUS_INCREMENT'
assert dispatch({'rule':'comparison@1'})=='CHECK_SAME_EXACT_TARGET'
assert dispatch({'rule':'bound-weakening@1'})=='CHECK_SAME_NORMAL_WEIGHTS_AND_SURPLUS_INCREMENT'
for bad in ({},{'rule':'comparison'},{'rule':'comparison@2'},{'rule':['comparison@1','bound-weakening@1']},{'rule':'comparison@1|bound-weakening@1'}):
 assert dispatch(bad)=='UNKNOWN_OR_AMBIGUOUS_RULE_VERSION'
report={'passed':True,'admitted_rule_labels':sorted(rules),'rejected':'missing/unversioned/future/array/compound labels','scope':'Rule dispatch gate only, not endpoint proof, historical occurrence, issuer or analytic mapping.'}
out=Path(__file__).resolve().parents[1]/'results/closed-catalogue-rule-versions.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
