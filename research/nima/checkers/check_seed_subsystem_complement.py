"""First WG-first boundary step on the actual six-packet seed.

Extract labelled crossing ports and exhaustive first-return paths for marked A.
Counting linearization and formal path length are not physical response/time.
No gravitational target coefficients enter the construction.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_natural_tower_return import PACKETS, LABELS, incidence

ROOT=Path(__file__).resolve().parents[1]


def mm(a,b):
    return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)


def main():
    root='A';outside=tuple(x for x in LABELS if x!=root)
    outgoing=tuple(p for p in PACKETS if p[1]==root and p[2] in outside)
    incoming=tuple(p for p in PACKETS if p[1] in outside and p[2]==root)
    internal=tuple(p for p in PACKETS if p[1] in outside and p[2] in outside)
    assert tuple(p[0] for p in outgoing)==('AB','AD')
    assert tuple(p[0] for p in incoming)==('CA','BA')
    assert tuple(p[0] for p in internal)==('BC','DB')
    assert set(outgoing+incoming+internal)==set(PACKETS)
    M=incidence(PACKETS)
    idx=[LABELS.index(v) for v in outside]
    C=tuple(tuple(M[i][j] for j in idx) for i in idx)
    U=tuple((M[i][0],) for i in idx)
    V=(tuple(M[0][j] for j in idx),)
    C2=mm(C,C);C3=mm(C2,C)
    assert C3==((0,0,0),)*3 and any(x for row in C2 for x in row)
    # C^3=0 certifies no complement-only route of length >=3. Consequently
    # first returns have at most four edges; enumeration is exhaustive.
    adjacency={v:tuple(p for p in PACKETS if p[1]==v) for v in LABELS}
    frontier=[(root,())];returns=[]
    while frontier:
        vertex,path=frontier.pop()
        for name,s,t in adjacency[vertex]:
            new=path+(name,)
            if t==root:returns.append(new)
            else:
                assert len(new)<=3
                frontier.append((t,new))
    returns=sorted(returns,key=lambda p:(len(p),p))
    assert set(returns)=={('AB','BA'),('AB','BC','CA'),('AD','DB','BA'),('AD','DB','BC','CA')}
    counts=Counter(map(len,returns));assert counts=={2:1,3:2,4:1}
    assert (mm(V,U)[0][0],mm(mm(V,C),U)[0][0],mm(mm(V,C2),U)[0][0])==(1,2,1)
    by_name={p[0]:p for p in PACKETS}
    port_packet=[]
    for path in returns:
        at=root;boundary=Counter();visited=[root]
        for name in path:
            _,s,t=by_name[name]
            assert s==at
            boundary[t]+=1;boundary[s]-=1
            at=t;visited.append(t)
        assert at==root and all(v!=root for v in visited[1:-1])
        assert all(x==0 for x in boundary.values())
        # A closed path is not an empty history: all paid arrow occurrences
        # and their direction are retained, even for the two-edge AB/BA return.
        assert len(path)>0
        port_packet.append(dict(outgoing=path[0],incoming=path[-1],arrows=path,
                                length=len(path),vertices=visited))
    # Row order BA,CA; column order AB,AD. Keep the full port matrix before
    # any aggregate sum or choice of a physical response observable.
    ordered_in=('BA','CA');ordered_out=('AB','AD')
    degrees=tuple(tuple(next(len(p) for p in returns if p[0]==out and p[-1]==inc)
                        for out in ordered_out) for inc in ordered_in)
    assert degrees==((2,3),(3,4))
    # Controls: the all-to-all complement response used in the older spectral
    # trial is an extension, not an inventory of these primitive seed arrows.
    complete={(s,t) for s in LABELS for t in LABELS if s!=t}
    seed={(s,t) for _,s,t in PACKETS}
    added=sorted(complete-seed)
    assert len(added)==6 and ('D','A') in added and ('A','C') in added
    assert ('AD','DA') not in returns
    source=ROOT/'checkers/check_natural_tower_return.py'
    result=dict(schema='marici.nima.seed-subsystem-complement.v1',status='pass',
                source='checkers/check_natural_tower_return.py:PACKETS',source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                obligation='source boundary inventory and composition of existing directed paths, before response-law selection',
                chosen_subsystem=[root],complement=outside,primitive_packets=PACKETS,
                outgoing_ports=outgoing,incoming_ports=incoming,complement_internal=internal,
                complement_order=outside,complement_incidence=[[str(x) for x in row] for row in C],
                complement_nilpotence_index=3,first_return_paths=port_packet,
                port_rows=ordered_in,port_columns=ordered_out,port_path_length_degrees=degrees,
                formal_port_kernel='[[z^2,z^3],[z^3,z^4]]',
                formal_aggregate_first_return='z^2+2*z^3+z^4',
                kernel_meaning='z grades primitive traversal count; entries retain their actual labelled path witnesses. No physical time, probability, energy or gain interpretation supplied.',
                extra_edges_required_by_complete_directed_support=added,
                disposition='Actual seed supplies two outward and two inward ports, linked by four exhaustive first-return paths through its acyclic complement. No all-to-all source extension or 1/90, -1/5280 coefficients used.',
                residual='Chosen marked subsystem, not uniquely selected physical split. Composable paths give return histories, not null-homotopies or a physical complement reaction law. Need a sourced operator/state/readout on this retained port packet to claim a gravitational response.')
    (ROOT/'results/seed-subsystem-complement.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('primitive_packets','first_return_paths')},indent=2))


if __name__=='__main__':main()
