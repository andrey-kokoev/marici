# The Theta Zero-State and the Euler Currents Live in Different Towers and Meet Only through Source Incidence

## A necessary typing correction

The reciprocal weighted spaces from the previous result are coefficient
spaces for Euler boundary packets indexed by primes.  The completed theta
zero-state is not a vector in that label space.

Three distinct objects are present:

1. theta source atoms indexed by positive integers;
2. Euler boundary currents indexed by prime powers;
3. Green tail states on the archimedean scale coordinate.

Their labels and topologies are not interchangeable.  Attempting to place the
completed theta zero-state in `H_a` silently identifies the theta-label source,
the Euler-current port, and the archimedean state tower.

## The native correspondence

Let `E_theta` be the positive-chart theta test space.  The superexponential
theta estimate puts the fixed forcing `f` in `E_theta`.  Primitive,
prime-square, and connected Euler currents define elements of
`E_theta'` because their sampled evaluations on `f` converge absolutely.

The source incidence and its topological transpose are

\[
B_f:\mathbb C\longrightarrow E_\theta,
\qquad
B_f(c)=cf,
\]

and

\[
B_f^\times:E_\theta'\longrightarrow\mathbb C,
\qquad
B_f^\times(\nu)=\nu(f).
\]

The tail resolvent then maps the scalar source channel into the archimedean
graph domain:

\[
R_s:E_\theta\longrightarrow H^1(\mathbb R_+),
\qquad
f\longmapsto G_s.
\]

Thus the legitimate path is

`Euler current -> theta-source evaluation -> scalar control -> Green tail`.

There is no step pairing an Euler distribution directly with a dual-valued
Green state.  The apparent dual-times-dual obstruction arose only after
collapsing these typed towers into one ambient completion.

## Reciprocal structure

The weighted pair `H_a x H_-a` still has a real role: it pairs the direct and
reciprocal Euler coefficient packets.  The `H1` trace pullback pairs the two
archimedean tail charts.  The scalar control line is the mate cell through
which the arithmetic transpose and analytic Green construction compose.

This gives the precise multi-tower diagram:

```text
Euler+  <---- reciprocal pairing ----> Euler-
  |                                  |
  v                                  v
theta-source dual evaluations -> common scalar control
                                      |
                                      v
tail+   <------- trace sewing ------> tail-
```

The common scalar line is not another state sector.  It is the composition
object that prevents illegal direct pairings between unlike towers.

## Consequence for the RH programme

Completion no longer asks for one common domain containing both theta states
and Euler currents.  It asks for continuity and commutativity of a
correspondence:

\[
E_\theta'
\xrightarrow{B_f^\times}
\mathbb C
\xrightarrow{B_f}
E_\theta
\xrightarrow{R_s}
H^1.
\]

On the reciprocal sheet the corresponding path must be the Fourier–Tate mate.
The remaining RH-bearing gate is whether the two composed paths give exactly
the boundary current required by the doubled Green identity, with the
augmentation incidence retained separately.

The finite falsifier is categorical.  At any cutoff, compute the two routes:

1. Euler current through source evaluation and tail propagation;
2. reciprocal transport first, then reciprocal source evaluation and tail
   propagation.

A nonzero mate-square residual closes the route.  Scalar agreement after
erasing the intermediate domains does not count.

## Result

The earlier demand to place the completed theta zero-state in a weighted prime
coefficient space was ill-typed.  The zero-state, Euler currents, and theta
source occupy different towers.  Their only authorized interaction is the
source incidence and its transpose through the common scalar control port.
This removes the artificial dual-times-dual pairing problem and identifies
the next exact object: the reciprocal mate square of the full source-to-tail
correspondence.
