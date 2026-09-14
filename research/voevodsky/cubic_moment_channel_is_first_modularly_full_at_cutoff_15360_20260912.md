# Cubic moment channel is first modularly full at cutoff 15360

## Question

Does the quadratic moment pattern remain sufficient under a substantially larger arithmetic cutoff hostile?

## Claim boundary

Not according to two independent modular rank calculations. At cutoffs \(15360\) and \(30720\), the unmodulated, linear, and quadratic channel stack is deficient, while adding the cubic channel gives full rank modulo both primes. Modular deficiency alone is not an exact rational countercycle; modular full rank does prove rational full rank for the cubic stack at those finite cutoffs.

## Extended census

For shell-index moments and, separately, scale moments, the ranks are identical.

At cutoff \(15360\), with \(4592\) edges, cumulative ranks for powers \(0,1,2,3\) are

\[
3719,\quad4491,\quad4590,\quad4592.
\]

At cutoff \(30720\), with \(9204\) edges, they are

\[
7427,\quad8978,\quad9197,\quad9204.
\]

The same sequences occur modulo \(1000000007\) and \(1000000009\). Thus quadratic stacks have modular deficiencies \(2\) and \(7\), while cubic stacks are full.

## Correction

Withdraw the reported stability of maximum power two beyond cutoff \(7680\). The earlier finite theorem remains correct at its tested cutoffs, but it does not support a cutoff-independent two-moment conjecture.

The present computation does not yet exhibit a rational quadratic-stack countercycle. Rank can drop after reduction modulo a prime, so matching deficiencies over two primes are strong hostile evidence but not a proof of rational deficiency. Exact rational extraction at this matrix size remains unperformed.

## Interpretation

The required moment depth appears to grow when the graph admits more overlapping shell directions. This disfavors any claim that a fixed small number of polynomial moment channels captures the completed residue.

A countable moment family

\[
(BD_{x^r})_{r\geq0}
\]

is algebraically separating on every finite packet: finitely many distinct label values are separated by a finite Vandermonde matrix. With suitable damping in both edge grade and moment order, it is a plausible completed probe family. That completed continuity and lower-frame problem is separate.

## Disposition

Cubic moments are certified sufficient at cutoffs \(15360\) and \(30720\) by modular full rank. Quadratic sufficiency is no longer supported globally. The next robust construction should use a countable label-moment family or physically distinct finite label bins, rather than guessing a fixed polynomial depth.
