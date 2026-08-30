# Correction: polarized pole matching fixes a paired amplitude, not one amplitude field

Events 10270–10271 implicitly chose a reciprocal-even square root of the Euler
pole metric. That choice is natural but is not forced by pole matching alone.

Let \(c_P(a)\) and \(c_Q(b)\) be the two typed heat amplitudes. Along the seam
\(b=1-a\), residue matching requires only

\[
\frac{c_P(a)c_Q(1-a)}{\pi}
=
\frac{1}
{a(1-a)\zeta(1+a)\zeta(2-a)}.
\]

Define the positive central factor

\[
c_0(a)
=
\sqrt{
\frac{\pi}
{a(1-a)\zeta(1+a)\zeta(2-a)}
}.
\]

Then every positive factorization has the form

\[
c_P(a)=c_0(a)e^{\phi(a)},
\qquad
c_Q(1-a)=c_0(a)e^{-\phi(a)}
\]

for a real gauge function \(\phi\). If the source identifies the two typed
amplitudes by reciprocal reflection,

\[
c_Q(1-a)=c_P(a),
\]

then \(\phi=0\) and the even square root \(c_0\) is forced. Without that
identification, the pole determines only the product.

## Connection correction

The two connections are

\[
\omega_P=d\log c_0+d\phi,
\qquad
\omega_Q=d\log c_0-d\phi
\]

after reciprocal pullback to the same seam coordinate. Their sum is fixed:

\[
\omega_P+\omega_Q=2\,d\log c_0,
\]

but their difference

\[
\omega_P-\omega_Q=2\,d\phi
\]

is invisible to the polarized scalar residue.

Thus event 10271 remains correct conditionally:

- for the reciprocal-even square-root frame, the amplitude connection is
  exact, endpoint-regular, and uniformly bi-bounded;
- pole matching alone does not authorize that frame.

A gauge \(\phi\) can also destroy uniform completion control while preserving
the pole product. For example, a cutoff-dependent \(\phi_X\) with
\(\sup|\phi_X|\to\infty\) makes one typed amplitude large and the other small,
although every paired residue is unchanged.

## Finite Todd correction

The transported quarter-heat constant is likewise factorization-independent
only as a mixed pairing:

\[
-\frac{c_P(a)c_Q(1-a)}{12}
=
-\frac{\pi}
{12a(1-a)\zeta(1+a)\zeta(2-a)}.
\]

Therefore the finite scalar defect \(\Delta(a)\) from event 10270 is valid.
What was overstated was the uniqueness of the individual amplitude and its
connection.

The next source obligation is precise:

> Prove that reciprocal sewing identifies the primitive and square heat
> amplitude lines isometrically, thereby selecting the even square root; or
> retain the relative gauge \(\phi\) as an additional typed connection datum
> and prove it is uniformly bounded.

This correction prevents a scalar residue factorization from silently
becoming authority for two separate constructor arrows.
