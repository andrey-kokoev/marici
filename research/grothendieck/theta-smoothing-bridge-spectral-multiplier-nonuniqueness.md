# Static source symmetries do not select a unique smoothing bridge

## 1. Candidate completion generator

Let \(A_\Phi\ge0\) be the completed source diffusion with compact resolvent,

\[
  A_\Phi e_n=\lambda_ne_n,
  \qquad
  0=\lambda_0<\lambda_1\le\lambda_2\le\cdots,
\]

and normalized ground mode \(e_0=\Omega\).

A smoothing bridge between the two rigged Clifford charts should map

\[
  K:E'\longrightarrow E
\]

and be nuclear on the Hilbert pivot.

## 2. Infinite spectral-multiplier family

For any positive function \(f\) on the spectrum satisfying

\[
  f(0)=1,
  \qquad
  f(\lambda_n)>0,
  \qquad
  \sum_nf(\lambda_n)<\infty,
\]

the spectral multiplier

\[
  K_f=f(A_\Phi)
\]

is positive, injective, trace class, preserves the ground mode, and commutes
with \(A_\Phi\).

If a source symmetry \(R\) commutes with \(A_\Phi\), then every \(K_f\)
commutes with \(R\) as well. Thus reflection or any Fourier/metaplectic
symmetry already contained in the commutant does not reduce this family.

Examples include

\[
  e^{-tA_\Phi},
  \qquad
  (I+A_\Phi)^{-m},
  \qquad
  e^{-tA_\Phi^\alpha},
\]

whenever the displayed parameters give trace-class decay.

## 3. Determinant ambiguity

Different multipliers have different excited spectra and therefore different
Fredholm determinants after seam or crossing compression. All visible static
typing conditions may remain unchanged:

\[
\boxed{
\text{positive}
+\text{nuclear}
+\text{ground preserving}
+\text{symmetry commuting}
\not\Longrightarrow
\text{unique theta bridge}.}
\]

This realizes the principal risk identified in the previous disposition.

## 4. Why Fourier exchange does not automatically help

If the actual cross-chart comparison has the form

\[
  \widetilde K_f=Jf(A_\Phi)
\]

or

\[
  \widetilde K_f=f(A_\Phi)J,
\]

then the quarter-turn \(J\) types the direction of the bridge but still
leaves the spectral multiplier \(f\) arbitrary. Static covariance determines
which spaces are connected, not how strongly each excited mode is weighted.

## 5. Required dynamical law

The heat family gains uniqueness only after imposing:

\[
  K_{t+s}=K_tK_s,
  \qquad
  K_0=I,
  \qquad
  \left.\partial_tK_t\right|_{t=0}=-A_\Phi.
\]

These conditions force

\[
  K_t=e^{-tA_\Phi}.
\]

But they still leave the physical comparison time \(t\) unspecified. A
source-derived modular-scale law must select the relevant member or produce
a time-independent relative determinant.

Thus two independent authorities are required:

1. the diffusion/gluing law selects the *family*;
2. modular incidence selects the *comparison time or relative invariant*.

## 6. Strongest next test

Use the theta modular parameter before setting it to the self-dual point.
Derive a two-parameter composition law for the cross-chart kernel and ask
whether reciprocal sewing

\[
  t\longmapsto t^{-1}
\]

selects \(t=1\) as a fixed comparison without fitting \(X\).

Then apply the same construction to a hostile self-Fourier source. If its
heat family and fixed point satisfy the identical laws, modular-time
selection still supplies no RH force; one must retain the arithmetic label
connection.

## 7. Falsifiers

The unique-bridge programme fails if:

1. more than one spectral multiplier obeys the full gluing and modular laws;
2. selecting \(t=1\) depends on a coordinate normalization not fixed by Haar
   and Fourier conventions;
3. the cross-chart determinant changes under an admissible reparameterization
   of diffusion time; or
4. the determinant matches \(X\) only after a scalar correction with zeros.

## 8. Scope

The spectral-multiplier nonuniqueness theorem and heat-semigroup uniqueness
under a fixed generator are exact. They show that static geometric-algebra
and completion data do not select the theta bridge. No modular-time
selection, regulator-independent spinor pairing, de Branges positivity, or
RH theorem is established.
