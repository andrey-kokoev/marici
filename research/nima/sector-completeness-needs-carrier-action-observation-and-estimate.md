# Sector completeness needs carrier, action, observation, and estimate

## Correction to the three-gate compiler

Carrier splitting, action splitting, and completion estimates are not enough.
The readout may still identify independently actuated sectors.  Observation is
a separate gate.

The minimal sector-completeness stack therefore has four layers.

## Gate 1: carrier splitting

Source-authorized idempotents decompose the state carrier into typed sectors.
This is an object-level statement.

## Gate 2: action splitting

The admitted noncentral actions independently address those sectors.  This is
a controllability or action-fullness statement.

## Gate 3: observation splitting

The declared readouts, including their propagation under the source dynamics,
separate the sectors and every admissible state direction.  This is an
observability or joint-faithfulness statement.

## Gate 4: estimate splitting

The action and observation witnesses retain cutoff-uniform lower bounds in the
declared source topology.  This is the completion-stability statement.

## Hostile 1: control without observation

Let the carrier be \(V=\mathbf R^2\), with its two coordinate idempotents.
Take the control matrix

\[
B=I_2.
\]

Both sectors are independently actuated.  Let the dynamics vanish and use the
single readout

\[
C=\begin{pmatrix}1&1\end{pmatrix}.
\]

The antisymmetric state \((1,-1)\) is invisible.  Carrier and action splitting
pass while observation splitting fails.

Adding a second identical readout does not help.  The observation rank remains
one.  A signed or dynamically propagated independent row is required.

## Hostile 2: finite observation without a completion estimate

At cutoff \(N\), use

\[
C_N=
\begin{pmatrix}
1&0\\
0&N^{-1}
\end{pmatrix}.
\]

Every finite \(C_N\) is injective.  Yet its smallest singular value tends to
zero, so the second sector becomes invisible at completion.  Finite
observability does not imply uniform observability.

The dual hostile applies to action matrices and controllability Gramians.

## Categorical form

The four gates have distinct categorical types:

1. carrier splitting is a Karoubi or idempotent-completion property;
2. action splitting is fullness of the admitted action on the summands;
3. observation splitting is joint faithfulness of the readout family;
4. estimate splitting is bounded fullness and faithfulness in the enriched
   completion.

No gate can be inferred from a later-looking scalar equality.

## Theta reading

Reciprocal framing supplies carrier splitting.  A noncentral sheet-asymmetric
operator would supply action splitting.  Grothendieck's triangular tail shows
that the adjoint observation gate is independent: forcing the reverse equation
can reject genuine Evans zero-states and change the divisor.  A valid observer
must preserve the zero-to-state bridge before any positivity or spectral
estimate is considered.

Eventual compact exclusion remains the estimate gate.

## Kitaev reading

Central block characters split the endpoint carrier.  The dynamical Lie
closure tests action splitting.  A physically authorized measurement family
must separately observe every independently controlled block.  Fault-tolerant
uniform bounds then supply the estimate gate.

## Strominger reading

The universal Hall quotient splits the carrier of presentations.  Adjoint
cocircuit lifts provide candidate actions or observers.  Growing deep-column
support may destroy either observation continuity or the final uniform
estimate even when every finite chart is algebraically valid.

## Flavor reading

Distinct stage observers may be separate records and independently perturbed,
yet a common scalar flavor readout can annihilate their difference.  Signed
observer rows or source dynamics must establish observation rank before a
numerical prediction can be called complete.

## Compiler output

For every multisector claim, report:

1. source idempotents;
2. noncentral controllability rank;
3. observability rank and invisible-state witnesses;
4. cutoff-uniform Gramian or right-inverse bounds.

The first failed gate is the typed frontier.

