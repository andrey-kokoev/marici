"""Post-prediction diagnosis only. Do not change the frozen classifier."""
from collections import Counter
from unittest.mock import patch
from ramsey38_rotation_holdout import g
import ramsey38_root15_pair_obstructions as ob

for root,drop in ((7,8),(19,7)):
    P=g[root];rows={v:frozenset(P&m) for v,m in g.items() if v not in P|{root}};fs=set(rows.values())
    with patch.multiple(ob,P=P,rows=rows,short={v:s for v,s in rows.items() if len(s)<4},facets=fs,tri=set.union(*(ob.sub(s,3) for s in fs)),all_edges=set.union(*(ob.sub(s,2) for s in fs)),tet={s for s in fs if len(s)==4}):
        outcomes=ob.audit((drop,));print(root,drop,Counter(map(str,outcomes)))
        if root==7:
            assert set(map(str,outcomes))=={'([3, 6, 21], None)','(None, [6, 21])'}
            assert {3,6,21}<=rows[23] and rows[8]=={9,27} and rows[1]=={11,27}
        else:assert outcomes==[(None,None)]*2
