# The visible protected D(S3) torus group has order 144

Owner: `marici.Kitaev`

## Bounded question

How does the protected \(C\leftrightarrow F\) duality compose with the modular
mapping-class action on the canonical eight-dimensional torus ground space?

## Exact group

Using the previously reconstructed exact modular matrices over
\(\mathbb Q(\omega)\), exhaustive closure gives

\[
  |\langle S,T\rangle|=72,
  \qquad |\langle S,T,P_{CF}\rangle|=144.
\]

The duality satisfies

\[
  P_{CF}^2=1,qquad [P_{CF},S]=[P_{CF},T]=0,
  \qquad P_{CF}\notin\langle S,T\rangle.
\]

Consequently the visible protected action is

\[
  \langle S,T,P_{CF}\rangle
  \cong \operatorname{im}(S,T)\times\mathbb Z_2^{CF}.
\]

The new duality doubles the mapping-class image but does not generate new
gates through noncommuting conjugation.

## Operation classes

The matrices share one canonical torus Hilbert space, but their physical
origins remain distinct:

- \(S,T\) are large-diffeomorphism or code-deformation operations;
- \(P_{CF}\) is an anyon autoequivalence with a source-supported
  constant-depth duality circuit or self-dual lattice realization.

This packet classifies their visible ground-space action. It does not assert a
single microscopic fault-tolerant schedule containing both operation classes.

## Control boundary

The checker also computes the exact \(\mathbb Q(\omega)\)-linear operator
algebra spanned by each finite group. A proper span inside the 64-dimensional
ambient matrix algebra is an exact obstruction to arbitrary protected torus
control even though the gate group contains a non-Clifford element.

This is the direct-action alternative to the falsified label-bus route. It
supplies a genuine protected non-Clifford gate, but neither \(S_8\) nor the
continuous 36-dimensional endpoint block-control algebra follows.

## Representation-theoretic anatomy

The commutant and center are computed from exact linear equations
\(XS=SX\), \(XT=TX\), and \(XP_{CF}=P_{CF}X\). For a semisimple finite-group
representation

\[
  \mathcal H=\bigoplus_i \mathbb C^{d_i}\otimes\mathbb C^{m_i},
\]

the three dimensions obey

\[
 \dim\mathcal A=\sum_i d_i^2,
 \quad \dim\mathcal A'=\sum_i m_i^2,
 \quad 8=\sum_i d_i m_i.
\]

Together with the center dimension, these identities uniquely determine the
protected isotypic profile recorded by the checker. Multiplicities \(m_i>1\)
are coherent degrees of freedom that every protected gate leaves unresolved;
they are a stronger obstruction than merely counting 49 absent ambient
directions.

The profile is

\[
 (d_i,m_i)=(1,1),(1,2),(2,1),(3,1),
\]

so

\[
 \mathcal A_{\rm prot}\cong
 \mathbb C\oplus\mathbb C\oplus M_2\oplus M_3,
 \qquad
 \mathcal A_{\rm prot}'\cong
 \mathbb C\oplus M_2\oplus\mathbb C\oplus\mathbb C.
\]

The \(M_2\) commutant factor is an exact protected-blind coherent doublet.
Every word in \(S,T,P_{CF}\) acts by one scalar on this entire two-dimensional
multiplicity space. The checker locates its support in the frozen anyon basis;
any proposed completion must contain an operator with a non-scalar compression
to that doublet.

An exhaustive completion test adjoins each coherent sector projector
\(Q_a=|a\rangle\langle a|\) in turn and closes the associative algebra with
\(S,T,P_{CF}\). This tests a Hamiltonian or phase port, not a measurement:
measuring or dephasing \(Q_a\) destroys coherence and does not authorize the
same control algebra. The checker records which individual ports, if any,
promote the 15-dimensional protected algebra to all of \(M_8\).

No single sector projector suffices. Exhausting all 28 unordered pairs gives
exactly four complete families:

\[
 \{Q_A,Q_C\},\quad \{Q_A,Q_F\},\quad
 \{Q_B,Q_C\},\quad \{Q_B,Q_F\}.
\]

Thus two coherent ports are necessary and sufficient within the sector-
projector family. The pattern is exact: choose one of the one-dimensional
electric sectors \(A/B\) and one member of the protected dual pair \(C/F\).
All other 24 pairs leave a proper algebra. The largest incomplete pair is
\(A+B\) or \(A+D\) or \(B+D\), each of dimension 50.

This completion is a controllability statement. A projective measurement of
the same sectors supplies effects and records, not the Hamiltonians
\(e^{itQ_a}\), and therefore does not inherit the \(M_8\) closure.

## Falsifiers

The theorem fails if exact closure has a different order, if \(P_{CF}\) lies
in the modular image, if either commutator is nonzero, or if the protected
operator span equals the full \(8\times8\) matrix algebra.

## Artifacts

- Checker: `checkers/check_s3_torus_protected_gate_group.py`
- Result: `results/s3-torus-protected-gate-group.json`
- Graph admission: `ev-000000003364-c3ab4b85-55fc-450e-ab9d-4fd7d4ac15f6`
- Ledger: `src/ledger/20260825-2459 Protected D(S3) Torus Gates Form an Order-144 Span-15 Algebra.md`
- Two-port completion admission: `ev-000000003367-a3707136-954c-4dd1-83f1-011c359809e0`
- Two-port ledger: `src/ledger/20260825-2462 Exactly Two Coherent Sector Ports Complete Protected D(S3) Torus Control.md`
