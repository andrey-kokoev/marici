# The Doubled Tail Needs Diagonal Control Sewing Before Evans Evaluation

The constructible-rank obstruction has been applied to the source-derived tail
ODE

\[
G'+sG+cf=0,
\qquad c'=0.
\]

After imposing decay at infinity, one sheet has a rank-one solution module:

\[
G(q)=c\int_q^\infty f(v)e^{s(v-q)}\,dv.
\]

Two unsown sheets therefore have independent amplitudes `(c_+,c_-)` and a
rank-two pre-Evans module. Every scalar Evans row on that module has a nonzero
kernel. The reciprocal completion must identify the two controls as one source
preparation, minimally through `c_+=c_-`. This diagonal pullback reduces the
module to rank one before scalar evaluation.

The repair is necessary but not RH-bearing by itself. On the sewn line the
Evans coefficient is `F_+(s)+F_-(s)`, namely the completed scalar transform
whose nonvanishing is at issue. Control sewing correctly types the spectral
problem; it cannot prove its answer.

This gives the multi-tower coherence cell an exact role: it identifies the two
transport towers as actions on one input preparation. Without it, scalar zero
exclusion is algebraically impossible. With it, the remaining work is an
independently derived off-seam constraint on the rank-one Evans coefficient.

Research packet:
`research/grothendieck/the-doubled-tail-needs-diagonal-control-sewing-before-evans-evaluation.md`

Exact checker:
`research/grothendieck/checkers/check_doubled_tail_control_sewing_rank.py`

The checker passes 8/8 exact tests.
