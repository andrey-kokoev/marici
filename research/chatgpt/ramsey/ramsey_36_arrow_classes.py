"""Count orbits of directed positive links under each host's full group."""
from ramsey_36_try_deck import data,unpack

def main():
    for idx,s in enumerate(data(17).splitlines(),1):
        g=unpack(s);group=g.get_automorphisms_vf2();assert len(group)==g.count_automorphisms()
        arcs={(u,v) for u in range(17) for v in g.neighbors(u)};remaining=arcs.copy();reps=[]
        while remaining:
            u,v=min(remaining);orbit={(p[u],p[v]) for p in group};assert orbit<=remaining
            remaining-=orbit;reps.append((u,v))
        print(idx,len(group),len(arcs),len(reps),'representatives (0-based)',reps)
if __name__=='__main__':main()
