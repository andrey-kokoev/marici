# Generic rational cosets form an exact four-port Fourier orbit

## Support and character ports

Fix a denominator (q\geq2), and let indices be read modulo (q). Define the
shifted support comb

\[
P_r=\sum_{n\in\mathbb Z}\delta_{n+r/q}
\]

and the character-weighted integer comb

\[
C_r=\sum_{n\in\mathbb Z}e^{2\pi i rn/q}\delta_n.
\]

These are distinct types of port:

- (P_r) stores displacement in support;
- (C_r) stores displacement as label phase on fixed support.

With the standard Fourier convention, Poisson summation gives

\[
\mathcal FP_r=C_{-r},
\qquad
\mathcal FC_r=P_r.
\]

Thus Fourier transport exchanges position and amplitude information.

## The generic four-cycle

Starting with a shifted support port gives

\[
P_r
\longmapsto C_{-r}
\longmapsto P_{-r}
\longmapsto C_r
\longmapsto P_r.
\]

For a generic index (r\neq-r) modulo (q), these are four distinct
distributional states. The identity \(\mathcal F^2f(x)=f(-x)\) appears as the
middle reflection, and \(\mathcal F^4=1\) closes the orbit.

This is an exact mathematical realization of the four-rung coherence tower.
The four stages are not repeated presentations of one scalar object. They
retain support shift, dual character, reflected support, and conjugate
character separately.

The four Fourier eigenpackets on this orbit have eigenvalues

\[
1,quad i,quad-1,quad-i.
\]

For an eigenvalue \(\lambda^4=1\), one may write

\[
E_{r,\lambda}
=P_r+\lambda^{-1}C_{-r}
+\lambda^{-2}P_{-r}
+\lambda^{-3}C_r.
\]

These eigenpackets are source-complete only as four-port objects.

## Orbit degenerations

There are exactly two smaller cases.

For (r=0),

\[
P_0=C_0=\Delta_{\mathbb Z},
\]

so the orbit collapses to the one-port Fourier-fixed integer comb.

If (q) is even and (r=q/2), then (r=-r) modulo (q), but (P_r\neq C_r).
The orbit becomes the two-cycle

\[
P_{q/2}\longleftrightarrow C_{q/2}.
\]

Hence the possible minimal orbit sizes are one, two, and four. The generic
rational sector genuinely requires the fourth rung.

## Why scalar compression is dangerous

A scalar combination of the four ports can be a Fourier eigenvector, but the
compression erases which component carried support and which carried phase.
Positivity of the shifted quantization current belongs to the (P_r) port;
the (C_r) ports are generally complex or signed. Claiming positivity after
mixing them without retaining the orbit type would conflate constructibility
with coherence.

This also clarifies why a nonconstant periodic weight sequence was rejected
as a deformation of the integer comb. It is not invalid data. It is one port
of a larger rational-coset orbit.

## Relation to the multi-tower language

The orbit separates four comparisons:

1. input support displacement;
2. output amplitude character;
3. reflected input support;
4. conjugate output character.

The closing cell is the equality between the fourth Fourier transport and the
original support port. For generic (r), omitting any stage destroys closure.

The one-port integer source is therefore exceptional not because the theory
has only one tower, but because all four generic ports coincide at its fixed
point. What looked like one thing is a four-port orbit collapsed by exact
coherence.

## Consequence for the RH source

Within the finite rational-coset category, the scalar unit-weight integer comb
is the unique one-port object. Every nontrivial rational support or amplitude
deformation exposes at least one additional port before Mellin aggregation.

This strengthens canonical-source rigidity but still does not locate the
zeros of the canonical source. The next hostile family lies beyond finite
rational cosets: genuinely aperiodic Fourier quasicrystals or continuous
self-Fourier measures. Those must be tested without collapsing their support
and character modules.

## Operator stimulus

The operator repeatedly proposed a four-rung tower and later multiple coupled
towers. The rational-coset calculation shows why: Fourier transport has order
four, while its square is reflection. A generic source comparison therefore
needs four typed ports; the ordinary integer comb only appears one-port
because it sits at their common fixed point.
