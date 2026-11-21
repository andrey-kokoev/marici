"""Blind decision from maximum independent rows only. Test against six previously solved regular-lift cases."""
from ramsey_slack_ladder_replay import attach,D,json
from itertools import combinations

def predict(H):
    I=[0]
    for i,r in enumerate(H):I += [s|1<<i for s in I if not s&r]
    top=[s for s in I if s.bit_count()==7];anchors=[i for i,r in enumerate(H) if r.bit_count()==7];active=sum(1<<i for i in anchors);assert len(anchors)==8
    domains=[[s for s in top if s&active==1<<v] for v in anchors];miss={s:sum(1<<j for j,t in enumerate(top) if not t&s) for dom in domains for s in dom};sizes=list(map(len,domains))
    # Arc consistency: every candidate must have a compatible partner in every other domain.
    while True:
        new=[[s for s in dom if all(i==j or any(not miss[s]&miss[t] for t in other) for j,other in enumerate(domains))] for i,dom in enumerate(domains)]
        if any(not dom for dom in new) or new==domains:break
        domains=new
    def find(rows,selected):
        if not rows:return selected
        rows=sorted(rows,key=len)
        for s in rows[0]:
            ans=find([[t for t in other if not miss[s]&miss[t]] for other in rows[1:]],selected+[s]);
            if ans:return ans
    return {'maximum_rows':len(top),'domains':sizes,'survivors':list(map(len,new)),'top_only_clique':find(new,[])}
if __name__=='__main__':
    K=json.loads((D/'ramsey_slack_ladder_certificates.json').read_text())[0]['graph'];rows=json.loads((D/'ramsey_sparse26_forward_check.json').read_text());out=[]
    for row in rows:
        H=attach(K,row['first_supports']);r=predict(H);r['supports_to26']=row['first_supports'];r['verified_regular_lift']='graph' in row['anchor_lift'];print(r['maximum_rows'],r['survivors'],bool(r['top_only_clique']),r['verified_regular_lift']);out.append(r)
    (D/'ramsey_miss_prediction.json').write_text(json.dumps(out)+'\n')
