# Relational certificates have an arity ladder

## Result

A relational instrument can be complete for metric reconstruction and still be
incomplete for physical orientation.

For rays represented by nonzero vectors (psi_i), distinguish three levels:

1. one-point data record norm or purity;
2. two-point magnitudes record metric geometry and conditioning;
3. cyclic overlap phases record orientation and phase holonomy.

The third level is not derivable from the first two.

## One-point and two-point closure

For pure qubit probes, the syndrome-row Gram entries satisfy

[
K_{ij}=2|langlepsi_i,psi_jangle|^2.
]

The diagonal entries certify normalization. For mixed qubit states the
corresponding Hilbert--Schmidt relation is

[
K_{ij}=2operatorname{Tr}(ho_iho_j),
]

so diagonal self-overlaps also carry purity. Pairwise relational data can
therefore certify rank and conditioning without selecting an absolute Pauli
frame.

However, magnitude data are invariant under complex conjugation:

[
|langleoverline{psi_i},overline{psi_j}angle|^2
=
|langlepsi_i,psi_jangle|^2.
]

A frame and its mirror consequently have identical metric certificates.

## Three-point orientation

The cyclic Bargmann invariant is

[
B_{ijk}
=
langlepsi_i,psi_jangle
langlepsi_j,psi_kangle
langlepsi_k,psi_iangle.
]

Independent phase changes of the three vectors cancel around the cycle, and a
common unitary preserves the invariant. Complex conjugation sends (B_{ijk})
to its conjugate. Hence a nonzero imaginary part distinguishes the two
orientation components that every pairwise magnitude misses.

This proves a strict information hierarchy:

[
	ext{one-point data}
;<;
	ext{pairwise metric data}
;<;
	ext{cyclic orientation data}.
]

The ordering concerns distinguishability, not temporal succession.

## Graph formulation

Choose a graph whose vertices are preparations and whose edges carry pairwise
overlap magnitudes. Edge data determine a metric realization only up to the
symmetries preserving those magnitudes. Triangle holonomies carry the first
phase information invariant under vertex rephasing.

On a connected graph, phases assigned to individual overlaps depend on local
phase choices. Products around cycles do not. A spanning tree fixes the local
phase gauge; independent cycle invariants then contain the residual relational
phase data.

Thus the coherencer is not another edge. It is a cycle observable.

## DPC

A proposed relational certificate for a complex preparation frame is admitted
only if it passes all applicable gates:

1. diagonal self-data establish the declared normalization or purity class;
2. pairwise data establish the required rank and conditioning;
3. a hostile antiunitary or reflection-related realization is tested;
4. if the hostile preserves all pairwise data, an independently
   source-authorized cyclic instrument must separate it;
5. the cyclic observable must be invariant under admitted local phase gauge;
6. all measurements must refer to one typed preparation family under an
   explicit resource law.

Failure at gate 4 proves that the certificate is metric-complete but
orientation-incomplete. Algebraic availability of a Bargmann invariant does
not authorize a physical triple-overlap instrument.

## Cross-sector consequences

### Optics

Aspect's tetrahedral frame is the exact finite witness. Pairwise fidelities
certify its spectrum but not its handedness. One phase-sensitive triple cycle
rejects the complex-conjugate mirror. Photon-mode indistinguishability remains
a prerequisite for the intended overlap semantics.

### Flavor

Magnitude-only masses, widths, or absolute mixing data can close a metric
reconstruction while leaving a conjugation or CP-orientation ambiguity. The
natural next audit is not to add another magnitude probe. It is to identify
the smallest source-derived closed mixing cycle whose imaginary component
changes sign under conjugation, then ask whether the current source grammar
can execute that oriented cycle.

This does not assert that the missing flavor observable is necessarily a
three-vertex optical Bargmann invariant. Flavor may require a longer typed
cycle because production, propagation, and readout occupy different domains.
The transferable theorem is that orientation lives in cycle holonomy rather
than edge magnitudes.

### Strominger

The symmetric and antisymmetric sheet ports solve a different but compatible
problem: character completeness. On the known magnetic kernel, the electric
port is injective when the one-sheet map is injective and two is not a zero
divisor. Arbitrary-state reconstruction still requires their joint
instrument. Character completion and cyclic orientation completion are
independent axes.

### Grothendieck

The source-derived theta boundary current now closes positivity and evenness
of the real source profile through Fourier self-duality and reciprocal-lobe
exclusion. That is not yet orientation of the oscillatory Mellin comparison.
The arity theorem suggests a precise hostile test: determine whether conjugate
or reflected Mellin realizations preserve every currently admitted one- and
two-copy certificate. If they do, search for a source-derived cyclic phase
observable. This is a hypothesis generator, not an RH result.

### Kitaev

Wilson magnitudes or pairwise overlaps can leave conjugation and ribbon
orientation unresolved. The required extra datum is a gauge-invariant cycle
phase, typed separately from character-sector completeness and from the
physical constructor that measures it.

## Finite falsifiers

For any proposed pairwise-complete certificate:

1. complex-conjugate every preparation;
2. verify that all declared one- and two-point records are unchanged;
3. compute one admitted cycle invariant.

If the physical theory distinguishes the two realizations but the declared
certificate does not, the certificate is incomplete. If no source-authorized
cycle instrument exists, the correct result is a typed acquisition
obstruction, not an inferred orientation.

## Frontier

The shared minimum joint instrument is now factored into independent
requirements:

- reachable-locus span;
- metric Gram certificate;
- symmetry-character completeness;
- cyclic orientation certificate;
- same-preparation resource law;
- completion stability.

None can be replaced by another.
