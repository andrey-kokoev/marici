# The one-qubit Hadamard--Pauli square realizes three-lens coherence

## Minimal packet

Let

\[
v=(a,b)\in\mathbf F_2^2
\]

and choose the Pauli section

\[
P(v)=X^aZ^b.
\]

Let \(H\) be the Hadamard operator, with

\[
HXH=Z,
\qquad
HZH=X.
\]

The induced additive label transformation is

\[
h(a,b)=(b,a).
\]

## Exact transported command

Conjugation gives

\[
HP(a,b)H
=
Z^aX^b
=
(-1)^{ab}X^bZ^a.
\]

Therefore

\[
HP(v)
=
\beta(v)P(hv)H,
\qquad
\beta(a,b)=(-1)^{ab}.
\]

This is the smallest non-strict source-transport/intervention square.

## Three lens readings

### Sum lens

The command label transports by the linear swap

\[
(a,b)\longmapsto(b,a).
\]

At this level the square commutes strictly. The mixed-command phase is
invisible.

### Product lens

The scalar coherence is

\[
\beta(a,b)=(-1)^{ab}.
\]

It is trivial for \(X\) and \(Z\) separately and nontrivial for the mixed
label \((1,1)\).

Thus the Product lens records the precise correction erased by the additive
label transport.

### Endo lens

The full ordered statement is

\[
HP(v)=\beta(v)P(hv)H.
\]

This is an equality of state transformations. It retains command order,
operator action, and the scalar coherence simultaneously.

## Cocycle compatibility

For the chosen section,

\[
P(v)P(w)=\omega(v,w)P(v+w),
\]

with

\[
\omega((a,b),(a',b'))
=
(-1)^{ba'}.
\]

Transport by \(h\) is compatible with multiplication exactly when

\[
\beta(v)\beta(w)\omega(hv,hw)
=
\omega(v,w)\beta(v+w).
\]

Substitution verifies the identity over \(\mathbf F_2\). The phase
\(\beta\) is therefore not a fitted correction. It is the coherence forced by
the Pauli section, multiplication cocycle, and Hadamard transport.

Changing the Pauli section changes \(\beta\) by the corresponding coboundary,
while the projective obstruction class remains invariant.

## Double-category interpretation

Use \(H\) as the horizontal source/frame transformation and \(P(v)\) as the
vertical intervention. Then:

- \(h\) is the Sum shadow of the square;
- \(\beta\) is its Product coherence cell;
- the operator equality is its Endo realization.

The square is strict in the additive quotient but weak in the chosen operator
section. All three readings belong to one packet.

## Control-theoretic interpretation

The additive controller transports the command state by \(h\). A phase-aware
controller also updates the scalar memory by \(\beta(v)\). The quantum plant
implements the full intertwining relation.

If the controller transports only labels, it predicts the correct projective
command but cannot distinguish the mixed-command sign. An interferometric or
phase-sensitive port is required to observe that coherence.

This is a finite example in which:

- coarse command covariance passes;
- scalar coherence carries the hidden correction;
- full actuator covariance requires both.

## Failure signatures

1. **Erase Product coherence:** the \(X\) and \(Z\) squares still pass, while
   the \(XZ\) square fails by a sign.
2. **Use the wrong label transport:** a pure \(X\) or \(Z\) command already
   fails at the Sum lens.
3. **Change Pauli section without transporting \(\beta\):** projective labels
   agree but the Endo square becomes convention-inconsistent.
4. **Declare the phase physically executable:** mathematical coherence is
   mistaken for an actuator constructor.
5. **Check only scalar determinant:** every Pauli and Hadamard determinant
   shadow is too coarse to certify the intertwining relation.

## Explanatory status

This packet is a positive finite realization of the double-functor proposal.
It does not merely classify a result. It predicts exactly which lower-lens
test survives when the phase cell is erased and which mixed command first
falsifies strict covariance.

The example is algebraically complete. Physical implementation of \(H\), the
Pauli commands, and a phase-sensitive readout remains a separately typed
control problem.
