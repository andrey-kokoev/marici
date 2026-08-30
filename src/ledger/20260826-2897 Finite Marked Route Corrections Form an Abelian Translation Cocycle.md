# 2897 — Finite Marked Route Corrections Form an Abelian Translation Cocycle

## Hostile question

Do successive route corrections at the two finite marked collisions commute?
The strongest finite obstruction occurs at

\[
\kappa=0,
\]

where their base supports

\[
\xi=-\kappa,
\qquad
\xi=+\kappa
\]

coincide.

## Source-labelled affine system

Use the ordered affine basis

\[
(P_{\rm aff},\tau_1,\tau_{-3}),
\]

where \(\tau_1\) and \(\tau_{-3}\) are the deck-odd Leray tubes at the
normalized marked points \(x=1\) and \(x=-3\).  Entries 2889 and 2890 proved
that these marked points are constant and do not exchange under transport.

The two translation nilpotents are

\[
N_1=
\begin{pmatrix}
0&1&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad
N_{-3}=
\begin{pmatrix}
0&0&1\\
0&0&0\\
0&0&0
\end{pmatrix}.
\]

They obey

\[
N_1^2=N_{-3}^2=N_1N_{-3}=N_{-3}N_1=0.
\]

Therefore

\[
[N_1,N_{-3}]=0
\]

and

\[
T_1(c_1)T_{-3}(c_3)
=
T_{-3}(c_3)T_1(c_1)
=
I+c_1N_1+c_3N_{-3}.
\]

## Coalesced base support

At \(\kappa=0,\xi=0\), the two collision divisors meet in the base, but
their fiber occurrences remain the distinct labelled points \(x=1\) and
\(x=-3\).  The normalized marked-point connection is zero.  Hence the
coalescence does not braid or identify the two tubes, and the same vanishing
commutator applies.

## Result

The finite marked route corrections form an abelian Tate/Kummer translation
cocycle.  No supported commutator and no new carrier cell appear at the
coincident base support.

This narrows the architecture further:

- compact elliptic state: unchanged;
- marked relative readout: shifted;
- composition of marked shifts: additive and occurrence-labelled.

## Next falsifier

Test whether the additive route cocycle is exact after imposing all
source-authorized endpoint normalizations.  If one global source-normalized
affine primitive removes both translations simultaneously, the cocycle is
presentation data.  If not, its cohomology class is the intrinsic relative
readout invariant.

## Durable artifacts

- `research/benincasa/check_soft_marked_route_commutator.py`
- `research/benincasa/soft-marked-route-commutator.json`
