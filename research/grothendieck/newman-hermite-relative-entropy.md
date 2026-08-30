# Hermite-normalized discriminant gives a finite Newman relative entropy

## Canonical Hermite reference

Let `h_N` be the monic probabilists' Hermite polynomial. Its roots are
centered and satisfy

`R_H^2=sum_i h_i^2=N(N-1)`.

Its discriminant is

`Delta_H=product_(k=1)^N k^k`.

Therefore its scale-normalized discriminant is the explicit number

`Delta_hat_H`

` =product_(k=1)^N k^k / [N(N-1)]^(N(N-1)/2)`.

## Extremal theorem

Among `N` distinct real configurations with fixed center and second moment,
the Hermite configuration uniquely maximizes the squared Vandermonde.

Indeed, an interior constrained critical point satisfies

`A_i=c r_i`.

The center constraint removes the translation multiplier, and multiplying by
`r_i` fixes `c=N(N-1)/(2R^2)`. After scaling, these are precisely the Hermite
electrostatic equations. The Vandermonde vanishes at collision boundaries;
the ordered chamber and fixed sphere give the global maximizer. Standard
strictness arguments give uniqueness up to ordering and reflection.

## Relative shape entropy

Define

`E_N=log(Delta_hat_H/Delta_hat)`.

Then `E_N>=0`, with equality exactly at the scaled Hermite configuration.
Under backward heat,

`dE_N/dlambda`

` =-4 sum_i [A_i-N(N-1)r_i/(2R^2)]^2 <=0`.

Thus the scale-normalized zero configuration relaxes monotonically toward
Hermite equilibrium in relative logarithmic-discriminant entropy.

## Infinite-rank renormalization proposal

For a symmetric window of `N` Newman/Xi zeros:

1. center and scale the window by its actual second moment;
2. compute `E_N` relative to the explicit Hermite reference above;
3. identify and subtract only any remaining Riemann--von Mangoldt density
   mismatch;
4. seek a finite limit or a local entropy density as `N` tends to infinity;
5. pass the nonnegative centered-repulsion dissipation to the limit.

This is substantially more canonical than subtracting an arbitrary continuum
energy: the reference is the unique equilibrium of the same finite Newman
flow after null modes are removed.

## Collision behavior

When any two roots collide, `Delta_hat` tends to zero and `E_N` tends to
positive infinity. Therefore the relative entropy is a barrier functional
for the real-simple-root chamber. Approaching the Newman threshold from the
real-rooted side should manifest as entropy blow-up in the colliding sector.

## Limitations

The finite extremal theorem does not prove convergence for Xi windows,
control edge effects, or determine the Newman constant. The infinite window
may require a local rather than total entropy because Xi density is
logarithmically nonuniform. Those are the next hostile tests.
