# The finite native equalizer forms a cutoff-natural coherence cube

Scope correction: the finite checker uses a real normal coordinate.  The full
spectral-plane version replaces the reciprocal parameter by
\(1-\overline{s}\); using \(1-s\) would not vanish along the critical line.

## Nested labelled packets

Let \(X\subset Y\) be finite labelled cutoffs.  Each label \(j\) carries a
distinct rate \(\lambda_j\), a nonzero incidence \(b_j\), a tail amplitude
\(A_j\), and a reservoir amplitude \(c_j\).  The two sector equations on that
mode are

\[
(z-\lambda_j)A_j+b_jc_j=0
\]

and

\[
(1-z-\lambda_j)A_j+b_jc_j=0.
\]

Cutoff inclusion pads every new labelled coordinate by zero and preserves the
old rates and incidences.

## Exact finite naturality

Because the sector constraint matrices are block diagonal by label, padding by
zero commutes with both sector operators.  The common-frame equalizer also
commutes with cutoff inclusion.

For each label, the stacked equalizer block is

\[
\begin{pmatrix}
z-\lambda_j&b_j\\
1-z-\lambda_j&b_j
\end{pmatrix}.
\]

Its determinant is

\[
b_j(2z-1).
\]

Thus every finite equalizer is trivial off the seam and has one-dimensional
labelwise solution space on the seam.

The reservoir boundary jet is natural as well.  If \(J_X\) uses the first
\(|X|\) endpoint derivatives and \(J_Y\) uses the first \(|Y|\), then

\[
\pi_{Y,X}J_Y\iota_{X,Y}=J_X,
\]

where \(\iota_{X,Y}\) pads coefficients by zero and \(\pi_{Y,X}\) truncates
the longer jet.

Hence the following finite data commute simultaneously:

- labelled cutoff inclusion;
- direct-sector dynamics;
- reciprocal-sector dynamics;
- common-frame equalizer formation;
- endpoint-jet observation.

## What remains unproved

Finite naturality does not itself produce a completed equalizer.  Limits need
not preserve kernels, closed range, exactness, or uniform inverse bounds.  The
finite cube therefore moves the obstruction to four precise completion gates:

1. the labelled coefficient topology must make both sector systems continuous;
2. the growing jet carrier must have a source-derived limit topology;
3. the equalizer must commute with restricted-product completion;
4. the off-seam inverse margin must remain uniform on compact subsets.

Failure of any gate permits a nonzero state to appear at infinity even though
every finite equalizer is trivial.

## DPC verdict

Under stable labelled incidence, all expected finite paths commute.  The live
coherencer is no longer a missing finite square.  It is a completion cell
comparing

\[
\varinjlim_X\operatorname{Eq}(D_{+,X},D_{-,X})
\]

with

\[
\operatorname{Eq}
\left(
\varinjlim_XD_{+,X},
\varinjlim_XD_{-,X}
\right).
\]

The first object is zero off the seam.  RH-strength content requires proving
that the comparison into the second object is an isomorphism after the actual
theta/Tate completion.

The finite falsifier for naturality is any cutoff extension that changes an old
incidence coefficient or mixes an old label with a newly added one.  The
completion falsifier is a normalized sequence of cutoff states whose sector
residuals and boundary observations converge to zero off the seam.

## Verification

`check_rh_finite_equalizer_coherence_cube.py` verifies direct and reciprocal
cutoff naturality, full off-seam equalizer rank, seam rank drop, and jet
truncation naturality for nested packets of sizes one through four.  It also
checks an incidence-drift hostile that breaks the square.
