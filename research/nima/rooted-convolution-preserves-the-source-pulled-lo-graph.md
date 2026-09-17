# Rooted convolution preserves the source-pulled L/O graph

## Admitted multiplier scope

Let `p` and `q` be source packets whose Mellin amplitudes belong to the declared multiplier algebra of the retained analytic graph. Write

\[
f=\mathcal M p,
\qquad g=\mathcal M q.
\]

The source convolution theorem gives

\[
\mathcal M(p*q)=fg.
\]

This is the analytic realization of the scalar rooted-substitution operation `H`.

## Transport of the L/O coordinates

For a fixed observer `a`, multiplication is associative:

\[
M_{m_a}(fg)=(M_{m_a}f)g=f(M_{m_a}g).
\]

Endpoint evaluation is multiplicative:

\[
\beta(p*q)=\beta(p)\odot\beta(q),
\]

and therefore

\[
\beta(a*(p*q))
=D_a^\partial\bigl(\beta(p)\odot\beta(q)\bigr).
\]

Consequently every coordinate of the source-pulled graph of `p*q` is obtained continuously from coordinates already retained for `p`, `q`, and `a`:

\[
(p*q,\ fg,\ m_afg,\ \beta(p)\odot\beta(q),\ D_a^\partial(\beta(p)\odot\beta(q))).
\]

If `mu` is any submultiplicative seminorm of the admitted multiplier algebra, then

\[
\mu(fg)\le\mu(f)\mu(g),
\]

\[
\mu(m_afg)\le\mu(m_af)\mu(g).
\]

The finite-dimensional endpoint estimates are immediate. Together with the projective coefficient estimate

\[
q_\delta(p*q)\le q_\delta(p)q_\delta(q),
\]

these inequalities prove joint continuity of `H` on the source-pulled `L/O` graph.

## Rooted trees

Induction gives the same result for every finite rooted tree:

\[
\mathcal M\operatorname{ev}_\tau((p_v))
=
\prod_{v\in V(\tau)}m_{p_v}.
\]

Associativity identifies all parenthesizations. Since all maps are continuous and finite packets are dense, the identities extend to graph completion. Thus the mixed higher faces involving `R,C,L,O,H` commute strictly in the admitted multiplier scope.

## Boundary

The theorem applies to scalar rooted substitutions whose Mellin amplitudes are admitted graph multipliers. It does not assert that every arbitrary completed observer is a multiplier, nor does it cover nontransverse loaded physical divisors. The latter belongs to the `V` graph-stability problem.
