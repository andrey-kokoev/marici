"""Resume only between pairs; keep the registered timing driver unchanged. Load its exact pinned arm verbatim, add checkpoints outside the timed region."""
import ast,hashlib,inspect
import ramsey_six_hit_experiment as frozen
from ramsey_six_hit_experiment import D,Path,json,subprocess,tempfile,median

def run():
    T=D.parent;first=json.loads((T/'ramsey_six_hit_timing_partial.json').read_text());driver=Path(frozen.__file__);kern=driver.with_name('ramsey_six_hit_search.rs');port=driver.with_name('ramsey_free_port_census.rs');files=(driver,kern,port);pins={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in files};assert list(pins.values())==[first[k] for k in ('driver_sha256','kernel_sha256','port_solver_sha256')];source=inspect.getsource(frozen.run);arm_src=ast.get_source_segment(source,next(n for n in ast.walk(ast.parse(source)) if isinstance(n,ast.FunctionDef) and n.name=='arm'));p=T/'ramsey_six_hit_timing_resume.json';r=json.loads(p.read_text()) if p.exists() else dict(record=99148,pins=pins,pairs=first['completed_pairs'][:],outputs=None);assert r['pins']==pins and r['pairs'][0]==first['completed_pairs'][0];j=len(r['pairs']);assert 1<=j<5
    with tempfile.TemporaryDirectory() as td:
        exes=[]
        for f in (kern,port):
            exe=Path(td)/(f.stem+'.exe');subprocess.run(['rustc','--edition=2021','-O',str(f),'-o',str(exe)],check=True);exes.append(exe)
        env=dict(frozen.__dict__,exe=exes[0],ports=exes[1],data=' '.join(map(str,frozen.read(99148))));exec(compile(arm_src,str(driver),'exec'),env);pair={}
        for s in (('off','on') if j%2==0 else ('on','off')):
            v,_=env['arm'](s,'quiet',[]);out=json.loads(json.dumps(v.pop('outputs')));assert out and v['counts']==r['pairs'][0][s]['counts'];
            if r['outputs'] is None:r['outputs']=out
            assert out==r['outputs'];pair[s]=v;print(j,s,v,flush=True)
        pair['outputs_matched']=True;r['pairs'].append(pair);r['median_ratio']=median(x['on']['seconds']/x['off']['seconds'] for x in r['pairs']);r['complete']=len(r['pairs'])==5;tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(r,indent=1)+'\n');tmp.replace(p);print('complete pairs',len(r['pairs']),'median paired ratio',r['median_ratio'],flush=True)
if __name__=='__main__':run()
