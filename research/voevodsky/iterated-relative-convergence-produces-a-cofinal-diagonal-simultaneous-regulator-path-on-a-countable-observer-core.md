# Iterated relative convergence produces a cofinal diagonal simultaneous-regulator path on a countable observer core

## Countable core

Choose a countable complex-linear observer core

\[
E_{count}
=
\operatorname{span}_{\mathbb Q(i)}
\{g_1,g_2,\ldots\}
\]

inside the Bruhat--Schwartz semilocal test space. Enumerate all ordered pairs from this core as

\[
(u_1,v_1),
(u_2,v_2),
\ldots.
\]

Let

\[
W_j
=W_S(u_j*v_j^*).
\]

## Regulated relative forms

Let

\[
T_{L,R,N,n,F}(u,v)
\]

be the signed `C_34` readout of the finite positive relative feature with:

- physical logarithmic cutoff `L`;
- outer regulator `R`;
- angular cutoff `N`;
- dyadic depth `n`;
- conductor level `F`.

The exact eight-leg and dyadic identities make this form well typed at every finite index.

## Iterated convergence hypothesis

Assume the proved/declared iterated limits have the following form for every core pair:

1. for fixed `L,n,F`,
   \[
   \lim_{R,N\to\infty}
   T_{L,R,N,n,F}(u,v)
   =T_{L,n,F}(u,v);
   \]
2. for conductor levels containing `u,v`, depth refinement does not change the signed readout;
3. as `L->infinity`,
   \[
   T_{L,n,F}(u,v)
   \longrightarrow
   W_S(u*v^*),
   \]
   after the translated-placement commutator vanishes.

No rate uniform in `L` is assumed.

## Exhausting source constraints

For each `k`, choose a conductor level `F_k` containing the angular support of

\[
g_1,
\ldots,
g_k.
\]

Choose `F_k` increasing and tending to infinity. Choose any increasing dyadic depths

\[
n_k\to\infty.
\]

The signed relative readout is invariant under dyadic refinement, so `n_k` may be selected independently of the scalar boundary convergence. It remains relevant to microscopic feature resolution.

## Admissible physical cutoff

Choose `L_k` recursively so that

\[
\boxed{
L_k
\ge
F_k+C_S,
}
\]

\[
L_k
\ge
L_{k-1}+1,
\]

and

\[
\boxed{
|T_{L_k,n_k,F_k}(u_j,v_j)-W_j|
<2^{-(k+1)}
}
\]

for every `j<=k` whose observers lie in the first `k` source generators.

This is possible because only finitely many pairs are imposed at stage `k` and each has the same large-`L` limit.

## Outer and angular regulators

For the selected finite tuple `(L_k,n_k,F_k)`, iterated trace-class regulator convergence permits choosing finite `R_k,N_k` such that

\[
R_k
\ge
R_{k-1}+1,
\qquad
N_k
\ge
N_{k-1}+1,
\]

and

\[
\boxed{
|T_{L_k,R_k,N_k,n_k,F_k}(u_j,v_j)
-T_{L_k,n_k,F_k}(u_j,v_j)|
<2^{-(k+1)}
}
\]

for all tested pairs `j<=k`.

Again only finitely many inequalities are required at each stage.

## Diagonal convergence

Combining the two error bounds gives

\[
\boxed{
|T_{L_k,R_k,N_k,n_k,F_k}(u_j,v_j)-W_j|
<2^{-k}
}
\]

for every fixed `j` once `k>=j` and the pair is included in the stage.

Therefore

\[
\boxed{
T_{L_k,R_k,N_k,n_k,F_k}(u,v)
\longrightarrow
W_S(u*v^*)
}
\]

for every `u,v in E_count`.

## Cofinality

The sequence

\[
\boxed{
(L_k,R_k,N_k,n_k,F_k)
}
\]

is coordinatewise increasing and every coordinate tends to infinity. It is therefore cofinal in the ordinary product order on finite regulator bounds, subject to the admissibility region

\[
L\ge F+C_S.
\]

More precisely, for every fixed admissible finite tuple, some sequence element dominates it.

## Positive features along the path

At every `k`, the eight-leg feature is an ordinary finite-regulator positive Hilbert feature. Dyadic refinements remain sign-preserving isometries, and conductor restrictions are exact.

Hence the diagonal path consists entirely of admitted positive finite stages while its signed readouts converge simultaneously on the countable core.

Raw positive norms may still diverge; the statement concerns relative signed observations and the stationary Hilbert--Schmidt difference row.

## Difference-row convergence

After common cutoff recentering, the difference row is exactly

\[
D_0M_g
\]

for every `L`. Outer regulator removal converges in Hilbert--Schmidt norm for each fixed observer. The same finite-stage diagonal choice can ensure

\[
\boxed{
\|\widetilde D_{R_k,N_k}(g_j)-D_0M_{g_j}\|_2
<2^{-k}
}
\]

for all `j<=k`.

Thus the diagonal path gives both:

- Hilbert--Schmidt convergence of relative difference legs on the countable core;
- convergence of signed cross readouts to the Weil form.

## Dependence on enumeration

The constructed path depends on:

- the chosen countable core;
- its enumeration;
- the order of requested error tolerances;
- arbitrary choices of sufficiently large regulators.

It is not canonical and does not define a uniform modulus of convergence.

Different diagonal paths have the same scalar limit on the common core but need not yield equivalent raw common-row presentations.

## Extension by continuity

If the limiting Weil/Tate form and the regulated relative forms satisfy one common bound

\[
|T_k(u,v)|
\le
C\|u\|_{\mathcal D}
\|v\|_{\mathcal D}
\]

on a Hilbert graph domain `D` containing `E_count` densely, then convergence extends from the countable core to all of `D` by uniform boundedness and density.

Without such a common bound, diagonal convergence remains a core-level statement only.

## What this does not prove

The diagonal argument does not provide:

1. convergence for every possible joint regulator path;
2. a regulator-independent rate;
3. uniform operator- or trace-norm estimates as `L->infinity`;
4. strong convergence of divergent common rows;
5. canonical compatibility between different countable cores.

It proves existence of at least one simultaneous cofinal realization of the already known iterated limits.

## Categorical interpretation

The relative positive filler defines a pro-object over the full regulator poset. Iterated convergence gives a boundary observation on its tails. The diagonal sequence is a countable cofinal presentation adapted to one observer core.

Thus one may compute or materialize the boundary using finite positive stages without asserting uniform convergence over the entire pro-object.

## Acceptance criterion for a canonical diagonal

A canonical path would require explicit error functions

\[
\epsilon_{outer}(L,R,N,F),
\qquad
\epsilon_{place}(L,F)
\]

with source-derived monotonicity and uniformity. One could then choose the least integer regulators satisfying prescribed bounds.

No such quantitative modulus is currently established.

## Disposition

Iterated convergence on a countable observer core implies existence of a cofinal simultaneous sequence

\[
\boxed{
(L_k,R_k,N_k,n_k,F_k)
\to
(\infty,\infty,\infty,\infty,\infty)
}
\]

such that every finite stage is positive and

\[
\boxed{
T_k(u,v)
\to
W_S(u*v^*)
}
\]

for all core observer pairs. This is a noncanonical diagonal simultaneous limit, strictly weaker than uniform all-path convergence but stronger than a merely formal iterated limit.
