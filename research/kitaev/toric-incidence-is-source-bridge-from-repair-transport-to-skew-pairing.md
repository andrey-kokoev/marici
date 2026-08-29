# Toric incidence is the source bridge from repair transport to skew logical pairing

## Question

Is there a pinned Marici system in which transition arrows and skew pairing coefficients arise from one source constructor, rather than being independently fitted?

## Claim boundary

The finite toric code supplies the bridge exactly.

Let \(z\in C_1\) be a residue-free primal Z-chain and \(x\in C_1^*\) a residue-free dual X-cocycle:

\[
\partial_1z=0,\qquad
\partial_2^Tx=0.
\]

Local stabilizer repairs act by

\[
z\longmapsto z+\partial_2b,\qquad
x\longmapsto x+\partial_1^Ta.
\]

The logical pairing is evaluation

\[
\omega(x,z)=x\cdot z\pmod2.
\]

Under both repairs,

\[
\begin{aligned}
\omega(x+\partial_1^Ta,z+\partial_2b)
={}&x\cdot z
+a\cdot\partial_1z
+(\partial_2^Tx)\cdot b
+a\cdot\partial_1\partial_2b.
\end{aligned}
\]

Every correction term vanishes:

- the first by electric syndrome closure \(\partial_1z=0\);
- the second by magnetic syndrome closure \(\partial_2^Tx=0\);
- the third by the chain identity \(\partial_1\partial_2=0\).

Therefore

\[
\omega(x+\partial_1^Ta,z+\partial_2b)=\omega(x,z).
\]

This is the missing bridge. The same cellular incidence data generate:

- transition arrows: addition of local boundaries and coboundaries;
- admissibility: vanishing commutator syndromes;
- pairing coefficients: primal–dual evaluation;
- descent: invariance of evaluation under those transitions.

No separate map from arbitrary transitions to arbitrary pairings is needed. Both are shadows of the chain–cochain evaluation constructor.

### Bridge to the ordered coefficient lens

The quantum lift sends a logical class \(v\in H_1\oplus H^1\) to a Weyl operator \(W_v\) and sends the Carrier pairing to the commutator phase:

\[
W_vW_w
=
(-1)^{\omega(v,w)}W_wW_v.
\]

Thus the source bridge factors as

\[
\text{incidence and evaluation}
\longrightarrow
\text{logical symplectic form}
\longrightarrow
\text{central Pauli commutator}.
\]

The first arrow belongs to shared Carrier geometry. The second requires the quantum coefficient lens.

### Naturality and self-closure

The geometric coherence closes because boundary-of-boundary vanishes. The ordered coherence closes because the Weyl multiplication phase is a 2-cocycle satisfying associativity:

\[
c(u,v)c(u+v,w)=c(v,w)c(u,v+w).
\]

Every logical commutator is central, so

\[
[[W_u,W_v],W_w]=I.
\]

Hence the next ordered rung self-closes. There is no independent triple-order invariant in the ideal logical Pauli sector.

This supplies both forms of the self-closure criterion:

- geometric self-closure by \(\partial^2=0\);
- coefficient self-closure by \(\delta c=1\) and centrality.

### Exact falsifier already present

The existing finite audit deliberately deletes one edge from a face. Then the alleged face boundary has nonzero endpoint residual, so the chain condition fails. In that hostile cell, the last term

\[
a\cdot\partial_1\partial_2b
\]

need not vanish, and local repair can change the proposed pairing.

Thus the bridge is falsifiable at its source: broken incidence simultaneously destroys syndrome invariance, pairing descent, and higher self-closure.

### Authority boundary

This theorem closes the ideal algebraic constructor nerve. It does not close the physical instrument nerve.

The recorded QND audit still lacks an authorized ancilla reset or replacement arrow. Algebraic associativity of logical Pauli operations does not manufacture low-entropy apparatus resources. Therefore:

\[
\text{algebraic self-closure}
\neq
\text{source-closed reusable implementation}.
\]

This is a useful hostile separation, not a defect in the bridge theorem.

## Disposition

The toric code is the smallest pinned example containing the desired bridge. Transition arrows and pairing coefficients share one source: chain–cochain incidence and evaluation. The bridge survives quotienting precisely because syndromes vanish and boundary-of-boundary is zero; the quantum lens then converts the descended pairing into the central commutator phase.

This validates the self-closure criterion on a nontrivial case and gives a reusable search signature: look for a common parent complex whose evaluation pairing is invariant under its repair action. Without such a common parent, transition holonomy and Pfaffian pairing must remain independent.