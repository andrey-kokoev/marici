# A two-plus-one coherence system is a homotopy pullback with a bridge-state sector

Owner: marici.Kitaev

## Question

What is a system consisting of two peer tetrahedral or higher-filler systems
plus one additional system whose role is to compare them?

## Claim boundary

The natural \(2+1\) architecture is not three symmetric replicas. It is a
homotopy pullback, or equivalently a shifted mapping-cone construction:

- two peer complexes carry the states or completed coherencers being compared;
- one interface complex carries the comparison witness.

Let \(A\) and \(B\) be the peer constructor complexes and let \(I\) be the
interface or comparison complex. Suppose the two peer outputs enter the
interface through cochain maps

\[
f:A\to I,
\qquad
g:B\to I.
\]

For degree-\(n\) closed peer states \(a\in A^n\) and \(b\in B^n\), the \(+1\)
system carries an interface witness

\[
h\in I^{n-1}
\]

satisfying

\[
d_Ih=f(a)-g(b).
\]

The triple

\[
(a,b,h)
\]

is a homotopy-coherent match. It does not require strict equality
\(f(a)=g(b)\); it requires their mismatch to be filled by an authorized
interface state.

### Why this is a shifted mapping cone

Define

\[
F=f-g:A\oplus B\to I.
\]

The homotopy pullback is modeled by the shifted cone

\[
\operatorname{Cone}(F)[-1].
\]

Its degree-\(n\) elements are triples

\[
(a,b,h)\in A^n\oplus B^n\oplus I^{n-1},
\]

with differential, up to the chosen sign convention,

\[
D(a,b,h)
=
(d_Aa,d_Bb,F(a,b)-d_Ih).
\]

Then

\[
D(a,b,h)=0
\]

is exactly the condition that both peer states close and the interface witness
fills their difference.

This is the algebraic meaning of a top coherencer comparing the final
coherencer of a source system with the final coherencer of a behavior system.

### The \(+1\) system has its own state

The interface is not merely a Boolean equality check. The witness \(h\) can
carry:

- orientation or phase;
- a repair history;
- resource cost;
- defect flux;
- environment record;
- a torsor frame;
- an ordered noncommutative comparison.

Therefore the \(+1\) port is a state-bearing bridge. Erasing it after checking
the endpoints loses precisely the higher information identified in the filler
torsor analysis.

### Existence, ambiguity, and higher symmetry

The equation

\[
d_Ih=f(a)-g(b)
\]

has a solution exactly when the cohomology class

\[
[f(a)-g(b)]\in H^n(I)
\]

vanishes.

Thus \(H^n(I)\) contains the obstruction to forming a coherent \(2+1\) object.

If one solution \(h_0\) exists, every other solution is

\[
h=h_0+z,
\qquad
z\in Z^{n-1}(I).
\]

Modulo authorized interface gauge changes \(z\sim z+d_Iu\), the inequivalent
bridge choices form a torsor under

\[
H^{n-1}(I).
\]

The next group \(H^{n-2}(I)\) controls higher automorphisms of those bridge
choices in the abelian model.

The mapping cone therefore produces the tower automatically:

- \(H^n(I)\): obstruction to a bridge;
- \(H^{n-1}(I)\): ambiguity among bridges;
- \(H^{n-2}(I)\): symmetry among bridge comparisons.

### Minimal \(\mathbb F_2\) tetrahedral instance

Let the two peer tetrahedral systems have volume syndromes

\[
\Omega_A,\Omega_B\in\mathbb F_2.
\]

A comparison that reads only their relative volume sees

\[
\Delta=\Omega_A+\Omega_B.
\]

If the interface has a face-level state \(h\) with boundary map
\(\delta_I\), coherence requires

\[
\delta_Ih=\Delta.
\]

Three regimes are distinct.

1. If \(\operatorname{im}\delta_I=0\), only equal peer syndromes can be joined.
2. If \(\operatorname{im}\delta_I=\mathbb F_2\), every mismatch can be absorbed
   by the interface.
