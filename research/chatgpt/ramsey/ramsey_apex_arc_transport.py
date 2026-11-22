"""Exhaust vertex relabelings with optional path reversal, comparing the image of a retained apex arc to the row-swapped outward arc. No clock assignment or score input."""
from itertools import permutations
from ramsey_handoff_distance_audit import run as tours,D,json

def arc(w,a,b):
    i,=[i for i,e in enumerate(w) if e[0]==a];s=w[i:]+w[:i];j,=[j for j,e in enumerate(s) if e[1]==b];return s[:j+1]

def run():
    ts=tours();E=set(ts[0]['word']);out=[]
    for p in permutations('ABCD'):
        g=dict(zip('ABCD',p))
        for rev in (False,True):
            def move(w):return [''.join(g[x] for x in (e[::-1] if rev else e)) for e in (w[::-1] if rev else w)]
            if set(move(list(E)))!=E:continue
            for t in ts:
                w=t['word'];v=move(w);before=arc(w,'C','D');image=move(before);wanted=arc(v,'D','C');out.append(dict(map=''.join(p),reverse=rev,seam=t['seam'],fixes_mark=g['A']=='A',apexes_exchanged=g['C']=='D',original=before,image=image,row_outward=wanted,same_arc=image==wanted))
    assert len(out)==8;row=[x for x in out if x['apexes_exchanged']];assert all(x['same_arc']!=x['fixes_mark'] for x in row);return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_apex_arc_transport.json').write_text(json.dumps(out)+'\n')
