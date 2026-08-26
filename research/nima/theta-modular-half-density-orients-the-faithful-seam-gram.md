# The modular half-density orients the faithful theta seam Gram

## Status

Algebraically exact candidate, subsequently narrowed by the gauge audit in
`theta-half-density-gauge-audit-forces-a-relative-modular-pairing.md`.
The weighted kernel has the stated covariance, but it is not yet an authorized
energy for the original source: a consistent basis change can cancel the
apparent modular factor contragrediently. The durable part of this packet is
the half-density covariance calculation; the live object is now a relative
comparison of independently typed additive and multiplicative sectors.

## The mismatch to repair

Let the unweighted full tail–seam atoms be \(u_n\), with logarithmic kernel

\[
K_0(n,m)
=
A\!\left(\left|\log\frac nm\right|\right).
\]

Prime multiplication preserves this kernel:

\[
K_0(pn,pm)=K_0(n,m).
\]

After Mellin multiplication by \(p^{-s}\), its quadratic energy therefore
scales only by

\[
p^{-2\operatorname{Re}s}.
\]

The missing factor is \(p\).

## Half-density renormalization

Define the modularly weighted atoms

\[
v_n=\sqrt n\,u_n.
\]

Their Gram kernel is

\[
K_{1/2}(n,m)
=
\sqrt{nm}\,
A\!\left(\left|\log\frac nm\right|\right).
\]

This remains positive definite because it is a diagonal congruence of
\(K_0\). At every finite cutoff,

\[
K_{1/2}=D K_0D,
\qquad
D=\operatorname{diag}(\sqrt n).
\]

Hence it has exactly the same rank and kernel as the faithful seam Gram.

Under simultaneous prime transport,

\[
K_{1/2}(pn,pm)=pK_{1/2}(n,m).
\]

Therefore the Mellin-weighted transport satisfies

\[
\left\|p^{-s}T_pv\right\|_{K_{1/2}}^2
=
p^{1-2\operatorname{Re}s}
\left\|v\right\|_{K_{1/2}}^2.
\]

This is precisely the oscillator orientation law, now on the faithful seam
state rather than on a vacuum-annihilating auxiliary block.

## Genesis from Haar measure

The weight \(\sqrt n\) is not an arbitrary diagonal repair if it arises from
the additive-to-logarithmic coordinate change. Put

\[
x=e^q,
\qquad
dx=e^q,dq.
\]

The unitary half-density transform is

\[
(\mathcal Wf)(q)=e^{q/2}f(e^q),
\]

because

\[
\int_0^\infty|f(x)|^2\,dx
=
\int_{-\infty}^{\infty}
\left|e^{q/2}f(e^q)\right|^2dq.
\]

At the arithmetic translate \(q=\log n\), the half-density is

\[
e^{q/2}=\sqrt n.
\]

Thus the missing transport factor \(p\) is the Radon–Nikodym derivative of
additive Haar measure under dilation, while the critical offset \(1/2\) is its
half-density exponent.

## Relation to the primitive current

Along a prime orbit \(n\mapsto p^kn\), the integrated metric factor is

\[
p^k=\exp(k\log p).
\]

Its infinitesimal logarithmic increment is

\[
\frac{d}{dk}\log p^k=\log p.
\]

Therefore Grothendieck's three appearances of \(\log p\) acquire one common
interpretation: they are the generator of the modular metric transported by
prime multiplication. The static primitive weight \(\log p\) cannot replace
the factor \(p\), but its exponential transport does produce it.

This also realizes the earlier size intuition: the relationship metric grows
exponentially in additive prime-step count and as a power law in the
multiplicative label.

## The exact source-typing gate

The construction is admissible only if the seam state before scalar Mellin
readout inherits the additive Haar half-density. This cannot be selected
afterward merely because it gives the desired exponent.

The finite source audit must distinguish:

\[
L^2(\mathbb R_+,dx)
\]

from

\[
L^2(\mathbb R_+,d^\times x),
\qquad
d^\times x=\frac{dx}{x}.
\]

In logarithmic coordinates, multiplicative Haar measure is \(dq\) and carries
no half-density factor. Additive Haar measure is \(e^q dq\) and does. Since
theta Poisson summation begins in additive Fourier analysis while Tate
aggregation uses multiplicative characters, their interface is the natural
place where the modular half-density could be forced.

If the already constructed tail–seam carrier is intrinsically a
multiplicative-Haar state with no additive-density incidence, inserting
\(\sqrt n\) is unauthorized and the proposal fails.

## No finite-port factorization

The half-density construction does not contradict the finite-jet obstruction.
It acts diagonally on the entire seam history:

\[
u_n\longmapsto\sqrt n\,u_n,
\]

and therefore preserves the cutoff-growing rank. It does not factor through
endpoint value and normal jump.

The candidate coupling is consequently not a finite-rank commutator. It is a
change of metric on the full boundary-history object induced by a change of
Haar measure.

## Minimal exact tests

At every finite label set, verify:

1. source derivation of the half-density map \(\mathcal W\);
2. the congruence \(K_{1/2}=DK_0D\);
3. the covariance \(T_p^*K_{1/2}T_p=pK_{1/2}\);
4. compatibility with the tail–seam bonding maps;
5. continuity of primitive, square, and archimedean boundary currents in the
   half-density topology;
6. appearance of the same metric in the doubled Green identity.

The first hostile is to keep the complete scalar functional equation and
replace the source carrier by multiplicative Haar measure throughout. Then
the half-density disappears and the energy scales by

\[
p^{-2\operatorname{Re}s},
\]

not by the critical-seam multiplier.

## Consequence for the physical model

The surviving physical analogy is a distributed lossless transmission system
whose boundary memory carries a modularly changing metric. Prime transport is
not merely motion of a state through a fixed Hilbert space; it transports the
state between fibers whose additive-Haar metrics differ by \(p\).

The two RH sectors may therefore be understood as the two sides of one
Haar-modular correspondence:

- additive Fourier/Poisson propagation supplies the physical norm;
- multiplicative Mellin/Tate propagation supplies the spectral character;
- the half-density comparison supplies the critical offset and orientation.

## Scope

This packet constructs a faithful finite-cutoff Gram with the exact critical
transport multiplier, conditional on source authorization of the additive
half-density. It does not prove that a scalar zero produces a nonzero state in
this Gram, prove completion continuity, account for every boundary current,
or prove RH.
