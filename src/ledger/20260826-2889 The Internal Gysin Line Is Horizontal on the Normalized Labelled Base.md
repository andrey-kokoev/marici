# 2889 — The Internal Gysin Line Is Horizontal on the Normalized Labelled Base

## Normalized marked sections

The four marked occurrences of Entry 2887 factor globally as

\[
\begin{aligned}
s_{1,+}&=(1,+4(\kappa+\xi)),&
s_{1,-}&=(1,-4(\kappa+\xi)),\\
s_{3,+}&=(-3,+4(\kappa-\xi)),&
s_{3,-}&=(-3,-4(\kappa-\xi)).
\end{aligned}
\]

These are labelled algebraic sections, not the two branches of an unresolved
square root. In their ordered point basis, the normalized point-local-system
connection is

\[
A_D=0.
\]

## Deck decomposition

The deck involution exchanges the two signs in each pair. The Gysin kernel
decomposes into

\[
\begin{aligned}
e_{1,-}&=(1,-1,0,0),\\
e_{3,-}&=(0,0,1,-1),\\
e_{13,+}&=(1,1,-1,-1).
\end{aligned}
\]

The first two lines are deck anti-invariant; the last is deck invariant.

Since \(A_D=0\), the internal bypass line

\[
\mathcal L_{\rm bypass}=\mathbb Q\langle e_{1,-}\rangle
\]

is horizontal on the fixed labelled \(\xi\)-base.

## Local monodromy

Around \(\xi=-\kappa\), the normalized sections

\[
y=\pm4(\xi+\kappa)
\]

return to themselves. Therefore the occurrence monodromy is identity. The
cubic factor in the source residue is a meromorphic pole, not branch
monodromy.

## Qualification

This result excludes mixing on the fixed normalized base and excludes a new
local inertia character at the collision. It does not yet exclude permutation
of the two deck-odd lines under nontrivial transitions between different
occurrence charts.

The next finite test is the complete cyclic and noncyclic transport of

\[
\langle e_{1,-},e_{3,-}\rangle.
\]

## Durable artifacts

- `research/benincasa/check_soft_internal_gysin_line_transport.py`
- `research/benincasa/soft-internal-gysin-line-transport.json`

