"""Keep the intermediate matching exactly, change only the literal involution. Test existence of the original single ten-flag criterion on successive sides, and distinguish a word period from a matching period."""
from ramsey_join_flag_phase import lift,final,move,R,D,json
from ramsey_history_matching_provenance import enum
from ramsey_fork_missing_corner import partner

def trans(a,b):return lift(tuple(b if i==a else a if i==b else i for i in range(1,5)))
def sizes(m,n):
    adj={}
    for i,j in m^n:adj.setdefault(i,set()).add(j);adj.setdefault(j,set()).add(i)
    out=[]
    while adj:
        todo=[next(iter(adj))];seen=set(todo)
        for x in todo:
            for y in adj.pop(x):
                if y not in seen:seen.add(y);todo.append(y)
        out.append(len(todo))
    return sorted(out)

def run():
    M,=final;initial=M;rows=[];half=None
    for k,(a,b) in enumerate([(3,2),(2,4),(4,3)]*2):
        n=move(M,trans(a,b));assert partner(next(d for d,j in M if j==29))==a and partner(next(d for d,j in n if j==29))==b;rows.append(dict(exchange=[a,b],common=len(M&n),components=sizes(M,n),equals_initial=n==initial));M=n
        if k==2:half=n
    assert M==initial;eligible=[]
    for m in enum():
        if (4,29) not in m:continue
        eligible.append([sizes(m,move(m,trans(a,b)))==[10] for a,b in [(2,3),(2,4)]])
    return dict(steps=rows,three_step_common=len(initial&half),dual_ten_controls={str(test):eligible.count(list(test)) for test in ((False,False),(True,False),(False,True),(True,True))})
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_hold_matching_switch_swap.json').write_text(json.dumps(out)+'\n')
