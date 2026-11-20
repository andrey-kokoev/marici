"""Express boundary regrouping as alternating switches on the six ground labels. Distinguish four-label local replacement from six-label connected replacement, including the pole as a control."""
from ramsey_strip_boundary_mark_branch import X,P,T
for e,d in ((16,7),(17,4)):
    old=set(T[e-15]);block=P[d]
    for j,t in enumerate(T,15):
        if block not in t:continue
        new=set(t);edges=old^new;adj={}
        for a,b in edges:adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
        todo=set(adj);cycles=[]
        while todo:
            start=min(todo);cy=[start];prev=None;cur=start
            while True:
                nxt=min(adj[cur]-({prev} if prev is not None else set()))
                if nxt==start:break
                cy.append(nxt);prev,cur=cur,nxt
            todo-=set(cy);cycles.append([X[v] for v in cy])
        print('entry',e,'next',j,'common blocks',len(old&new),'alternating switches',cycles,'pole backtrack',j==29)
    # Requiring a connected switch covering all six labels, and no immediate return to pole, is sufficient.
    full=[j for j,t in enumerate(T,15) if block in t and not old&set(t) and j!=29];assert full==([22] if e==16 else [28])
