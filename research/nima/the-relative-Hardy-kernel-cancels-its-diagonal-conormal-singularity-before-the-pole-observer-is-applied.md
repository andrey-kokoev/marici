# The relative Hardy kernel cancels its diagonal conormal singularity before the pole observer is applied

## Question

Does the kernel of `Q^T-Q^0` pass the diagonal wavefront transversality test?

## Projection formula

After removal of the common translation, the two projections are

\[
Q^T=M_\gamma\Pi M_\gamma^*,
\qquad
Q^0=\Pi,
\]

where `Pi` is the Hardy projection and the Tate scattering multiplier `gamma`
is smooth and unimodular on the regular boundary line. Hence

\[
K_{Q^T-Q^0}(s,t)
=
\bigl(\gamma(s)\overline{\gamma(t)}-1\bigr)K_\Pi(s,t).
\]

The Hardy kernel has a diagonal delta/principal-value singularity. Unimodularity
gives

\[
\gamma(t)\overline{\gamma(t)}-1=0.
\]

Therefore the delta contribution vanishes. Moreover,

\[
\gamma(s)\overline{\gamma(t)}-1
=(s-t)b(s,t)
\]

with smooth `b` locally, so multiplication cancels the principal-value factor
`pv(1/(s-t))`. The relative kernel consequently has a smooth diagonal
restriction. Its diagonal value is proportional, with the fixed Hardy
orientation convention, to

\[
\partial_s\log\gamma(s),
\]

which is the symbol already appearing in the local Tate boundary formula.

## Pole observer consequence

For one rapid multiplier and one physical-line principal-value multiplier, the
relative kernel has no surviving conormal diagonal component. The wavefront
obstruction identified previously is absent locally away from poles of the
scattering multiplier itself. Thus the diagonal pullback of

\[
\overline{m_\Phi(s)}K_{Q^T-Q^0}(s,t)m_g(t)
\]

is defined distributionally and yields the Sokhotski wall/jump readout.

## Scope boundary

This proves local diagonal regularity. It does not by itself establish:

- global decay of the pulled-back kernel;
- summability over characters and conductors;
- continuity in the full retained graph topology;
- equality with the independent pair-state Green energy.

The rapid forcing multiplier supplies a plausible global test factor, but its
bounds must still be combined with the known logarithmic-derivative estimates.

## Disposition

The first operator-level microlocal gate passes: relative Tate/reference
subtraction removes the Hardy diagonal singularity before the pole observer is
applied. The next executable gate is global continuity and character/conductor
summability of this polarized distributional trace.