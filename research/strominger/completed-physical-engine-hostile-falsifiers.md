# Twelve hostile falsifiers delimit the completed physical engine theorem

The theorem is accepted only in the source category actually derived. Each
test below gives a nearby construction that would make a broader claim false.

1. **Coordinate Green representative.** Replacing `S log S` by
   `S log|z-xi|^2` produces the spurious transition ratio `xi^2/z^2`.
2. **One-chart determinant.** The jet transition determinant vanishes at
   `xi=0`, which is outside that chart overlap; the second chart is regular.
3. **Finite Laurent cutoff.** Dropping the coherent remainder changes the
   grade-three response at every cutoff.
4. **One parity port.** Either `E` or `M` alone has a complementary eigenspace
   kernel; the paired port is faithful.
5. **Periods instead of local ports.** `dz/(z-xi)^2` is locally nonzero but
   exact and has zero period.
6. **One contour.** A single period aliases residue packets whenever
   `dim H1>1`.
7. **Untyped antipodal sum.** Mapping `(h+,h-)` to `h++h-` has an
   anti-diagonal kernel; restriction to the graph of the true adapter does not.
8. **Exact collision.** Two coincident labels map to their sum and lose their
   difference.
9. **Insufficient collision moments.** `L+1<n` leaves a Vandermonde kernel;
   moments through `n-1` restore distinct tangent labels.
10. **Special charge fixture.** Four distinct celestial directions can still
    have rank-three momentum columns; genericity must be checked.
11. **Characteristic enlargement.** Smooth functions of `x+y` are killed by
    `partial_x^4-partial_y^4`, although no finite point-supported polynomial
    jet is.
12. **Zero-mode omission.** Green inversion without the constant subtraction,
    or spin reconstruction without the `l<=1` quotient, is not invertible.

## Surviving theorem boundary

After these attacks, the strongest supported statement is:

- source construction and two-chart transport are faithful;
- the magnetic projection loses exactly the electric sector;
- grade-three transport is injective on every finite magnetic point jet;
- distinct supports add no kernel;
- collisions lose exactly the deficient moment coordinates;
- local-to-period passage loses exact forms and higher distribution jets;
- complete periods are faithful on punctured-sphere cohomology;
- conservation restricts admissible sources and antipodal matching is an
  invertible graph condition.

No assertion is made for arbitrary smooth characteristic solutions,
infinite-order point distributions, fractional covers, or independently
chosen Laurent coefficient products.

## Evidence

`checkers/completed_physical_engine_hostile_falsifiers.py` realizes all twelve
countermodels symbolically and verifies the stated repair in each case.
