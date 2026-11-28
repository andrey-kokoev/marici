"""Full prefix screen on 448077. Held-out timing: 5 predeclared pairs, one worker, alternate first arm, include all search and completion work; compile and read catalogue before timing. 'pilot' uses one site only and cannot decide speed transfer."""
from ramsey_port_descendants import D,CAT,decode,gzip,islice,json,subprocess,tempfile,Path
from time import perf_counter
from statistics import median
import sys

def read(idx):
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:return decode(next(islice(f,idx,None)).strip())

def run(mode):
    T=D.parent;idx=448077 if mode=='screen' else 99148;b=read(idx);data=' '.join(map(str,b));
    with tempfile.TemporaryDirectory() as td:
        def build(name):
            exe=Path(td)/(name+'.exe');subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_name(name+'.rs')),'-o',str(exe)],check=True);return exe
        exe=build('ramsey_six_hit_search');ports=build('ramsey_free_port_census')
        def arm(switch,detail,scope):
            t=perf_counter();ls=subprocess.run([str(exe),switch,detail,*scope],input=data,text=True,capture_output=True,check=True).stdout.splitlines();st=[];survivors=[];cores=set()
            for l in ls:
                k,z,line=l.split(' ',2);z=int(z)
                if k=='core':cores.add((z,tuple(json.loads(line))))
                elif k=='done':st.append(json.loads(line))
                else:
                    i,j,u,v,q,g=line.split(' ',5);survivors.append(dict(z=z,additions=[[int(i),int(j)],[int(u),int(v)]],failed_probe=int(q),core=json.loads(g)))
            cores=sorted(cores);out=[];done=[]
            if cores:
                ls=subprocess.run([str(ports)],input='\n'.join(' '.join(map(str,g)) for _,g in cores),text=True,capture_output=True,check=True).stdout.splitlines();
                for l in ls:
                    k,v=l.split(' ',1)
                    if k=='done':done.append(int(v))
                    else:out.append([*cores[int(k)],json.loads(v)])
                assert done==list(range(len(cores)))
            return dict(seconds=perf_counter()-t,counts=list(map(sum,zip(*st))),outputs=out),survivors
        if mode=='screen':
            r,p=arm('on','detail',[]);exact=json.loads((T/'ramsey_free_cross_profile.json').read_text());assert len(r['outputs'])==len(exact['outputs'])==1;z,g,rows=r['outputs'][0];true=exact['outputs'][0];assert (z,list(g),sorted(rows))==(true['z'],true['core'],sorted(true['profile']['rows']));ws=[x for x in p if x['z']==z and all(h&v==v for h,v in zip(x['core'],g)) and x['additions']==[[[i for i in range(27) if i!=z].index(j) for j in e] for e in true['additions']]];assert ws and all(not x['failed_probe'] for x in ws);out=dict(record=idx,run=r,winning_prefixes=len(ws),baseline_prefixes=p)
        else:
            pairs=[];scope=['25'] if mode=='pilot' else [];ref=None
            for j in range(1 if scope else 5):
                pair={}
                for s in (('off','on') if j%2==0 else ('on','off')):
                    v,_=arm(s,'quiet',scope);assert v['outputs'];
                    if ref is None:ref=v['outputs']
                    assert ref==v.pop('outputs');pair[s]=v;print(j,s,v,flush=True)
                pairs.append(pair)
            out=dict(record=idx,scope=scope,pairs=pairs,outputs=ref,median_ratio=median(p['on']['seconds']/p['off']['seconds'] for p in pairs))
        print(mode,out.get('run',{}).get('counts'),out.get('winning_prefixes'),out.get('median_ratio'),flush=True);(T/('ramsey_six_hit_'+mode+'.json')).write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':run(sys.argv[1])
