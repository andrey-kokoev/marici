"""Fibers after deleting reciprocal seam events, even when the projected tour starts at a specified apex. No shortest-path or cube-color inputs."""
from ramsey_handoff_distance_audit import run as native_tours, D, json

def run():
    out={}
    for tail,head in ('CD','DC'):
        rows=[]
        for t in native_tours():
            word=t['word'];k,=[i for i,e in enumerate(word) if e[0]==tail];w=word[k:]+word[:k];j,=[i+1 for i,e in enumerate(w) if e[1]==head];first,rest=w[:j],w[j:];recip={e for e in w if e[::-1] in w};rim=lambda arc:[e for e in arc if e not in recip];assert len(rim(first))==len(rim(rest))==2;assert sorted(map(len,(first,rest)))==[2,4];long=max((first,rest),key=len);assert long[1]==long[2][::-1];rows.append(dict(seam=t['seam'],outward=first,inward=rest,projected=[rim(first),rim(rest)]))
        assert rows[0]['projected']==rows[1]['projected'] and rows[0]['seam']!=rows[1]['seam'];out[tail+head]=rows
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_based_rim_projection_fiber.json').write_text(json.dumps(out)+'\n')
