# 1788 — The Surviving Five-Site Pinch Lies in the Open Cayley–Menger Domain

## Question

Entry 1787 leaves one (g_5) representative crossing with positive internal
energies and same-sign Landau multipliers. Does either source-labelled root
assignment lie in the full positive Cayley–Menger domain?

## Quadratic assignment field

At the certified root, write

\[
s=y_i+y_j=\sqrt{x},
\qquad
p=y_i y_j,
\qquad
z=\sqrt{x(x-4p)}.
\]

The two labelled assignments have squared radii

\[
y_i^2=\frac{x-2p\mp z}{2},
\qquad
y_j^2=\frac{x-2p\pm z}{2}.
\]

Every principal minor of the displacement Gram matrix is therefore of the
form

\[
D_0(x)+D_1(x)z,
\qquad
D_i\in\mathbb Q(\sqrt5)(x).
\]

## Exact sign certificate

For each minor, certify nonvanishing at the isolated Landau root through its
quadratic norm

\[
\boxed{
D_0^2-D_1^2x(x-4p).
}
\]

The norm numerator and denominator have no zero in the exact Sturm interval.
The sign of the chosen real embedding is then fixed by one interval endpoint;
the displayed decimal coordinates are not used as proof.

In the ordered list

\[
(y_i^2,y_j^2,y_e^2,
M_{ij},M_{ie},M_{je},\det G),
\]

the two assignment sign vectors are

\[
\boxed{(+,+,+,+,+,+,+)}
\]

and

\[
\boxed{(+,+,+,+,+,-,-)}.
\]

Thus exactly one source-labelled assignment lies in the open
Cayley–Menger/Gram domain. Numerically it is the ordering

\[
y_i\approx0.4234810679,
\qquad
y_j\approx1.0087856807,
\qquad
y_e\approx3.5806668715.
\]

## Result

\[
\boxed{
\text{The surviving }g_5\text{ branch is a genuine interior real Landau
pinch candidate, with a unique labelled root assignment.}
}
\]

Its free (C_5)-orbit gives five labelled interior candidates. The swapped
assignment is excluded by the source domain and does not double the count.

## Remaining falsifier

Interior location, nonzero Hessian, and same-sign multipliers establish the
geometric pinch conditions. A singularity of the complete source period still
requires a nonzero coefficient after summing the double residues of all frozen
180 OFPT terms containing this labelled pair.

Compute that source residue before asserting a physical discontinuity. A zero
sum would be a numerator/canonical-function cancellation, not a carrier
failure.

## Evidence

- `research/benincasa/checkers/five_site_g5_cm_domain.py`
- `research/benincasa/results/five-site-g5-cm-domain.json`
- allocator claim: `seqclaim-3a37b97235598324e9e1f891`
