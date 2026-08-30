# Annotation cycle holonomy and gauge obstruction

## Repairable mismatch versus obstruction

Some constructor annotations take values in an abelian group: phase
exponents, signed resource differences, transition functions, or other
invertible comparison data. For such a component, assign each oriented
rewrite edge \(e:x\to y\) a label \(a_e\in G\).

A change of node presentation by potentials \(p_x\in G\) acts as

\[
a_e\longmapsto a_e+p_x-p_y.
\]

This can move discrepancies between edges but cannot change the sum around
an oriented cycle:

\[
\operatorname{Hol}(C)=\sum_{e\in C}\epsilon_e a_e.
\]

Therefore nonzero cycle holonomy is a presentation-independent obstruction
to globally path-independent annotations.

## Finite theorem

For a connected finite constructor graph with group-valued edge labels, the
following are equivalent:

1. every cycle has zero holonomy;
2. every two directed paths with common endpoints have the same accumulated
   label;
3. there exist node potentials \(p_x\) making every transformed edge label
   zero.

A spanning tree gives a finite test. Integrate potentials along the tree,
then check each non-tree edge. Its residual is the holonomy of the associated
fundamental cycle. One nonzero residual is the smallest global falsifier.

## Three-node witness

For the triangle \(A\to B\to C\to A\), use labels

\[
a_{AB}=2,\qquad a_{BC}=3,\qquad a_{CA}=-4.
\]

The cycle holonomy is \(1\). No node retyping can remove it. Changing the
last label to \(-5\) makes the holonomy zero, after which spanning-tree
potentials trivialize all three edges.

## Essential modality boundary

This gauge theorem applies only to invertible group-valued annotations.
It does not license cancellation of:

- accumulated support obligations under union;
- consumed resources in a positive cone;
- epoch narrowing by intersection;
- fault-model crossings;
- one-way authority grants.

Those live in monoids, semilattices, partial orders, or partial
multicategories. They require literal path equality or an explicitly
authorized comparison constructor. Group-completing them would invent
inverse authority operations.

## Cross-sector consequences

- **Benincasa.** The missing ordered degree-two/three covariant composition
  is precisely the curvature test: derivative terms, commutators, Lie action
  on contacts, and global de-Rham-Cech reduction determine whether local
  transition data have nonzero holonomy. The exact invertible
  Faa-di-Bruno coefficient conversion is a gauge change; it cannot remove a
  nonzero covariant-square obstruction.
- **Grothendieck.** Integrality projection followed by circle heat flow gives
  a canonical positive seam repair with theta norm. Mellin aggregation of
  the full lattice produces the Epstein object
  \(4\zeta(s/2)\beta(s/2)\). Selecting a Riemann minor is not a harmless
  gauge choice: it requires a source-authorized constructor selecting the
  relevant subobject.
- **Kitaev.** Phase exponents can admit group-valued gauge simplification,
  but magic-state counts, work-block peaks, and factory schedules cannot be
  subtracted as if they were phases. The serial/parallel countermodels show
  that the current resource annotation is under-specified, not gauge
  equivalent.
- **Strominger.** Capability grants, leases, epochs, and fault obligations
  are generally noninvertible. A compiler must reject any coherence repair
  that obtains equality only after formal group completion of authority.
- **Arithmetic/RH.** Functional-equation phases and metaplectic transition
  data may have genuine gauge freedom. Prime weights and the coupled
  endpoint-gamma correction do not thereby acquire cancellable authority.
  A nonzero seam holonomy would be a finite obstruction; zero holonomy would
  establish coherence only, not positivity of \(C_Y\).

## Durable statement

> For invertible annotations, cycle holonomy separates presentation changes
> from genuine coherence obstructions. For noninvertible authority data,
> cancellation is forbidden unless a source-authorized inverse constructor
> actually exists.

