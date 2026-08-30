# The complete finite RH operator must be a two-sided linking block

## Why incidence alone is triangular

Let \(V_X\) be the finite arithmetic carrier, \(H_X\) the finite analytic
tail--seam carrier, and \(U_X:V_X\to H_X\) the source-derived synthesis map.

The graph presentation of incidence is encoded by

\[
G_{U_X}=
\begin{pmatrix}
I_{V_X}&0\\
U_X&-I_{H_X}
\end{pmatrix}.
\]

Its determinant is a fixed unit, independent of \(U_X\). Graph incidence
preserves provenance but cannot by itself supply the multiplicative RH
determinant. Any one-way triangular assembly has the same defect: its
determinant factorizes into diagonal pieces and does not see the cross-sector
relation.

## Minimal two-sided operator

Let \(E_{+,X}\) and \(E_{-,X}\) be the reciprocal sector carriers. A determinant
capable of seeing their interaction must have the linking form

\[
T_X(s)=
\begin{pmatrix}
A_{+,X}(s)&M_X(s)\\
N_X(s)&A_{-,X}(s)
\end{pmatrix}.
\]

Here \(A_{+,X}\) and \(A_{-,X}\) are sector operators,
\(M_X:E_{-,X}\to E_{+,X}\) is the forward source link, and
\(N_X:E_{+,X}\to E_{-,X}\) is the reciprocal link.

Arithmetic-to-analytic synthesis, moving seam, endpoint complex, and Gaussian
line must be incorporated into these typed blocks before taking the
determinant.

## Schur determinant

When \(A_{+,X}\) is invertible,

\[
\det T_X
=
\det A_{+,X}\,
\det\!\left(A_{-,X}-N_XA_{+,X}^{-1}M_X\right).
\]

The interaction

\[
\Sigma_{-,X}=N_XA_{+,X}^{-1}M_X
\]

is the cross-sector feedback seen from the negative sector. The symmetric
formula using \(A_{-,X}^{-1}\) gives

\[
\Sigma_{+,X}=M_XA_{-,X}^{-1}N_X.
\]

These are Schur complements of one complete block, not independently fitted
scalar transfers.

## One-way no-go

If \(N_X=0\), then

\[
\det T_X=\det A_{+,X}\det A_{-,X}.
\]

The forward incidence \(M_X\) disappears from the determinant. Likewise,
\(M_X=0\) erases \(N_X\).

Therefore a one-way synthesis graph cannot influence the multiplicative zero
locus. Both cross-sector arrows are necessary before top-exterior totalization
can carry RH information.

Nonzero arrows are still insufficient: their paired images may lie in proper
ideals and fail to act faithfully.

## Morita fullness gate

Let the sector algebras be \(A_+\) and \(A_-\), with linking bimodules \(M\)
and \(N\). The pairings

\[
M\otimes_{A_-}N\longrightarrow A_+,
\qquad
N\otimes_{A_+}M\longrightarrow A_-
\]

must be source-derived and Morita-full.

At finite cutoff, their images must generate both diagonal algebras.
Quantitatively, the linking action must have a positive lower margin on the
declared finite carrier.

Under completion, that margin must remain bounded away from zero on every
compact subset of a claimed open sector. Otherwise the Schur interaction can
vanish on an escaped direction although every finite link is nonzero.

## Placement of the Euler translation carrier

The logarithmic Euler operator

\[
H_X=-\sum_{p\le X}\log(1-p^{-1/2}S_{\log p})
\]

acts first on the labelled arithmetic/analytic graph carrier. It cannot be
inserted as a scalar diagonal block.

Its three-grade decomposition supplies primitive and square anomaly-line
components, the connected \(S_3\) component, and endpoint coboundary columns.
Adams type transport acts on the same labelled carrier. Erasing labels before
forming \(M_X\) and \(N_X\) loses Morita support.

## Placement of seam and endpoint data

Moving-seam transport compares cut fibers unitarily. Endpoint translation gives
a relative boundary complex rather than an invariant scalar line.

Consequently, the links must act on carriers containing

\[
\text{tail}\oplus
\text{seam}\oplus
\text{primitive endpoint}\oplus
\text{square endpoint}\oplus
\text{connected endpoint}.
\]

The endpoint-current border is a boundary row and column inside this linking
system, not the full determinant block. A cross link defined only after
endpoint scalar projection cannot be Morita-full on the source carrier.

## Placement of the Gaussian line

The archimedean character

\[
\chi_s(a)=a^{-s}
\]

represents the same scale translations. It must attach to the linking block as
a typed tensor factor or boundary line, with

\[
\chi_s(a)\chi_{1-s}(a)=a^{-1}.
\]

Appending a gamma scalar after taking \(\det T_X\) does not prove that the
archimedean line participates in cross-sector action or anomaly
trivialization.

## Reciprocal comparison

A source-derived reciprocal structure must compare

\[
A_{-,X}(s)\longleftrightarrow A_{+,X}(1-s)
\]

and exchange

\[
M_X(s)\longleftrightarrow N_X(1-s).
\]

The comparison may be anti-linear or dagger-valued according to source typing.
It cannot be inferred from equality of final determinants.

At determinant-line level this supplies the functional-equation frame. At
operator level it ensures that both Schur complements arise from one
reciprocal block.

## Candidate finite assembly signature

The constructor must take the positive and negative sector carriers,
arithmetic-to-analytic graph, forward and reciprocal links, moving seam,
endpoint relative complex, primitive and square anomaly lines, connected
\(S_3\) operator, Gaussian Mellin line, and reciprocal orientation, and return
one complete linking operator \(T_X\).

Only after this constructor exists may one apply the top-exterior or relative
determinant functor.

## Hostile tests

1. A triangular block makes cross incidence disappear from the determinant.
2. One nonzero off-diagonal link does not produce a two-sided interaction.
3. Two links with proper image ideals fail Morita fullness.
4. A scalar gamma factor appended after determinant formation lacks operator
   provenance.
5. Endpoint projection before linking erases the relative boundary complex.
6. Finite fullness with collapsing minimum margin permits a completion-null
   direction.
7. Equal Schur determinants without a common full block do not prove
   reciprocal coherence.

## Consequence for categorical RH

The abstract common operator \(T_X\) now has a minimal forced shape: it is a
two-sided reciprocal linking block. The source-incidence graph supplies its
carrier, but only Morita-full forward and backward links make the determinant
sensitive to the relationship between sectors.

The next concrete problem is to derive \(M_X\) and \(N_X\) on the full typed
boundary carrier and verify their pairing ideals before making completed
determinant or observability claims.

## Verdict

A categorical RH operator cannot be triangular. Its finite determinant must
come from a two-sided reciprocal linking block whose off-diagonal bimodules are
Morita-full and whose boundary and archimedean lines are present before
totalization. The missing object is the source-derived reciprocal linking pair,
not another scalar section.
