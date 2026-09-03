# A safe single-prime cutoff removes root isolation from the finite bound

## Question

Can one obtain a finite first-prime tail dimension without certifying every bad-set root and interval measure?

## Claim boundary

Yes, conditionally on a standard explicit digamma asymptotic remainder bound. A conservative exterior cutoff, cell-count bound, and total enclosure measure can be inserted into the resonance estimate. This produces a root-free finite dimension below one million. The current numerical evaluation is not directed-interval certified because the classical digamma remainder constant has not yet been instantiated.

## Safe cutoff

Take

\[
L=\frac7{20},
\qquad
\delta=0.05,
\qquad
R=10000.
\]

The six-term digamma asymptotic gives diagnostically

\[
m_\Gamma(R)
\approx0.5866819889.
\]

The required exterior level is

\[
\frac{\log2}{\sqrt2}+\delta
\approx0.5401290717.
\]

Thus the apparent margin is about \(0.04655\), far larger than the omitted asymptotic terms at imaginary argument \(5000\). A cited explicit remainder theorem would convert this separation into a rigorous inequality.

## Root-free geometry bounds

The bad set lies inside \([-R,R]\), so

\[
W\leq2R=20000.
\]

The number of intersected cosine cells is bounded by

\[
N
\leq
\left\lceil\frac{2R}{p}\right\rceil+1
=2208,
\qquad
p=\frac{2\pi}{\log2}.
\]

No root isolation is required.

## Explicit dimension

Substitution into the resonance-transition formula gives the diagnostic bounds

\[
\operatorname{Tr}(T)
\leq2228.17,
\]

\[
\operatorname{Tr}(T-T^2)
\leq47283.54.
\]

With

\[
\eta
=
\frac{0.05}{0.05+C_-}
\approx0.0516724,
\]

a sufficient integer is

\[
M=917292.
\]

This is larger than the root-scout value \(474019\) but avoids certifying \(1229\) separate intervals.

## Remaining certification datum

The first missing object is now one classical analytic inequality: an explicit remainder bound for

\[
\psi(z)
=
\log z-rac1{2z}
-
\sum_{k=1}^{K}
\frac{B_{2k}}{2kz^{2k}}
+R_K(z)
\]

at \(z=1/4+5000i\), strong enough to prove

\[
m_\Gamma(10000)>0.5401290717.
\]

Once supplied, the exterior cutoff, component bound, measure bound, transition estimate, and finite dimension become rigorous without root isolation.

## Disposition

The geometric enclosure problem is bypassed by a conservative root-free certificate. The remaining tail-certification blocker is a single sourced digamma remainder theorem. The finite Schur positivity problem remains RH-bearing.

## Verification

- `research/voevodsky/checkers/check_safe_single_prime_cutoff.py`
- `research/voevodsky/results/safe_single_prime_cutoff.json`
