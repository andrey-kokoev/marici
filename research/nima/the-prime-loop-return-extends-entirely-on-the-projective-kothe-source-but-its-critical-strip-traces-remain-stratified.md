# The prime-loop return extends entirely on the projective Köthe source, but its critical-strip traces remain stratified

## Source topology

Let

\[
\mathcal A_{\exp}
=
\bigcap_{\delta>0}\ell^1(\mathbb P,p^\delta)
\]

with seminorms

\[
q_\delta(c)=\sum_p|c_p|p^\delta.
\]

This is the prime-coordinate slice of the projective exponential labelled
source. Finite prime packets are dense, and cutoff projections converge in
every seminorm.

## Entire diagonal return family

For \(s\in\mathbb C\), define

\[
L(s)c=(p^{-s}c_p)_p.
\]

For every \(\delta>0\),

\[
q_\delta(L(s)c)
=
\sum_p|c_p|p^{\delta-\operatorname{Re}s}.
\]

Choose any

\[
\delta'>
\max\{\delta-\operatorname{Re}s,0\}.
\]

Then

\[
q_\delta(L(s)c)\le q_{\delta'}(c).
\]

On compact \(s\)-sets, one \(\delta'\) works uniformly. Hence \(L(s)\) is a
continuous operator on \(\mathcal A_{\exp}\) for every \(s\), and
\(s\mapsto L(s)\) is an entire family in the topology of uniform convergence
on bounded sets.

Its powers are exact:

\[
L(s)^k=L(ks).
\]

Prime cutoffs commute with the family:

\[
P_XL(s)=L(s)P_X.
\]

Thus the ordered prime-loop return itself has a critical-strip source lift.
What fails there is ordinary Hilbert trace class, not operator continuity on
the source test space.

## Dual current hierarchy

For each \(k\ge1\), define the coefficient functional

\[
J_k(s;c)
=
\sum_p c_p p^{-ks}.
\]

For \(c\in\mathcal A_{\exp}\), this is continuous for every \(s\), again by a
seminorm shift. Therefore every power \(L(s)^k\) has a well-defined
distributional diagonal current on the test source.

The scalar specialization \(c_p=1\) is not a test vector. Its admissibility
depends on \(k\) and \(s\):

- \(k=1\): the primitive scalar sum diverges near the critical line and exists
  only as a distributional boundary current;
- \(k=2\): the square scalar sum is absolutely convergent for
  \(\operatorname{Re}s>1/2\) and has a Hilbert boundary interpretation at the
  seam;
- \(k\ge3\): the connected scalar sums converge absolutely whenever
  \(k\operatorname{Re}s>1\), in particular in a neighborhood of the critical
  line for every \(k\ge3\).

This is exactly the primitive--square--connected completion filtration.

## Relative determinant germ

On the half-neighborhood

\[
\operatorname{Re}s>\frac13,
\]

the connected logarithm

\[
\mathcal C_3(s)
=
\sum_{k\ge3}\frac1k\sum_p p^{-ks}
\]

converges normally on compact subsets bounded away from \(1/3\). It defines the
connected determinant-three germ

\[
\Delta_{\ge3}(s)=\exp\mathcal C_3(s).
\]

The missing first two terms are not absent. They live in their separately
typed anomaly lines:

\[
J_1(s),\qquad \frac12J_2(s).
\]

Thus the source-level lift has the form

\[
\bigl(L(s),J_1(s),J_2(s),\Delta_{\ge3}(s)\bigr),
\]

rather than one ordinary Fredholm determinant on prime Hilbert space.

## Reciprocal completion

The right-side germ \(\operatorname{Re}s>1/3\) does not by itself cover the
whole critical strip. Reciprocal sewing supplies the corresponding germ in
the reflected chart. The overlap comparison must include:

- the primitive distributional line;
- the square Hilbert line;
- the connected determinant-three line;
- the two endpoint ports;
- the archimedean gamma line.

A scalar analytic continuation obtained after forgetting these lines does not
construct the overlap isomorphism.

## Kernel qualification

Because \(L(s)\) is diagonal and \(p^{-s}\ne1\) in the nontrivial-zero region,

\[
\ker(I-L(s))=\{0\}
\]

on the test source. Zeta zeros therefore cannot be kernels of this open-loop
prime return.

They can only appear as defects of the closed reciprocal boundary
totalization. The eventual pencil must be a boundary feedback or mapping-cone
operator assembled from \(L(s)\), not \(I-L(s)\) alone.

This sharply separates:

- source operator existence, now closed;
- relative determinant-line totalization, still open;
- closed-loop kernel identification, still open.

## Completion theorem obtained

The prime-loop return admits an entire, cutoff-natural lift on the projective
exponential source. Its powers generate continuous distributional currents,
and their scalar shadows fall into the exact three regularity strata.

No analytic continuation of an operator was needed. The test topology carries
the entire family directly.

## Remaining gate

The next constructor is the closed-loop boundary cone

\[
\mathcal D_{\mathrm{cl}}(s)
=
\operatorname{Cone}
\left(
\text{prime-loop return}
\longrightarrow
\text{reciprocal, seam, and archimedean boundary}
\right).
\]

One must prove that:

1. its relative determinant section is completed \(\Xi(s)\);
2. its domain imposes the maximal isotropic Green boundary relation;
3. determinant zero produces a kernel state;
4. its kernel comparison with the positive Green pencil is source-derived.

## Hostiles

1. Declare that failure of Hilbert trace class means \(L(s)\) does not exist.
2. Evaluate the distributional primitive current on the non-test vector
   \((1,1,\ldots)\) without boundary totalization.
3. Combine the three strata into one scalar series before reciprocal sewing.
4. Identify zeta zeros with primewise eigenvalue one.
5. Call scalar continuation of the Euler determinant an operator determinant.

## Verdict

The critical-strip lift of the ordered prime-loop return exists canonically on
the projective Köthe source and is entire. Its traces do not collapse to one
ordinary determinant; they remain distributional, Hilbert, and
determinant-three boundary data.

The earliest missing operator is now the reciprocal closed-loop boundary cone,
not the open-loop prime return.
