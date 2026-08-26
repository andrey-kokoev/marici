# Theta translation generator plus history Dirac has continuous, not Riemann, spectrum

## Bounded question

Does adjoining the canonical unbounded logarithmic translation generator turn
the bounded history Dirac into a Hilbert--Pólya operator?

## Natural generator

On the bilateral logarithmic carrier, let

\[
K=-i\partial_q
\]

with its standard self-adjoint domain. The history operators (H_+) and
(H_+^*) are translation-invariant convolutions, so they commute with (K).

Consider the source-derived candidate

\[
\mathcal L=K\otimes I_2+D_H.
\]

## Fourier diagonalization

Fourier transformation sends (K) to multiplication by \(\xi\) and sends the
history Dirac to

\[
D_H(\xi)=
\begin{pmatrix}
0&\overline{m(\xi)}\\
m(\xi)&0
\end{pmatrix}.
\]

Therefore \(\mathcal L\) is the decomposable multiplier

\[
\mathcal L(\xi)
=
\begin{pmatrix}
\xi&\overline{m(\xi)}\\
m(\xi)&\xi
\end{pmatrix},
\]

whose two spectral branches are

\[
\lambda_\pm(\xi)=\xi\pm|m(\xi)|.
\]

These branches vary continuously with \(\xi\) and are unbounded because of the
translation term.

## Spectral-type obstruction

The candidate has continuous essential spectrum. It does not have compact
resolvent and does not produce a discrete unbounded sequence that could be
identified directly with Riemann ordinates.

Thus the two canonical pieces supply complementary but insufficient data:

- (K) supplies unbounded spectral scale;
- (D_H) supplies source incidence and reciprocal adjointness;
- their translation-invariant sum supplies no confinement or quantization.

## Half-line warning

Restricting (K) to one half-line does not automatically fix the problem. The
momentum operator on a half-line has a boundary-domain obstruction to
self-adjoint translation dynamics, and the essential continuous spectrum is
not removed by a bounded history coupling.

Any boundary condition used to discretize the spectrum must be derived from
the completed theta/Tate source and reciprocal sewing, not chosen to fit the
zeros.

## Missing constructor

A viable Hilbert--Pólya operator now requires a source-derived
nontranslation-invariant term that confines logarithmic motion or produces a
compact-resolvent relative problem. Candidate origins include:

1. the archimedean theta potential;
2. reciprocal sewing at the modular origin;
3. a prime-labelled nonlocal boundary condition;
4. an adelic quotient that makes the translation orbit spectrally discrete.

The sharp acceptance test is compactness of the resolvent or an independently
derived discrete spectral measure before comparison with zero data.

## Scope

This packet proves that the canonical logarithmic translation generator coupled
to the full history Dirac has continuous essential spectrum. It does not rule
out a source-derived confining extension, construct one, or prove RH.
