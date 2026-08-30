# Coherent control falsifies a fixed contextual quotient

## Target

The hidden-ancilla repair said that extensional physical content is the contextual-equivalence class of a process relative to declared external contexts.

That is not stable unless the context class is closed under every admitted higher-order constructor.

## Exact hostile

Consider two unitary implementations

\[
U=I,
\qquad
V=-I.
\]

As ordinary quantum channels they are identical:

\[
U\rho U^*=V\rho V^*=\rho
\]

for every state, including states entangled with an external reference. The ordinary channel quotient therefore identifies them.

Now place each implementation under coherent control. The controlled matrices are

\[
\operatorname{ctrl}(U)=
\begin{pmatrix}I&0\\0&I\end{pmatrix},
\qquad
\operatorname{ctrl}(V)=
\begin{pmatrix}I&0\\0&-I\end{pmatrix}.
\]

On control input \(|+\rangle\), their outputs have control states \(|+\rangle\) and \(|-\rangle\). An \(X\)-basis measurement returns expectations \(+1\) and \(-1\). They are perfectly distinguishable.

Thus coherent control is not a well-defined operation on the ordinary channel quotient. It acts on a lift of the channel in which the relative phase is retained.

## What failed

Contextual equivalence at one categorical level need not be a congruence for constructors at the next level. Quotienting first and enlarging the grammar later can erase exactly the cell needed by the enlarged grammar.

There is no context-independent final boundary quotient. There is a stratified family of equivalences indexed by the admitted constructors.

## Repaired statement

> At a declared categorical depth, physical equivalence is the largest congruence preserved by every admitted composition, tensor product, comparison, and higher-order constructor at that depth. Whenever a constructor fails to descend to the quotient, the missing lift becomes a typed cell at the next depth.

This makes accessibility algebraic rather than verbal. A context doctrine must declare not only which ports can be observed, but which constructors may accept processes as inputs.

For the hostile above:

- ordinary state preparation and channel measurement identify \(I\) and \(-I\);
- coherent control does not;
- the phase is therefore a lift cell relative to the channel quotient;
- no extra absolute scalar port is implied.

## Relation to the network grammar

The static quotient from unitaries to channels is contravariantly consistent for ordinary tests. The covariant controlled constructor does not factor through it. Their comparison square has a sign residual. The correct network retains that residual rather than calling the channel quotient final.

This is the same architecture as Strominger's central full twist: projective identity at one level, nontrivial comparison after a lifted composition, and trivialization after doubling.

## Next falsifier

Attack congruence closure itself. Find an operationally admitted family of higher-order constructors for which no set-sized or locally generated largest congruence exists, or for which closing under one constructor continually creates a new distinguisher at the next depth. That would force a genuinely open-ended context tower rather than a stabilized higher equipment.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_coherent_control_context_quotient_falsifier.py
```
