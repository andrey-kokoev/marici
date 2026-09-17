# The lax tail feeds the next cycle but is not yet a ninth axis

## Exact reservoir realization

For a cutoff projection `P_X`, put `T_X=I-P_X`. Every completed sewing operator has the block decomposition

\[
F=
\begin{pmatrix}
P_XFP_X&P_XFT_X\\
T_XFP_X&T_XFT_X
\end{pmatrix}
=
\begin{pmatrix}
F_{vv}&A_X\\
B_X&F_{tt}
\end{pmatrix}.
\]

Retaining a visible state `v_n` and complement state `t_n` gives the exact next-cycle equations

\[
v_{n+1}=F_{vv}v_n+A_Xt_n,
\]

\[
t_{n+1}=B_Xv_n+F_{tt}t_n.
\]

Thus the lax tail does have a destination: it is a state-valued complement channel that can return to the visible sector in a later cycle. Eliminating it produces a memory kernel; retaining it gives a Markovian block system.

## Independence test

This does not yet produce a ninth axis. The putative tail projection is

\[
T_X=I-P_X,
\]

so it is completely determined by the regulator coordinate `X`. The cross blocks are likewise determined by `P_X` and `F`:

\[
A_X=P_XFT_X,
\qquad
B_X=T_XFP_X.
\]

There is no new independent binary choice at every vertex. `visible only` versus `visible plus complement` is a choice to forget or retain part of the existing regulator decomposition, not a source-derived operation independent of `R` and `q`.

The refinement identity confirms this dependence: the next shell is the difference of two regulator projections,

\[
\Delta_{X,Y}=P_Y-P_X.
\]

Hence shell propagation is the internal composition law of the `R x q` lax face.

## Moving-boundary warning

For every fixed diagnostic `P_m`, the remote residual

\[
P_mF(I-P_n)
\]

converges to zero as `n` grows. Nevertheless the moving-boundary leakage

\[
P_nF(I-P_n)
\]

can retain norm one at every stage. The backward-shift witness realizes exactly this behavior.

Therefore the tail should not be described as one hidden state at infinity. It is generally a moving incidence boundary indexed by the regulator filtration.

## Promotion gate for a genuine ninth direction

A ninth axis would require additional source data not recoverable from `P_X` and `F`, for example:

- an independent reservoir carrier with its own source labels;
- a source-derived reservoir evolution not equal to `T_XFT_X`;
- an independent injection and return pair satisfying a new coherence law;
- or a new cycle index whose transitions are not cutoff refinements.

The previously considered compression `V^dagger B` cannot supply this by itself: prior work classifies it as a Gram readout, not an authorized primitive dynamic block.

## Verdict

\[
\boxed{\text{The lax tail feeds the next cycle as a retained reservoir fiber.}}
\]

but

\[
\boxed{\text{it is not an independent ninth binary dimension.}}
\]

Its present categorical location is the state-valued fiber and modification cell over the existing `R x q` face.
