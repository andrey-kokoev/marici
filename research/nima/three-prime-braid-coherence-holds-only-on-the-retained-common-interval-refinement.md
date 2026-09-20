# Three-prime braid coherence holds only on the retained common interval refinement

## Question

Do adjacent-prime ratio-window transports satisfy the three-prime braid law, and at what source type?

## Source operation

Choose three ordered interval lengths and retain their finest common interval refinement. For the exact finite fixture use lengths

\[
L_p=1,\qquad L_q=2,\qquad L_r=4.
\]

All prefix cuts from the six prime orderings lie at the integer points from zero through seven. The source carrier is therefore the seven-piece atomic interval packet. Each ordered prime word is obtained by reaggregating these atoms into three consecutive stage windows.

## Braid transport

The two adjacent-swap paths are

\[
pqr\to qpr\to qrp\to rqp
\]

and

\[
pqr\to prq\to rpq\to rqp.
\]

On the retained atomic carrier every swap is a change of aggregation, not a change of source state. Both paths therefore induce the same final aggregation. The involution and distant-commutation laws follow by the same retained-refinement construction.

## Quotient-before-transport hostile

The atomic state

\[
h=(0,1,-1,0,0,0,0)
\]

has zero readout in the initial three-port packet but a nonzero readout after the first adjacent swap. Hence the initial three-port quotient has erased a ratio-window direction required by transport.

No path-independent braid theorem can be inferred after that quotient. Braid coherence holds on the common refinement and descends only through quotients proved invariant under every adjacent aggregation.

## Claim boundary

The exact checker proves finite-cutoff source-typed braid coherence for the interval attachment packet. It also proves that scalar total-window equality and one three-port presentation are not faithful coordinates for transport.

It does not construct:

- a determinant-line image of the ratio faces;
- compatibility with the order-three anomaly;
- a cofinal all-prime refinement or completion.

## Disposition

The adjacent ratio-window cells assemble coherently at three primes when the common interval refinement is retained. Quotient-before-transport is falsified. The next analytical obligation is a source-derived determinant-line functor on this refined packet; no scalar determinant may be assigned before its action on the signed ratio faces is specified.

Verification:

- `research/nima/checkers/check_three_prime_permutohedral_braid.py`
- `research/nima/results/three-prime-permutohedral-braid.json`
