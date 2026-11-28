"""Expand beyond the two siblings: score all legal single trial cuts after the winning prefix on 448077 and all four failed completed cores. Extract checkable minimal integer conflicts on the three fractionally feasible losing branches."""
from ramsey_exchange_veto_transfer import *
from ramsey_port_descendants import gzip,CAT,islice,decode
from pathlib import Path
import subprocess,tempfile

def run():
    T=D.parent;full=json.loads((T/'ramsey_free_cross_profile.json').read_text());r=json.loads((T/'ramsey_cross_residual_propagation.json').read_text())['survivors'][0];start=r['start'];z=start['z'];vs=[i for i in range(27) if i!=z];
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,448077,None)).strip());
    for e in start['pair']+start['forced']:b=flip(b,e)
    pre=induced(b,vs);adds={tuple(vs.index(i) for i in e) for e in start['pair']};old=len(sets(pre,7));F=(1<<26)-1;win=set(map(tuple,r['legal'][0]));moves=[]
    for i,j in combinations(range(26),2):
        if not pre[i]>>j&1 or (i,j) in adds:continue
        h=flip(pre,(i,j));
        if not check(h,F,3,8):continue
        rows,qs=candidates(h,adds);w=packing(rows,qs);e=vs[i],vs[j];moves.append(dict(cut=e,winning=e in win,new_sevens=len(qs)-old,packing=w));assert w is None or len(w)==8 and all(sum(not q&s for s in w)<=1 for q in qs)
    ends=[]
    for c in full['core_candidates']:
        qs=sets(c['core'],7);ends.append(dict(z=c['z'],pair=c['additions'],winning=c['passes_seven'],cert=certify(qs,qs)))
    print('moves',[(m['cut'],m['winning'],m['new_sevens'],bool(m['packing'])) for m in moves],'finished',[(e['winning'],e['cert'].get('bound','feasible')) for e in ends],flush=True)
    prev=json.loads((T/'ramsey_exchange_veto_transfer.json').read_text());labels=prev['core_labels'];a=induced(G,labels);cores={}
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'reduce.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_minimal_seven_demands.rs')),'-o',str(exe)],check=True)
        for idx,c in prev['cases'].items():
            for x in c['exchanges']:
                if 'primal' not in x['early_fractional']:continue
                route=c['route'];g=a[:];
                for e in set(map(tuple,route['removed']))-set(map(tuple,route['correct'][0])):g=flip(g,e)
                g=flip(g,x['bad']);rows,qs=candidates(g,set(map(tuple,route['pair'])));ls=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,v)) for v in [rows,qs]),text=True,capture_output=True,check=True).stdout.splitlines();core=[qs[j] for j in json.loads(ls[0])];wits=[[rows[j] for j in json.loads(l)] for l in ls[1:]];assert len(wits)==len(core)
                for q,w in zip(core,wits):assert len(w)==8 and all(sum(not s&d for s in w)<=1 for d in core if d!=q) and sum(not s&q for s in w)>1
                cores[idx]=dict(all_demands=len(qs),optimistic_rows=len(rows),minimal_core=core,ablation_witnesses=wits);print(idx,len(qs),'->',len(core),flush=True)
    # Previously exhausted starts for the alternate pair: do not restrict the early test to siblings of the true route.
    alt=[];negative=json.loads((T/'ramsey_port_descendants.json').read_text());assert all(c['completions']==0 for c in negative['cases'])
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:base=decode(next(islice(f,448077,None)).strip())
    for c in negative['cases']:
        s=c['proposal'];v=[i for i in range(27) if i!=s['z']];h=base[:]
        for e in s['pair']+s['forced']:h=flip(h,e)
        h=flip(h,(17,20));g=induced(h,v)
        if not check(g,F,3,8):continue
        rows,qs=candidates(g,{tuple(v.index(i) for i in e) for e in s['pair']});covers=[r for r in rows if all(r&q for q in qs)];w=packing(rows,qs);assert w is None or len(w)==8 and all(sum(not r&q for r in w)<=1 for q in qs);alt.append(dict(z=s['z'],pair=s['pair'],extra_cut=[17,20],core_labels=v,relaxed_witness=w,rows_missing_nothing=len(covers)))
    print('false starts',[(r['z'],r['rows_missing_nothing']) for r in alt]);out=dict(record=448077,trial_core_labels=vs,moves=moves,finished=ends,transfer_core_labels=labels,integer_conflicts=cores,negative_start_controls=alt);(T/'ramsey_exchange_adversarial_replay.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
