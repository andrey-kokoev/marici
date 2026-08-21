# 1413 — The Chord-Type Compatibility Split Descends to the Cyclic Augmentation Base

## Status

Replicated two-prime modular descent test. Not a characteristic-zero theorem.

> **CORRECTION (Entry 1423).** Representatives (5,11) are absent from the growth-four boundary grade, not compatible solutions. What descends is the support partition and the obstruction on all four supported orbits.

## Question

Corrected Entry 1411 finds a chord-sensitive boundary pattern on five independent labelled radicands. The five-dimensional permutation base contains a redundant diagonal direction.

Does the obstruction disappear on the canonical four-dimensional cyclic base?

## Augmentation model

Impose

\[
s_1+s_2+s_3+s_4+s_5=0
\]

while retaining all five labelled Kummer radicands

\[
y_i^2=s_i.
\]

Use (s_1,\ldots,s_4) as coordinates and set

\[
s_5=-s_1-s_2-s_3-s_4.
\]

Therefore the source derivative is typed as

\[
\frac{d}{ds_i}
=
\partial_{s_i}-\partial_{s_5},
\qquad i=1,\ldots,4.
\]

No occurrence label or Kummer character is discarded.

## Census

At the generic orbit sample (z=7), both \(\mathbf F_{1019}\) and \(\mathbf F_{1009}\) give:

\[
\begin{array}{c|c|c|c}
\text{primitive degree}&\text{unknowns}&\operatorname{rank}A&\dim\ker A\\
\hline
1&641&641&0\\
2&1921&1921&0
\end{array}
\]

At both degrees the unique affine primitive satisfies exactly two of the six exact cyclic occurrence orbits:

\[
\boxed{\text{cyclic representatives }5\text{ and }11.}
\]

These are the diagonal-pair orbit and its complementary three-site orbit. Representatives (1,3,7,15) remain inconsistent.

## Narrow result

The chord-type split found in corrected Entry 1411 is not caused by the diagonal scale direction of the five-dimensional permutation representation.

It survives descent to

\[
V_{\rm cyc}
=
\{(s_1,\ldots,s_5):\sum_i s_i=0\}
\simeq\mathbb Q(\zeta_5)
\]

through quadratic primitive degree in the tested modular model.

Thus the current surviving statement is:

\[
\boxed{
\text{exact cyclic occurrence symmetry}
+
\text{augmentation descent}
\Longrightarrow
\text{compatibility exactly on the diagonal chord orbit and its complement.}
}
\]

## Limits

The calculation does not establish characteristic-zero persistence, cutoff stability, or physical string-boundary typing. The radial grading remains a declared test model.

## Next finite falsifier

Derive the adjacent-versus-diagonal distinction as an explicit labelled obstruction functional rather than increasing the primitive cutoff blindly.

Artifacts:

- `research/benincasa/marici-gm/src/bin/five_site_cyclic_kummer_ibp_pilot.rs`
- `research/benincasa/results/five-site-cyclic-kummer-augmentation-descent.json`

Allocator claim: `seqclaim-ece558a8729c53b46769fcd9`.
