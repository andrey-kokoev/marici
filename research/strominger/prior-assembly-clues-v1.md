# Prior research clues for the N-14/composite-neutron question

**Follow-up executed:** the [reference-only N-14 search](reference-only-n14-search-v1.md)
tested the unchanged prior grammar through origin 10. Neutral N-14 remains
absent within those finite bounds; a revalidated 7P/7N/5e charge control passes.

## Main correction

The prior work contains a more conservative alternative to enlarging neutron
bodies: **the existing seed-driven reference rules already allow N readers
whose reference proton is not occupied**. The isotope-search ansatz added an
occupied-reference requirement. That restriction should be investigated before
inventing a whole-octahedron neutron law.

This note distinguishes source reading from fresh execution. Other-owner files
and receipts were not edited. The earlier large searches and Python native
bridges were read, not newly certified by this review.

## 1. Unoccupied reference geometry is not a constructed particle

Sources:
- `../nima/generative-phase-assembly-v1.md`, especially “Inputs and stage convention”.
- `../nima/generative-phase-assembly.mjs`, `completeN`, `outgoing`, `describe`, `inspect`.
- `../nima/origin-bounded-assemblies-v1.md`.

The generator obtains a neutron's complementary C0 from the actual regular-P
neighbor across its native reference face. **That P need not be occupied.**
Only selected records contribute particle counts. Native inverse-PN can later
construct the P; it is not forced just to define N's reader.

By contrast, `lithium6-assembly-model.mjs` rejects any nuclear geometry containing
an N without an occupied P neighbor, and builds its N charts from occupied PN
interfaces. Removing only the enumeration rejection would therefore be
insufficient: the compiler's chart construction must also accommodate the
existing reference-only convention.

### Small fresh replay

Using the unchanged prior generator, a complete four-operation enumeration
produces **112 configurations**, with layer counts `1,2,6,21,82`. It contains an
exit-certified **1P/2N/1e** construction:

`PN -> NN-phase-advance -> NE`.

One neutron has a valid native P reference that is **not occupied**. Every
occupied face contact is witnessed and every selected packet reaches an exit.
This is a concrete counterexample to treating the occupied-P condition as a
necessary consequence of the retained source rules. It is not an N-14 witness
or a physical isotope identification.

**Usefulness:** a targeted N-14 search using this already implemented chart
convention is a smaller change than redefining a neutron's volume. Previous
bounded negatives remain correct for their stated ansatz, not for this larger
reference grammar.

## 2. The subdivision diagonal is a supplied choice

Source: `emergent-cm-incidence-audit-v1.md` and
`checkers/check_emergent_cm_roles.mjs`.

Before subdivision, all 24 coordinate permutations preserve the supplied
assembly. The chosen octahedral diagonals leave eight tested symmetries and an
invariant **unnamed** 2+2 partition; the blocks can still be exchanged.
The note explicitly calls the subdivision an implementation choice, not a
source-derived physical rule.

**Usefulness:** the new whole-octahedron probe's fixed-root obstruction is
conditional on this diagonal choice. Test alternative subdivisions while
retaining the actual root marking and recording coordinate/reader adapters.
Do not silently recolor the root or assume that subdivisions are physically
interchangeable. A common refinement can compare geometry, but native primitive
operations must still be transported explicitly.

## 3. Regular electron targets and local generation already exist

Source: `../nima/generative-phase-assembly-v1.md` and implementation `outgoing`.

NE admits the actual regular or split primitive across the ordered face.
The prior generator does not require a finite 343-cell ambient list, a chosen
isotope layout, or a retained earlier isotope. It keeps all compatible branches
rather than automatically filling every terminal E opportunity.

A fresh local replay of all **24 ordered seed markings** gives **8 regular E
endpoints and 16 split E endpoints**, with the existing transfer validations.
This confirms that the successful local octahedron-boundary embeddings were
not a new electron constructor; that geometry was already available in the
broader reference grammar.

The recent original-domain “permit regular electrons” N-14 test still failed,
but it retained the occupied-P requirement and other nuclear restrictions.
That result does not test all these prior conventions jointly.

**Usefulness:** favor a targeted search over the existing local rule system,
with explicit packet/origin limits and all-contact certification, before a
new composite-particle law. Avoid presenting a resource-limited search as a
complete whole-domain negative.

