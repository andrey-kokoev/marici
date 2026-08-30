# The Newman Threshold Has a Cubic Local Collision Model but May Be Set at Infinity

## Source deformation

Use the standard de Bruijn--Newman family

\[
H_\lambda(x)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(xu)\,du,
\qquad
\partial_\lambda H_\lambda=-\partial_x^2H_\lambda.
\]

There is a finite constant \(\Lambda\) such that every zero of
\(H_\lambda\) is real exactly when \(\lambda\geq\Lambda\). The Riemann
hypothesis is equivalent to \(\Lambda\leq0\), while the theorem of Rodgers
and Tao gives \(\Lambda\geq0\). Consequently, if RH is true, then
\(\Lambda=0\): the physical source is exactly at the last permitted heat
time, not safely inside the real-zero phase.

This gives a mathematically precise version of the operator's “last-moment
split” intuition, but only after separating a local collision from a possible
obstruction at spectral infinity.

## Universal finite collision

Choose a local coordinate \(w\) in which the critical line is the real axis.
Near a generic collision of two line zeros, the derivative readout has the
versal normal form

\[
X_\tau(w)=w^2-\tau.
\]

Its source potential is

\[
Y_\tau(w)=\frac{w^3}{3}-\tau w,
\qquad
\partial_wY_\tau=X_\tau.
\]

The discriminant is \(4\tau\). Hence:

- for \(\tau>0\), two simple boundary folds lie on the seam;
- for \(\tau=0\), they collide into one cubic critical event;
- for \(\tau<0\), they leave the seam as a conjugate pair of interior branch
  points.

The earlier quadratic fold is therefore one stable side of a cubic
catastrophe. At collision, the potential changes from a two-sheet fold to a
three-jet singularity. This is the missing geometric meaning of a multiple
zero under the heat deformation.

## What the reduction explains

The critical line is fixed before the zeros, by reciprocal Fourier--Tate
sewing. The Newman deformation then asks whether the branch divisor can cross
that fixed interface. A finite crossing cannot occur continuously through an
ordinary simple fold. It must pass through the cubic collision above.

Thus the local forbidden construction is explicit:

1. bring two seam folds together;
2. annihilate their separation discriminant;
3. reverse the discriminant sign;
4. emit an off-seam conjugate pair.

The squared Vandermonde from the earlier Newman calculation is exactly the
many-zero extension of this local discriminant. Its backward-heat derivative
is a sum of squares while all zeros remain real and simple. That law describes
repulsion inside the real phase; the cubic normal form describes its boundary.

## The real obstruction: collision at infinity

This does not yet reduce RH to excluding one finite cubic event. Even if every
finite-height zero at \(\lambda=\Lambda\) is simple, there need not be a
uniform neighbourhood below \(\Lambda\) in which all infinitely many zeros
remain real. The first failures may occur at heights tending to infinity.

Equivalently, local structural stability at each zero does not imply uniform
structural stability of the complete divisor. The Newman threshold can be an
accumulation of cubic collisions escaping to spectral infinity rather than a
single collision visible in a compact window.

This is the exact place where the proposed relative index budget must do more
than local singularity theory. It must control the infinity current strongly
enough that branch charge cannot enter from arbitrarily high spectral height.

## Sharpened Deutsch--Popper target

The next conjecture is:

> For the completed theta source, every sign change of the seam-fold
> discriminant is accounted for by a source-derived relative index current;
> the current has no incoming flux from spectral infinity at physical heat
> time zero.

This has two independent falsifiers:

1. a finite theta-compatible cubic collision that emits an off-seam pair;
2. a sequence of collision heights tending to infinity whose renormalized
   index flux remains nonzero.

The second is now the load-bearing test. The local cubic geometry explains how
zeros can leave the line. Only a global no-incoming-flux theorem can explain
why they do not arrive from infinity.

## Exact finite check

The checker verifies the derivative relation, double-critical condition,
discriminant, and the two sides of the seam/off-seam transition for the
universal unfolding. It does not test the theta source or the infinity flux.

