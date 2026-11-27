"""All first pins on unresolved one-pin holdout; if still ambiguous test every second pin."""
from ramsey38_mesh_single_pin import domains,reduce_domains,boundary,attaches,shelling,faces,permutations
from ramsey38_one_pin_holdout import P,prev,json
from collections import Counter

def run():
    out=[]
    for e in json.loads(P.read_text())['cases']:
        for d in e['requests']:
            if not d.get('pin') or d['pick']:continue
            Q,E,B,F=domains(e,d['commit']);meshes={};tests=[]
            def inspect(D):
                if not all(D.values()):return 'inconsistent'
                if not all(len(ss)==1 for ss in D.values()):return 'open'
                mesh=frozenset.union(*(ss[0] for ss in D.values()));assert all({t for t in mesh if w in t}==ss[0] for w,ss in D.items());o=shelling(mesh);seq=next((s for s in permutations(E) if all(attaches(mesh|set(s[:i]),t) for i,t in enumerate(s))),None);assert boundary(mesh)==B and boundary(mesh|E)==F
                if not o or seq is None:return 'invalid'
                if mesh not in meshes:meshes[mesh]=dict(id=len(meshes),initial_order=[sorted(t) for t in o],append=[sorted(t) for t in seq]);return meshes[mesh]['id']
                return meshes[mesh]['id']
            for a,opts in sorted(Q.items()):
                if len(opts)<2:continue
                for i,s in enumerate(opts):
                    D,n=reduce_domains({**Q,a:[s]});result=inspect(D);rec=dict(vertex=a,choice=i,rounds=n,result=result,second=[])
                    if result=='open':
                        for b,ss in D.items():
                            if len(ss)<2:continue
                            for h in ss:
                                DD,nn=reduce_domains({**D,b:[h]});rec['second'].append(dict(vertex=b,choice=Q[b].index(h),result=inspect(DD)))
                    tests.append(rec)
            print(e['record'],[(a,[r['result'] for r in tests if r['vertex']==a]) for a in sorted(Q)],'seconds',Counter(str(s['result']) for r in tests for s in r['second']));out.append(dict(record=e['record'],root=e['u'],j=d['j'],l=d['l'],commit=d['commit'],tests=tests,meshes=list(meshes.values())))
    assert len(out)==2;prev.save(prev.out/'ramsey38_pin_pivot_audit.json',dict(source_sha=prev.sha(P.read_bytes()),cases=out))
if __name__=='__main__':run()
