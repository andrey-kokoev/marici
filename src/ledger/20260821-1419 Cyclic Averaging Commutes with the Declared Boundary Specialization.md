# 1419 — Cyclic Averaging Commutes with the Declared Boundary Specialization

## Status

Exact labelled denominator/incidence naturality test.

## Comparison square

Let (T) denote the source cyclic permutation and let

\[
\operatorname{Sp}_{\infty}
\]

denote the radial growth specialization used in Entries 1411–1418.

The required comparison is

\[
\begin{array}{ccc}
\mathcal C&\xrightarrow{T}&\mathcal C\\
\big\downarrow{\scriptstyle\operatorname{Sp}_{\infty}}
&&\big\downarrow{\scriptstyle\operatorname{Sp}_{\infty}}\\
\operatorname{gr}_{\infty}\mathcal C
&\xrightarrow{T}&
\operatorname{gr}_{\infty}\mathcal C
\end{array}
\]

## Frozen audit

Rotate simultaneously:

- all (26) source-labelled denominators;
- all (32) resolved Kummer sheets;
- all (180) OFPT terms;
- their ordered orientation-normalized weights.

For every denominator (q) and sheet (S), the checker verifies

\[
\operatorname{growth}(q,S)
=
\operatorname{growth}(Tq,TS).
\]

The finite census is

\[
26\times32=832
\]

label–sheet checks, with zero failures. Every rotated OFPT term remains in the source term set, and all orientation-normalized weights are (+1).

Hence

\[
\boxed{
T\operatorname{Sp}_{\infty}
=
\operatorname{Sp}_{\infty}T
}
\]

on the frozen labelled denominator carrier.

## Averaging

Because the comparison is strict, the invariant projector of Entry 1418 also commutes:

\[
\boxed{
P_{\rm inv}\operatorname{Sp}_{\infty}
=
\operatorname{Sp}_{\infty}P_{\rm inv}.
}
\]

Thus Entry 1418’s surviving invariant line is not produced by averaging after specialization. It is the specialization of the source-defined cyclic average.

## Type boundary

This establishes naturality for the declared combinatorial radial grade. It does not yet identify that grade with the physical compactification residue, integration-cycle boundary, or full de Rham specialization.

## Next finite falsifier

Lift the same square from denominator growth to the source differential form: include Jacobian/orientation degree and compute the actual logarithmic residue. A failure there would leave the Carrier naturality intact while rejecting the proposed coefficient map.

Artifacts:

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_boundary_naturality.rs`
- `research/benincasa/results/five-site-cyclic-boundary-naturality.json`

Allocator claim: `seqclaim-f682b6415714c2345d864b59`.
