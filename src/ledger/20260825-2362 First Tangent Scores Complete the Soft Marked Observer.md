# 2362 — First Tangent Scores Complete the Soft Marked Observer

## Frozen observer family

Entry 2361 proves that the \(g_{23}\) residue port recovers the rank-four
quotient of

\[
0\longrightarrow M_{16}^{\rm deleted}
\longrightarrow M_{20}^{X_1\text{-soft}}
\longrightarrow Q_4\longrightarrow0.
\]

Test the remaining deleted bulk using only the five source-admitted marked
residues and their tangent Gauss--Manin scores.  Do not add a projector after
seeing the blind kernel.

Every residue is reduced in its own one-dimensional twisted wall cohomology,
including the restricted Cayley--Menger polynomial and all nonunit retained
walls.

## Ordinary residue rank

On \(M_{16}^{\rm deleted}\), the individual cohomological residue ranks are

\[
\begin{array}{c|ccccc}
\text{wall}&g_1&g_2&g_3&g_{23}&g_{31}\\ \hline
\text{rank}&3&3&4&0&5.
\end{array}
\]

Their direct-sum observer has rank

\[
\boxed{10<16.}
\]

Thus ordinary marked residues alone leave a six-dimensional blind kernel.
The vanishing \(g_{23}\) rank is forced: every deleted numerator contains the
factor \(b=q_{g_{23}}\).

## First score closure

Retain the two tangent directions on \(X_1=0\):

\[
\partial_{X_2},\qquad\partial_{X_3}.
\]

Transport the ten residue covectors by the dual tangent connection.  The
cumulative observer ranks are

\[
\boxed{
10\quad\xrightarrow{\text{first tangent score}}\quad16.
}
\]

No higher score is required.  All source vectors lie in the declared
simple-pole frame; the unsupported-term count is zero.

## Complete algebraic observer

Combining this result with Entry 2361 gives a faithful supported observer:

\[
\boxed{
\left(
\operatorname{Res}_{g_{23}}Q_4,
\operatorname{Res}_{g_i}M_{16}^{\rm deleted},
\nabla_{\rm tan}\operatorname{Res}_{g_i}M_{16}^{\rm deleted}
\right)
\text{ has rank }4+16=20.
}
\]

Therefore the first supported maximal-parabolic obstruction does not defeat
the full admissible marked-score port family.  It demonstrates why context
closure is necessary: zeroth-order ports are not jointly faithful, while the
source-generated first score tower is.

## Classification

- Carrier support: existing \(X_1\)-soft and marked-wall strata;
- coefficient structure: nonsplit maximal-parabolic extension;
- ordinary observer defect: rank six;
- first-score defect: zero;
- new Carrier datum: none;
- physical relative-cycle activation: still separate and unproved.

## Artifacts

- `research/benincasa/check_x1_soft_joint_marked_residue_ports.py`
- `research/benincasa/x1-soft-joint-marked-residue-ports.json`

Sequence claim: `seqclaim-c5197efc24d79053c59baac8`.