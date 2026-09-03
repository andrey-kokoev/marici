# The cyclic converter factors exactly through triangle incidence

Let `B` be the ordered boundary from edges `(g12,g23,g31)` to vertices
`(g1,g2,g3)`, and let `C` send each vertex to its opposite occurrence pair:
`g1->G23:e6`, `g2->G31:e6`, `g3->G12:e6`. Then the unique converter satisfies
\[
A=CB.
\]
Indeed, `B(0,-1,-1)=(-1,1,0)` and
`C(-1,1,0)=(0,-1,1)`. Also `B(1,1,1)=0`, so the ordered face boundary closes.

Both `B` and `C` are canonical on free labelled lattices. The remaining gap is
now singular: `C` has not been lifted to maps between source vertex modules and
`e6` occurrence modules with transport coherence. The literal source also
lacks the `q_g12` object needed for the full cyclic edge complex.
