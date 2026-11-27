"""Outcome-blind enrichment: first local-veto then later local pass in fixed ranking."""
from ramsey38_precommit_holdout import both,compare,last,old,prior,previous,P as recent,prev,json,sys
from ramsey38_append_holdout import source,key,graph,setup,gzip,add,proposals
from collections import Counter
P=prev.out/'ramsey38_retry_contrast_predictions.json';R=prev.out/'ramsey38_retry_contrast_comparison.json'
protocol='After 1242, first eligible novel array per record using previous structural criteria. Among goals with >=2 ranked candidates, select first final-pass candidate raw-pair veto followed by later raw-pair pass, regardless of whether latter predicts a mesh. Stop at 3 qualifying records or 80 novel arrays or record 2500. Do not use filling outcomes. Report conditional yield only.'
def scan():
    seen={key(*setup(graph(e['word']),e['u'])) for p in [source,old,prior,previous,last,recent] for e in json.loads(p.read_text())['cases']};out=[];stats=Counter();exam=[]
    def selector(e,L,rs,cands):
        stats['goals']+=1
        if len(cands)<2:return dict(pick=None,contrast=False)
        stats['multi_candidate_goals']+=1;r=both(e,L,rs,cands);stats['veto_first_multi']+=bool(r['skipped']);return dict(r,contrast=bool(r['skipped'] and r['commit']))
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=1242:continue
            if i>2500:break
            word=line.strip();g=graph(word)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,moves=setup(g,u)
                if len(moves)<2 or sum(s.bit_count()==2 for s in rs.values())<2 or max(map(int.bit_count,rs.values()))>4 or not any(setup(add(g,m),u)[2] for m in moves):continue
                k=key(L,rs,moves)
                if k in seen:continue
                seen.add(k);e=dict(record=i,u=u,word=word);ds=proposals(e,selector);rows=[d for d in ds if d['contrast']];exam.append([i,u]);stats['arrays']+=1
                if rows:out.append(dict(e,requests=rows));print('contrast',i,len(rows),flush=True)
                break
            if len(out)>=3 or len(exam)>=80:break
    print(stats,exam[-1],len(out));prev.save(P,dict(protocol=protocol,screened=exam,counts=dict(stats),cases=out))
if __name__=='__main__':
    if sys.argv[1]=='freeze':scan()
    elif sys.argv[1]=='compare':compare(P,R)
