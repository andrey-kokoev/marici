from interface_centrality import *
def test_shared_bottleneck_beats_leaf():
 actions=[InterfaceAction('B',frozenset({'bridge'}),frozenset({'x'}),1),InterfaceAction('C',frozenset({'bridge'}),frozenset({'y'}),1),InterfaceAction('T',frozenset({'x','y'}),frozenset({'goal'}),1)]
 scores=score_interfaces(actions,frozenset(),'goal',{'bridge':2,'leaf':1})
 assert scores[0].interface=='bridge' and scores[0].closure_unlocks==3 and scores[0].target_reachable
 assert not next(x for x in scores if x.interface=='leaf').target_reachable
if __name__=='__main__':test_shared_bottleneck_beats_leaf();print('PASS 1/1')
