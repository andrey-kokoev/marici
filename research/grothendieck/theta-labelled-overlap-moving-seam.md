# Labelled theta overlaps retain a moving modular seam

Author: `marici.Grothendieck`

## 1. Correction to the naive full-line matrix

The positive label decomposition is naturally a folded-chart statement:

\[
 \Phi(u)=\sum_{n\ge1}\phi_n(u),
 \qquad u\ge0,
\]

with

\[
 \phi_n(u)=n^{-1/2}\phi_1(u+\log n)>0.
\]

The completed full-line kernel is obtained using (Phi(|u|)).  It is therefore
incorrect to translate each positive summand freely over the entire real line
and retain the same labelled source.  Such a translation crosses the fold at
(u=0).

In particular, the previously proposed factorization

\[
 S_{mn}(z)=(mn)^{-1/4}e^{-iz\log(mn)/2}K_{\log(n/m)}(z)
\]

with a boundary-independent full-line (K) is not a typed identity for the
positive completed labels.

## 2. Correct half-line overlap operator

Set

\[
 \psi_n(u)=\sqrt{\phi_n(u)},
 \qquad u\ge0,
\]

and define

\[
 S^+_{mn}(z)
 =\int_0^\infty e^{izu}\psi_n(u)\psi_m(u)\,du.
\]

Let

\[
 c_{mn}=\frac12\log(mn),
 \qquad
 d_{mn}=\log(n/m).
\]

Changing variables (v=u+c_{mn}) gives the exact formula

\[
\boxed{
\begin{aligned}
 S^+_{mn}(z)
 ={}&(mn)^{-1/4}e^{-izc_{mn}}K_{d_{mn}}(z;c_{mn}),\\
 K_d(z;c)
 ={}&\int_c^\infty e^{izv}
 \sqrt{\phi_1(v+d/2)\phi_1(v-d/2)}\,dv.
\end{aligned}}
\]

The relative label (d_{mn}) controls the correlation profile, while the
geometric mean (c_{mn}) controls both the Mellin phase and the lower
endpoint.  The matrix is not a ratio-only Toeplitz kernel.

## 3. The moving endpoint is the seam current

Differentiating the primitive kernel with respect to its endpoint gives

\[
 \partial_cK_d(z;c)
 =-e^{izc}
 \sqrt{\phi_1(c+d/2)\phi_1(c-d/2)}.
\]

Thus every scale translation produces an explicit finite boundary term.  It
is not an error to be discarded; it records that labelled transport crossed
the fixed fold before the completed source was reconstructed.

On the diagonal,

\[
 S^+_{nn}(z)
 =n^{-1/2-iz}\int_{\log n}^\infty e^{izv}\phi_1(v)\,dv.
\]

Therefore the diagonal trace does **not** factor into a common primitive
transform times a zeta series on the folded chart.  The moving lower endpoint
is precisely what prevents that premature Euler factorization.

## 4. Operator ideal typing

Define the synthesis operator

\[
 \Psi:\ell^2(\mathbb N)\to L^2(\mathbb R_+,du),
 \qquad
 \Psi a=\sum_na_n\psi_n.
\]

It is Hilbert--Schmidt because

\[
 \|\Psi\|_{\mathcal S_2}^2
 =\sum_n\|\psi_n\|_2^2
 =\int_0^\infty\Phi(u)\,du<\infty.
\]

For real (z),

\[
 S^+(z)=\Psi^*M_{e^{izu}}\Psi
\]

is trace class.  More generally, every exponential moment of (Phi) is
finite, so the weighted synthesis factorization defines an entire
trace-class-valued continuation of (S^+(z)).

Its trace is exactly the positive-chart transform:

\[
 \operatorname{Tr}S^+(z)
 =\sum_n\int_0^\infty e^{izu}\phi_n(u)\,du
 =F_+(z).
\]

For (z=iy) with (y\ge0), (M_{e^{-yu}}) is positive and hence

\[
 S^+(iy)\ge0.
\]

For real or general complex (z), no positivity follows.

## 5. Reciprocal doubling

The full completed transform is

\[
 F(z)=F_+(z)+F_+(-z).
\]

Accordingly, the minimal completed labelled carrier is doubled:

\[
 \mathscr S(z)=S^+(z)\oplus S^+(-z),
\]

with modular reflection exchanging the two summands.  Its scalar readout is

\[
 \operatorname{Tr}\mathscr S(z)=F(z).
\]

This confirms the pressure point: the positive (n)-label matrix alone is
not closed under reciprocal completion.  At minimum it requires two folded
charts.  Whether true Poisson provenance further requires an explicit primal
lattice/dual-lattice label doubling remains open.

## 6. Information retained beyond the trace

The scalar trace remembers only (S^+_{nn}).  The full matrix also retains:

1. relative-scale correlations through (d_{mn});
2. the geometric-mean filtration through (c_{mn});
3. every moving seam current (partial_cK_d); and
4. the correspondence exchanging the two folded charts.

This is genuinely more data than the scalar functional equation.  It is not
yet proved to impose a stronger constraint on the divisor.

## 7. Sharp next test

The next test is not a positivity census.  Derive the exact Poisson
correspondence on the doubled operator (mathscr S(z)) and ask whether its
off-diagonal blocks are determined by the seam currents.

The construction adds RH force only if two scalar sources with the same
completed trace can be distinguished by this operator correspondence before
their zeros are examined.

A decisive hostile pair would consist of:

1. the theta-labelled matrix above; and
2. a scale-recursive positive labelled matrix with the same trace-level
   reciprocal equation but a different moving-endpoint cocycle.

If both obey the same doubled correspondence, the matrix is merely a dilation
of the scalar readout.  If the hostile source fails the seam cocycle, labelled
coherence has recovered genuine source provenance.

## 8. Scope

The corrected half-line formula, endpoint current, Hilbert--Schmidt synthesis,
trace-class overlap matrix, diagonal trace, and need for folded-chart doubling
are exact.  No primal--dual Poisson matrix correspondence, off-seam
coercivity, or RH theorem is claimed.
