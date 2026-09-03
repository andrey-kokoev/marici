# One positive spline can scale only through its full translate Gram kernel

## Question

Can the certified positive preconditioned spline be promoted into a positivity constructor rather than remain one test value?

## Translation-cyclic reduction

Let `q` be the source-side Weil form on logarithmic test functions and choose one compact smooth packet `f`. For real `a`, write

`f_a(x)=f(x-a)`.

For a finite combination

`g=sum_j c_j f_(a_j)`,

positivity is equivalent to positivity of the translate Gram matrices

`G_(i,j)=q(f_(a_i),f_(a_j))`.

If the Weil form is translation invariant in the centered logarithmic convention, then

`G_(i,j)=k_f(a_i-a_j)`

for one scalar Hermitian kernel `k_f`. Positivity on every finite translate combination is exactly positive definiteness of `k_f`.

If the ordinary Fourier transform of `f` is nonzero almost everywhere, Wiener cyclicity makes the closed translation span of `f` dense in `L^2`. With the required form-core control, nonnegativity of every translate Gram matrix would then imply nonnegativity of the full closed Weil form.

## Why the existing spline certificate is insufficient

The repaired checker proves only

`k_f(0)=q(f,f)>0`.

A positive diagonal value does not imply that `k_f` is positive definite. The first hostile is the two-translate determinant

`k_f(0)^2-|k_f(a)|^2`.

A negative value supplies an explicit negative combination of two authorized compact packets. Higher Toeplitz Gram minors test additional directions.

## Source-side implementation

The existing spline machinery already contains exact prime-power enumeration, archimedean series bounds, endpoint constants, and deliberate sign failures for one diagonal value. Its reusable extension is polarization:

1. derive `q(f_a,f_b)` in the same explicit-formula convention;
2. certify `k_f(a)` on rational translation grids;
3. test Gram eigenvalue intervals, not only diagonal energies;
4. verify the centered convention really makes the form translation invariant;
5. prove `fhat` is nonzero almost everywhere and that its translates form a form core.

## Limitation

This reduction does not make positivity easier automatically. In a Fourier-multiplier realization,

`k_f(a)=integral e^(iua) w(u)|fhat(u)|^2 du`,

so Bochner positivity of `k_f` is equivalent to positivity of the weighted spectral distribution seen by the cyclic packet. If `fhat` is cyclic, this is essentially the original Weil positivity problem.

Its value is operational: it turns the gap between one positive instance and global positivity into explicit finite Gram falsifiers and reuses the strongest existing certified checker.

## Disposition

The spline result should not be generalized by sampling more unrelated positive diagonals. The only coherent promotion route is the full translate Gram kernel plus cyclicity. The next cheap test is the certified two-translate determinant over a bounded rational grid, after the source normalization map is supplied.
