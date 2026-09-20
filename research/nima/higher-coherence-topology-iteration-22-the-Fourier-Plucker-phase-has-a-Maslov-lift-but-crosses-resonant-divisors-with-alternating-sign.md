# Higher-coherence topology iteration 22: the Fourier Plücker phase has a Maslov lift, but crosses resonant divisors with alternating sign

## Candidate topology

Retain the determinant-line phase of each Fourier minor rather than replacing
it by its squared norm. For

\[
\Delta_F
=e^{-i(\xi_1q_1+\xi_2q_2)}
-e^{-i(\xi_2q_1+\xi_1q_2)},
\]

put

\[
\theta=(\xi_2-\xi_1)(q_2-q_1),
\qquad
m=\frac{(\xi_1+\xi_2)(q_1+q_2)}2.
\]

Then

\[
\boxed{
\Delta_F=-2i\,e^{-im}\sin(\theta/2).
}
\]

Away from its zero set, the Plücker line therefore carries a continuous phase
lift together with the sign chamber of `sin(theta/2)`.

## Maslov divisor

The resonant set is

\[
\theta\in2\pi\mathbb Z.
\]

Crossing it changes the sign chamber and contributes a Maslov/spectral-flow
increment. This topology retains the orientation information lost by the
Hermitian square.

## Crossing-sign audit

The derivative transverse to the `k`th resonance has sign

\[
\frac{d}{d\theta}\sin(\theta/2)
\bigg|_{\theta=2\pi k}
=\frac12(-1)^k.
\]

Hence successive crossings alternate orientation. The signed Maslov count may
cancel even when the unsigned number of resonances grows. No one-sign crossing
theorem is available for the unrestricted Fourier rectangles.

Thus the phase lift records the failure exactly but does not restore variation
diminution.

## Higher-cone interpretation

Repeated cone attachments can be organized as paths in the Plücker line bundle.
Their obstruction is then a winding or Maslov class rather than loss of norm.
But a null total winding does not imply that the path avoided the divisor: it
may have equal forward and backward crossings.

To turn Maslov coherence into noncollision, one needs either:

- a source-derived monotone phase;
- one-sign crossing forms;
- or a chamber contraction avoiding the divisor at every intermediate stage.

Each is additional order data.

## Comparison with Xi counting

The argument principle counts zeros with nonnegative multiplicity, whereas a
Maslov index is signed. Identifying them requires proof that every regular
crossing has the same orientation, or a theorem comparing absolute
intersection multiplicity with the chosen phase lift. The Fourier minor model
provides an explicit alternating-sign hostile.

## Completion

Dense spectral sampling meets or approaches infinitely many resonance
hypersurfaces. A global continuous phase lift cannot cross their zeros. One
must work on the complement with chamber data and clutching maps; completion
cannot collapse those maps without forgetting the divisor.

## Verdict for topology 22

Phase-lifted/Maslov topology preserves the Fourier orientation that Hermitian
pairing lost. Its explicit crossing forms alternate sign, so winding coherence
cannot enforce ordered signature or divisor avoidance.

The next nonredundant topology to test is a real-oriented blow-up or chamber
topology of the resonant divisor, retaining approach direction at every
crossing instead of trying to extend one phase through it.