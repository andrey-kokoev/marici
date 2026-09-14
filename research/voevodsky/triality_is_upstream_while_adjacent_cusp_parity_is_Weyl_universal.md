# Triality is upstream while adjacent-cusp parity is Weyl-universal

The three conductor matchings carry the natural action

\[
\mathrm{GL}(2,\mathbb F_2)\cong S_3,
\]

so the upstream compound-\(D_4\) triality statement is confirmed.

Its proposed equivariant embedding into Picard parity fails. The three nonzero classes of

\[
D_4^\vee/D_4\cong(\mathbb Z/2)^2
\]

would all have to map to the universal bitangent class

\[
-K_S\pmod2.
\]

This assignment is incompatible with addition: in \((\mathbb Z/2)^2\),

\[
(1,0)+(0,1)=(1,1),
\]

whereas their proposed images satisfy

\[
1+1=0
\]

in the \(E_7\) discriminant group \(\mathbb Z/2\). Hence integral Picard parity forgets the triality label. C7 is confirmed upstream and rejected as a downstream equivariant embedding.

The quartic family has four critical values

\[
0,\quad2x,\quad2y,\quad2(x+y).
\]

They split into two repeated collision types:

\[
\{0,2(x+y)\},
\qquad
\{2x,2y\}.
\]

At every endpoint, the split-pair difference is primitive, has square \(-6\), is orthogonal to \(K_S\), lies in the single \(W(E_7)\)-orbit, and satisfies

\[
d\equiv-K_S\pmod2.
\]

Thus the invariant part of C8 is confirmed: divisibility and mod-two parity are preserved at all four adjacent cusps.

A labelled transport matrix still depends on the physical basepoint, based path, Hurwitz ordering, and integral Picard--Lefschetz lift. These data select the endpoint Weyl element and orientation sign while leaving the universal parity unchanged.

Certificate:

- `research/voevodsky/checkers/transport_C7_C8_triality_and_adjacent_cusps.py`;
- `research/voevodsky/results/C7_C8_triality_adjacent_cusp_transport.json`.
