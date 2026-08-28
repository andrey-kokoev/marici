# Exchange modality classifies the residual boundary gauge

## Question

Does reciprocal exchange always reduce the normalization ambiguity of a dual
boundary pair to a sign?

## Claim boundary

No. The answer depends on whether the exchange is linear or antilinear. This
packet classifies the one-dimensional stabilizers. It does not determine which
modality theta/Tate sewing supplies.

## Paired-line gauge

Let \(L_+\) and \(L_-\) be complex lines with a nondegenerate bilinear pairing.
Every pairing-preserving diagonal automorphism has the form

\[
g_\lambda=(\lambda,\lambda^{-1}),
\qquad \lambda\in\mathbb C^\times.
\]

The scalar product therefore forgets a copy of \(\mathbb C^\times\).

## Linear exchange

Let \(E:L_+\to L_-\) be complex-linear and require \(g_\lambda\) to commute
with exchange. Then

\[
\lambda^{-1}=\lambda,
\]

so \(\lambda^2=1\). The residual stabilizer is \(\mu_2=\{1,-1\}\). A positive
or otherwise oriented augmentation selects one sign.

## Antilinear dagger exchange

Let \(J:L_+\to L_-\) be conjugate-linear. Commutation now requires

\[
\lambda^{-1}=\overline\lambda,
\]

equivalently \(|\lambda|=1\). The residual stabilizer is the full phase group
\(U(1)\), not merely a sign. A real positivity convention cannot fix this
phase by itself; the augmentation must be phase-sensitive or accompanied by a
source-derived real structure.

This is the typing correction to the preceding finite theorem. Product plus
linear exchange leaves two choices. Product plus dagger exchange leaves a
circle of choices.

## Mixed exchange

If the source supplies both a linear exchange \(E\) and an antilinear dagger
exchange \(J\) in compatible frames, their common stabilizer is

\[
\mu_2=\mathbb C^\times\cap U(1)\cap\{\lambda:\lambda^2=1\}.
\]

The composite \(J^{-1}E\) is then an antilinear real structure on one boundary
line. This structure is not decorative: it is precisely what collapses the
phase gauge to an orientation sign.

## Source-specific consequence

The theta/Tate programme must type three maps separately:

1. bilinear determinant pairing;
2. linear sheet exchange, if one exists;
3. antilinear reciprocal dagger exchange.

Calling both exchanges “reflection” erases the decisive distinction. If only
the dagger exchange is source-derived, a proposed endpoint normalization still
has a hostile \(U(1)\) phase family. If both are source-derived and compatible,
only a sign remains for an augmentation to select.

## Finite falsifier

Take any unit phase other than \(1\) or \(-1\), such as \(i\). It preserves the
pairing and commutes with antilinear dagger exchange, but fails linear exchange.
Therefore any argument that obtains a two-valued ambiguity from dagger exchange
alone is false.

## Disposition

The residual gauge is classified. The next source-level question is whether
theta/Tate sewing provides one exchange modality or two compatible modalities.
That question must be answered before an augmentation can be specified.

## Verification

`check_exchange_modality_residual_gauge.py` verifies the linear, antilinear,
and common stabilizers using exact Gaussian-rational arithmetic and an exact
rational parametrization of unit phases.
