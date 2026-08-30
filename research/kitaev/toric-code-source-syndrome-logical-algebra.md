# Finite toric code: source, syndromes, and logical algebra

Status: finite-cutoff theorem for periodic square lattices checked at
`2 <= L <= 5`; the algebraic derivation is valid for the frozen finite
cellulation.  This packet covers WP1--WP3 only.

## Frozen conventions

Let vertices, horizontal edges, vertical edges, and faces be labelled by
`(x,y)` in `Z/LZ x Z/LZ`.  Orient horizontal edges from `(x,y)` to
`(x+1,y)`, vertical edges from `(x,y)` to `(x,y+1)`, and faces
counterclockwise.  Orientation signs disappear after transport to
`F_2`, but the integral orientation remains part of the source label.

There is one qubit on each edge, so `n=2L^2`.  On the edge Hilbert space set

\[
A_v=\prod_{e\ni v}X_e,\qquad
B_f=\prod_{e\subset\partial f}Z_e,\qquad
H=-J_e\sum_vA_v-J_m\sum_fB_f,
\]

with `J_e,J_m>0`.  Thus an `A_v=-1` defect is called electric and a
`B_f=-1` defect magnetic.  Every star and face share zero or two edges, so
all Hamiltonian terms commute.  The ground space is their common `+1`
eigenspace.  The two global stabilizer relations are
`prod_v A_v=prod_f B_f=I`; hence its dimension is
`2^(2L^2-(2L^2-2))=4`.

An admissible local Pauli operation is a finite-support product
`P(x,z)=X^x Z^z`, with phase suppressed for syndrome and quotient
calculations.  The primal complex is
`C_2 --d2--> C_1 --d1--> C_0`.  The dual complex is separately labelled;
under the square-cell correspondence its boundary is represented by the
transpose incidence maps, not identified with the primal complex by fiat.

## Syndromes derived from commutation

The one-qubit law `XZ=-ZX` gives

\[
A_vP(x,z)=(-1)^{\langle d_1^Tv,z\rangle}P(x,z)A_v,
\]

so the electric syndrome of a Pauli is

\[
s_e(P)=d_1z\in C_0.
\]

Likewise

\[
B_fP(x,z)=(-1)^{\langle d_2f,x\rangle}P(x,z)B_f,
\]

and therefore the magnetic syndrome is

\[
s_m(P)=d_2^Tx\in C_2^*.
\]

These formulas are consequences of overlap parity in the Pauli algebra.
Only after that derivation do they become the primal boundary and dual
boundary maps.  Multiplying a `Z` history by a plaquette stabilizer adds
`d_2f` and preserves `s_e` because `d_1d_2=0`.  Multiplying an `X` history
by a star stabilizer adds `d_1^Tv` and preserves `s_m` by the transposed
identity.  The checker deliberately deletes one edge from a face and obtains
a nonzero two-vertex chain-condition obstruction.

## Logical quotients and pairing

Residue-free `Z` strings modulo `Z` plaquettes give

\[
\mathcal L_Z=\ker d_1/\operatorname{im}d_2\cong H_1(T^2;\mathbf F_2),
\]

while residue-free `X` strings modulo `X` stars give

\[
\mathcal L_X=\ker d_2^T/\operatorname{im}d_1^T\cong H^1(T^2;\mathbf F_2).
\]

Both have dimension two.  Their evaluation/intersection pairing is

\[
\langle[x],[z]\rangle=x\cdot z\pmod2,
\qquad X^xZ^z=(-1)^{x\cdot z}Z^zX^x.
\]

For primal horizontal/vertical cycles `Z_x,Z_y` and dual transverse cuts
`X_y,X_x`, respectively, the checked pairing matrix is the identity after
ordering dual generators by the primal cycle they cross.  Consequently each
matched noncontractible pair anticommutes and the unmatched pairs commute.
This is the two-qubit logical Pauli algebra.

These ordered coordinates are a **framed theorem**.  The frozen `(x,y)`
labels mark a homology basis.  If that marking is not physical data, the
mod-two mapping-class image `GL(2,F_2)` acts transitively on the three nonzero
logical vectors: an individual loop bit does not descend, while zero versus
nonzero does.  A lattice seam, boundary pattern, preparation circuit, or
explicit reference loop can supply the marking only when it is retained as
relational source data; choosing coordinates on paper does not.

## Carrier versus quantum coefficient lens

Carrier geometry supplies labelled cells, incidence, primal/dual support,
cycle and boundary quotients, and the mod-two intersection form.  It does
not supply qubits, `X` and `Z`, operator phases, a positive Hamiltonian, a
ground eigenspace, or measurement probabilities.  The quantum coefficient
lens transports incidence supports into a Pauli symplectic module; the phase
`(-1)^intersection`, stabilizer code space, and state--effect readout live
there.  In particular, homological intersection predicts the exponent, but
Pauli multiplication turns it into physical anticommutation.
The unframed intersection pairing remains invariant under simultaneous
transport of both arguments, even though their ordered coordinate bits do
not.

## Assumptions and falsifiers

Assumptions are periodic square incidence, one qubit per edge, the displayed
CSS convention, positive couplings, and phase-forgetting only in the binary
syndrome calculation.  A nonzero star--plaquette overlap parity, a syndrome
not equal to the commutator vector, a degenerate intersection pairing, or a
ground-space dimension other than four falsifies this packet.

Primary sources: Kitaev's original toric-code construction and the
Dennis--Kitaev--Landahl--Preskill surface-code treatment (arXiv
`quant-ph/9707021` and `quant-ph/0110143`).
