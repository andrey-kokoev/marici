from itertools import combinations
from ramsey_relative_sign_joint_context import D, build, graph, grow, json, sha256, verdict


def obstruction(n, rows, reds):
    # For each mutually blue port set, greedily take the leftmost available
    # site on each path run, then every second site. This maximizes its size.
    for k in range(6):
        for p in combinations(range(5), k):
            if any(a in p and b in p for a, b in reds):
                continue
            blocked = {v for a in p for v in rows[a]}
            sites = []
            for v in range(n):
                if v not in blocked and (not sites or sites[-1] != v-1):
                    sites.append(v)
            if len(sites)+k >= 7:
                return dict(sites=[v+1 for v in sites], ports=[a+1 for a in p])
    return None


def run():
    pairs = list(combinations(range(5), 2)); cases = []; wins = set()
    for last in (7,8):
        rows = sorted([(1,3,7),(1,3,8),(2,4,7),(2,4,8),(1,4,last)])
        ss = [tuple(v-1 for v in s) for s in rows]
        edges = [e for e in pairs if set(ss[e[0]]).isdisjoint(ss[e[1]])]; assert len(edges)==2
        for first in (0,1,2,3,7,8):
            gap = 5 + (first < 5); parent = grow(ss,first); child = grow(parent,gap)
            obs = []; valid = []
            for reds in (edges[:1],edges[1:],edges):
                c=sum(1<<pairs.index(e) for e in reds)
                w=[obstruction(9,parent,reds),obstruction(10,child,reds)]
                ok=[x is None for x in w]; assert ok==[verdict(graph(9,parent,c)),verdict(build({gap:()},parent,c))]
                obs.append(w);valid.append(ok)
            usable=valid==[[True,False],[True,False],[True,True]]
            if usable:wins.add((tuple(rows),first,gap))
            cases.append(dict(rows=rows,first=first,gap=gap,edges=edges,obstructions=obs,usable=usable))
            print(last,first,valid)
    census=json.loads((D.parent/'ramsey_double_flank_contact.json').read_text());prev={(tuple(map(tuple,c['rows'])),chart['first'],c['gap']) for chart in census['charts'] for c in chart['cases'] if c['gap'] not in (chart['first'],chart['first']+1)}
    mirror=lambda rows:tuple(sorted(tuple(9-x for x in reversed(s)) for s in rows))
    assert wins|{(mirror(r),8-f,9-g) for r,f,g in wins}==prev
    prefix=D.parent/'ramsey_six_site_partitions';prefix.with_suffix('.json').write_text(json.dumps(dict(protocol_sha=sha256((D.parent/'ramsey_six_site_partitions_protocol.md').read_bytes()).hexdigest(),cases=cases),indent=2)+'\n')

if __name__=='__main__':run()
