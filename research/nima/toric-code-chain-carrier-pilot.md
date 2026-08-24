# Toric-code chain Carrier pilot

## Question

Can Marici's sequence

\[
\text{legal operation}\to\text{residue}\to\text{repair}\to\text{readout}
\]

recover the elementary architecture of a topologically ordered system without
inserting its usual physical interpretation?

## Source-independent finite model

For the periodic square lattice over \(\mathbf F_2\), take the cellular chain
complex

\[
C_2\xrightarrow{\partial_2}C_1\xrightarrow{\partial_1}C_0.
\]

An edge chain \(e\in C_1\) is an error history. Its vertex syndrome is

\[
s(e)=\partial_1e.
\]

Face boundaries are local repairs because

\[
e\sim e+\partial_2f,
\qquad
\partial_1\partial_2=0.
\]

The residue-free histories modulo local repair are

\[
H_1=\ker\partial_1/\operatorname{im}\partial_2.
\]

This already supplies a hostile test of a tempting Marici claim:

\[
\text{zero local residue}\not\Rightarrow\text{globally trivial history}.
\]

## Exact census

For an \(L\times L\) periodic lattice, the checker verifies for
\(2\le L\le5\):

\[
\partial_1\partial_2=0,
\qquad
\dim H_1=2.
\]

At \(L=2\), all \(2^8=256\) edge histories are enumerated. There are eight
realized local syndromes. Every syndrome fiber contains 32 histories and,
after quotienting by the eight face-boundary repairs, exactly four logical
classes remain.

Thus even complete local syndrome data leaves two global bits unresolved:

\[
\boxed{
\text{local residue classifies repair demand, while homology classifies
residue-free global capability.}
}
\]

## First Marici translation

| Toric-code datum | Marici role |
|---|---|
| edge chain \(e\) | labelled operational history |
| \(\partial_1e\) | local coherence residue/syndrome |
| face boundary \(\partial_2f\) | legal local repair |
| \(\partial_1\partial_2=0\) | repair preserves syndrome typing |
| \(H_1\) | globally persistent capability invisible to local residue |
| logical loop probe | nonlocal readout port |

The important correction is that the persistent object is not accumulated
error. It is a legal, residue-free global class. Marici therefore needs at
least two readout channels in this sector:

1. a local syndrome readout detecting endpoints;
2. a nonlocal cycle pairing detecting homology.

Neither channel reconstructs the other.

The positive complement is also exact. Add two cocycles represented by a
vertical and a horizontal cut. They measure the two noncontractible winding
classes and vanish on every face boundary. For every tested \(2\le L\le5\),
the combined map

\[
e\longmapsto
\bigl(\partial_1e,\langle\ell_x,e\rangle,
\langle\ell_y,e\rangle\bigr)
\]

has kernel exactly \(\operatorname{im}\partial_2\). Thus local syndrome plus
two global loop ports is jointly faithful modulo legal local repair. Neither
more local syndrome resolution nor a preferred decoder is required for that
classification theorem.

The decoder is genuinely extra structure. On the \(3\times3\) torus, choose
the syndrome supported at the diagonally adjacent vertices \((0,0)\) and
\((1,1)\). Exact enumeration finds two minimum-weight corrections, both of
weight two. Their difference is a face boundary, so they represent the same
legal repair class. The chain complex fixes the syndrome fiber and its repair
equivalence, but it does not select one path:

\[
\boxed{
\text{error model or dynamics selects a decoder; homology alone does not.}
}
\]

This reproduces, in a real physical sector, Marici's selector-versus-
rigidifier distinction. Local repair equivalence rigidifies the capability
class; it does not choose the physical recovery operation.

## What is genuinely new

Earlier Marici work showed that a syndrome need not determine an internal
repair. The topological pilot adds the converse limitation: a complete local
syndrome can vanish while a protected global capability remains nontrivial.
The distinction is source-canonical because it is the homology of the same
chain complex that defines the syndrome and repairs.

This suggests a sharper shared architecture:

\[
\text{Carrier complex}
\longmapsto
\bigl(\text{boundary residue},\ \text{homology capability}\bigr),
\]

not a single error channel.

## Next hostile tests before sector handoff

1. Add the dual cochain complex and verify the two complementary syndrome
   families and their intersection pairing.
2. Only afterward hand the programme to `marici.Kitaev` for physical source,
  Hamiltonian, excitation, and braiding typing.

## Verification

- Checker: `research/nima/checkers/check_toric_code_chain_carrier.py`
- Dependency-free invocation:
  `python research/nima/checkers/check_toric_code_chain_carrier.py`
