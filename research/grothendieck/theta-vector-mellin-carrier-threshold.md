# The vector-valued theta Mellin Carrier selects the critical seam

Author: `marici.Grothendieck`

## 0. Operator stimulus

The operator proposed that the Carrier remains meaningful after its scalar
readout has become undefined, and that the half-plane distinction precedes
that loss. The Euler occupation tensor established this arithmetically.
This packet derives the same `1/2` boundary directly from the undecomposed
theta heat source, before any scalar zeta continuation.

## 1. Label-preserving theta heat state

Let

\[
\mathcal H_{\mathbb N}=\ell^2(\mathbb N)
\]

with labelled basis `e_n`. For `t>0` define

\[
G(t)=\sum_{n\ge1}e^{-\pi n^2t}e_n.
\]

This is an honest Hilbert vector for every positive `t`. Its squared norm is

\[
\|G(t)\|^2=\sum_{n\ge1}e^{-2\pi n^2t}.
\]

The elementary Gaussian integral comparison gives

\[
\|G(t)\|^2\asymp t^{-1/2},
\qquad
\|G(t)\|\asymp t^{-1/4}
\qquad(t\downarrow0).
\]

The exponent `1/4` is the label-space heat singularity before scalar
summation.

## 2. Vector-valued Mellin transform

Consider the Bochner integral

\[
\mathcal K(s)
=\int_0^\infty t^{s/2-1}G(t)\,dt.
\]

The large-`t` tail is exponentially convergent. At zero, its norm is bounded
by a constant times

\[
t^{\operatorname{Re}s/2-1}t^{-1/4}.
\]

This is integrable exactly when

\[
\frac{\operatorname{Re}s}{2}-1-\frac14>-1,
\]

or

\[
\operatorname{Re}s>\frac12.
\]

Componentwise Mellin transformation gives

\[
\mathcal K(s)
=\pi^{-s/2}\Gamma(s/2)
\sum_{n\ge1}n^{-s}e_n.
\]

Thus the labelled theta--Dirichlet state exists as one Hilbert vector
throughout precisely the open RH chamber.

## 3. Agreement with the Euler tensor Carrier

Unique factorization identifies

\[
\ell^2(\mathbb N)
\cong
\bigotimes_p^{e_{p,0}}\ell^2(\mathbb N_0).
\]

Under this unitary label identification,

\[
\sum_{n\ge1}n^{-s}e_n
=\bigotimes_p\left(\sum_{a\ge0}p^{-as}e_{p,a}\right)
\]

whenever interpreted in the normalized incomplete tensor sector. Its norm is

\[
\sum_{n\ge1}|n^{-s}|^2
=\zeta(2\operatorname{Re}s).
\]

Consequently the normalized Euler product state is exactly

\[
\Psi_s
=\frac1{\sqrt{\zeta(2\operatorname{Re}s)}}
\sum_{n\ge1}n^{-s}e_n.
\]

The prime-exponent tensor criterion and the theta heat-Mellin criterion are
not analogous estimates. They are the same labelled Hilbert vector in two
coordinate systems.

## 4. The scalar observer fails earlier

The scalar zeta readout is

\[
\zeta(s)
=\left\langle\mathbf1,
\sum_{n\ge1}n^{-s}e_n\right\rangle,
\qquad
\mathbf1=(1,1,\ldots).
\]

The all-label covector is not in `ell^2(N)`. Its pairing is absolutely
defined only when the Hilbert vector happens additionally to lie in
`ell^1(N)`:

\[
\operatorname{Re}s>1.
\]

Therefore the theta construction gives the same exact corridor:

The labelled Mellin Carrier exists for
(\operatorname{Re}s>1/2), while the unlabelled scalar sum is directly
defined only for (\operatorname{Re}s>1).

The scalar loses meaning after the labelled half-plane Carrier has already
become a valid Hilbert object.

## 5. Completed scalar projection

The completed readout is formally

\[
\xi(s)
=\frac12s(s-1)
\left\langle\mathbf1,\mathcal K(s)\right\rangle.
\]

The formula is valid directly only in the Euler region. Modular reflection
rewrites the scalar theta integral into an entire expression, but it does not
turn `1` into a bounded covector on the labelled Mellin Hilbert space.

Thus completion performs a relative scalar projection after the faithful
vector `K(s)` has been formed. A zero of `xi` means failure of this completed
projection, not failure of the vector-valued theta Mellin transform.

## 6. Why the seam is source-derived

The threshold `1/2` has now been obtained twice:

\[
\sum_p p^{-2\operatorname{Re}s}<\infty
\]

from prime occupation geometry, and

\[
\int_0^1
t^{\operatorname{Re}s/2-1}\|G(t)\|\,dt<\infty
\]

