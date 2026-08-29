# The Prime Fluctuation Is the Required Wave Trace, Not a Spectral-Shift Shortcut

## The canonical fluctuation measure

In logarithmic scale, define the signed arithmetic current

$$
d\nu(q)
=\sum_{n\ge2}\Lambda(n)\,\delta_{\log n}(dq)-e^q\,dq.
$$

Its Laplace transform is

$$
\int_0^\infty e^{-sq}\,d\nu(q)
=-\frac{\zeta'(s)}{\zeta(s)}-\frac1{s-1}
$$

for $\operatorname{Re}s>1$. The difference between this endpoint convention
and the integrated formula with $s/(s-1)$ is one explicit boundary constant.

Thus $d\nu$ is the precise primitive-plus-continuum current left after the
mean wall is removed.

## Why an abstract spectral-shift realization does not solve RH

The displayed transform is Laplace in the geometric variable $q$. A Krein
spectral-shift formula is Cauchy-resolvent in the spectral variable. Declaring
$\psi(e^q)-e^q$ to be a spectral-shift function silently changes transforms
and repeats the already closed exponential-versus-resolvent shortcut.

The transform must be implemented by a source-derived dynamics that explains
why logarithmic prime-power times become the time-domain trace of a fixed
operator.

## Logarithmic differentiation changes zeros into spectral-type poles

Let

$$
X(\lambda)=\xi\left(\frac12+i\lambda\right).
$$

Then

$$
\frac{d}{d\lambda}\log X(\lambda)
=i\frac{\xi'}{\xi}\left(\frac12+i\lambda\right).
$$

A zero of Xi becomes a pole of this logarithmic derivative with integer
residue. This is exactly the singularity type of a regularized resolvent trace
of a self-adjoint operator. With a consistent sign convention, the desired
identity is

$$
\frac{d}{d\lambda}\log X(\lambda)
=-\operatorname{Tr}_{\mathrm{reg}}(A-\lambda)^{-1}
+B(\lambda),
$$

where $B$ contains the source-derived gamma, endpoint, primitive, and square
counterterms.

If $A$ is fixed and self-adjoint, every resolvent pole lies on the real
$\lambda$ axis. The identity would therefore imply RH. Integrating it with a
source basepoint would recover the determinant section and remove the common
factor ambiguity.

## Time-domain form

The resolvent is the half-Fourier transform of the unitary evolution
$e^{-itA}$. Therefore the same theorem can be stated as a trace formula:

> The completed prime-power fluctuation current is the regularized wave trace
> of one source-derived self-adjoint generator.

This is the Riemann analogue of the periodic-orbit versus spectrum relation in
a Selberg trace formula:

- prime powers are the source-labelled return events;
- logarithms of primes are their orbit lengths;
- the archimedean term is the continuum/background trace;
- Riemann zeros are the spectral poles.

The analogy becomes a proof mechanism only after the operator and trace
formula are constructed independently from theta/Tate data.

## Exact next target

Construct a boundary-bearing unitary evolution $U(t)$ from the completed
adelic source such that its regularized trace distribution is

$$
\operatorname{Tr}_{\mathrm{reg}}U(t)
=\sum_{n\ge2}\Lambda(n)\delta(t-\log n)
-e^t
+\text{reciprocal and archimedean terms}.
$$

The construction must pass these gates:

1. $U(t)=e^{-itA}$ for a fixed self-adjoint $A$;
2. the prime-power coefficients arise from the positive Fock/connected source
   grammar, not from the explicit formula read backward;
3. primitive and square boundary currents are retained separately;
4. the trace is defined in the correct rigged or relative class;
5. Fourier--Tate sewing derives the reciprocal and gamma terms;
6. logarithmic integration reproduces framed Xi up to a source-fixed constant;
7. a hostile divisor multiplier fails to lift to the same evolution before
   its zeros are examined.

This target is stronger than a prime-counting estimate and more explanatory:
it would derive zero confinement from unitary dynamics rather than encode it
as analytic regularity.

## Honest boundary

No such evolution has yet been constructed. The prime current supplies the
required wave-trace distribution, but inverse-building an operator from that
distribution would be circular. The next discovery must identify the
constructor in the adelic theta machinery whose return trace already carries
the von Mangoldt events.
