"""Ordinary width-six triple rows; legal parent required. Hidden-port ambiguity bound and sharp example."""
from ramsey_forward_path_insertion import graph,trial,check,D,combinations,sha256,json

def run():
    rows=[s for s in combinations(range(6),3) if min(s[1]-s[0],s[2]-s[1])>=2];pairs=[(a,b) for a,b in combinations(rows,2) if set(a).isdisjoint(b)];assert pairs==[((0,2,4),(1,3,5))];a,b=pairs[0];ss=[a]*3+[b]*3;bit=1<<list(combinations(range(6),2)).index((0,3));cases={}
    for col in (0,bit):
        assert check(graph(6,ss,col),(1<<12)-1,3,7);cases[str(col)]=[trial(6,ss,col,i)[0] for i in range(7)]
    print(cases);assert cases['0'][1:6]==['X']*5 and cases[str(bit)][1:6]==['pass']*5
    # A witness changing legality has to contain an edge whose color changes.
    # Its two (disjoint) triples cover all old sites. Of path sites only the insertion can join it.
    assert all(set(a)|set(b)==set(range(6)) for a,b in pairs)
    p=D.parent/'ramsey_seam_hidden_port_protocol.md';r=dict(protocol_sha=sha256(p.read_bytes()).hexdigest(),zero_based_supports=ss,port_edge_bit_order=list(combinations(range(6),2)),seams=cases,min_ports=6);dest=D.parent/'ramsey_seam_hidden_port.json';text=json.dumps(r,indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':run()
