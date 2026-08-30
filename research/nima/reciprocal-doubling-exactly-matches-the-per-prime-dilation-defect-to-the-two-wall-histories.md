# Reciprocal doubling exactly matches the per-prime dilation defect to the two wall histories

Event 10301 showed that an undoubled global wall cannot absorb the
prime-indexed attenuation bath. Retaining both prime labels and reciprocal
sectors removes the rank mismatch locally.

For one prime, the attenuation

\[
a_p=p^{-1/2}
\]

has one defect line

\[
\mathcal D_p
=
\operatorname{Ran}\sqrt{1-a_p^2}.
\]

The source cut colligation requires reciprocal doubling, so the actual local
passive object has defect carrier

\[
\mathcal D_p^+\oplus\mathcal D_p^-.
\]

Its rank is two.

The correctly typed primitive history target also has two lines:

\[
\mathcal H_{p,-}\oplus\mathcal H_{p,+},
\]

corresponding to the twisted resolvents of
\(\partial_u-\frac12\) and \(\partial_u+\frac12\). Reciprocal reflection
exchanges these histories.

Thus, prime by prime,

\[
\dim(\mathcal D_p^+\oplus\mathcal D_p^-)
=
\dim(\mathcal H_{p,-}\oplus\mathcal H_{p,+})
=
2.
\]

The rank obstruction disappears exactly when both label retention and
reciprocal doubling are enforced.

## Local sewing type

The first possible source sewing is therefore not a global rank-two map. It is

\[
J_p:
\mathcal D_p^+\oplus\mathcal D_p^-
\longrightarrow
\mathcal H_{p,-}\oplus\mathcal H_{p,+}.
\]

Let \(R_D\) and \(R_H\) be the reciprocal exchanges. Source covariance
requires

\[
J_pR_D=R_HJ_p.
\]

In the exchange basis, every such map has the form

\[
J_p=
\begin{pmatrix}
\alpha_p&\beta_p\\
\beta_p&\alpha_p
\end{pmatrix}.
\]

In the even/odd parity basis it becomes diagonal:

\[
J_p^{\mathrm{par}}
=
\begin{pmatrix}
j_{p,+}&0\\
0&j_{p,-}
\end{pmatrix},
\qquad
j_{p,\pm}=\alpha_p\pm\beta_p.
\]

This is exactly the two-channel incidence structure previously derived for
the causal-history Schur cell.

## Metric gate

The attenuation defect metric has scale

\[
1-a_p^2=1-p^{-1}.
\]

The history side carries the transported Mellin half-density metric. A
source-isometric sewing must satisfy

\[
J_p^*G_{H,p}J_p
=
G_{D,p}.
\]

This fixes the magnitudes of \(j_{p,+}\) and \(j_{p,-}\) once both source
metrics are frozen. It does not fix their relative sign or phase; that
orientation must come from the causal/anti-causal Green identity.

Hence rank and metric compatibility reduce the local freedom but do not
source-authorize \(J_p\).

## Direct-sum assembly

If every \(J_p\) exists and preserves the prime idempotent, then

\[
J=\bigoplus_pJ_p
\]

maps the reciprocal valuation defect bundle into the prime-labelled
primitive history bundle with no dark cross-prime direction.

Only after this direct sum is constructed may a separate synthesis aggregate
the labelled wall histories.

## Smallest hostile

Choose \(j_{p,+}\ne0\) and \(j_{p,-}=0\). Rank matching, reflection
equivariance, the even scalar primitive trace, and one metric channel can all
pass, while the odd reciprocal defect direction remains dark.

A second hostile chooses both magnitudes correctly but reverses the relative
phase. It is isometric and reflection-equivariant yet gives the opposite
causal orientation.

## Frontier contraction

The first meeting cell is now sharply typed:

\[
\text{reciprocal doubled Julia defect at }p
\to
\text{twisted half-density history pair at }p.
\]

What remains is one source Green/Stokes theorem deriving \(J_p\), including
its two nonzero parity coefficients, metric normalization, and causal sign.
The global boundary pencil is still downstream.
