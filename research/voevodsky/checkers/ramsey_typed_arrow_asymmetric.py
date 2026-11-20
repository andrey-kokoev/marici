"""Exhaustive single-table arrow readout, K4, asymmetric targets (3,4)."""
from itertools import combinations, product
from pathlib import Path
import sqlite3,json,hashlib

QUERY='''WITH units AS (
 SELECT r.src,r.sign,max(CASE WHEN a.dst IS NULL THEN r.dst END) AS missing
 FROM arrow r LEFT JOIN arrow a ON a.role='assigns' AND a.src='g' AND a.dst=r.dst
 WHERE r.role='forbids_jointly' GROUP BY r.src,r.sign
 HAVING count(*)-count(a.dst)=1 AND sum(CASE WHEN r.sign<>a.sign THEN 1 ELSE 0 END)=0
) SELECT missing,sign,src FROM units'''

def run():
    db=sqlite3.connect(':memory:');db.execute('create table arrow(src text,dst text,role text,sign text,primary key(src,role,dst))');V='0123';edges=[''.join(x) for x in combinations(V,2)]
    for sign,k in [('+',3),('-',4)]:
        for vs in combinations(V,k):
            db.executemany("insert into arrow values(?,?,'forbids_jointly',?)",[(''.join(vs),''.join(e),sign) for e in combinations(vs,2)])
    # Oracle tests explicit triangles and the unique four-clique in fixed edge order 01,02,03,12,13,23.
    def forbidden(x):
        a,b,c,d,e,f=x
        return {w for w,test in [('012',a==b==d=='+'),('013',a==c==e=='+'),('023',b==c==f=='+'),('123',d==e==f=='+'),('0123',a==b==c==d==e==f=='-')] if test}
    legal=moves=plus=minus=0
    for x in product((None,'+','-'),repeat=6):
        if forbidden(x):continue
        legal+=1;db.execute("delete from arrow where role='assigns'");db.executemany("insert into arrow values('g',?,'assigns',?)",[(e,v) for e,v in zip(edges,x) if v is not None]);expected=set()
        for j,v in enumerate(x):
            if v is not None:continue
            for s in '+-':
                moves+=1;expected.update((edges[j],s,w) for w in forbidden(x[:j]+(s,)+x[j+1:]))
        assert set(db.execute(QUERY))==expected,(x,expected)
        plus+=sum(s=='+' for _,s,_ in expected);minus+=sum(s=='-' for _,s,_ in expected)
    return dict(domain='K4; plus forbids K3; minus forbids K4; unknown = absent assignment',ternary_states=729,admitted_states=legal,moves_compared=moves,plus_witness_rows=plus,minus_witness_rows=minus,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run();print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_typed_arrow_asymmetric.json').write_text(json.dumps(out,indent=2)+'\n')
