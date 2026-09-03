# Infinitely supported obstruction class

## Question

Does a non-atomic fixture with infinitely supported signed defect change
the rival-2/rival-3 boundary of the cyclic residue-feedback model, or
is the boundary an artifact of atomicity?

## Claim boundary

The fixture class is measures with density

\[
d\rho(x)=\bigl(1+\varepsilon\cos(ax)\bigr)\,d\mu(x),
\]

\(\varepsilon>1\), \(\mu\) a positive base measure with full
support (Gauss weight \(e^{-x^2}\) for the executable instance). The
natural obstruction is the negative-part class
\((\varepsilon,\Sigma)\), where

\[
\Sigma=\{x:\cos(ax)<-\varepsilon^{-1}\}
\]

is the defect sign set. The packet classifies how the transports from
the fork (gauge width, support displacement) and the one new
amplitude-editing transport act on this class. No positivity claim is
made.

## Structural facts

1. A positive multiplicative factor — gauge \(e^{-sx^2}\), base-mass
density — never changes \(\Sigma\). Gauge acts trivially on the sign
set and fixes \(\varepsilon\).
2. Translation \(x\mapsto x+\delta\) maps \(\Sigma\) to a translate;
the obstruction class is unchanged up to congruence.
3. Amplitude editing \(\varepsilon\mapsto\varepsilon'\) with
\(|\varepsilon'|\u003c|\varepsilon|\) strictly decreases the obstruction
order, but it edits the defect parameter directly: convergence is by
construction.

## Strongest falsification attempt

Exhibit an amplitude-preserving transport (gauge, displacement, or any
positive-measure-preserving deformation of the density's sign
structure) that strictly decreases the natural order. The sign-set
invariance under positive factors and congruence under translation are
exact, so the attempt fails on this class; the checker verifies both
symbolically.

## Disposition

The boundary is not an artifact of atomicity. On the infinitely
supported class: every amplitude-preserving transport leaves the
natural obstruction order invariant, and the only order-decreasing
transports are amplitude-editing ones, whose convergence is
definitional (order-selection, disqualified as loop evidence by the
fork's honesty controls). The cyclic residue-feedback model therefore
fails to be a proof engine on this class for the same structural
reason as on atoms: the obstruction class is either preserved or
edited, never cohered.

Residual: a transport acting nontrivially on the sign-set geometry
\(\Sigma\) itself (e.g., residue-selected spectral shift changing the
relative measure of negative intervals) would escape the boundary;
constructing one that is not secretly amplitude editing is the next
typed object. It is not opened here.

## Verification

- `research/voevodsky/checkers/scout_infinitely_supported_obstruction.py`
- `research/voevodsky/results/infinitely_supported_obstruction.json`
