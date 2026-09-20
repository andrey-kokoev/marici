# Higher-coherence topology iteration 44: a strict horizontal Köthe codiagonal would exclude Xi torsion by differentiating the divisor equation

## Candidate topology

Equip the analytic Köthe modules with a connection in the spectral direction.
For the labelled synthesis

\[
C(f)(z)=\sum_\lambda f_\lambda(z)e^{-zL_\lambda},
\]

differentiation obeys

\[
\partial_z C(f)
=C\bigl((\partial_z-L_\lambda)f_\lambda\bigr).
\]

Multiplication by `L_lambda` is continuous with an arbitrarily small loss of
exponential Köthe order. Thus the labelled source has a natural continuous
connection and `C` is horizontal.

If the common-history module carries the matching connection, the cokernel

\[
Q=\operatorname{coker}C
\]

inherits one.

## Why a connection attacks torsion

Let `u` be a local coordinate at a Xi zero and suppose

\[
u^m q=0
\]

in `Q`. Applying the connection gives

\[
m u^{m-1}q+u^m\nabla q=0.
\]

For coherent modules over a smooth characteristic-zero curve, a module with
connection is locally free. In particular it has no divisor torsion. Hence a
coherent horizontal cokernel would make

\[
\operatorname{Tor}_1^O(Q,O/(\tau))=0.
\]

This would turn the bordered identity into coordinatewise Xi-divisibility and
would close the confinement step.

## Infinite-dimensional qualification

The present Köthe cokernel is not known to be coherent or finite rank. In a
locally convex module, differentiating the torsion equation only forces the
class into successively deeper powers of `u`. To conclude `q=0`, one needs:

1. a continuous quotient connection on `Q`;
2. `u`-adic separatedness of `Q`;
3. strict/closed image of `C` in the connection topology;
4. compatibility of the connection with the bordered Green domain.

Without separatedness, an infinitely divisible nonzero class may survive.
Without strictness, differentiation may leave the source-generated quotient.

## Application to the bordered factor

From

\[
C(R)=\tau H_{\rm border}
\]

we have `q=[H_border]` with `tau q=0`. If `Q` has the strict horizontal
properties above, repeated covariant differentiation forces `q` into every
power of the local parameter. Separatedness then gives `q=0`, so

\[
H_{\rm border}=C(S),
\qquad
R=\tau S.
\]

This is the first topology in the sequence that offers a structural route to
the exact missing lift rather than merely restating it.

## Flatness and monodromy

On a one-dimensional spectral domain every holomorphic connection is locally
integrable, but global horizontal lifting may have monodromy. The confinement
argument is local at each Xi zero, so local flatness suffices. Singular or
meromorphic connection terms at the Xi divisor would invalidate the torsion-
free argument and must be excluded.

## Source audit still required

The formal spectral derivative exists on labelled theta coefficients. It is
not yet proved that:

- the complete bordered target is stable under the same derivative;
- Green closure and endpoint traces share one invariant domain;
- the codiagonal image is strict in the connection-enhanced Köthe topology;
- the quotient is adically separated.

These are concrete analytic questions, not a request for another arbitrary
higher cell.

## Verdict for topology 44

Crystalline/connection topology supplies a plausible noncircular mechanism:
a strict, adically separated horizontal cokernel cannot support the Xi-torsion
class detected in iteration 42. If these properties hold, `H_border` lifts and
the labelled Haar residual is Xi-divisible.

The next nonredundant topology to test is a D-module topology, where coherence,
strictness, and absence of divisor-supported submodules can be formulated as
standard characteristic-support conditions.