# Heat seam interpolates from non-Fredholm bulk to rank-one vacuum readout

## 1. Completed ground mode

The completed diffusion \(A_\Phi\) has the normalized constant ground mode

\[
  \Omega=\mathbf 1,
  \qquad
  Z=\int_{\mathbb R}\Phi(u)\,du,
\]

in

\[
  \mathcal H_\Phi=L^2(\mathbb R,Z^{-1}\Phi(u)\,du).
\]

Indeed, the normalization of the measure gives \(\|\mathbf1\|=1\).

Let \(P_\Omega=|\Omega\rangle\langle\Omega|\). Compact resolvent and the
one-dimensional zero eigenspace give

\[
  e^{-tA_\Phi}\longrightarrow P_\Omega
\]

as \(t\to\infty\), in operator norm, and in trace norm whenever one positive
heat time is trace class.

## 2. Long-time seam limit

For the heat-sandwiched seam

\[
  C_{a,t}
  =
  e^{-tA_\Phi/2}C_ae^{-tA_\Phi/2},
\]

one obtains

\[
  C_{a,t}
  \longrightarrow
  P_\Omega C_aP_\Omega
  =
  \langle\Omega,C_a\Omega\rangle P_\Omega
\]

in trace norm under the same hypothesis.

For \(a>0\), using

\[
  C_a=-M_{\mathbf1_{[-a,0)}},
\]

the surviving scalar is

\[
  \langle\Omega,C_a\Omega\rangle
  =
  -\frac1Z\int_{-a}^0\Phi(u)\,du.
\]

Thus the long-time determinant is exactly

\[
  \lim_{t\to\infty}
  \det(I+\lambda C_{a,t})
  =
  1-\frac{\lambda}{Z}
  \int_{-a}^0\Phi(u)\,du.
\]

It is the vacuum-compressed finite seam current.

## 3. Two limiting failures

The heat family has two transparent ends:

\[
\begin{array}{ccl}
t\downarrow0
&:&
C_{a,t}\to C_a
\quad\text{strongly, with a noncompact limit},\\[3pt]
t\to\infty
&:&
C_{a,t}\to
\langle\Omega,C_a\Omega\rangle P_\Omega
\quad\text{in trace norm}.
\end{array}
\]

The ultraviolet end has the full continuum boundary but no Fredholm
determinant. The infrared end has a determinant but retains only the
universal rank-one scalar seam.

\[
\boxed{
\text{heat regularization interpolates between
non-Fredholm geometry and scalar tautology}.}
\]

No intermediate heat time is selected by this interpolation alone.

## 4. Spectral content at finite heat time

In an eigenbasis \(A_\Phi e_j=\lambda_je_j\),

\[
  C_{a,t}
  =
  \sum_{j,k}
  e^{-t(\lambda_j+\lambda_k)/2}
  \langle e_j,C_ae_k\rangle
  |e_j\rangle\langle e_k|.
\]

Finite \(t\) retains excited source modes and seam matrix elements, but the
weights are regulator weights. To become physical, the modular source must
derive either:

1. a particular spectral function of \(A_\Phi\), not merely \(e^{-tA_\Phi}\);
   or
2. a regulator-independent relative determinant formed from two completed
   seams whose ultraviolet divergences cancel.

## 5. Strongest next target

Compare reciprocal seams before taking either limit. Seek a relative operator

\[
  R_{a,t}
  =
  (I+\lambda C_{a,t}^{+})
  (I+\lambda C_{a,t}^{-})^{-1}
\]

or the correctly typed modular analogue, and test whether its determinant is
independent of \(t\). Heat-time independence would be an actual conservation
law:

\[
  \partial_t\log\det R_{a,t}=0.
\]

It must be derived from Fourier/Poisson sewing and fail for hostile
self-Fourier sources if it is to carry RH information.

## 6. Scope

The ground-mode limit, interval-mass formula, and rank-one determinant limit
are exact under the stated heat-trace condition. They show that fixed heat
compression alone does not select the theta determinant. No
regulator-independent relative operator, conservation law, identity with
\(X\), or RH theorem is established.
