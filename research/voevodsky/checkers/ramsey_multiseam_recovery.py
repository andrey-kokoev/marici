from ramsey_relative_sign_joint_context import graph,grow,build,verdict,D,combinations,sha256,json
from collections import defaultdict

def run():
    z=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());S=grow(tuple(tuple(x-1 for x in s) for s in z['supports']),1);parents=[]
    for c in range(1024):
        a=graph(9,S,c)
        if not verdict(a):continue
        f={6,7};qs={frozenset(i-8 for i in q if i>=9) for q in combinations(sorted(set(range(14))-f),6) if all(not a[i]>>j&1 for i,j in combinations(q,2))};target=tuple(sorted(tuple(sorted(p)) for p in qs if not any(s<p for s in qs)));resp=[sum(1<<m for m in range(32) if verdict(build({k:tuple(i+1 for i in range(5) if m>>i&1)},S,c))) for k in range(10)];parents.append((c,target,resp))
    def evaluate(gaps):
        fibers=defaultdict(list)
        for c,t,r in parents:fibers[tuple(r[k] for k in gaps)].append((c,t))
        bad=[v for v in fibers.values() if len({t for c,t in v})>1];return dict(classes=len(fibers),ambiguous=len(bad),example=bad[:1])
    def minima(pool):
        for n in range(len(pool)+1):
            fits=[p for p in combinations(pool,n) if not evaluate(p)['ambiguous']];
            if fits:return fits
        return []
    # Post-census compact decoder, checked on the same finite domain, not a new holdout.
    decoder={tuple((r[9]>>m)&1 for m in [11,13]):t for c,t,r in parents};assert len(decoder)==3 and all(decoder[tuple((r[9]>>m)&1 for m in [11,13])]==t for c,t,r in parents)
    other=tuple(i for i in range(10) if i!=7);out=dict(protocol_sha=sha256((D.parent/'ramsey_multiseam_recovery_protocol.md').read_bytes()).hexdigest(),legal_parents=len(parents),targets=len({t for c,t,r in parents}),own=evaluate([7]),holdout=evaluate(other),all=evaluate(range(10)),minimum_other=minima(other),minimum_any=minima(tuple(range(10))),parents=parents);print({k:v for k,v in out.items() if k!='parents'});dest=D.parent/'ramsey_multiseam_recovery.json';text=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':run()
