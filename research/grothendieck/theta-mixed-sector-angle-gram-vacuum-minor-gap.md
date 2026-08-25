# Mixed-sector angle operator exists, but \(X\) is only its vacuum minor

## 1. Canonical mixed operator

Let

\[
  E_t=e^{-tA_\Phi/2},
\]

and let \(W_x\) denote the real-character Fourier/Poisson crossing between the
two reciprocal polarization charts. For real \(x\), \(W_x\) is unitary on the
ambient carrier. With the two sector projections \(P_\pm\), define

\[
  K_t(x)
  =
  P_+E_tW_xE_tP_-.
\]

If \(E_t\) is Hilbert--Schmidt, then \(K_t(x)\) is trace class. Moreover,

\[
  \|K_t(x)\|\le1
\]

because \(E_t\), \(P_\pm\), and \(W_x\) are contractions or unitaries.

## 2. Relative-angle Gram operator

The coupled block

\[
  G_t(x)
  =
  \begin{pmatrix}
    I & K_t(x)\\
    K_t(x)^* & I
  \end{pmatrix}
\]

is positive semidefinite. Its Fredholm determinant is

\[
  \det G_t(x)
  =
  \det\bigl(I-K_t(x)^*K_t(x)\bigr)\ge0.
\]

Geometrically, the singular values of \(K_t(x)\) are cosines of regularized
principal angles between the transported sectors, and the determinant is the
product of their squared sines.

This is a genuine full-space relative-angle object.

## 3. Universality obstruction

The construction used only:

1. a positive heat contraction;
2. two orthogonal sector projections; and
3. a unitary crossing.

It therefore works for hostile self-Fourier sources as well as for theta.
Its positivity on real character transport is operator-theoretically
automatic and has no RH force.

More importantly, the theta scalar is at most a distinguished matrix
coefficient of \(K_t(x)\):

\[
  X(x)
  \sim
  \langle\Omega_+,K_t(x)\Omega_-\rangle
\]

after the exact endpoint and normalization maps are supplied. Vanishing of
one matrix entry does not imply vanishing of the determinant of the full Gram
operator.

\[
\boxed{
\text{vacuum orthogonality}
\not\Longrightarrow
\text{sector nontransversality}.}
\]

This is the operator version of the scalar-readout faithfulness problem.

## 4. Vacuum/excited decomposition

Decompose each sector into its vacuum line and excited complement:

\[
  \mathcal H_\pm
  =
  \mathbb C\Omega_\pm\oplus\mathcal H_\pm^\circ.
\]

In this decomposition, \(K_t\) has blocks

\[
  K_t
  =
  \begin{pmatrix}
    k_{00} & k_{0\circ}\\
    k_{\circ0} & K_{\circ\circ}
  \end{pmatrix}.
\]

The physical scalar sees \(k_{00}\). A full Fredholm determinant sees all
four blocks. Schur reduction produces the corrected vacuum channel

\[
  k_{00}^{\mathrm{eff}}
  =
  k_{00}
  -
  k_{0\circ}
  K_{\circ\circ}^{-1}
  k_{\circ0}
\]

whenever the indicated complement block is invertible in the correctly typed
comparison operator.

Hence \(X=k_{00}\) can equal a full incidence determinant only if the excited
correction is:

1. identically zero by source selection; or
2. a nowhere-zero transition unit that can be separated without using zero
   information.

## 5. Commutator test

The vacuum/excited couplings vanish only under a strong reduction law. A
necessary diagnostic is whether the crossing preserves the diffusion ground
line:

\[
  [A_\Phi,W_x]\Omega=0.
\]

For generic character transport this fails: multiplication by
\(e^{ixu}\) moves the constant ground state into excited diffusion modes.
Therefore the Schur correction is expected to be nonzero.

This identifies the exact theorem needed:

\[
\boxed{
\text{prove that excited-mode Schur dressing is a nowhere-zero source unit}.}
\]

Without it, the full operator determinant and the physical scalar readout
have different divisors.

## 6. Falsifier

The smallest falsifier is a parameter \(x\) at which \(k_{00}(x)=0\) while
the full Gram determinant remains positive. Such behavior is generic for a
matrix entry and requires no numerical search to be possible.

Conversely, a source-derived triangularity or invariant flag making
\(k_{0\circ}=0\) or \(k_{\circ0}=0\) would collapse the determinant divisor to
the vacuum divisor and constitute real progress.

## 7. Scope

Trace-class typing, contraction, Gram positivity, and the vacuum-minor
distinction are exact under the heat-trace and unitary-crossing hypotheses.
The displayed Schur scalar is schematic until the final comparison operator
is fixed. No invariant flag, determinant equality with \(X\), off-seam
exclusion, or RH theorem is established.
