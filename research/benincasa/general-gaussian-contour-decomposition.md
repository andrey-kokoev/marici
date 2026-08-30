# General Gaussian contour decomposition

## Frozen primary source

Use Agarwal--Holman--Tolley--Lin, arXiv:1212.1172, without changing its
normalization:

- Eqs. (103), (106)--(108): the initial quadratic density-matrix kernels
  (A_k\in\mathbb C) and (B_k\in\mathbb R), including the endpoint factor
  (\int_{t_0}^{\infty}\delta(t-t_0)dt=1/2);
- Eqs. (130)--(141): the (SU(1,1)) diagonalization and the equivalent
  covariance coordinates ((\xi_k,\eta_k,\sigma_k));
- Eqs. (142)--(162): the pure-state mode functions and the restoration of
  mixedness;
- Sec. 4: the source's Hadamard requirement on the ultraviolet falloff of
  the Bogoliubov coefficient.

The source relations are

\[
-iA_k=\frac{\sigma_k^2+1}{4\xi_k^2}
-i\frac{\eta_k}{\xi_k},
\qquad
B_k=\frac{1-\sigma_k^2}{4\xi_k^2},
\]

and

\[
A_{kI}^2-B_k^2
=\left(\frac{\sigma_k}{2\xi_k^2}\right)^2>0.
\]

For a pure state, the mode pair is a normalized Bogoliubov transform,

\[
f_k^>=\alpha_k h_k+\beta_k h_k^*,
\qquad
|\alpha_k|^2-|\beta_k|^2=1.
\]

After undoing the (SU(1,1)) transformation, Eq. (162) gives, for every
contour pair (a,b\in\{+,-\}),

\[
G_k^{ab}
=G_k^{\prime ab}
+\frac{\sigma_k-1}{2}
\left(G_k^{\prime-+}+G_k^{\prime+-}\right).
\]

## Typed decomposition

At fixed momentum, a homogeneous isotropic Gaussian state has three real
coefficient directions.  The source formulas distinguish them canonically:

\[
\boxed{
\mathcal G_k^{\rm Gauss}
=\mathcal G_k^{\rm Bog}(2\ \text{real directions})
\oplus
\mathcal G_k^{\rm stat}(1\ \text{real direction}).
}
\]

The first summand changes the normalized pure mode through the complex
Bogoliubov coordinate.  The second changes mixedness and is represented in
contour-index space by the rank-one matrix

\[
J_{\rm stat}=
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

This is a coefficient decomposition, not a decomposition of the resolved
energy/Cut carrier.  The statistical line is also not a new contour cell:
it is a distinguished coefficient direction on the already doubled
Schwinger--Keldysh occurrence object.

## Ultraviolet filtration

The source imposes Hadamard admissibility through ultraviolet decay of the
Bogoliubov coefficient (and implements it with a physical cutoff).  This is
extra support/falloff data on the Gaussian coefficient object.  It is not
implied by finite-dimensional closure in

\[
(\operatorname{Re}A_k,\operatorname{Im}A_k,B_k).
\]

Accordingly, Entries 1568, 1570, and 1573 establish target-type closure for
the frozen one-loop toy packet, but cannot establish preservation of this
filtered subobject.

## Next finite falsifier

For one source interaction, expand the one-loop map to first order around a
general pure Hadamard-filtered mode and independently around the statistical
direction (J_{\rm stat}).  Before momentum integration, test:

1. whether the pure variation remains tangent to the normalized
   (SU(1,1)/U(1)) Bogoliubov orbit;
2. whether a statistical input remains in the rank-one common-contour line;
3. whether either channel generates a slower ultraviolet tail than its
   source input after Bunch--Davies subtraction and the declared bulk and
   boundary counterterms.

A contour-rank failure is a coefficient-object obstruction.  A falloff
failure is a filtration obstruction.  Neither, by itself, creates a new
carrier stratum.

