# Detector null-exposure quotient theorem

Work package: WP574  
Owner: marici.Figueiredo

## Sector-independent statement

This packet freezes the detector theorem requested by Nima independently of
HHH. It composes WP569--WP571 in one finite experiment and identifies the same
lost source direction under two ordinary readout quotients.

Let a completed detector record have selected outcomes \(S\) and a null or
failed-selection outcome \(N\). Let \(q_S\) be the selected baseline vector and
\(Q=\mathbf 1^Tq_S\). Suppose a source direction \(v\) has completed detector
tangent

\[
d_{v,S}=\alpha q_S,
\qquad
d_{v,N}=-\alpha Q.
\]

The direction changes the selected rate uniformly and compensates it in the
null record, preserving total probability.

Two consequences follow exactly.

First, conditioning on selection gives

\[
{d_{v,i}Q-q_i\mathbf 1^Td_{v,S}\over Q^2}=0.
\]

Thus the selected-shape quotient erases \(v\).

Second, in a selected-count experiment the same response is proportional to
the exposure nuisance direction \(q_S\). If exposure is freely profiled, \(v\)
is erased again. A typed null outcome or an independently calibrated exposure
port can retain it, but they define different completed experiments.

## Exact finite witness

Take the normalized three-outcome baseline

\[
q=(1/3,1/3,1/3)^T
\]

and the two-direction response

\[
D=
\begin{pmatrix}
1&0\\
-1&1\\
0&-1
\end{pmatrix}.
\]

The columns conserve probability. In the multinomial metric \(W=3I_3\), the
full Gram is

\[
G_{\mathrm{full}}=
\begin{pmatrix}6&-3\\-3&6\end{pmatrix},
\]

with eigenvalues \(3,9\). The complete record therefore has rank two.

For

\[
v=(1,2)^T,
\]

the detector tangent is

\[
Dv=(1,1,-2)^T.
\]

This is the general form above with \(q_S=(1/3,1/3)^T\), \(Q=2/3\), and
\(\alpha=3\).

## Quotient one: delete null and normalize shape

Delete the third outcome and condition on selection. The exact conditional
response is

\[
D_{\mathrm{shape}}=
\begin{pmatrix}
3/2&-3/4\\
-3/2&3/4
\end{pmatrix}.
\]

It has rank one and

\[
D_{\mathrm{shape}}v=0.
\]

The first nonfaithful arrow is conditional normalization after null deletion.
No covariance applied downstream can reconstruct \(v\).

## Quotient two: retain selected counts but profile exposure

Instead retain the two absolute selected counts. Their response is

\[
D_{\mathrm{count}}=
\begin{pmatrix}1&0\\-1&1\end{pmatrix},
\]

which has rank two. At the baseline, a fractional exposure nuisance has count
direction \(n=(1/3,1/3)^T\), and

\[
D_{\mathrm{count}}v=3n.
\]

Let \(\pi\ge0\) be independent exposure-calibration precision. Profiling the
exposure nuisance gives

\[
G_{\mathrm{profiled}}(\pi)
=
\begin{pmatrix}6&-3\\-3&3\end{pmatrix}
-{1\over2/3+\pi}
\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]

Its determinant is

\[
\det G_{\mathrm{profiled}}(\pi)
={27\pi\over2+3\pi}.
\]

At \(\pi=0\), the Gram has rank one and kernel spanned by \(v\). For every
\(\pi>0\), formal rank two is restored. Robust authority still requires the
smallest eigenvalue to survive the uncertainty bounds of WP568--WP569.

## Exact quotient diagram

The finite experiment has two distinct lossy arrows. The completed
selected-plus-null record maps to selected conditional shape, where (v) is
erased. It also maps to selected counts with free exposure, where (v) is
profiled out.

In ordinary prose: null deletion erases the selected-rate-versus-null contrast;
free exposure profiling erases the same contrast by identifying its selected
part with normalization drift.

The repairs are not interchangeable presentations of one absolute observable:

- retaining the null record preserves a completed probability experiment;
- calibrating exposure creates a relational count experiment over the
  stabilizer groupoid.

Aspect packet 39 supplies a physical photon-counting realization of the second
repair with a tapped monitor port. That realization validates the detector
theorem, not the flavor portal application.

## Classification and hostile tests

The completed detector family is a rank-two separator. Both quotients are
nonfaithful readouts, not selectors or rigidifiers. The smallest hostile is the
single source vector \(v=(1,2)^T\): it is visible in the completed record,
invisible in selected shape, visible in raw counts, and invisible again after
free exposure profiling.

The theorem is sector-independent. For flavor, the entrance must still be a
source-derived physical16 response and the detector must still be the
publication-bound portal instrument. Until that join exists, the application
is prospective. Full weak-basis descent passes for an invariant entrance; the
exposure repair explicitly declares its new relational groupoid.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp574_detector_null_exposure_quotient_theorem.py

The generated result is
`research/flavor/results/wp574_detector_null_exposure_quotient_theorem.json`.
