# Theta history adjoint is causal reflection, not one Fourier quarter-turn

## Bounded question

Does Fourier--Tate sewing turn the full seam-history synthesis into its Hilbert
adjoint?

## Bilateral history operator

On the bilateral logarithmic carrier, define the anti-causal history synthesis

\[
(H_+c)(t)=\int_0^\infty\Phi(r)c(t+r)\,dr.
\]

For real \(\Phi\in L^1\), its Hilbert adjoint is the causal operator

\[
(H_+^*g)(q)=\int_0^\infty\Phi(r)g(q-r)\,dr.
\]

Both maps retain a full history port and have matching infinite rank.

## Fourier action

With Fourier convention

\[
\widehat c(\xi)=\int_{\mathbb R}c(t)e^{-i\xi t}\,dt,
\]

the anti-causal synthesis has multiplier

\[
m_+(\xi)=\int_0^\infty\Phi(r)e^{i\xi r}\,dr,
\]

while its adjoint has multiplier

\[
m_-(\xi)=\overline{m_+(\xi)}.
\]

Consequently one Fourier transform diagonalizes (H_+):

\[
\mathcal F H_+\mathcal F^{-1}=M_{m_+}.
\]

It does not produce (H_+^*). Fourier self-duality of the source does not
change this operator typing.

## Causal reflection

Let

\[
(Rc)(t)=c(-t).
\]

Direct substitution gives

\[
RH_+R=H_+^*.
\]

With the standard Fourier convention, (R=\mathcal F^2\). Thus the history
adjoint is produced by a Fourier half-turn, not by one metaplectic quarter-turn.

This distinguishes two source operations:

- one Fourier turn changes to the spectral presentation;
- valuation reflection reverses causal variance and produces the adjoint.

## Half-line sectors

Compression to one half-line gives

\[
H_{+,0}=P_+H_+P_+.
\]

Reflection transports it to the opposite sector:

\[
RH_{+,0}R=P_-H_+^*P_-.
\]

Therefore adjoint completion is naturally anti-diagonal between the two
valuation sectors. It is not a role-preserving diagonal pairing. Because both
ports are full histories, their ranks match at every cutoff and after
completion.

## What this repairs

Nima's triangular-block obstruction applies to reflected forward forcings with
rank-one scalar ports. It does not apply to the full history pair

\[
H_+:mathcal H_{\mathrm{history},+}	o\mathcal H_{\mathrm{tail},+},
\qquad
H_+^*:\mathcal H_{\mathrm{tail},-}	o\mathcal H_{\mathrm{history},-}.
\]

Here reciprocal reflection genuinely reverses variance and supplies the
required adjoint incidence.

## Remaining Schur gate

Adjoint incidence alone still does not preserve the scalar Evans divisor. The
completed block system needs a source-derived diagonal history operator whose
Schur complement agrees with the endpoint Mellin determinant. Packet 234's
Schur--Evans test remains mandatory.

The next finite calculation is therefore the block determinant built from
(H_+), (H_+^*), and the independently derived history diagonal—not another
attempt to identify a Fourier multiplier with a causal adjoint.

## Scope

This packet proves the exact conjugation law for full seam-history synthesis.
It identifies causal reflection, equivalently a Fourier half-turn, as the
source operation producing the adjoint. It does not derive the diagonal history
block, prove Schur--Evans agreement, or prove RH.
