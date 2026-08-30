# Holomorphic Tate sewing rotates modular slope into seam phase velocity

Event 10275 separated the positive Tate modulus from the reciprocal unitary
phase. The full holomorphic local coefficient reconnects them.

Define

\[
\chi_\infty(s)
=
\pi^{s-\frac12}
\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\]

It satisfies

\[
\chi_\infty(s)\chi_\infty(1-s)=1.
\]

On the real interval \(s=a\in(0,1)\), this coefficient is positive and equals
the modulus candidate \(s_\infty(a)\). On the critical seam

\[
s=\frac12+it,
\]

reciprocity and complex conjugation give

\[
|\chi_\infty(1/2+it)|=1.
\]

Hence the same holomorphic constructor is modular in the transverse real
direction and unitary in the vertical seam direction.

Its logarithmic derivative is

\[
L'(s)
=
\frac{d}{ds}\log\chi_\infty(s)
=
\log\pi
-\frac12\psi((1-s)/2)
-\frac12\psi(s/2).
\]

At \(s=1/2\),

\[
L'(1/2)
=
\log\pi-\psi(1/4)
=
\log\pi+\gamma+\frac{\pi}{2}+3\log2.
\]

Along the real direction this is the modular slope:

\[
\left.
\frac{d}{da}\log|\chi_\infty(a)|
\right|_{a=1/2}
=
L'(1/2).
\]

Along the vertical seam direction,

\[
\left.
\frac{d}{dt}\log\chi_\infty(1/2+it)
\right|_{t=0}
=
iL'(1/2).
\]

Therefore the phase velocity is exactly

\[
\left.
\frac{d}{dt}\arg\chi_\infty(1/2+it)
\right|_{t=0}
=
\log\pi+\gamma+\frac{\pi}{2}+3\log2.
\]

This is the Cauchy–Riemann rotation of the real modular derivative into the
unitary seam derivative.

## Constructor consequence

The gamma modulus and gamma phase must not be constructed as unrelated ports.
They are boundary restrictions of one holomorphic Tate sewing coefficient.
A source theorem that establishes holomorphic sewing automatically supplies:

1. reciprocal modular scaling off the seam;
2. unitary phase transport on the seam;
3. the exact equality between transverse metric slope and vertical phase
   velocity.

This gives the first precise candidate linking identity for the odd port:

\[
J_{\mathrm{odd},\infty}
\stackrel{?}{=}
\partial_t\arg\chi_\infty(1/2+it),
\]

with the central normalization fixed by the displayed constant.

The remaining authority test is whether the causal-history/Wronskian odd
current represents this logarithmic phase derivative in the declared source
frame. Equality of scalar values at \(t=0\) is insufficient; the theorem must
intertwine the complete \(t\)-dependent phase family.

The sharp hostile uses the correct real modulus
\(|\chi_\infty(a)|\) but replaces the seam phase by its inverse. It violates
holomorphic continuation and the Cauchy–Riemann linking law even though each
real-axis metric test passes.
