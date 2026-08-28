# The anti-diagonal Hardy residual is the minimal divisor observer

## Sectorwise normalization

Let `F_+` and `F_-` be the normalized completed sections in the right and
left half-planes. Assume the standard bounded-type hypotheses needed for
sectorwise canonical factorization, and remove the declared nowhere-zero
carrier units before forming the factors.

On a seam interval avoiding boundary zeros, define the oriented phase
residual in each sector by

\[
\kappa_\pm(t)
=
\partial_t\arg F_\pm(it)
-
\mathcal H_\pm\!\left(\partial_t\log|F_\pm(it)|\right).
\]

The Hilbert-transform sign is fixed by the orientation of the corresponding
half-plane. This subtraction removes the outer phase predicted by the
boundary magnitude. What remains is the inner-factor current, together with
any separately declared singular-inner boundary measure.

## Reciprocal decomposition

Fourier--Tate reflection identifies the two boundary magnitudes and reverses
the sector orientation. Consequently the Blaschke parts obey

\[
\kappa_-(t)=-\kappa_+(t)
\]

when both are written in one common seam coordinate. Therefore

\[
\kappa_{\mathrm{diag}}
=
\kappa_++\kappa_-=0,
\qquad
\kappa_{\mathrm{rel}}
=
\kappa_+-\kappa_-=2\kappa_+.
\]

The scalar reciprocal channel is automatically blind. The anti-diagonal
channel is exactly the complete sectorwise Blaschke current.

For a right-sector zero `w=a+ib`, with `a>0`, its contribution is

\[
\kappa_{\mathrm{rel},w}(t)
=
-\frac{4a}{a^2+(t-b)^2}
\]

under the right-sector orientation convention. Its integral is `-4 pi`, or
twice the oriented multiplicity unit. A conjugate zero adds the conjugate
Poisson kernel.

## Gauge invariance

Multiplication by a declared cutoff anomaly transition changes the phase by
the boundary value of an exact logarithmic derivative. Such transitions are
global nowhere-zero exponentials and have zero loop residue. Hence they can
change the representative of `kappa_rel`, but not its integral divisor class.

Let `P` denote the space of sectorwise phase currents and `A_exact` the
subspace of exact anomaly-frame currents. The natural target is therefore
the relative current space

\[
[\kappa_{\mathrm{rel}}]
\in
\mathcal P/\mathcal A_{\mathrm{exact}}.
\]

This quotient is the smallest observer that is simultaneously:

- insensitive to legal cutoff-frame changes;
- sensitive to a reciprocal off-seam Blaschke packet;
- invisible in the reciprocal codiagonal;
- computable from the two boundary quadratures and the source magnitude
  control, without locating interior zeros first.

## Hostile multiplier response

Multiplying by a reciprocal/conjugate Blaschke packet preserves boundary
magnitude and scalar reciprocal symmetry. It adds its Poisson-kernel packet
to `kappa_rel`. Because that packet has nonzero integral residue, no exact
anomaly-frame current can remove it.

Thus the observer distinguishes the actual source section from the hostile
packet at the boundary, before any interior zero search.

## Remaining theorem

The RH-bearing target is now a source statement rather than an observer
design problem:

\[
[\kappa_{\mathrm{rel}}]=0
\]

in both open sectors, with the singular-inner contribution separately shown
absent. Calling this class zero from canonical factorization alone would just
rename RH. The required explanation must derive the vanishing from labelled
theta/Poisson transport and its boundary conditions.

## Scope

This result constructs and types the minimal phase observer conditionally on
the usual sectorwise bounded-type factorization. It does not establish those
analytic hypotheses for every chosen normalization, eliminate a possible
singular-inner measure, prove the relative class vanishes, or prove RH.
