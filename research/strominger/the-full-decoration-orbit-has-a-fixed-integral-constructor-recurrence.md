# The full decoration orbit has a fixed integral constructor recurrence

## Result

The failure of bounded congruence jets does not force retention of the expanding source word.

Let \(C\in GL(4,\mathbb Z)\) be the faithful response of the neutral commutator \([x,y]\). Define the two-sided state

\[
S_n=(U_n,V_n)=(C^n,C^{-n}).
\]

It obeys the fixed update

\[
(U_n,V_n)
\longmapsto
(CU_n,C^{-1}V_n).
\]

This state has 32 integral entries independent of \(n\).

## Constructor readout

Let \(Z,X,Y\) denote the fixed response matrices for the remaining source generators. Because the response is an anti-representation,

\[
\rho([a,b])
=
ho(b)^{-1}\rho(a)^{-1}\rho(b)\rho(a).
\]

The decorated tail response and its inverse are reconstructed from the state:

\[
T_n=U_nX,
\qquad
T_n^{-1}=X^{-1}V_n.
\]

The complete magnetic response is then obtained by applying the same two nested commutator constructors to \(Z,T_n,Y\). Finally the Smith packet is read from the resulting integral matrix.

Thus the full orbit factors as

\[
S_n
\xrightarrow{\text{fixed nested commutator}}
A_n
\xrightarrow{\text{Smith packet}}
(d_1,d_2,d_3)
\xrightarrow{\text{ratio}}
I_n.
\]

## Theorem status

The recurrence and reconstruction formulas are exact group-representation identities for every integer \(n\). They do not depend on interpolation from the seven tested points.

The bounded checker verifies that the implementation of the compressed constructor agrees byte-for-byte with independently expanded source words for \(-3\le n\le3\).

## Explanation

This locates the nonlinearity precisely.

The source evolution is a fixed integral recurrence. Nonlinearity appears only when:

1. the state is inserted into nested commutators;
2. determinantal gcds and saturation are taken.

The huge word and kernel-vector growth are presentation growth, not growth of constructor memory.

## Relation to the failed jet summary

A residue projection such as \(S_n\bmod9\) is not faithful enough to determine the Smith discriminant. The integral state \(S_n\) is.

So the alternatives are not “bounded jet” versus “retain the entire history.” There is a third option:

> retain a fixed-size exact integral state whose entries may grow.

This is the appropriate constructor-level explanation for the orbit.

## Categorical reading

The decoration monoid \(\mathbb Z\) acts on the state object \(GL(4,\mathbb Z)^2\). The magnetic constructor is a fixed readout from that action state to typed lattice maps. The Smith functor then sends those maps to arithmetic invariants.

Atomicity and square class are predicates on the readout. They are not state-transition labels.

## Next falsifier

The remaining compression question is whether both \(U_n\) and \(V_n\) are necessary.

Because \(V_n=U_n^{-1}\), one matrix is mathematically sufficient over \(GL(4,\mathbb Z)\). But if the constructor grammar does not authorize inversion as a local operation, the two-sided state is operationally minimal.

The next test should therefore distinguish algebraic reconstructibility from executable constructor capability.

## Evidence

All four gates pass:

- seven compressed responses equal independent expanded responses;
- every two-sided state multiplies to the identity;
- all six forward transitions use the same update;
- all six inverse transitions use the same update.
