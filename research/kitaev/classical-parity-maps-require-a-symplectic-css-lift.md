# Classical parity maps require a symplectic CSS lift

## Bounded question

Which additional law is required before two classical parity maps may be
interpreted as quantum CSS syndrome maps?

## Pauli convention and operator derivation

For \(x,z\in\mathbf F_2^n\), write

\[
P(x,z)=X^xZ^z.
\]

Moving the \(X\) factors of one Pauli word past the \(Z\) factors of another
gives

\[
P(x,z)P(x',z')
=(-1)^{x\cdot z'+z\cdot x'}P(x',z')P(x,z).
\]

Thus the commutator is controlled by the symplectic pairing

\[
\omega((x,z),(x',z'))=x\cdot z'+z\cdot x'.
\]

This is derived from the single-qubit relation \(XZ=-ZX\), not declared as a
cellular boundary map.

## CSS typing theorem

Let rows of \(H_X\) label proposed \(X\)-type stabilizers \(P(h,0)\), and
rows of \(H_Z\) label proposed \(Z\)-type stabilizers \(P(0,h)\). They form a
commuting stabilizer family exactly when

\[
H_XH_Z^{\mathsf T}=0.
\]

For an error \((x,z)\), operator commutation gives the two syndrome maps

\[
\sigma_X(x,z)=H_Xz,
\qquad
\sigma_Z(x,z)=H_Zx.
\]

The proposed local-repair subgroup is

\[
\mathcal S=operatorname{row}(H_X)\oplus\operatorname{row}(H_Z),
\]

with the first row space occupying the \(x\) coordinate and the second the
\(z\) coordinate. The same orthogonality law is exactly the descent condition

\[
\mathcal S\subseteq\ker\sigma.
\]

Hence commutation and quotient typing are one residual viewed in operator and
linear-algebra languages.

If \(r_X=\operatorname{rank}H_X\) and
\(r_Z=\operatorname{rank}H_Z\), then orthogonality implies
\(r_X+r_Z\le n\). The logical Pauli quotient is

\[
\mathcal L=\ker\sigma/\mathcal S
\]

and has dimension

\[
\dim_{\mathbf F_2}\mathcal L=2(n-r_X-r_Z)=2k.
\]

Its induced symplectic pairing records logical anticommutation. A choice of
logical basis is additional frame data; the quotient itself does not select
one.

## Classical success does not authorize the lift

Take

\[
H_X=H_Z=
\begin{pmatrix}
1&0\\
0&1\\
1&1
\end{pmatrix}.
\]

Each classical systematic encoder \(x\mapsto(x,H_Xx)\) has distance three,
so each component corrects one classical command/record fault. Nevertheless

\[
H_XH_Z^{\mathsf T}\ne0.
\]

In particular, the first proposed \(X\) check and first proposed \(Z\) check
act on the same qubit and anticommute. Good classical distances therefore do
not supply a quantum coefficient lens.

## Quantum distance is a second optimization

Once the CSS lift is typed, its quantum distance is

\[
d_Q=min_{(x,z)\in\ker\sigma\setminus\mathcal S}
\left|\operatorname{supp}(x)\cup\operatorname{supp}(z)\right|.
\]

This is not either component systematic-code distance. The latter prices
classical command plus record faults; \(d_Q\) prices the qubits supporting a
logical Pauli. Conflating them erases both the repair quotient and the Pauli
support type.

## Carrier geometry versus quantum coefficient lens

The labelled support hypergraph and its incidence matrices are shared Carrier
geometry. Binary parity is a classical coefficient choice. The symplectic
pairing, Pauli commutator, commuting-stabilizer law, repair quotient, and
logical anticommutation require the quantum coefficient lens. Geometry may
propose \(H_X,H_Z\); it cannot make a nonzero commutator residual vanish.

## Exact audit and falsifiers

The checker exhausts every pair of two-row binary matrices for
\(1\le n\le3\). For every commuting pair it verifies repair descent, the
logical quotient cardinality, and the rank formula. For every noncommuting
pair it verifies an explicit repair with nonzero syndrome. It also checks the
hostile distance-three classical fixture and reproduces its anticommutation
with exact Pauli matrices.

The lift is falsified by any nonzero entry of \(H_XH_Z^{\mathsf T}\). A
claimed logical quotient is falsified if \(\mathcal S\not\subseteq\ker\sigma\).
A claimed quantum distance is falsified by a lower-weight centralizer element
outside \(\mathcal S\).

## Claim boundary

This is a finite CSS typing theorem. It does not derive a physical Hamiltonian,
fault-tolerant measurement circuit, decoder, threshold, topological locality,
or source authority for particular matrices. It does not treat subsystem or
non-CSS stabilizer codes.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
8/10. The frozen branches were automatic composition of classical maps and an
independent symplectic coherence cell. Measurements were the commutator
residual, repair descent, quotient dimension, and a classically capable hostile
fixture.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
9/10. Automatic composition was eliminated. One residual was shown to control
both operator commutation and repair descent, and the logical quotient dimension
was recovered. Physical realization, locality, and decoding remain unresolved.
