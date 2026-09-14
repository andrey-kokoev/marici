#!/usr/bin/env python3
"""Assign four-way static relation types and compile the frozen action quiver."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
inv=json.loads((R/'research/conjecture_replay/results/del_pezzo_entrance_conjectures.json').read_text())
# Each original alternative receives exactly one relation type. The pair is a
# static classification: candidate polarity -> resolved polarity.
maps={
'DP1':{'++':3,'+-':2,'-+':0,'--':1},
'DP2':{'++':3,'+-':2,'-+':1,'--':0},
'DP3':{'++':3,'+-':2,'-+':0,'--':1},
'DP4':{'++':1,'+-':2,'-+':0,'--':3},
'DP5':{'++':3,'+-':2,'-+':0,'--':1},
'DP6':{'++':2,'+-':3,'-+':0,'--':1},
'DP7':{'++':3,'+-':2,'-+':0,'--':1},
'DP8':{'++':3,'+-':2,'-+':0,'--':1}}
meaning={
'++':'the proposed mechanism and its target interpretation are established',
'+-':'the proposed structure exists, while its advertised target interpretation is rejected',
'-+':'the proposed mechanism is absent and that rejection is established',
'--':'the attempted rejection is itself unsupported or inconclusive'}
typed=[]
for c in inv['conjectures']:
 m=maps[c['id']]; assert set(m)==set(meaning) and sorted(m.values())==[0,1,2,3]
 typed.append({'id':c['id'],'relations':{s:{'meaning':meaning[s],'concrete_outcome':c['explicit_alternatives'][i]} for s,i in m.items()}})
# Outcome-labelled adjacency. This is a finite retrospective policy search
# grammar, not a temporal claim about the mathematical net.
A={
 'O':{'*':['DP1','DP2','DP6','DP7','DP8']},
 'DP1':{'++':['DP2','DP3','DP4','DP5'],'+-':['DP7'],'-+':['DP7'],'--':['DP7']},
 'DP2':{'++':['DP3','DP4','DP6'],'+-':['DP4','DP6'],'-+':['DP6'],'--':['DP6']},
 'DP3':{'++':['DP6'],'+-':['DP4','DP6'],'-+':['DP6'],'--':['DP7']},
 'DP4':{'++':['DP5','DP6'],'+-':['DP5','DP6'],'-+':['DP5','DP6'],'--':['DP7']},
 'DP5':{'++':['DP6'],'+-':['DP6'],'-+':['DP6'],'--':['DP6']},
 'DP7':{'++':['DP2','DP3','DP4'],'+-':['DP2','DP3'],'-+':['DP2','DP6'],'--':['DP2','DP6']},
 'DP8':{'++':['DP5','DP6'],'+-':['DP5','DP6'],'-+':['DP6'],'--':['DP6']},
 'DP6':{'++':['T_readout'],'+-':['T_partial'],'-+':['T_rejected'],'--':['T_unresolved']}}
# Enumerate simple outcome-labelled paths; revisiting an action is disallowed.
paths=[]
def walk(node,used,steps):
 if node.startswith('T_'):
  paths.append({'terminal':node,'steps':steps});return
 for outcome,targets in A[node].items():
  for target in targets:
   if target not in used:
    walk(target,used|{target},steps+([{'action':node,'outcome':outcome,'next':target}] if node!='O' else [{'action':'O','outcome':'*','next':target}]))
walk('O',{'O'},[])
readout=[p for p in paths if p['terminal']=='T_readout']
checks={'all_four_types_used':all(set(x['relations'])==set(meaning) for x in typed),'bijective_outcome_typing':all(len({v['concrete_outcome'] for v in x['relations'].values()})==4 for x in typed),'all_inventory_nodes_typed':{x['id'] for x in typed}=={x['id'] for x in inv['conjectures']},'finite_paths':len(paths)>0,'readout_reachable':len(readout)>0,'paths_simple':all(len([s['action'] for s in p['steps']])==len(set(s['action'] for s in p['steps'])) for p in paths)}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-typed-quiver.v1','sign_semantics':meaning,'typed_conjectures':typed,'initially_available':A['O']['*'],'adjacency':A,'terminals':{'T_readout':'physical integral class resolved','T_partial':'physical degeneration found but target rank rejected','T_rejected':'absence of proposed physical degeneration confirmed','T_unresolved':'physical experiment inconclusive'},'enumeration':{'simple_policy_paths':len(paths),'readout_paths':len(readout),'terminal_counts':{t:sum(p['terminal']==t for p in paths) for t in ['T_readout','T_partial','T_rejected','T_unresolved']},'maximum_steps':max(len(p['steps']) for p in paths)},'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_typed_quiver.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,**out['enumeration']}))
