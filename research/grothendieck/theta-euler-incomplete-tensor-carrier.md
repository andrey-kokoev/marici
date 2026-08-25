# The Euler incomplete tensor Carrier exists exactly to the critical seam

Author: `marici.Grothendieck`

## 0. Operator stimulus

The operator proposed that the half-planes acquire distinct integral
structures before the scalar readout loses meaning.  Prime-exponent
coordinates now give an exact Carrier realizing this order without passing
first to a scalar Euler product.

## 1. Local integer occupation state

For every prime `p`, let

\[
\mathcal H_p=\ell^2(\mathbb N_0)
\]

with basis `e_(p,a)` indexed by the integer valuation `a=v_p(n)`.  Put

\[
q_p(s)=p^{-s}.
\]

For `Re(s)>0`, define the normalized geometric occupation state

\[
\boxed{
\psi_{p,s}
=\sqrt{1-|q_p(s)|^2}
\sum_{a\ge0}q_p(s)^a e_{p,a}.
}
\]

The geometric-series identity gives

\[
\|\psi_{p,s}\|=1.
\]

This state retains every prime-power label.  It is not the scalar local Euler
factor.

## 2. Infinite tensor-product threshold

Use the vacuum reference `Omega_p=e_(p,0)`.  Von Neumann's incomplete tensor
product

\[
\mathcal H_{\rm Euler}
=\bigotimes_p^{\Omega_p}\mathcal H_p
\]

contains the product state

\[
\Psi_s=\bigotimes_p\psi_{p,s}
\]

exactly when

\[
\sum_p\left(1-|\langle\Omega_p,\psi_{p,s}\rangle|\right)<\infty.
\]

Here

\[
\langle\Omega_p,\psi_{p,s}\rangle
=\sqrt{1-p^{-2\operatorname{Re}s}},
\]

and

\[
1-\sqrt{1-p^{-2\sigma}}
=\frac12p^{-2\sigma}+O(p^{-4\sigma}).
\]

Therefore

\[
\boxed{
\Psi_s\in\mathcal H_{\rm Euler}
\quad\Longleftrightarrow\quad
\operatorname{Re}s>\frac12.
}
\]

The critical line is the exact existence boundary of the full
integer-valuation tensor Carrier.

## 3. Vacuum overlap and orthogonality catastrophe

Inside the chamber,

\[
\begin{aligned}
\langle\Omega,\Psi_s\rangle
&=\prod_p\sqrt{1-p^{-2\operatorname{Re}s}}\\
&=\zeta(2\operatorname{Re}s)^{-1/2}.
\end{aligned}
\]

This overlap is strictly positive for `Re(s)>1/2` and tends to zero as the
critical seam is approached.  Thus the seam is an arithmetic orthogonality
catastrophe: the integer occupation state leaves the vacuum representation.

No Riemann-zero information enters this statement.  It follows solely from
unique factorization and the harmonic divergence of the primes.

## 4. The Euler scalar observer is different

On a single prime fiber, the local Euler factor is obtained by the formal
all-occupations covector

\[
\ell_p(e_{p,a})=1:
\]

\[
\ell_p(\psi_{p,s})
=\frac{\sqrt{1-|p^{-s}|^2}}{1-p^{-s}}.
\]

The covector `ell_p` is not bounded on `ell^2(N_0)`.  Its tensor product over
all primes is therefore not an ordinary vector in the incomplete tensor
Carrier.

Formally removing the normalization gives

\[
\prod_p(1-p^{-s})^{-1}=\zeta(s),
\]

but this scalar projection is absolutely meaningful only for
`Re(s)>1`.  Hence:

\[
\boxed{
\text{the labelled tensor state exists down to }1/2,
\quad
\text{while the unlabelled scalar Euler observer fails already at }1.
}
\]

This is the exact two-threshold structure anticipated by the operator.

## 5. Relation to the Schatten model

The one-particle displacement coordinate of `Psi_s` is the prime vector

\[
v_s=(p^{-s})_p.
\]

Existence of the incomplete tensor product is controlled by

\[
\sum_p\|q_p(s)e_{p,1}\|^2,
\]

the same Hilbert--Schmidt sum that defines `P_s in S_2`.  The determinant
cocycle and the tensor-product criterion are therefore two presentations of
one geometry:

\[
\boxed{
\text{Hilbert--Schmidt polarization}
\;\Longleftrightarrow\;
\text{integer Euler product state in the vacuum representation}.
}
\]

The former emphasizes pairwise angles; the latter emphasizes integral
valuation fibers.

## 6. Completion as a relative boundary functional

The completed xi readout cannot be an ordinary scalar product with the
all-occupations covector.  It must be a relative functional coupling:

\[
\text{Euler occupation Carrier}
+\text{endpoint state}
+\text{gamma/theta modular state}.
\]

The completion-selected anomaly section `T(s)` is the scalar produced by
that still-unknown relative boundary functional after the nonvanishing
`det_2` tail is removed.

The desired theorem becomes:

\[
\boxed{
\text{the completed relative observer has nonzero overlap with }\Psi_s
\text{ everywhere that }\Psi_s\text{ belongs to the vacuum sector.}
}
\]

This is precisely RH in the right chamber, but its source object is now
faithful: the entire prime-exponent packet is retained before observation.

## 7. Circle and integral phase

The product state is a ray in projective Fock space.  Its intrinsic scalar
ambiguity is a `U(1)` phase fiber.  A zero of the completed overlap is a
failure of transversality between the Euler ray and the completed boundary
state.  A small loop around that failure winds in the determinant-line
`U(1)` fiber and becomes a circle in its Hermitian metric.

Thus the circle asked about by the operator is naturally the phase fiber of
the integer tensor Carrier around a vanishing relative overlap.

## 8. Falsifiers

A proposed completion fails if it:

1. replaces the valuation tensor state by the scalar Euler product before
   forming the relative pairing;
2. treats the all-occupations covector as a bounded Hilbert vector;
3. asserts the product state exists on the critical line itself;
4. changes prime labels or valuation normalization to force convergence; or
5. defines the boundary functional using the zeros of `xi`.

## 9. Scope

The local normalized states, incomplete tensor-product criterion, vacuum
overlap, and thresholds `1` and `1/2` are exact.  The endpoint--gamma--theta
relative observer and its nonzero-overlap theorem remain unconstructed.  RH
is not proved.
