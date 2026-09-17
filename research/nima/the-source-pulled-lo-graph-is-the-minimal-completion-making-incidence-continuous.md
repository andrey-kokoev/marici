# The source-pulled L/O graph is the minimal completion making incidence continuous

## Construction

Let `D_0` be the finite labelled source, let

\[
U_0:D_0\to G
\]

be the finite arithmetic-to-analytic synthesis, and fix an admitted multiplier/observer pair `(M_a,O)`. Define

\[
K_{a,O}c=
\bigl(
 c,
 U_0c,
 M_aU_0c,
 \mathcal OU_0c,
 \mathcal OM_aU_0c
\bigr).
\]

Complete the graph:

\[
D^{\mathrm{src}}_{a,O}
=
\overline{K_{a,O}(D_0)}
\subset
\widehat{\mathcal A}\times G\times G\times B\times B.
\]

Retaining the source coordinate does not by itself make projection to the completed source faithful. Faithfulness holds exactly when the displayed operator family is jointly closable: a source-null net may otherwise converge to a nonzero vertical graph vector. The required joint closability is now proved by dependency induction from continuity of `U_4` and closability of the admitted multiplier and retained observation. Therefore the analytic coordinates extend continuously by construction. In particular,

\[
\widehat U_4:D^{\mathrm{src}}_{a,O}\to D_{a,O}
\]

is continuous and

\[
\widehat{\mathcal O}\widehat M_a\widehat U_4
=D_a^\partial\widehat{\mathcal O}\widehat U_4.
\]

Thus this gives the canonical candidate for closing the arithmetic incidence gate without claiming that the old, coarser completion of all `A_exp` already lands in the `L/O` graph. The gate is closed for admitted closed multipliers and retained closed observation, for finite families and coordinatewise projective pro-families.

## Minimality

Suppose `E` is any complete locally convex source carrier receiving `D_0` densely such that the five coordinates above extend continuously. By the joint-closability theorem, the map from `D_0` into `E` is continuous for every seminorm defining the graph closure, so it extends uniquely through `D^{src}_{a,O}`. Hence this graph topology is the minimal faithful source refinement only after the closability gate passes.

For a finite observer family, include all such coordinates in one graph. For a pro-family, take the projective limit of finite-family source-pulled graphs. No uniform Hilbert norm is implied.

## What this resolves

In the declared retained-graph scope, it resolves the incidence problem in the retained-graph semantics:

\[
D_0\longrightarrow D^{\mathrm{src}}_{a,O}
\xrightarrow{\widehat U_4}D_{a,O}.
\]

It avoids the false stronger assertion

\[
U_4(\mathcal A_{\exp})\subset D_{a,O}
\]

for the unchanged coarse topology.

## New coherence gate

Changing the source topology creates a nonredundant higher-coherence obligation. Rooted substitution and physical cut maps were proved continuous for the projective coefficient/Laurent topology. To act on `D^{src}_{a,O}`, they must also transport the pulled-back graph coordinates. For each `S` in `{H,V}`, one needs estimates of the form

\[
p(K_{a,O}Sc)
\le C\sum_j p_j(K_{a_j,O_j}c).
\]

Equivalently, `H` and `V` must preserve the source-pulled `L/O` graph family, possibly while transporting the observer labels. These are `R-C-L-H`, `R-C-O-H`, `R-C-L-V`, and `R-C-O-V` higher faces, not failures of the already proved pairwise `R x H` and `R x V` continuity theorems.

The eighth completion prism therefore has all pairwise face types, but its higher assembly still requires graph stability under the two arity actions.
