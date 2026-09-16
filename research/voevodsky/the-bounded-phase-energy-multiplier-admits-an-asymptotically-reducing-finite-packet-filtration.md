# The bounded phase-energy multiplier admits an asymptotically reducing finite-packet filtration

## Objective

Construct a packet-natural global target for absolute-Gram convergence, avoiding arbitrary packetwise Jordan decompositions.

## Global target already available

On the local phase-energy completion \(\mathscr E_S\), the Tate form is represented by the bounded self-adjoint multiplier

\[
\mathcal A_S=M_{a_S},
\qquad
|a_S|\le C_S.
\]

Therefore its positive target is the packet-independent bounded operator

\[
\boxed{R_S=|\mathcal A_S|=M_{|a_S|}.}
\]

The global two-polarity feature is

\[
m\longmapsto
(\mathcal A_{S,+}^{1/2}m,
 \mathcal A_{S,-}^{1/2}m).
\]

Thus the limit form does not need to be assembled from finite packet Jordan decompositions.

## Spectrally adapted packets

Let \(A=\mathcal A_S\). Partition the compact interval \([-C_S,C_S]\) into Borel intervals of mesh \(\delta_n\downarrow0\). Write \(E_A(I)\) for the spectral projection of \(A\).

Inside each spectral cell choose an increasing finite-dimensional family from a fixed countable dense set in \(E_A(I)\mathscr E_S\). Taking the direct sum over the finitely many cells gives finite-rank orthogonal projections \(P_n\) such that

\[
P_n\to I
\quad\text{strongly}.
\]

Each finite-dimensional summand of \(P_n\) stays inside one spectral cell. If \(c_I\) is a point of that cell, then

\[
\|(A-c_I)E_A(I)\|\le\delta_n.
\]

Since \(c_I I\) commutes with every projection inside the cell,

\[
\boxed{
\|[A,P_n]\|\le 2\delta_n.}
\]

The same argument applies to every Lipschitz function of \(A\). In particular,

\[
\boxed{
\|[|A|,P_n]\|\le2\delta_n,}
\]

because \(x\mapsto|x|\) is one-Lipschitz.

## Compression versus packetwise absolute value

Let

\[
A_n=P_nAP_n|_{P_n\mathscr E_S}.
\]

On each spectral cell, both \(A\) and \(A_n\) differ from the same scalar \(c_I\) by at most \(\delta_n\). Finite-dimensional functional calculus then yields

\[
\boxed{
\bigl\|
|A_n|-P_n|A|P_n
\bigr\|
\le 2\delta_n.}
\]

Consequently packetwise Jordan decomposition becomes asymptotically compatible along this filtration, despite being incompatible for arbitrary compressions.

## Exact global form convergence of the target filtration

Since \(|A|\) is bounded and \(P_n\to I\) strongly,

\[
P_n|A|P_n\to|A|
\quad\text{strongly}.
\]

Combining with the preceding estimate gives

\[
|P_nAP_n|P_n
\to |A|
\quad\text{strongly}.
\]

Thus the bounded phase-energy completion supplies both:

1. a packet-independent closed positive target form;
2. a cofinal finite-packet filtration on which compressed absolute values converge to that target.

No uniform observability lower bound is used.

## What this does not solve

The construction concerns the limiting Tate multiplier, not the finite physical prolate residuals \(R_\Lambda\). To prove physical Mosco convergence one still needs:

- exact positive-regulator alignment producing \(R_\Lambda\) globally before compression;
- comparison of the physical source completion with \(\mathscr E_S\);
- a regulator-tail estimate such as
  \[
  \sup_{\Lambda\ge\Lambda_n}
  \|[R_\Lambda^{1/2},P_n]\|_{graph\to H}
  \longrightarrow0;
  \]
- convergence on these adapted packets.

The new point is that the target-side packet naturality is no longer open. The sole off-packet estimate belongs to the physical residual family.

## Updated channel-2 frontier

1. global limit form \(|\mathcal A_S|\) on the phase-energy completion: constructed;
2. asymptotically reducing cofinal packet filtration for the limit: constructed;
3. physical aligned global residual feature: open;
4. uniform commutator/tail comparison for that physical residual: open;
5. Mosco convergence: formal after 3 and 4 plus completion identification.

## Repository dependencies

- `the-local-phase-energy-completion-turns-the-tate-form-into-a-bounded-self-adjoint-multiplier.md`
- `global-absolute-gram-mosco-convergence-reduces-to-uniform-graph-core-and-compression-control.md`
- `completed_four_port_behavior_is_pro_faithful_but_not_uniformly-observable_20260910.md`
