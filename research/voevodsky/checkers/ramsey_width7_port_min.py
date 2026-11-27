from ramsey_forward_path_insertion import graph,check,D,combinations,Counter,sha256,json

def run():
    rows=[t for t in combinations(range(7),3) if min(t[1]-t[0],t[2]-t[1])>=2];stats=Counter();cases=[]
    for A,B in combinations(rows,2):
        if set(A)&set(B):continue
        h,=set(range(7))-set(A+B);stats['pairs']+=1
        for m in range(1,5):
            ss=[A]*m+[B]*(5-m);bit=1<<list(combinations(range(5),2)).index((0,m));cols=(0,bit)
            if not all(check(graph(7,ss,c),(1<<12)-1,3,7) for c in cols):continue
            stats['legal_parent_pairs']+=1;split=[];both=[];neither=[]
            for gap in range(8):
                t=[tuple(j+(j>=gap) for j in s) for s in ss];flags=[check(graph(8,t,c),(1<<13)-1,3,7) for c in cols];assert flags!=[True,False]
                if flags==[False,True]:
                    split.append(gap);assert h not in (gap-1,gap);cl=[h+(h>=gap),gap,*range(8,13)];g=graph(8,t,0);assert all(not(g[u]>>v&1) for u,v in combinations(cl,2))
                elif flags[0]:both.append(gap)
                else:neither.append(gap)
            stats['opposite_decisions']+=len(split);cases.append(dict(A=[x+1 for x in A],B=[x+1 for x in B],copies_A=m,uncovered=h+1,separating=split,both_legal=both,both_illegal=neither))
    example=next(c for c in cases if any(0<g<7 for g in c['separating']));print(stats,example);p=D.parent/'ramsey_width7_port_protocol.md';data=dict(protocol_sha=sha256(p.read_bytes()).hexdigest(),counts=stats,gap_convention='number of old sites before insertion',cases=cases);r=D.parent/'ramsey_width7_port_min.json';s=json.dumps(data,indent=2)+'\n';assert not r.exists() or r.read_text()==s;r.write_text(s)
if __name__=='__main__':run()
