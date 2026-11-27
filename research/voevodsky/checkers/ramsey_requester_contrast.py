from ramsey_relative_sign_joint_context import build,verdict,grow,graph,D,combinations,sha256,json

def run():
    z=json.loads((D.parent/'ramsey_port_repair_orbits.json').read_text());orig=z['supports'];pairs=list(combinations(range(5),2));col=sum(1<<pairs.index((i-1,j-1)) for i,j in [(2,4),(2,5)]);out={}
    for name,ss in [('base',orig),('5_to_4',orig[:4]+[orig[3]]),('4_to_5',orig[:3]+[orig[4]]+orig[4:])]:
        S=grow(tuple(tuple(v-1 for v in s) for s in ss),1);a=graph(9,S,col);legal=verdict(a);rec=dict(parent_legal=legal);out[name]=rec
        if not legal:
            from ramsey_five_port_multi import sevens
            rec['parent_blue_seven']=next(sevens(a),None);print(name,rec);continue
        def blue(q):return all(not(a[i]>>j&1) for i,j in combinations(q,2))
        rec['moves']=[]
        for twin,req,gap in ((t,r,g) for t in (2,3) for r in (4,5) for g in range(10)):
            f={gap-1,gap}&set(range(9));ports={8+twin,8+req};N=f|ports;T=[(i,j) for i,j in combinations(sorted(N),2) if {i,j}!=f and a[i]>>j&1];X=[q for q in combinations(sorted(set(range(14))-N),6) if blue(q)];E=[q for q in combinations(sorted(v for v in set(range(14))-f if all(not a[v]>>h&1 for h in f)),5) if blue(q)] if len(f)==2 else [];ok=verdict(build({gap:(twin,req)},S,col));assert ok==(not T and not X and not E);rec['moves'].append(dict(twin=twin,req=req,gap=gap,red_edges=T,blue_sixes=X,flank_fives=E,legal=ok))
        for req in (4,5):print(name,req,[(m['gap'],len(m['red_edges']),len(m['blue_sixes']),len(m['flank_fives'])) for m in rec['moves'] if m['twin']==3 and m['req']==req]);print('last',rec['moves'][-1]['red_edges'])
    print([m for m in out['base']['moves'] if m['gap']==9 and m['twin']==3]);r=D.parent/'ramsey_requester_contrast.json';s=json.dumps(dict(protocol_sha=sha256((D.parent/'ramsey_requester_contrast_protocol.md').read_bytes()).hexdigest(),vertex_convention='0..8 current width-nine sites, 9..13 ports 1..5 in obstruction lists',cases=out),indent=2)+'\n';assert not r.exists() or r.read_text()==s;r.write_text(s)
if __name__=='__main__':run()
