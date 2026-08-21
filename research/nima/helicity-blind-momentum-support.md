# Helicity-blind momentum support preserves the Bell packet

## Source support

Sinha and Zahed formulate their qubits at fixed outgoing momenta. Their
amplitudes vary over Mandelstam kinematics, while the local measurement acts
on the two-dimensional helicity fiber at the selected momenta.

This defines a natural theoretical support class: restrict to a momentum point
or integrate over a positive momentum region with a weight that is independent
of analyzer setting and helicity outcome. On every helicity fiber, the support
operator is therefore scalar.

## Two-bin theorem

Take two momentum bins with nonnegative weights \(w_1,w_2\) and normalized
states

\[
|\psi_j\rangle
=
\frac{r_j|00\rangle+s_j|11\rangle}
{\sqrt{r_j^2+s_j^2}}.
\]

Mix their Born tables using the same \(w_j\) for all analyzer settings and
outcomes. The exact checker verifies all four normalizations and all eight
no-signalling identities. The Bell value is the convex mixture

\[
I=\frac{w_1I_1+w_2I_2}{w_1+w_2},
\]

and its Tsirelson slack factors as

\[
2\sqrt2-I
=
\frac{2\sqrt2}{w_1+w_2}
\sum_{j=1}^2
w_j\frac{(r_j-s_j)^2}{r_j^2+s_j^2}
\geq0.
\]

The same proof extends to any finite positive binning and, when integrable, to
a positive helicity-blind phase-space measure.

## Interpretation

Entry 1578's hostile filter acted inside the coefficient fiber and was
outcome dependent. The present support acts only on the momentum base and is
the identity on the helicity fiber. That base/fiber distinction is exactly
what makes normalization safe.

Thus the theoretical photon packet now has a legitimate supported readout:

\[
\boxed{
\text{positive momentum support}
\boxtimes
1_{\rm helicity}.
}
\]

This does not establish a loophole-free experimental Bell test. A real
detector must still prove that its acceptance approximates this factorized
support or satisfies the weaker state-specific marginal equations.

## Marici frontier

The next comparison is no longer abstract positivity. It is whether the
scattering Carrier's boundary/phase-space pushforward separates in the same
base/fiber way before normalization. If it does, the source Bell readout
descends through the admitted support calculus; if not, the precise mixed
support term is the obstruction.
