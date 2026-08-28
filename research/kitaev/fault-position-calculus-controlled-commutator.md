# Fault-position calculus for the controlled commutator

## Question

For the controlled logical word

\[
W=U_m\cdots U_2U_1=sI,
\qquad s=(-1)^{I(Z,X)},
\]

what residual reaches the control record when a target fault is inserted at a specified position?

For the commutator echo, the ideal factors are the four loop operations in \(ZXZ^{-1}X^{-1}\).

## Claim boundary

Define the prefix

\[
P_j=U_j\cdots U_1.
\]

Insert a target operator \(E\) immediately after \(U_j\). The faulty word is

\[
W_{E,j}
=
U_m\cdots U_{j+1}E\,U_j\cdots U_1.
\]

Since \(W=(U_m\cdots U_{j+1})P_j\),

\[
W_{E,j}
=
W\,P_j^{-1}EP_j
=
sE_j^{\mathrm{prop}},
\]

where

\[
E_j^{\mathrm{prop}}=P_j^{-1}EP_j.
\]

Thus fault location matters only through conjugation by the preceding constructor prefix. For Pauli faults and Pauli loop prefixes, \(E_j^{\mathrm{prop}}\) remains a Pauli operator.

The ancilla coherence becomes

\[
\langle X_{\mathrm c}\rangle+i\langle Y_{\mathrm c}\rangle
=
s\,\operatorname{Tr}(\rho E_j^{\mathrm{prop}}).
\]

This gives three exact cases on the code space:

1. If \(E_j^{\mathrm{prop}}\) is a stabilizer, the ideal sign survives.
2. If it has nonzero syndrome, an ideal final syndrome measurement detects it.
3. If it is a nontrivial logical operator, syndrome is zero but the control record becomes target-state dependent.

The undetectable residual is therefore typed by the normalizer quotient

\[
N(\mathcal S)/\mathcal S,
\]

not by syndrome alone.

A target-only trace-preserving channel applied identically after both control branches cannot change the reduced control record. A common target fault before the ideal central commutator changes \(\rho\) but not the ideal sign. Branch-selective faults and faults inserted inside the controlled word are not common-mode and obey the propagated-residual formula above.

Control faults form a different class:

- a control \(Z\) fault flips the inferred intersection sign;
- control dephasing reduces coherence magnitude;
- a control \(X\) fault exchanges the branches and changes the circuit semantics;
- a branch-controlled phase can exactly imitate the topological sign.

These faults do not possess a syndrome in the toric target code unless the control is itself encoded and coupled through a typed fault-tolerant interface.

For a general noisy channel inserted at position \(j\), replace \(E\) by its Kraus operators. The reduced control coherence is then a channel-dependent overlap, not a single propagated Pauli expectation. This packet does not derive a threshold or claim that Pauli twirling is source-authorized.

## Disposition

The first-failed classification is:

\[
\text{fault location}
\longrightarrow
\text{propagated residual}
\longrightarrow
\text{syndrome class}
\longrightarrow
\text{logical quotient}
\longrightarrow
\text{control record}.
\]

The first falsifier is one of:

1. the prefix convention does not match the implemented word order;
2. the inserted fault is not target-local, so prefix conjugation is incomplete;
3. a zero syndrome residual is called harmless without quotienting by stabilizers;
4. a common-mode argument is applied to a branch-selective fault;
5. a control fault is claimed detectable by target syndrome;
6. target-state independence is claimed when the propagated residual is noncentral.

The missing engineering theorem is an encoded-control construction for which every admitted single fault either produces a detectable syndrome, reduces to a stabilizer, or is flagged by an independent control/interface check.
