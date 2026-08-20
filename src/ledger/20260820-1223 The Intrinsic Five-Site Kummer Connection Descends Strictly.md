# Entry 1223 — The Intrinsic Five-Site Kummer Connection Descends Strictly

## Frozen physical coefficient cover

On the physical $d=3$ five-edge locus, Entry 1217 gives the labelled Kummer cover

\[
\det(H)y_i^2=F_i,
\qquad i=1,\ldots,5.
\]

Its finite pushforward has the rank-32 character basis

\[
y_S=\prod_{i\in S}y_i,
\qquad S\subseteq\{1,\ldots,5\}.
\]

No master-basis reduction is chosen.

## Intrinsic logarithmic connection

Define

\[
\alpha_i
=
\frac12d\log\!\left(\frac{F_i}{\det H}\right).
\]

Differentiating the cover equation forces

\[
\nabla y_S
=
\left(\sum_{i\in S}\alpha_i\right)y_S.
\]

The deck generator $T_j$ acts in the same basis by

\[
T_j(y_S)=(-1)^{[j\in S]}y_S.
\]

Both operators are diagonal. Consequently

\[
\boxed{
[\nabla,T_j]=0
}
\]

for every character and generator. Since the $\alpha_i$ are closed scalar logarithmic forms, the intrinsic connection is flat.

## Moving marked equations

Every one of the 26 source-labelled physical marked equations is affine-linear in the $y_i$. The derivation rule

\[
d y_i=\alpha_i y_i
\]

and the sheet rule $y_i\mapsto-y_i$ give the same sign to a term and its derivative. Therefore the marked equations and their logarithmic differentials are strictly covariant between chambers.

The exhaustive checker verifies:

\[
160
\]

character–generator connection commutators,

\[
320
\]

abelian curvature checks, and

\[
4160
\]

marked-equation derivative transports. Every check passes.

Hence

\[
\boxed{
\text{the intrinsic rank-32 Kummer }D\text{-module descends strictly under }(\mathbb Z_2)^5.
}
\]

There is no projective connection cocycle and no new carrier datum.

## Scope and correction of the frontier

Entries 1221–1222 left “Gauss–Manin horizontality” open. The intrinsic unreduced Kummer connection is now horizontal under deck transport. What remains open is narrower:

- a source-normalized finite master reduction and its gauge comparison;
- possible additional coefficient geometry beyond the Kummer cover;
- descent and pairing of the physical Bunch–Davies relative cycle.

A failure in a chosen finite connection matrix is not intrinsic unless it survives gauge and contradicts the unreduced equivariance proved here.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_kummer_connection_descent.rs`
- `research/benincasa/results/five-site-kummer-connection-descent.json`

## Next falsifier

Construct the physical chamber-relative cycle package on the rank-32 cover and test its deck trace and boundary covariance. If the source cycle descends, the five-site sheet multiplicity is fully coefficient-theoretic at the frozen level. If it does not, record the obstruction as physical-cycle data rather than modifying the carrier or Čech differential.
