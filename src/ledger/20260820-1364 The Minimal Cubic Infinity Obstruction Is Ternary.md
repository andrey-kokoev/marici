# 1364 — The Minimal Cubic Infinity Obstruction Is Ternary

## Status

Supported modular refinement of Entry 1356, replicated at two maximal-rank fibers. Characteristic-zero certification remains open.

Entry 1356 correctly showed that both deck-complement sectors are separately trivializable while their union is not. The present audit determines the minimal occurrence support and shows that the pair decomposition is not fundamental.

## Four cyclic occurrence orbits

Write the twenty growth-four sheets as four labelled \(C_5\)-orbits

\[
\mathcal O_1,\mathcal O_2,\mathcal O_3,\mathcal O_4
\]

of Hamming weights \(1,2,3,4\).

The cubic affine kernel has dimension

\[
\dim K=769.
\]

Each individual orbit is boundary-trivializable and has boundary rank

\[
r_i=360.
\]

## Every pair is trivializable

There are two rank types.

Deck-complement pairs:

\[
(\mathcal O_1,\mathcal O_4),
\qquad
(\mathcal O_2,\mathcal O_3)
\]

have

\[
r_{\rm comp}=550,
\qquad
\dim T_{\rm comp}=769-550=219.
\]

Cross pairs, represented by

\[
(\mathcal O_1,\mathcal O_2),
\qquad
(\mathcal O_1,\mathcal O_3),
\]

have

\[
r_{\rm cross}=617,
\qquad
\dim T_{\rm cross}=769-617=152.
\]

All six labelled pairs are therefore separately trivializable.

## Every triple is obstructed

Up to deck complement there are two triple types:

\[
(\mathcal O_2,\mathcal O_3,\mathcal O_4)
\]

and

\[
(\mathcal O_1,\mathcal O_3,\mathcal O_4).
\]

Both have

\[
r_{\rm triple}=769
\]

and inconsistent inhomogeneous boundary-zero systems.

By complement symmetry, every three-orbit subset is obstructed.

## Independent-base replication

At the second maximal-rank fiber

\[
(p,z)=(1019,13),
\]

the affine rank and kernel dimension remain

\[
1152,
\qquad
769.
\]

The two pair types reproduce ranks

\[
550,
\qquad
617,
\]

and remain consistent. The two complement-inequivalent triple types both reproduce boundary rank

\[
769
\]

and remain inconsistent. The minimality pattern is therefore not specific to the original base value \(z=7\), although both replications remain in characteristic \(1019\).

Hence the exact minimality pattern is

\[
\boxed{
\begin{array}{c|c}
\text{number of cyclic orbits imposed}&\text{boundary trivialization}\\
\hline
1&\text{exists}\\
2&\text{exists}\\
3&\text{does not exist}\\
4&\text{does not exist}.
\end{array}
}
\]

## Interpretation

The first nonzero compatibility datum is ternary.

It is not:

- a class on one infinity sheet;
- a class on one cyclic occurrence orbit;
- a pairwise mismatch between two sectors.

It first appears on a three-orbit overlap. In Čech language, the candidate has the type of a 2-simplex coherence obstruction:

\[
\boxed{
\delta\tau_{ijk}\ne0
}
\]

despite the existence of all one-orbit and two-orbit trivializations.

This refines, rather than negates, Entry 1356: the two complement-pair torsors indeed fail to glue, but every other pair also glues locally. Triple compatibility is the minimal failure.

## Architectural consequence

The five-site modular candidate now exhibits precisely the distinction

\[
\text{pairwise compatibility}
\not\Rightarrow
\text{global compatibility}.
\]

This is native Carrier behavior. The existing occurrence nerve detects a higher coherence class without adding a new cell after seeing the target.

The candidate therefore supports

\[
\text{shared occurrence/Čech carrier calculus}
+
\text{string-sector Kummer coefficient object}.
\]

## Exact-certification target

Choose one representative triple, for example

\[
(\mathcal O_1,\mathcal O_2,\mathcal O_3).
\]

Construct a characteristic-zero dual functional supported only on its fifteen sheets such that:

1. it annihilates the cubic affine-gauge image;
2. its restrictions to every one- and two-orbit face vanish;
3. it evaluates nontrivially on the triple inhomogeneous class;
4. it is transported to the other triples by deck complement and cyclic occurrence symmetry.

This is now the smallest possible exact certificate.

## Artifact

- `research/benincasa/results/five-site-asymmetric-cubic-boundary-localization.json`

Allocator claim: `seqclaim-f29828478efe906434ad0dc6`.
