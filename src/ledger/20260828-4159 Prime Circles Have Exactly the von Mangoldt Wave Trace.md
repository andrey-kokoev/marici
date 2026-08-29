# Prime Circles Have Exactly the von Mangoldt Wave Trace

For every prime $p$, take the circle of circumference $\log p$ with periodic
translation generator $A_p=-i\,d/dx$. Poisson summation gives

$$
\operatorname{Tr}e^{-itA_p}
=(\log p)\sum_{k\in\mathbb Z}\delta(t-k\log p).
$$

The positive-time trace of the direct sum over primes is exactly

$$
\sum_{n\ge2}\Lambda(n)\delta(t-\log n).
$$

Thus prime powers are repeated primitive orbits, their weight remains
$\log p$, and non-prime-power composites are not primitive returns. The same
carrier produces the Euler factors as dynamical determinants and the
primitive/square/det3 filtration by repetition depth.

This is not yet the RH operator: its spectrum is the union of the elementary
circle frequencies. The remaining theorem is an adelic relative coupling
whose trace retains the prime returns while cancelling the local spectra and
leaving the completed global spectrum.

Research packet:
`research/grothendieck/prime-circles-have-exactly-the-von-mangoldt-wave-trace.md`.
