# 1373 — A Source-Labelled Modular Dual Detects the Ternary Infinity Class

## Status

Explicit verified modular certificate at one maximal-rank fiber. Characteristic-zero reconstruction and face-vanishing normalization remain open.

## Frozen system

Use the cubic full-Kummer primitive system of Entry 1364 at

\[
(p,z)=(1019,13)
\]

and impose the growth-four boundary conditions on the representative occurrence triple

\[
(\mathcal O_1,\mathcal O_2,\mathcal O_3).
\]

The affine system has

\[
1921
\]

unknowns,

\[
\operatorname{rank}A=1152,
\qquad
\dim\ker A=769.
\]

The triple boundary map has rank

\[
769
\]

on the affine kernel, while the inhomogeneous boundary-zero system is inconsistent.

## Explicit dual certificate

A labelled elimination trace produces a finite-field row functional \(\lambda\) satisfying

\[
\boxed{
\lambda A_{m triple}=0,
\qquad
\lambda r_{m triple}=1.
}
\]

The checker reconstructs the contradictory reduced row in the original labelled row basis and verifies both identities against all \(1921\) coefficient columns.

The normalized certificate has

\[
1917
\]

nonzero terms:

\[
1150
\]

affine-sample terms and

\[
767
\]

boundary terms.

Its boundary support by occurrence weight is

\[
\begin{array}{c|ccc}
\text{weight}&1&2&3\\
\hline
\text{terms}&328&234&205.
\end{array}
\]

Its boundary support by radial level is

\[
\begin{array}{c|rrrrrrr}
\text{level}&0&1&2&3&4&5&6\\
\hline
\text{terms}&67&131&162&163&164&68&12.
\end{array}
\]

Thus the first explicit obstruction functional genuinely uses all three labelled occurrence orbits.

## What this proves

At the declared modular fiber, the triple inconsistency is not merely a rank comparison. It has an explicit source-labelled dual witness.

This strengthens Entry 1364 from

\[
\text{rank inconsistency}
\]

to

\[
\text{verified modular functional detecting the inhomogeneous class}.
\]

## What this does not prove

The emitted functional is dense and elimination-section dependent. It has not yet been normalized so that its restrictions to every one- and two-orbit face vanish separately.

It is also defined over \(\mathbb F_{1019}\), not over the characteristic-zero source field.

Therefore it does not yet establish:

- a canonical Čech \(2\)-cocycle;
- an integral or rational obstruction class;
- cross-characteristic persistence;
- a physical string-sector period class.

## Next finite falsifier

Use the explicit dual as discovery data, but reconstruct only the quotient class modulo duals induced from one- and two-orbit faces.

The acceptance conditions are:

1. the quotient dual is nonzero;
2. it admits a characteristic-zero representative;
3. its restrictions to all proper faces vanish;
4. deck complement and \(C_5\) transport preserve the class;
5. exact source identities verify the representative without modular fitting.

Failure at step 1 would show that the current dense witness detects inconsistency but not an intrinsic ternary Čech class.

## Artifacts

- `research/benincasa/results/five-site-asymmetric-ternary-dual-certificate.json`
- `research/benincasa/results/five-site-asymmetric-kummer-resolved-ibp-pilot.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`

Allocator claim: `seqclaim-b33baf4e7853aca3f3ace3a3`.
