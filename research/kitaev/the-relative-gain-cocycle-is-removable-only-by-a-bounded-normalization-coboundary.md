# The Relative-Gain Cocycle Is Removable Only by a Bounded Normalization Coboundary

Assume the source involution has frozen the ordered repair and drift rays and
that each transport constructor preserves them. At stage \(n\), write its
positive relative gain as

\[
\gamma_n=\frac{g_{+,n}}{g_{-,n}}>0.
\]

Then the safety factor evolves by

\[
M_{n+1}=\gamma_nM_n.
\]

The gains form a multiplicative \(\mathbb R_{>0}\)-valued one-cocycle on the
transport graph.

## Gauge transformation

Let the relative normalization of the two port frames at vertex \(n\) be
changed by \(q_n>0\). For a transport edge \(n\to n+1\), the coordinate gain
becomes

\[
\gamma_n'
=\gamma_n\frac{q_n}{q_{n+1}}.
\]

Thus a frame change acts by a multiplicative coboundary.

On a finite open chain, choose

\[
q_{n+1}=\gamma_nq_n.
\]

Then \(\gamma_n'=1\) on every edge. Algebraically, every gain cocycle on a
tree is trivial.

## Loop obstruction

For a closed cycle \(C\), define the relative-gain holonomy

\[
H_C=\prod_{e\in C}\gamma_e.
\]

The normalization factors telescope, so

\[
H_C'=H_C.
\]

A single-valued frame trivializing every edge exists only if

\[
H_C=1
\]

for every cycle. The loop products represent the class in

\[
H^1(G;\mathbb R_{>0}),
\]

or, after logarithms, in \(H^1(G;\mathbb R)\).

## Infinite-chain obstruction

On a ray, the recursive trivializing frame is

\[
q_N=q_0\prod_{n=0}^{N-1}\gamma_n.
\]

It defines a topology-preserving normalization only if the frame and its
inverse remain uniformly bounded:

\[
0<c
\le
\prod_{n=0}^{N-1}\gamma_n
\le C<\infty
\]

for all \(N\).

Equivalently, the logarithmic partial sums

\[
S_N=\sum_{n=0}^{N-1}\log\gamma_n
\]

must remain bounded. An algebraic coboundary with \(q_N\to0\) or
\(q_N\to\infty\) changes the completion topology and is not an admissible
normalization repair.

## Hostile and repaired families

For

\[
\gamma_n=\frac12,
\]

one has

\[
q_N=2^{-N}q_0\longrightarrow0.
\]

Every finite prefix can be normalized to unit gain, but there is no uniformly
nondegenerate trivialization of the completed ray.

By contrast, the alternating sequence

\[
\gamma_{2k}=2,
\qquad
\gamma_{2k+1}=\frac12
\]

has partial products alternating between \(2\) and \(1\). Its cocycle admits a
bounded trivialization despite nontrivial edge gains.

## Safety versus equivalence

To preserve only a lower positivity margin, a uniform lower bound on partial
products may suffice. To claim that normalization leaves the completed source
topology unchanged, both lower and upper bounds are required. These are
different theorem strengths and must not be conflated.

## Exchange boundary

This theorem treats constructors commuting with the involution. A constructor
that exchanges the two character rays inverts the relative coordinate and
requires a twisted cocycle valued in

\[
\mathbb R_{>0}\rtimes C_2.
\]

Such exchange must be typed explicitly rather than folded into the commuting
gain formula.

## Falsifiers

- A cycle with \(H_C\ne1\) under a claimed global unit-gain frame.
- A trivializing normalization tending to zero or infinity on the tail.
- Cutoffwise unit-gain frames with no uniform equivalence constants.
- Treating an algebraic coboundary as automatically continuous in completion.
- Ignoring a ray-exchanging constructor in the cocycle law.
- Renormalizing stages independently without respecting composition.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to decide exactly when the remaining gain cocycle is a
gauge artifact and when it is a completion obstruction.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Cycle holonomy and unbounded tail frames are the two independent
obstructions; finite normalization alone proves neither away.
