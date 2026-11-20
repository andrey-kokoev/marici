"""Small SQL experiment: join local COLOR ASSIGNMENTS, rather than finding cliques in a supplied graph. Stdlib only. No target order argument."""
import sqlite3
from itertools import combinations, product, count

def column(edge):return 'e%d_%d'%edge

def run(l,k):
    db=sqlite3.connect(':memory:');db.execute('create table bit(c integer primary key)');db.executemany('insert into bit values (?)',[(0,),(1,)])
    for r,bad in [(l,1),(k,0)]:
        w=r*(r-1)//2;db.execute(f'create table t{bad}('+','.join(f'x{i} integer' for i in range(w))+')');db.executemany(f'insert into t{bad} values ('+','.join('?'*w)+')',(t for t in product((0,1),repeat=w) if any(v!=bad for v in t)))
    for n in count(2):
        pairs=list(combinations(range(n),2));parts=[];seen=set()
        for r,bad in [(l,1),(k,0)]:
            for s in combinations(range(n),r):
                es=list(combinations(s,2));seen.update(es);parts.append('(select '+','.join(f'x{i} as {column(e)}' for i,e in enumerate(es))+f' from t{bad})')
        parts+=['(select c as '+column(e)+' from bit)' for e in pairs if e not in seen];sql='select count(*) from '+' natural join '.join(parts);num=db.execute(sql).fetchone()[0];print(n,num,flush=True)
        if num==0:break
    db.close()
if __name__=='__main__':run(3,3)
