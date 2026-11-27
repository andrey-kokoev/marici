"""Hold edits, tip and shells fixed; pin one local disk and propagate, no mesh search."""
from ramsey38_matched_mesh_trial import P,prev,json,graph,setup,disks,faces,attaches,shelling
from ramsey38_compare_support_fillings import boundary
from itertools import permutations

def reduce_domains(Q):
    rounds=0
    while all(Q.values()):
        N={a:[s for s in opts if all(any({t for t in s if b in t}=={t for t in h if a in t} for h in Q[b]) for b in Q if b!=a)] for a,opts in Q.items()}
        if N==Q:break
        Q=N;rounds+=1
    return Q,rounds

def domains(e,q):
    L,rs,_=setup(graph(e['word']),e['u']);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);x,v=q['first'];y,t=q['second'];r1={**rs,x:rs[x]|1<<L.index(v)};r2={**r1,y:r1[y]|1<<L.index(t)};tip=dec(rs[x])|{q['tip']};E=set(map(frozenset,q['collar']));B=set(map(dec,q['bd']));F=set(map(dec,q['end']));Q={}
    for a in L:
        D=set(disks(L,a,F,set(map(dec,r2.values()))|E|{tip}));Q[a]=sorted((s for s in disks(L,a,B,set(map(dec,r1.values()))|{tip}) if not s&E and s|{t for t in E if a in t} in D),key=faces)
    return reduce_domains(Q)[0],E,B,F

def run():
    out=[]
    for e in json.loads(P.read_text())['cases']:
        for d in e['requests']:
            if not d['commit'] or d['pick']:continue
            Q,E,B,F=domains(e,d['commit']);assert {str(a):len(ss) for a,ss in Q.items()}==d['sizes'];cert={};pins=[]
            for a,opts in Q.items():
                if len(opts)==1:continue
                for i,s in enumerate(opts):
                    D,n=reduce_domains({**Q,a:[s]});r=dict(vertex=a,choice=i,sizes=[len(ss) for ss in D.values()],rounds=n)
                    if all(len(ss)==1 for ss in D.values()):
                        mesh=frozenset.union(*(ss[0] for ss in D.values()));assert all({t for t in mesh if w in t}==ss[0] for w,ss in D.items());r['mesh']=cert.setdefault(mesh,len(cert))
                    pins.append(r)
            plans=[]
            for mesh,num in cert.items():
                o=shelling(mesh);orders=[s for s in permutations(E) if all(attaches(mesh|set(s[:i]),t) for i,t in enumerate(s))];assert boundary(mesh)==B and boundary(mesh|E)==F;plans.append(dict(id=num,old_order=[sorted(t) for t in o],extensions=[[sorted(t) for t in s] for s in orders]));print(e['record'],num,len(mesh),bool(o),len(orders))
            diff=None
            if len(cert)==2:
                a,b=cert;diff=[faces(a-b),faces(b-a)];print('difference',diff)
            print('pins',[(z['vertex'],z['choice'],z.get('mesh'),z['rounds']) for z in pins]);out.append(dict(record=e['record'],root=e['u'],j=d['j'],l=d['l'],commit=d['commit'],pins=pins,plans=plans,difference=diff))
    prev.save(prev.out/'ramsey38_mesh_single_pin.json',dict(source_sha=prev.sha(P.read_bytes()),cases=out))
if __name__=='__main__':run()
