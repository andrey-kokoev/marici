# The two-bit parity is the D4 discriminant group of the conductor singularity

At any of the four marked conductor points, the cubic leading term of the total-space equation is, up to a nonzero factor,

\[
XY=E\bigl(2uv+E(u+v)+2E^2\bigr).
\]

Introduce

\[
n=u+v,
\qquad s=u-v,
\qquad n'=n+E.
\]

Then

\[
2uv+E(u+v)+2E^2
=\frac12\bigl((n')^2-s^2+3E^2\bigr).
\]

The displayed quadratic is nondegenerate. Hence the total-space singularity has compound-\(D_4\) form

\[
XY=E\,q_2(n',s,E),
\]

with \(q_2\) nondegenerate. Higher terms do not alter this local ADE type under the usual finite-determinacy hypothesis.

The \(D_4\) Cartan lattice has Smith form

\[
\operatorname{diag}(1,1,2,2).
\]

Therefore its discriminant group is

\[
D_4^\vee/D_4\cong(\mathbb Z/2)^2.
\]

This identifies the two-bit group intrinsically. It is the discriminant group of the conductor's \(D_4\) resolution lattice—not an arbitrary pair of coefficients added to the calculation.

The three nonzero elements are the familiar vector and two spinor classes of \(D_4\). Triality permutes them. Geometrically, these are exactly the three perfect matchings of the four marked conductor points found from the bitangent-component saturation calculation.

Thus several previously separate facts are one structure:

- four marked smoothing points;
- three pairings of four points;
- an index-four primitive saturation;
- the Klein four parity group;
- an automorphism action factoring through \(S_3\);
- three nonzero classes permuted by triality.

The parity value should now be obtained by resolving the physical point \(p_{++}\) and following its oriented thimble to one outer node of the \(D_4\) exceptional configuration. That outer-node incidence determines whether the resulting discriminant class is vector, spinor, or conjugate spinor.

Certificate:

- `research/voevodsky/checkers/identify_conductor_singularity_as_cD4.py`;
- `research/voevodsky/results/conductor_cD4.json`.
