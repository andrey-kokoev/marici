"""Compare rule-first GROUP BY, edge-first relational division, and direct clique readout. Group payload is a set of rule IDs (vertex masks, with sign in the key)."""
import sqlite3, json, hashlib
from pathlib import Path
from itertools import combinations,product
from collections import Counter
H=Path(__file__).resolve().parents[1]
RULE='''with units as (select r,s,max(case when a.v is null then t.e end) e from t left join a using(e) group by r,s having count(*)-count(a.v)=1 and sum(case when v<>s then 1 else 0 end)=0) select e,s,json_group_array(r) from units group by e,s'''
EDGE='''select t.e,t.s,json_group_array(t.r) from t where not exists(select 1 from a where a.e=t.e) and not exists(select 1 from t q left join a on a.e=q.e where q.r=t.r and q.s=t.s and q.e<>t.e and a.v is not t.s) group by t.e,t.s'''
class Trial:
 def __init__(self,n,k):
    self.n=n;self.k=k;self.E=list(combinations(range(n),2)); self.rules=[(sum(1<<v for v in vs),s,[self.E.index(e) for e in combinations(vs,2)]) for s,size in [('+',3),('-',k)] for vs in combinations(range(n),size)];d=self.db=sqlite3.connect(':memory:');d.executescript('create table t(r,s,e, primary key(r,s,e));create index transpose on t(e,s,r); create table a(e integer primary key,v text not null);');d.executemany('insert into t values(?,?,?)',[(r,s,e) for r,s,es in self.rules for e in es]);self.count=Counter()
 def test(self,state):
    if any(all(state[i]==s for i in es) for _,s,es in self.rules):self.count['already_illegal']+=1;return
    self.count['tested']+=1;d=self.db;d.execute('delete from a');d.executemany('insert into a values(?,?)',[(i,v) for i,v in enumerate(state) if v]);
    def read(q):return {(e,s):sorted(json.loads(rs)) for e,s,rs in d.execute(q)}
    first=read(RULE);assert first==read(EDGE)
    # Directly insert each proposed sign, enumerate monochromatic subsets in resulting graph.
    adj={e:v for e,v in zip(self.E,state)};direct={}
    for i,e in enumerate(self.E):
        if adj[e]:continue
        for s,size in [('+',3),('-',self.k)]:
            adj[e]=s;found=[sum(1<<x for x in vs) for vs in combinations(range(self.n),size) if all(adj[p]==s for p in combinations(vs,2))];
            if found:direct[i,s]=sorted(found)
        adj[e]=None
    assert direct==first;self.count['witness_groups']+=len(first);return first

def main():
 a=Trial(4,3)
 for state in product((None,'+','-'),repeat=6):a.test(state)
 b=Trial(9,8);state=[None if e==(0,1) else '+' if e in [(0,8),(1,8)] else '-' for e in b.E];w=b.test(state);assert w=={(0,'+'):[259],(0,'-'):[255]}
 c=Trial(6,3);assert c.test([None]*15)=={};ok=sum(not any(all(bits[i]==s for i in es) for _,s,es in c.rules) for bits in product('+-',repeat=15));assert ok==0
 out=dict(checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),K4_33=dict(a.count),K9_38_double_block={s:[i for i in range(9) if rs[0]>>i&1] for (_,s),rs in w.items()},empty_K6_33=dict(groups=0,full_completions_checked=32768,legal=ok));print(json.dumps(out));(H/'results/ramsey_transpose_witness_groups.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