from theta heat geometry.

The equality of the resulting states is supplied by unique factorization and
the Mellin transform. Hence

Thus the critical seam is where one fixed labelled theta/Euler Carrier ceases
to be Hilbert-integrable.

This conclusion does not use zero locations.

## 7. Remaining relative-observer theorem

The scalar modular tail formula already constructs a completed functional

\[
\Lambda_{\operatorname{comp}}(s)
\]

on a source-derived tail presentation such that

\[
\Lambda_{\operatorname{comp}}(s)\mathcal K(s)=\xi(s)
\]

but does not make its nonvanishing manifest while `K(s)` remains in its
Hilbert chamber.

No fixed bounded functional on `ell^2(N)` can do this: agreement with the
Euler coefficients on an open half-plane would force the all-ones Riesz
vector. Endpoint and modular-reflection channels must therefore participate
in the functional itself.

## 8. Falsifier and scope

A proposed proof fails if it scalarizes `G(t)` before its vector Mellin
transform, treats the all-ones sequence as a Hilbert vector, or claims
Bochner convergence at the critical line. It also fails if the completed
functional is defined using `xi` rather than independently reproducing it.

The vector heat estimate, Bochner threshold, component identity, and
Euler-tensor equivalence are exact. The modular scalar observer exists, but
its nonzero relative-overlap realization remains missing. RH is not proved.

## 9. Weak collapse at the seam

Normalize the labelled Dirichlet state:

\[
\widehat k_s
=\frac1{\sqrt{\zeta(2\operatorname{Re}s)}}
\sum_{n\ge1}n^{-s}e_n.
\]

For every point in the open chamber,

\[
\|\widehat k_s\|=1.
\]

Fix the imaginary part and let `Re(s)` decrease to `1/2`.  For every
finite-support vector `f`,

\[
\langle f,\widehat k_s\rangle\longrightarrow0
\]

because the finite numerator remains bounded while
`zeta(2 Re(s))` diverges.  Density and the uniform unit norm then give

\[
\widehat k_s\rightharpoonup0
\qquad
\left(\operatorname{Re}s\downarrow\frac12\right).
\]

There is no strong limit because every state has norm one.  Mass escapes to
arbitrarily large integer labels.

Equivalently, for every fixed cutoff `N`,

\[
\sum_{n\le N}
\frac{n^{-2\operatorname{Re}s}}
{\zeta(2\operatorname{Re}s)}
\longrightarrow0.
\]

Thus no finite operational label census detects a nonzero fraction of the
boundary state, even though every interior state is normalized.

## 10. Entropy catastrophe

On the real radial slice, the normalized label probabilities are

\[
\mathbb P_\sigma(n)
=\frac{n^{-2\sigma}}{\zeta(2\sigma)}.
\]

Their Shannon entropy is exactly

\[
\mathsf H(\sigma)
=\log\zeta(2\sigma)
-2\sigma\frac{\zeta'(2\sigma)}{\zeta(2\sigma)}.
\]

Writing `epsilon=2sigma-1` and using the pole of zeta at one gives

\[
\mathsf H(\sigma)
=\frac1\epsilon-\log\epsilon+O(1)
\qquad(\epsilon\downarrow0).
\]

The inverse participation ratio gives the same delocalization:

\[
\sum_n\mathbb P_\sigma(n)^2
=\frac{\zeta(4\sigma)}{\zeta(2\sigma)^2}
\sim\zeta(2)\epsilon^2.
\]

Hence the effective number of occupied integer labels diverges at least on
the scale `epsilon^(-2)`.

This is a literal entropy gain at the critical seam: finite-label meaning
vanishes because the integral Carrier delocalizes over infinitely many labels.

It does not by itself locate zeros of the completed scalar observer.  It
explains why the boundary can support phase defects while every finite
interior Carrier remains normalized and nonzero.

## 11. Compact-observer extinction

Weak convergence of a bounded sequence implies strong convergence after any
compact operator.  Hence for every compact `A` on `ell^2(N)`,

\[
\|A\widehat k_s\|\longrightarrow0
\qquad
\left(\operatorname{Re}s\downarrow\frac12\right).
\]

Finite-rank label measurements are a special case.  Therefore no fixed
finite packet, compact detector, or norm-limit of such detectors can retain a
nonzero fraction of the Carrier at the seam.

Any completed boundary readout that survives must be noncompact,
distributional, or relative between two simultaneously diverging sectors.
The all-ones Euler observer has exactly this type.  Endpoint and gamma
completion must regularize it without converting it into a compact
observation that would vanish automatically.

This supplies a durable methodological consequence: finite scouting can test
interior formulas but cannot discover the boundary observer by convergence of
finite detectors alone.
