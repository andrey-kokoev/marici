# Protection boundary of the logical commutator record

## Question

Which perturbations leave the controlled logical commutator fixed by topology, and which remain unprotected interface faults?

Let \(Z_\gamma\) be a primal closed-loop operator and \(X_\delta\) a dual closed-loop operator. On the toric code space,

\[
Z_\gamma X_\delta
=
(-1)^{I(\gamma,\delta)}
X_\delta Z_\gamma.
\]

## Claim boundary

### Contractible deformation invariance

Replace the primal representative by

\[
\gamma'=\gamma+\partial\Sigma.
\]

For closed dual \(\delta\),

\[
I(\gamma',\delta)-I(\gamma,\delta)
=
I(\partial\Sigma,\delta)
=
I(\Sigma,\partial\delta)
=
0.
\]

The same holds for contractible deformation of \(\delta\). Therefore the commutator sign depends only on the primal and dual homology classes.

At operator level, contractible loop changes multiply logical representatives by stabilizers:

\[
Z_{\gamma'}=S_ZZ_\gamma,
\qquad
X_{\delta'}=S_XX_\delta.
\]

Toric stabilizers commute with every logical operator in the normalizer. Hence

\[
C(Z_{\gamma'},X_{\delta'})
=
C(Z_\gamma,X_\delta)
\]

on the code space.

This is the protected content of the interferometer: geometrically local rerouting and stabilizer multiplication cannot change the ideal central sign.

### Syndrome does not provide the missing guarantee

Two repairs with the same syndrome can differ by a closed cycle. If that cycle is contractible, the repairs differ by a stabilizer. If it is noncontractible, they differ by a logical operator. Local syndrome cannot distinguish these cases.

Thus syndrome-conditioned correction preserves the commutator protocol only after an additional condition ensures that the realized fault-plus-repair path is homologically trivial. Code distance suppresses low-weight undetectable logical paths; it does not make syndrome choose a unique homology class.

### Interface faults outside topological protection

The following are not removed by homology invariance:

1. a fault on the control qubit;
2. a control-target coupling with an uncontrolled branch phase;
3. failure to implement \(X^{-1}\) or \(Z^{-1}\) as the actual inverse;
4. leakage outside the code space;
5. an error inserted between loop segments whose propagated action is branch dependent;
6. a decoder whose repair differs from the intended repair by a logical loop.

These faults modify the controlled constructor rather than merely deforming its closed-loop representative.

A common target-state error before or after an ideal central commutator does not change the ideal control sign, because \(C=(-1)^I I\). This state independence does not extend to faults occurring inside the controlled sequence.

This packet gives an algebraic protection boundary. It does not supply a threshold theorem, stochastic noise estimate, or fault-tolerant controlled-loop circuit.

## Disposition

The logical commutator has two distinct robustness claims:

- homological robustness: invariant under contractible deformations and stabilizer repairs;
- interface robustness: requires a separate fault-tolerant construction and is not implied by the first claim.

The first falsifier is one of:

1. a claimed local deformation changes the homology class;
2. the multiplying repair is outside the stabilizer group;
3. the loop path has endpoints, so the closed-cycle intersection argument does not apply;
4. the implemented operator leaves the code space;
5. syndrome equality is used to infer equality of logical repair classes;
6. increasing code distance is claimed to calibrate a control-phase fault.

The next constructor theorem must type faults by location in the controlled word and prove that every admitted correctable fault reduces to a stabilizer deformation rather than a logical or control-phase residual.
