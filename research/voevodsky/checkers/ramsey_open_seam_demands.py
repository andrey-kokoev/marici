from ramsey_relative_sign_joint_context import build,verdict,grow,graph,D,combinations,sha256,json,Counter

def run():
    z=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());S=grow(tuple(tuple(v-1 for v in s) for s in z['supports']),1);pairs=list(combinations(range(5),2));out=[]
    for rep in z['representatives']:
        c=sum(1<<pairs.index((i-1,j-1)) for i,j in rep['edits']);a=graph(9,S,c);stats=Counter();gaps=[]
        def blue(q):return all(not a[i]>>j&1 for i,j in combinations(q,2))
        for k in range(10):
            f={k-1,k}&set(range(9));V=set(range(14))-f;qs=[q for q in combinations(sorted(V),6) if blue(q)];sets={frozenset(i for i in q if i>=9) for q in qs};small=sorted((s for s in sets if not any(t<s for t in sets)),key=sorted);E=len(f)==2 and any(blue(q) for q in combinations(sorted(i for i in V if all(not a[i]>>j&1 for j in f)),5));openmoves=[]
            for p in combinations(range(9,14),2):
                pc=tuple(i-8 for i in p);local=blue(p) and all(not(a[i]>>j&1) for i in p for j in f);X=any(not s.intersection(p) for s in small);assert verdict(build({k:pc},S,c))==(local and not X and not E)
                reason='triangle' if not local else ('XE' if E and X else 'E' if E else 'X' if X else 'legal');stats[reason]+=1
                if local:openmoves.append([pc,reason])
            gaps.append(dict(gap=k,sixes=len(qs),minimal_port_sets=[[i-8 for i in sorted(s)] for s in small],flank_veto=E,open_moves=openmoves))
        print(rep['edits'],stats,gaps[-1]);out.append(dict(repair=rep['edits'],counts=stats,seams=gaps))
    r=D.parent/'ramsey_open_seam_demands.json';s=json.dumps(dict(protocol_sha=sha256((D.parent/'ramsey_open_seam_demands_protocol.md').read_bytes()).hexdigest(),cases=out),indent=2)+'\n';assert not r.exists() or r.read_text()==s;r.write_text(s)
if __name__=='__main__':run()
