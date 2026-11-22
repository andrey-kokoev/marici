"""Enumerate first-hit apex trails without repeating native occurrences, with the WHOLE partition visible. Test linear use at the flag, underlying ground-label, and directed-occurrence levels separately."""
from ramsey_exit_port_types import run as types,D,json,X

def run():
    out=[]
    for t in types():
        p=t['binding'];blocks=t['blocks'];slot={e:d for d,es in blocks.items() for e in es};support={e:tuple(sorted(p.index(x)+1 for x in e)) for e in slot};rows=[]
        for row in t['rows']:
            a,b=row['arc'];tail,head=a[0],b[1];words=[]
            def walk(v,w):
                if v==head:words.append(w);return
                for e in slot:
                    if e not in w and e[0]==v:walk(e[1],w+[e])
            walk(tail,[]);assert sorted(map(len,words))==[2,4];tests=[]
            for w in sorted(words,key=len):
                d=[slot[e] for e in w];s=[support[e] for e in w];tests.append(dict(word=w,duads=d,ground_edges=s,flag_linear=len(set(d))==len(d),ground_linear=len(set(s))==len(s)));assert (len(w)==2)==tests[-1]['flag_linear']==tests[-1]['ground_linear'];assert (len(w)==2 or (d[1:3]==[9,9] and s[1:3]==[(1,4)]*2 and w[1]==w[2][::-1]))
            rows.append(tests)
        out.append(dict(binding=p,rows=rows))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_exit_consumption_units.json').write_text(json.dumps(out)+'\n')
