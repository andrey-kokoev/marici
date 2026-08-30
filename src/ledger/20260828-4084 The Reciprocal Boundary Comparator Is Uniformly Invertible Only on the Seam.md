# The Reciprocal Boundary Comparator Is Uniformly Invertible Only on the Seam

## Forced cutoff comparator

The direct and reciprocal Euler boundary currents are

\[
C_s(N)=\frac{N^{1-s}}{1-s},
\qquad
C_{1-s}(N)=\frac{N^s}{s}.
\]

Any scalar comparison taking the reciprocal current to the direct current at
the same cutoff is forced to be

\[
R_s(N)
=
\frac{C_s(N)}{C_{1-s}(N)}
=
\frac{s}{1-s}N^{1-2s}.
\]

Its modulus is

\[
|R_s(N)|
=
\left|\frac{s}{1-s}\right|
N^{1-2\Re s}.
\]

## Uniform-invertibility theorem

Suppose \(0<\Re s<1\). The family \(R_s(N)\), for \(N\geq1\), is
uniformly bounded and has uniformly bounded inverse if and only if

\[
\Re s=\frac12.
\]

Indeed:

- if \(\Re s<1/2\), then \(|R_s(N)|\) diverges;
- if \(\Re s>1/2\), then \(|R_s(N)|\) tends to zero and the inverse
  diverges;
- if \(\Re s=1/2\), then \(|s|=|1-s|\) and
  \[
  |R_s(N)|=1.
  \]

Thus the comparator is a pure phase on the seam and an increasingly singular
change of presentation off it.

## Logarithmic-cutoff geometry

Writing \(N=e^q\) gives

\[
R_s(e^q)
=
\frac{s}{1-s}e^{(1-2s)q}.
\]

The horizontal displacement from the critical line is exactly the real
Lyapunov exponent of the reciprocal boundary comparison:

\[
\lim_{q\to\infty}
\frac1q\log|R_s(e^q)|
=
1-2\Re s.
\]

The critical line is therefore the neutral-growth locus of the zero-germ
comparator.

## Conditional zero-confinement theorem

Assume a completed zero event has direct and reciprocal Euler germs, and the
source identifies those germs at common cutoff through a comparison that is
uniformly invertible in the completed boundary topology. Then the zero lies on
the critical line.

The proof is now one line: the source comparison must equal the forced
comparator on the nonzero leading boundary class, and uniform invertibility
forces \(\Re s=1/2\).

## Remaining source theorem

The unresolved step is not positivity. It is:

> Every source-admissible completed zero supplies a uniformly invertible,
> cutoff-compatible identification of its two reciprocal boundary germs.

The scalar functional equation identifies finite parts but does not by itself
control this comparison at divergent order. A hypothetical off-line quartet
passes scalar symmetry precisely by permitting the boundary comparator to
become singular in one direction.

## Falsifiers

The proposed source theorem fails if any of the following occurs:

- reciprocal sewing compares different cutoff scales rather than a common
  source cutoff;
- its transition is allowed to shift filtration degree;
- the leading Euler boundary class is killed in the completed quotient;
- a source-admissible zero has a comparison whose condition number diverges.

These are structural tests independent of zero locations.

## Explanatory status

This realizes the two-sector intuition as a measurable geometric fact. The
two sectors are not merely reflected pictures. Their zero-boundary frames are
related by a scale flow. On the seam that flow is a rotation; off the seam it
is a contraction in one direction and expansion in the other.

RH would follow if theta/Tate completion permits one zero event to retain both
meanings only under a reversible boundary-frame comparison.

