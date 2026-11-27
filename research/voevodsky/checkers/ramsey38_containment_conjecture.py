"""Conjecture 3: distinguish a missing destination from a missing relative shelling."""
from ramsey38_open_middle_cone_trial import P,R,prev,json
from ramsey38_middle_choice_holdout import graph,prepare,face_assignments,shelling,extend,faces,boundary

def audit():
    truth=json.loads(R.read_text());assert truth['prediction_sha']==prev.sha(P.read_bytes());it=iter(truth['results']);results=[]
    for e in json.loads(P.read_text())['cases']:
        prep=None
        for d in e['requests']:
            r=next(it);assert (e['record'],d['moves'],d['goal'])==(r['record'],r['moves'],r['goal']);bad=sorted(set(d['passes'])-set(r['ok']))
            if not bad:continue
            if prep is None:prep=prepare(graph(e['word']),e['u'])
            L,rows,cells,dec,stage,_=prep;req,shells=stage(tuple(sorted(map(tuple,d['moves']))));bds=shells.get(frozenset(d['goal']),[]);assign={};final={}
            for bd in bds:
                fs=set(map(dec,bd))
                for ts in face_assignments(L,req,fs):
                    B=frozenset(ts);assert boundary(B)==fs;assign[B]=bd;o=shelling(B)
                    if o:final[B]=[sorted(s) for s in o]
            for i in bad:
                M=frozenset(map(frozenset,d['pool'][i]));assert shelling(M);contains=[B for B in final if M<=B];assert all(extend(M,B) is None for B in contains);closest=min(final,key=lambda B:(len(M-B),len(B-M),faces(B)),default=None);z=dict(record=e['record'],root=e['u'],goal=d['goal'],moves=d['moves'],index=i,shells=len(bds),face_assignments=len(assign),containing_assignments=sum(M<=B for B in assign),final_balls=len(final),containing_balls=len(contains),min_remove=None if closest is None else len(M-closest),closest_order=None if closest is None else final[closest],order_obstructions=[dict(final_order=final[B],addition=faces(B-M)) for B in contains]);z['containing_assignment_defects']=[]
                for B,bd in assign.items():
                    if not M<=B:continue
                    from ramsey38_twist10_edge_certificate import failures
                    from ramsey38_novel_root8_diagonal import sub,link_profile
                    errors=failures(B,set(map(dec,bd)));links={}
                    if not errors:
                        for v in L:
                            fs={s-{v} for s in B if v in s}
                            if not fs:continue
                            n,ori=link_profile(fs);chi=len(set.union(set(),*fs))-len(set.union(*(sub(s,2) for s in fs)))+len(fs);want=1 if any(v in dec(f) for f in bd) else 2
                            if (n,ori,chi)!=(1,True,want):links[v]=dict(components=n,orientable=ori,chi=chi,expected=want)
                    z['containing_assignment_defects'].append(dict(cells=faces(B),edge_failures=[dict(edge=k,**v) for k,v in errors.items()],bad_links=links))
                results.append(z);print({k:v for k,v in z.items() if k not in ('moves','closest_order','order_obstructions')})
    assert len(results)==6 and next(it,None) is None;prev.save(prev.out/'ramsey38_containment_conjecture_defects.json',dict(verification_sha=prev.sha(R.read_bytes()),cases=results))
if __name__=='__main__':audit()
