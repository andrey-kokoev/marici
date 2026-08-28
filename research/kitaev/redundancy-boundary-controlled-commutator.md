# Redundancy boundary for the controlled commutator

## Question

Can redundancy distinguish the topological commutator sign from a control \(Z\) fault that flips the same ancilla record?

Separate two architectures:

1. repeat the complete experiment and compare classical records;
2. encode the coherent control before applying the controlled commutator.

## Claim boundary

### Classical record repetition

Let the ideal record be \(r\in\mathbf F_2\), with \(r=I(Z,X)\), and let run \(i\) report

\[
y_i=r+e_i.
\]

For two runs, the parity check

\[
s=y_1+y_2=e_1+e_2
\]

detects exactly one flipped record but cannot identify the correct value. For three runs, majority decoding corrects one flipped record. The common-mode transformation

\[
(e_1,e_2,e_3)\mapsto(e_1+1,e_2+1,e_3+1)
\]

changes the decoded value while preserving all equality relations among records.

This redundancy protects the reported classical bit under a declared independent-flip model. It does not certify that the coherent controlled commutator was implemented correctly.

### Encoded coherent control

To detect phase flips before actuation, encode the control in the two-qubit phase repetition code

\[
|0_L\rangle=|++\rangle,
\qquad
|1_L\rangle=|--\rangle.
\]

The stabilizer \(X_1X_2\) has eigenvalue \(+1\) on the code. A single physical \(Z_i\) anticommutes with it and is detected. The two-qubit code cannot locate the fault and therefore cannot correct it. The common-mode error \(Z_1Z_2\) preserves the stabilizer syndrome and acts as a logical branch exchange.

For correction of one phase flip, use

\[
|0_L\rangle=|+++\rangle,
\qquad
|1_L\rangle=|---\rangle
\]

with stabilizers \(X_1X_2\) and \(X_2X_3\). Their two syndrome bits locate one \(Z_i\). The weight-three operator \(Z_1Z_2Z_3\) is a syndrome-silent logical branch exchange.

The required encoded actuator is

\[
U_L
=
|0_L\rangle\!\langle0_L|\otimes I
+
|1_L\rangle\!\langle1_L|\otimes C(Z,X).
\]

Possession of the repetition code does not construct \(U_L\). A physical implementation must show that faults in the encoded control coupling do not spread into an undetectable logical operation on the toric target.

### Separation of guarantees

| mechanism | detects | does not certify |
|---|---|---|
| two classical records | one inconsistent output flip | correct value or actuator integrity |
| three classical records | corrects one output flip | common-mode error |
| two-qubit phase code | one pre-actuation phase flip | correction |
| three-qubit phase code | corrects one pre-actuation phase flip | logical common-mode fault |
| toric target syndrome | target excitations | control faults or logical target faults |

These are conditional finite-code statements. They do not provide a threshold theorem or a fault-tolerant construction of the encoded actuator.

## Disposition

Redundancy moves the first undetectable fault to a higher-weight or common-mode class only after the fault model and interface are frozen. It never proves the topological sign by repetition alone.

The first falsifier is one of:

1. record flips are correlated while independence is assumed;
2. majority correction is claimed with fewer than three records;
3. a two-qubit phase code is claimed to correct an unknown single \(Z_i\);
4. target syndrome is used as evidence about a control-only fault;
5. an encoded control state is presented without an encoded controlled actuator;
6. common-mode or logical errors are omitted from the admitted fault set.

The remaining constructor problem is fault propagation through \(U_L\): classify every single physical fault in the encoded control and coupling by its final control syndrome, target syndrome, and logical residual.
