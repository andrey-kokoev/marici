"""Two candidate input rules. Neither is assumed to be the operator's rule."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path


def run():
    full=127
    rows=[sum(1<<(i-1) for i in s) for s in combinations(range(1,8),3) if min(s[1]-s[0],s[2]-s[1])>=2]
    result={}
    for r in rows:
        static=Counter(); change=Counter()
        for plus in range(128):
            no_rm=not (r & ~plus);no_bp=not ((full^r)&plus)
            static[f'{int(no_rm)}{int(no_bp)}']+=1
        for t in rows:
            # Red loss and blue gain are the very same R -> B transition.
            red_lost=r & ~t;blue_gained=(full^t)&r
            assert red_lost==blue_gained
            change[f'{int(not red_lost)}{int(not blue_gained)}']+=1
        assert static=={'00':105,'01':7,'10':15,'11':1} and change=={'00':9,'11':1}
        result[''.join(str(i+1) for i in range(7) if r>>i&1)]=dict(static=static,row_change=change)
    path=Path(__file__).resolve().parents[1]/'results/ramsey_excel_sensor_inputs.json';path.write_text(json.dumps(result,indent=2)+'\n');print(result['135'])

if __name__=='__main__':run()
