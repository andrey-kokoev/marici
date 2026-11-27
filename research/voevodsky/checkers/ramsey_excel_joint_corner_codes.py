"""Maximal information in all square-membership tests, within one fixed frame."""
from itertools import combinations
from collections import Counter
from ramsey_excel_overlap_corner_supply import source,D,json

def profile(p):
    masks=sorted(m for m in p['supply'] if 0<m<15)
    def codes(ms):return [tuple((m>>j)&1 for m in ms) for j in range(4)]
    cs=codes(masks);classes=len(set(cs));pos=[]
    for j in range(4):
        both=15
        for m in masks:
            if m>>j&1:both&=m
        if both==1<<j:pos.append(j)
    best=next(ms for n in range(len(masks)+1) for ms in combinations(masks,n) if len(set(codes(ms)))==classes)
    # All Boolean expressions on the tests are precisely the unions of atoms.
    alg={0,15,*masks}
    while True:
        a=alg|{15^m for m in alg}|{m&n for m in alg for n in alg}
        if a==alg:break
        alg=a
    assert len(alg)==2**classes
    return dict(focal=p['rows'],membership_masks=masks,classes=classes,indistinguishable_pairs=[(i,j) for i,j in combinations(range(4),2) if cs[i]==cs[j]],positive_singletons=pos,minimum_common_tests=best,codes=codes(best))

def run():
    result=[]
    for w in (7,8):
        _,ps,_=source(w);cases=[profile(p) for p in ps];stats=dict(width=w,class_histogram=dict(Counter(p['classes'] for p in cases)),all_four_positive=sum(len(p['positive_singletons'])==4 for p in cases));print(stats);print(next((p for p in cases if p['classes']==4),cases[0]));result.append(dict(**stats,cases=cases))
    dest=D.parent/'ramsey_excel_joint_corner_codes.json';s=json.dumps(result,indent=2)+'\n';assert not dest.exists() or dest.read_text()==s;dest.write_text(s)
if __name__=='__main__':run()
