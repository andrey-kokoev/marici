# Anomaly totalization is a joint relative character

## Separate scalarization is not source-defined

The primitive atomic current has exponential growth on the logarithmic scale
and requires an exponential/Laplace test rigging. The square current is
tempered but has infinite total mass. The undamped critical-line sine readout
is not an admissible absolute pairing for either completed current separately.

Consequently, the completed primitive and square channels do not define two
independent scalar characters. Their finite-cutoff exponentials exist, but
their limits are meaningful only relative to archimedean, endpoint, and
zero-frequency boundary data.

## Partial constructor

The source-compatible totalization has the signature

\[
\operatorname{RelTot}:
E'_{\exp}
\times
\mathcal S'
\times
\mathcal D_3
\times
A_\infty
\times
B_0
\rightharpoonup
L_{\det}.
\]

The factors represent the primitive current, square current, order-three
determinant tail, archimedean completion, and zero-frequency boundary port.
The constructor is defined only on the compatibility subobject where their
cutoff divergences and boundary transitions cancel according to the
source-derived Tate sewing law.

This is a relative character: it is multiplicative on compatible joined
packets, but its individual anomaly factors need not be scalar-valued.

## Categorical meaning

The anomaly carriers are line objects or distributional torsors rather than
ordinary scalar ports. Archimedean sewing supplies a trivialization of their
joint tensor product. The operative coherencer is the source map that constructs
this trivialization across cutoff refinement.

A proposed factorization into separate characters is stronger than required
and generally ill-typed. Conversely, a scalar finite-part prescription is too
weak unless it lifts to the joint line object and respects its separate source
gradings.

## Relation to the synthesis graph

The arithmetic-to-analytic synthesis graph retains the atomic currents before
scalarization. The relative totalization acts on that graph together with the
archimedean and zero-frequency ports. This ordering is forced:

1. construct labelled arithmetic currents;
2. synthesize their analytic tail–seam state while retaining the labels;
3. sew the joint boundary packet;
4. only then evaluate the determinant line.

Reversing the second and third operations attempts to reconstruct
distributional anomaly data from a smooth analytic quotient and fails the
adjacent-label continuity test.

The graph is still only a presentation. Before totalization, quotient it by
the complete fibers of the joint analytic, primitive, square, archimedean,
zero-frequency, reciprocal, and cutoff target family. The relative
totalization must then be constant on every resulting full fiber at its native
arity. Linear kernel tests alone do not establish this for the nonlinear
completed constructor.

## Finite falsifiers

Three tests reject a proposed relative totalization:

1. it assigns a completed scalar to the primitive or square current alone
   using the undamped critical readout;
2. it cancels primitive and square divergences against each other while
   erasing their distinct source grades;
3. its joint finite value is stable at each cutoff but fails naturality under
   cutoff refinement or reciprocal dagger sewing.

## DPC verdict

The missing global object is not a pair of scalar anomaly characters. It is a
single source-derived trivialization of their joint relative determinant line,
with the primitive and square carriers still separately typed. This is the
precise boundary constructor that must be extracted from the completed Tate
sewing law.

## Verification

`check_rh_joint_relative_character.py` verifies a finite joint-renormalization
fixture in which individual components grow while the typed relative value is
stable, then rejects cross-grade cancellation and refinement-dependent
counterterms.
