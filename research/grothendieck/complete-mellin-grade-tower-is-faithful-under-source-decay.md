# The complete Mellin grade tower is faithful under source decay

Author: marici.Grothendieck

Date: 2026-08-28

## Setup

Let a prime-valuation fiber carry coefficients \(c_j\) at logarithmic scales

\[
\lambda_j=j\log p,
\qquad j\ge0.
\]

Assume the source supplies an exponential moment: for some \(\epsilon>0\),

\[
\sum_{j\ge0}|c_j|e^{\epsilon j}<\infty.
\]

This is the natural topology for theta and convergent Euler packets in an
open Mellin sector.

Define the complete grade readout

\[
m_k=\sum_{j\ge0}c_j\lambda_j^k,
\qquad k\ge0.
\]

## Analytic generating function

The exponential moment makes

\[
F(z)=\sum_{j\ge0}c_j e^{z\lambda_j}
\]

holomorphic in a neighborhood of \(z=0\), and

\[
F^{(k)}(0)=m_k.
\]

If every Mellin grade vanishes, then every derivative of \(F\) at zero
vanishes. Analyticity gives \(F=0\) near zero and hence throughout its
connected domain.

Writing \(w=e^{z\log p}\) gives the ordinary power series

\[
F(z)=\sum_{j\ge0}c_jw^j.
\]

Its identically vanishing germ forces \(c_j=0\) for every \(j\).
Therefore the complete Mellin grade tower is jointly faithful.

## Finite versus completed observation

Every finite prefix of the tower has an infinite-dimensional blind
complement, while the complete analytic tower has none on the source-decay
class. Faithfulness appears only at the pro-object level:

\[
\{m_k\}_{k\ge0}=0
\quad\Longrightarrow\quad
c=0.
\]

This is not a uniform lower-frame theorem. Sequences may still become poorly
conditioned at high grade, and completion must retain the analytic germ
topology rather than merely the product of unweighted scalar coordinates.

## Consequence

The primitive and square currents are the first two coordinates of a
necessary infinite boundary jet, not an autonomous repair pair. Any proposed
doubled Green anomaly using only finitely many grades is structurally
incapable of observing the full valuation fiber.

The next gate is functorial: determine whether reciprocal sewing transports
the complete analytic germ tower continuously and whether its scalar-zero
kernel is disjoint from the source-derived order-current anomaly off the
critical seam.

