"""All-port search on distinct one-edge exchanges from the last holdout, no ports fixed.
Usage: uv run --with igraph --with numpy python ... BULK_EXE INDEXED_EXE START COUNT
"""
from ramsey310_smallset_holdout import D,prev,eligible,cut,joint,key,json,sets,F
from pathlib import Path
from tempfile import TemporaryDirectory
from subprocess import run
import sys

def main(bulk,idx,start,n):
    old=json.loads((D/'ramsey310_matching_degree3_types.json').read_text());A=old[0].copy();skip={key(a) for a in old}
    def flip(a,i,j,x,y):a[i]^=1<<j;a[j]^=1<<i;a[x]|=1<<y;a[y]|=1<<x
    flip(A,18,9,25,17);skip.add(key(A));b=A.copy();flip(b,23,21,22,20);skip.add(key(b));flip(A,15,13,7,4);skip.add(key(A));prev.E=();graphs=[]
    for Z,edit in prev.neighbors(A):
        z=key(Z)
        if z not in skip:skip.add(z);graphs.append((Z,edit,z))
    import os
    shell=int(os.environ.get('RAMSEY_SHELL','1'));prefix='batch' if shell==1 else f'shell{shell}'
    for _ in range(1,shell):
        nxt=[]
        for parent,path,_ in graphs:
            for Z,edit in prev.neighbors(list(parent)):
                z=key(Z)
                if z not in skip:skip.add(z);nxt.append((Z,(path,edit),z))
        graphs=nxt
    if os.environ.get('RAMSEY_MIN5'):
        from ramsey310_matching_sides import instances,decode
        prefix='min5';graphs=[];skip.update(bytes.fromhex(json.loads(p.read_text())['key']) for pat in ('ramsey310_smallset_batch_*.json','ramsey310_smallset_shell*.json') for p in D.glob(pat))
        for parent,line in enumerate((D/'ramsey38_26_e73_hog.g6').read_bytes().splitlines(),1):
            for add,Z in enumerate(instances(decode(line))):
                if add<2 or min(a.bit_count() for a in Z)!=5:continue
                z=key(Z)
                if z not in skip:skip.add(z);graphs.append((Z,(parent,add),z));break
    if os.environ.get('RAMSEY_PARENT'):
        from ramsey310_matching_sides import instances,decode
        parent=int(os.environ['RAMSEY_PARENT']);prefix=f'parent{parent}';graphs=[];seen=set();line=(D/'ramsey38_26_e73_hog.g6').read_bytes().splitlines()[parent-1];labeled=0
        for add,Z in enumerate(instances(decode(line))):
            if min(a.bit_count() for a in Z)!=5:continue
            labeled+=1;z=key(Z)
            if z not in seen:seen.add(z);graphs.append((Z,(parent,add),z))
        print('labeled',labeled,flush=True)
    print('types available',len(graphs),flush=True)
    for i,(Z,edit,z) in enumerate(graphs[start:start+n],start):
        libs=[list(sets(Z,F,k)) for k in (5,6,7)];print(i,edit,len(libs[-1]),flush=True)
        if len(libs[-1])>768:continue
        with TemporaryDirectory() as tmp:
            p=Path(tmp)/'pack';s=p.with_name('sides');p.write_text(''.join(' '.join(map(str,[len(a),*a]))+'\n' for a in [Z,*libs]));
            with s.open('w') as f:bulklog=run([bulk,p],stdout=f,stderr=-1,text=True,check=True).stderr
            r=run([idx,p,s],capture_output=True,text=True,check=True);surv=[]
            for l in r.stdout.splitlines():
                E=tuple(map(int,l.split()));d,C=eligible(Z,E);t=cut(d,C);surv.append(dict(E=E,rows=len(C),certificate=t,exact=joint(Z,E)))
            out=dict(index=i,edit=edit,key=z.hex(),bulk=bulklog,join=r.stderr,survivors=surv);(D/f'ramsey310_smallset_{prefix}_{i}.json').write_text(json.dumps(out));print(r.stderr.strip(), 'uncut',sum(x['certificate'] is None for x in surv),flush=True)
if __name__=='__main__':main(*sys.argv[1:3],*map(int,sys.argv[3:]))