## 4. Reader gluing machinery exists—with a metric and scope boundary

Sources:
- `packet-handoff-naturality-06-v1.md`.
- `../voevodsky/belt-three-by-twelve.md`.
- `neutron-arrow-native-bridge.md`.

The prior native-source work constructs source encoders, metric-aware local
inverse charts and coherent reconstruction. In its notation:

`E_p = R_p K`, `S_p = E_p* E_p`, `D_p = S_p^-1 E_p*`,
`D_glue = sum_p (S_total^-1 S_p) D_p R_p`.

It checks reconstruction against the actual native return. **Uniform averaging
fails for the neutron** because geometric mode weights differ. The neutron
belt has three paired-face sectors with twelve intrinsic coordinates each;
its embedding into the old 54-coordinate geometry has explicit conversion
maps. Equality of collective return does not identify all local stage maps.

**Usefulness:** these are concrete tools for comparing genuine source-derived
readers, not a justification for declaring unknown octahedron vertices passive.
One must first construct an encoder from octahedral boundary data into the
actual native module, retain its metric, and test every required primitive and
reader square. No such octahedron encoder was located in this search.

## 5. “Several tetrahedra” can mean a refinement, not extra particles

Source: `../voevodsky/three-tetrahedron-belt.md`.

The prior work implements a 2-to-3 Pachner move on the same triangular
bipyramid, preserving its oriented outer boundary and total volume. A six-cell
common refinement retains both parent decompositions. The paper explicitly
rejects reading this as adding a neutron to unchanged old bodies. It also
lists new directed arrows a proposed expanded K4 interpretation would need;
the picture does not generate them.

**Usefulness:** compare alternative diagonal/support decompositions through
explicit refinement and retained histories. This is a template for avoiding
particle-count changes merely because a volume has been subdivided differently.
It is not itself a neutron identity law.

## 6. Stronger warning: reference windows are not the full native source

Sources:
- `cmc-mcm-carrier-semantics-audit.md`.
- `common-three-carrier-protocol.md`.
- `packet-assembly-bridge-conjecture-net-v1.md`.
- `../nima/origin-bounded-assemblies-v1.md`, “Sewing is an explicit separate obligation”.

Earlier CMC/MCM/MCC native words act on raw/local/aligned preparation objects
with complex dimensions, not literal counts of geometric vertices. The native
P/N raw carriers have 36 coordinates and the electron has eight. Their physical
geometric attachment was not established merely by matching role labels.

The five-slot phase model used in our recent probes is a declared reference
bookkeeping layer. Nima's later source explicitly separates local contact/exit
certification from globally sewing the fields: matching a geometric vertex is
not enough to identify occurrence indices or symbolic root-coordinate pullbacks.
An explicit input subspace may be required. A flat coordinate chart change
must not replace a native operation or erase a coherent sign/history.

**Usefulness:** qualify “native” in the recent local probes as the retained
window/reference protocol, not proof of a bridge to the full physical native
36/8-coordinate assemblies. New whole-volume claims need that distinction.
The present all-contact repair is necessary but is not a global coupled-field
sewing theorem.

## Recommended order

1. **First:** target N-14 within the prior reference-only-P, locally generated
   grammar, keeping contact witnesses, occurrence origins and continuation.
   Do not conflate the reference P with occupied proton count.
2. **Separately:** probe alternative octahedral diagonals with the fixed root
   and explicit adapters, to isolate a triangulation artifact.
3. **Only then, if needed:** attempt a whole-octahedron source encoder using
   the metric-aware chart/gluing machinery. Do not infer an encoder from volume
   or transfer-count equality.

These clues change the research priority; they do not establish neutral N-14.
No complete whole-octahedron particle law, E/E interaction law, nuclear binding
law or physical stability criterion was found.

## Fresh verification

```sh
node research/strominger/checkers/check_prior_assembly_clues.mjs
```

Passed. Evidence: `results/prior-assembly-clues/verification.json`, recording
source hashes, the certified absent-occupied-reference witness, its retained
construction word, and the 24-marking regular/split-E replay. The full prior
nine-operation and origin-budget-D2 runs were **not rerun** here.
