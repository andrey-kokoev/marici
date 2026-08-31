# Cross-shell label-dilation collisions create an explicit unlabelled radial kernel

## Question

Does fixed-shell ordered-pair faithfulness extend to a codiagonalized family of several shells by ordering shell endpoints and theta labels lexicographically?

## Claim boundary

Not without a noncollision hypothesis. Shell position and theta label enter through the products \(ne^a\) and \(me^a\), not as independent lexicographic scales. Two equal-width shells with matching product coordinates produce proportional ordered-pair histories and therefore an explicit signed kernel after shell labels are erased.

## Exact translated coordinates

The completed atoms satisfy

\[
\Phi_n(u)=n^{-1/2}\Phi_1(u+\log n).
\]

Hence

\[
\rho_{nm}^{[a,b]}(t)
=(nm)^{-1/2}
K_{[a+\log n,\,b+\log n]}
\left(t+\log\frac mn\right).
\]

The unlabelled history therefore sees the tuple

\[
\left(
A=a+\log n,
H=b-a,
D=\log\frac mn
\right)
\]

together with the half-density amplitude \((nm)^{-1/2}\). It does not separately see \(a,n,m\).

## Collision criterion

Consider two shell-label tuples

\[
(a,b;n,m),
\qquad
(a',b';n',m').
\]

If

\[
b-a=b'-a',
\qquad
ne^a=n'e^{a'},
\qquad
me^a=m'e^{a'},
\]

then their translated intervals and ratio shifts agree. Equivalently,

\[
a+\log n=a'+\log n',
\qquad
\frac mn=rac{m'}{n'}.
\]

The exact histories obey

\[
(nm)^{1/2}\rho_{nm}^{[a,b]}(t)
=
(n'm')^{1/2}\rho_{n'm'}^{[a',b']}(t)
\]

for every separation \(t\).

Therefore the nonzero signed packet with coefficients

\[
c_{a,b;n,m}=(nm)^{1/2},
\qquad
c_{a',b';n',m'}=-(n'm')^{1/2}
\]

lies in the unlabelled radial-history kernel.

## Why endpoint-first ordering fails

The positive-separation decay scale is

\[
\exp\left[-\pi m^2e^{2a}e^{2t}\right],
\]

so it is ordered by \(me^a\), not first by \(a\) and then by \(m\). A later shell with a smaller label can share the same scale as an earlier shell with a larger label. At exact product-coordinate collision, all endpoint asymptotic coefficients agree after the forced half-density rescaling; no higher asymptotic jet separates the tuples.

Thus the proposed lexicographic cross-shell extension of the fixed-shell proof is invalid.

## Arithmetic relevance

For logarithmic arithmetic endpoints, product collisions are not exceptional in principle. If \(e^a\) and \(e^{a'}\) are integer prime-power scales, labels can absorb their ratio. For example, the equations

\[
ne^a=n'e^{a'},
\qquad
me^a=m'e^{a'}
\]

have integer-label solutions whenever the endpoint-scale ratio is rational and both labels are enlarged by the required numerator and denominator. Exact kernel membership additionally requires matching shell widths.

The actual shell catalogue must therefore be audited for the full triple \((A,H,D)\), not only for distinct lower endpoints.

## Corrected source statement

The earlier results remain valid in their stated scopes:

- distinct shells are separated for the scalar completed forcing when no independent internal labels are varied;
- ordered pairs are faithful inside one fixed shell;
- diagonal labels are faithful inside one fixed shell.

They do not imply faithfulness after simultaneous shell-label codiagonalization.

Cross-shell ordered-pair faithfulness holds only after one of the following is supplied:

1. retained shell labels;
2. injectivity of the map \((a,b;n,m)\mapsto(A,H,D)\) on the admitted source;
3. an additional observer separating collided translation orbits.

## G4 consequence

A common-history G4 architecture can acquire a genuine source kernel before any Green metric is applied. This kernel is not the minimal endpoint–Wronskian balance; it is a label-dilation orbit collision caused by erasing shell provenance. G4 must state whether its carrier retains shell labels or quotients these collisions.

## Direction rescore

- Universal cross-shell ordered-pair faithfulness: disproved.
- Audit of the actual arithmetic shell catalogue for \((A,H,D)\) collisions: 9/10.
- Retained-label architecture: already avoids this kernel.
- Common-history G4 quotient: interface-blocked until shell provenance is exposed.

## Disposition

The depth-first cross-shell extension fails and yields an explicit hostile kernel instead. The next productive step is a source-specific collision census for the actual shell endpoints and widths. No RH conclusion is authorized.
