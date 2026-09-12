#!/usr/bin/env python3
"""Validate typing and relation coverage of the frozen constructor alphabet."""

import json
from pathlib import Path

HERE=Path(__file__).parent
SOURCE=HERE/'boundary-pfaffian-constructor-alphabet.v1.json'

def main():
 data=json.loads(SOURCE.read_text(encoding='utf-8'))
 constructors=data['constructors'];ids=[c['id'] for c in constructors]
 assert len(ids)==len(set(ids))
 known=set(ids)
 assert all(set(r['uses'])<=known for r in data['relations'])
 protocols=data['protocols']
 assert all(set(xs)<=known for xs in protocols.values())
 stationary={c['id'] for c in constructors if c['stationary_word_generator']}
 assert stationary==set(protocols['stationary_dihedral'])=={'translate','reverse'}
 varying={'refine_break','right_extend','left_compress'}
 assert all(next(c for c in constructors if c['id']==x)['source']!=next(c for c in constructors if c['id']==x)['target'] for x in varying)
 assert next(c for c in constructors if c['id']=='ordered_sew')['arity']==2
 result={'schema':'marici.coherence.boundary-pfaffian-constructor-alphabet-check.v1','constructor_count':len(ids),'relation_count':len(data['relations']),'stationary_word_generators':sorted(stationary),'typed_protocols':sorted(protocols),'all_relation_references_resolve':True,'all_varying_graph_actions_change_fiber_type':True,'binary_sewing_excluded_from_word_monoid':True}
 (HERE/'boundary-pfaffian-constructor-alphabet-check.v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
