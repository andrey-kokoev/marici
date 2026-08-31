# Triple incidence is a relative boundary-corner transport problem

Use the source wall coordinates

\[
u=q_1,\qquad v=q_2,\qquad q_3=u+v+p.
\]

The pairwise wall vertices are

\[
(0,0),\qquad(0,-p),\qquad(-p,0),
\]

and coalesce at \(p=0\). The fiber-normal circuit is
\((-1,-1,1)\), which has mixed signs under every common projective rescaling.
Moreover, the Cayley--Menger polynomial is generically nonzero at the
collision. Therefore this is not one of the ordinary interior \(A_1\) folds
for which earlier source-regulator calculations proved intersection magnitude
one.

The Bunch--Davies prescription still fixes the local approach

\[
p\mapsto p-i(\epsilon_1+\epsilon_2+3\epsilon_3).
\]

The correct next constructor is consequently a relative, ordered-wall blow-up
of \((u,v,p)=(0,0,0)\), followed by transport of the sewn source chain. A
nonzero physical period cannot be inferred before that variation is computed.

Artifacts:

- `research/nima/checkers/check_cosmology_triple_incidence_boundary_corner_transport.py`
- `research/nima/results/cosmology_triple_incidence_boundary_corner_transport.json`
