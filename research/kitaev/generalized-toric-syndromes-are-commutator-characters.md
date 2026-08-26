# Generalized Toric Syndromes Are Commutator Characters

Fix an oriented finite 2-complex with cellular matrices

\[
\partial_2:C_2\to C_1,
\qquad
\partial_1:C_1\to C_0,
\qquad
\partial_1\partial_2=0.
\]

Place one (n)-level qudit on every oriented edge. Freeze the generalized
Pauli convention

\[
X|j\rangle=|j+1\rangle,
\qquad
Z|j\rangle=\omega^j|j\rangle,
\qquad
\omega=e^{2\pi i/n},
\]

so that

\[
ZX=\omega XZ.
\]

For edge exponent vectors (a,b\in\mathbf Z_n^{E}), define

\[
X(a)=\prod_eX_e^{a_e},
\qquad
Z(b)=\prod_eZ_e^{b_e}.
\]

Tensor-factor commutation gives the operator identity

\[
Z(b)X(a)
=
\omega^{a\cdot b}X(a)Z(b).
\]

This identity, not a cellular declaration, determines both syndrome maps.

## Star syndrome from commutation

For a vertex (v), let (s_v\) be the (v)-th row of \(\partial_1\). Define
the oriented star operator

\[
A_v=X(s_v).
\]

A (Z)-type error (Z(z)) obeys

\[
Z(z)A_v
=
\omega^{s_v\cdot z}A_vZ(z).
\]

Therefore the measured star-eigenvalue shift is the character with exponent

\[
(s_{\mathrm e}(z))_v=s_v\cdot z.
\]

Collecting vertices gives

\[
s_{\mathrm e}(z)=\partial_1z\pmod n.
\]

Thus electric charge syndrome is derived from the commutator of the error with
the oriented star operators. The cellular boundary appears because its rows
are the Pauli exponent vectors frozen in the Hamiltonian.

## Plaquette syndrome from commutation

For a face (f), let (p_f\) be the (f)-th column of \(\partial_2\). Define
the oriented plaquette operator

\[
B_f=Z(p_f).
\]

An (X)-type error (X(x)) obeys

\[
B_fX(x)
=
\omega^{x\cdot p_f}X(x)B_f.
\]

Hence the plaquette-eigenvalue shift has exponent

\[
(s_{\mathrm m}(x))_f=x\cdot p_f,
\]

and therefore

\[
s_{\mathrm m}(x)=\partial_2^Tx\pmod n.
\]

Magnetic flux syndrome is thus derived from operator commutation with the
plaquette terms.

## Hamiltonian consistency

Star and plaquette stabilizers satisfy

\[
B_fA_v
=
\omega^{s_v\cdot p_f}A_vB_f.
\]

But

\[
s_v\cdot p_f=(\partial_1\partial_2)_{vf}=0,
\]

so every star commutes with every plaquette. The chain condition is exactly
the vanishing stabilizer commutator exponent.

For (n=2), orientation signs disappear because (+1=-1\pmod2\). For
(n>2), reversing an edge changes the relevant incidence column and the
edge Pauli exponent sign together. Ignoring orientation is therefore a qubit
accident, not a coefficient-independent convention.

## Exact filled-triangle witness

Use

\[
\partial_1=
\begin{pmatrix}
1&0&1\\
-1&1&0\\
0&-1&-1
\end{pmatrix},
\qquad
\partial_2=
\begin{pmatrix}1\\1\\-1\end{pmatrix}.
\]

Then \(\partial_1\partial_2=0\). For (n=3), a unit (Z)-error on the first
edge has star syndrome

\[
(1,-1,0)^T=(1,2,0)^T\pmod3,
\]

showing the two oriented endpoints. A unit (X)-error on that edge has
plaquette exponent one; on the oppositely oriented third edge it has exponent
(-1=2\pmod3\).

## Shared Carrier and quantum lens

Shared Carrier geometry supplies the oriented incidence matrices and chain
condition. The quantum coefficient lens supplies the edge Hilbert spaces,
generalized Pauli operators, root of unity, stabilizer Hamiltonian, and the
interpretation of commutator characters as measured syndrome.

The formulas may be written as cellular maps only after these operator
conventions have been frozen and the commutators computed.

## Falsifiers

- Declaring syndrome equal to a boundary map without deriving the stabilizer
  commutator.
- Using (ZX=\omega XZ) in one calculation and its inverse convention in
  another.
- Dropping orientation signs for (n>2).
- Defining star and plaquette exponents whose dot product violates
  \(\partial_1\partial_2=0\).
- Treating a zero local syndrome as a preferred decoder or trivial logical
  class.
- Inferring physical measurement circuitry from the abstract stabilizers.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to derive both generalized syndrome maps from the frozen
operator algebra.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Both cellular formulas now arise as commutator-character exponents, and
the chain condition is precisely stabilizer compatibility.
