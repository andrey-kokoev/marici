# Flavor Krylov Interaction Net Needs History and Volume Reference

## Result

The Krylov construction has an exact Interaction Net interpretation, but the
physical quotient separates two observers:

- a projective observer measures cyclicity through \(|\Omega|^2\);
- a signed observer requires an additional source-derived volume reference.

The interaction net must also retain execution history explicitly. A
destructive chain does not expose all three Krylov stages at once.

## Three candidate nets

Start with a seed wire carrying \(x\) and an interaction agent carrying \(A\).

### Destructive chain

Two successive applications produce only

\[
A^2x.
\]

The earlier stages have been consumed. A ternary determinant observer cannot
run because it receives only one port.

### Same-state fan-out

An untyped fan-out produces

\[
x,
\qquad
x,
\qquad
x.
\]

Its determinant is zero. Explicit duplication does not create the missing
relations.

### History-retaining chain

An authorized history constructor exposes

\[
(0,x),
\qquad
(1,Ax),
\qquad
(2,A^2x),
\]

where the first component is the interaction depth. For the exact witness the
determinant is nonzero.

The resource equation is not three seeds in and three vectors out. It is one
seed, two applications of \(A\), and two retained snapshots producing three
depth-typed outputs.

## Ordered-port law

The determinant observer consumes the ports in depth order. Exchanging depths
one and two reverses its sign. Consequently, erasing the depth labels before
observation destroys the orientation semantics even when the underlying
vectors remain available.

This is a direct instance of the ordered-port distinction in Marici: equal
multisets of values do not imply equal constructor inputs.

## Projective correction

Because the seed is physically a ray, rephasing gives

\[
x\longmapsto \zeta x.
\]

Linearity sends every history port to \(\zeta\) times itself. Hence

\[
\Omega_A(x)
\longmapsto
\zeta^3\Omega_A(x).
\]

The signed observer is not gauge-invariant. The projective observer

\[
|\Omega_A(x)|^2
\]

has zero phase weight and descends without further structure. It reports
whether the history spans the three-dimensional carrier, not which orientation
it has.

## Volume-reference repair

Let \(\rho\) be an independently derived reference port with phase weight
\(-3\). Then

\[
\rho\Omega_A(x)
\]

has total phase weight zero. Its phase or sign is a relational observable
between the Krylov history and the reference.

This is not a normalization convention. The net must contain a constructor for
\(\rho\), its transformation law, its temporal scope, and the comparison node
that joins it to the history determinant.

## Interaction Net contract

The minimal enriched net contains:

1. a seed-ray port;
2. an evolution agent \(A\);
3. a history constructor retaining depths zero, one, and two;
4. an ordered alternating observer;
5. optionally, a volume-reference port and relational comparison agent.

Without the fifth item, the only physical output is positive cyclicity.

## Finite falsifiers

The checker rejects:

- destructive execution, because only one terminal port survives;
- same-state fan-out, because the determinant vanishes;
- depth erasure, because exchanging two stages changes the signed output;
- unreferenced signed readout, because it has phase weight three.

## Interpretation

Interaction Nets provide the local operational syntax: which agents interact,
which ports survive, and where duplication or history is paid for. The
determinant supplies a global observer on the resulting trace. The physical
Flavor quotient then determines which observers descend.

This corrects the earlier intuition cleanly. The net topology really does
generate the three relations, but topology alone does not turn a
representative-dependent determinant into a physical orientation. That needs a
new relational interaction with a volume frame.
