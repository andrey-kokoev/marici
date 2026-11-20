"""Grow all legal small bases until some are absent from the unique 35-host."""
from ramsey_bottom_up_compare import children,graph
from ramsey_border_order import unpack
from ramsey_39_fixed_seed_exact import host

def main():
    h=unpack(host.encode());pool={0}
    for n in range(1,10):
        pool={c for p in pool for c in children(n-1,p,9)}
        missing=[m for m in sorted(pool) if not h.subisomorphic_lad(graph(n,m),induced=True)]
        print(n,len(pool),len(missing));
        if missing:
            for m in missing:print(graph(n,m).get_edgelist())
            return
if __name__=='__main__':main()
