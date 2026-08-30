# Controlled loop-order interferometer

## Question

What is the smallest protocol that operationally separates the ordered toric logical algebra from scalar sector labels and determinant data?

Choose one primal logical loop \(Z\) and one dual logical loop \(X\) with odd intersection. Algebraically,

\[
ZX=-XZ.
\]

The minus sign is a global phase if either word is applied alone, so ordinary final-state comparison cannot reveal it.

## Claim boundary

Introduce one control qubit in

\[
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}
\]

and an arbitrary nonzero logical target state \(|\psi\rangle\). Apply the coherently controlled order operation

\[
U_{\mathrm{ord}}
=
|0\rangle\!\langle0|\otimes ZX
+
|1\rangle\!\langle1|\otimes XZ.
\]

Then

\[
U_{\mathrm{ord}}\bigl(|+\rangle\otimes|\psi\rangle\bigr)
=
\frac{|0\rangle ZX|\psi\rangle+|1\rangle XZ|\psi\rangle}{\sqrt2}
=
|-\rangle\otimes ZX|\psi\rangle.
\]

An \(X\)-basis measurement of the control returns the negative eigenvalue with certainty.

For an even-intersection or commutative model, \(ZX=XZ\), and the same protocol returns the positive eigenvalue with certainty:

\[
U_{\mathrm{ord}}\bigl(|+\rangle\otimes|\psi\rangle\bigr)
=
|+\rangle\otimes ZX|\psi\rangle.
\]

The discrimination is independent of the target state because the commutator is central. It measures the projective multiplication cocycle, not a property of a specially prepared ground state.

One coherent control qubit is sufficient. Some coherent reference is necessary: without interference between the two constructor words, their relative sign remains an unobservable global phase. This is minimality of the comparison resource, not a proof that a particular laboratory can implement the controlled loop operations.

Scalar homology labels predict the same endpoint class for both branches. Determinant data also agrees because

\[
\det(ZX)=\det(XZ)
\]

and the commutator \(-I_4\) has determinant one. Neither lens determines the control record.

A classical model can reproduce the record only by adding an order-sensitive internal variable or a signed composition law. That enrichment is not a scalar-label model: it reinstates the missing central extension or an equivalent contextual constructor theory.

The protocol assumes:

1. coherent preparation and \(X\)-basis readout of one control qubit;
2. coherent controlled execution of the two complete logical words;
3. preservation of relative phase across both branches;
4. odd primal-dual intersection;
5. no uncontrolled branch-dependent phase that imitates or cancels the cocycle.

It does not follow from the abstract Wilson algebra that these controls are physically executable.

## Disposition

The protocol answers the Deutsch-style task question: ordered logical composition enables a state-independent loop-order interference record that scalar and determinant shadows do not determine.

Its first falsifier is one of:

1. the loops have even intersection;
2. controlled \(ZX\) and controlled \(XZ\) cannot be defined on one common phase reference;
3. a branch-dependent implementation phase is unconstrained;
4. the measured control record is unchanged when the intersection parity is switched;
5. a purported scalar model reproduces the record only after acquiring an order cocycle, in which case it has changed coefficient lens;
6. algebraic anticommutation is cited without a constructor for coherent control.

The unresolved constructor is physical controlled-loop execution with a common phase frame. The algebra predicts the record conditional on that constructor; it does not supply it.