3. If the interface has several face states with the same boundary, the
   mismatch can be repaired but the bridge retains a logical ambiguity.

The second regime is not automatically preferable. An interface that can
absorb every mismatch may hide peer defects unless its state \(h\) remains
observable and source-authorized.

### Common mode remains invisible

The relative port satisfies

\[
(\Omega_A,\Omega_B)
\longmapsto
\Omega_A+\Omega_B.
\]

Its kernel contains

\[
(0,0)
\quad\text{and}\quad
(1,1).
\]

Thus simultaneous equal flux in both peers is invisible to the comparator. The
\(+1\) bridge detects disagreement, not absolute correctness.

To distinguish common mode, the architecture needs an independent source
reference, an absolute syndrome port, or a task law excluding the common
nonzero sector. A comparator cannot manufacture that authority.

### Control-theoretic rotation

In control language:

- \(A\) and \(B\) are two plants or two realizations;
- \(f(a)\) and \(g(b)\) are their task-localized outputs;
- \(I\) is a dynamic interface model;
- \(h\) is the compensator or simulation state;
- \(d_Ih=f(a)-g(b)\) is the regulator or matching equation.

A static comparator corresponds to an interface with no internal state. A
dynamic compensator is exactly the \(+1\) system.

The internal modes in \(H^{n-1}(I)\) are zero-output bridge modes. They may be
harmless gauge, stored controller memory, or dangerous hidden state depending
on the task.

### Categorical rotation

Categorically, the architecture is a span of comparison data or a
pseudo-pullback:

\[
A\longrightarrow I\longleftarrow B.
\]

The object of compatible pairs must include the isomorphism or 2-cell joining
their images. An ordinary strict pullback discards that cell and is therefore
too rigid whenever comparison is only coherent up to process.

The \(+1\) object is precisely the retained comparison 2-cell.

### Dual and network rotation

Under cellular duality, the interface cochain becomes a dual chain whose
boundary terminates on the two peer defects. The bridge is then literally a
carrier joining two syndrome sources.

In network language, the \(+1\) is a factor node with internal state. It
enforces a relation between two variable nodes but can itself possess hidden
modes and faults.

This explains why a four-port or transistor analogy can be suggestive but not
categorically exact: the essential feature is not port count. It is the typed
mediator state and its incidence with the two peers.

### Hostile cases

The \(2+1\) interpretation fails or changes type under these witnesses:

- the two peers are treated symmetrically with the comparator, eliminating the
  distinguished bridge role;
- a mismatch is declared repaired although it is not in
  \(\operatorname{im}d_I\);
- existence of one bridge is mistaken for uniqueness despite
  \(H^{n-1}(I)\ne0\);
- a relative comparator is claimed to detect equal common-mode faults;
- the interface absorbs every mismatch but its state is erased from all
  readouts;
- a scalar comparison is used where \(f(a)-g(b)\) is an ordered or
  noncommutative relation;
- the interface map is not source-authorized.

## Disposition

A \(2+1\) system should be typed as:

\[
\text{peer A}
+
\text{peer B}
+
\text{state-bearing comparison complex}.
\]

Its decisive packet is:

- peer complexes \(A,B\);
- interface complex \(I\);
- comparison maps \(f,g\);
- obstruction class in \(H^n(I)\);
- bridge torsor \(H^{n-1}(I)\);
- common-mode kernel;
- interface observability and actuation;
- coefficient lens;
- completion-stable gain.

This architecture is more informative than three symmetric copies. It
separates disagreement detection from absolute truth, and bridge existence from
bridge uniqueness.

The highest-information next audit is to instantiate \(A\) as source
coherence, \(B\) as behavior coherence, and \(I\) as the independently typed
comparison theory. The key question is whether the observed top-level residue
is:

- a nonzero obstruction class;
- an unobserved bridge-state class;
- or a common-mode class invisible to relative comparison.
