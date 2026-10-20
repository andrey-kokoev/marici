# Native extension family: checked rule applications and source-structure lifts

## Result

The existing twelve-schema calculus already determines a rule-relative extension
family. The actual comparison rule admits the seed involution, given derivations
of its two correctly pointed endpoints. However, the same rule also admits
incidence-breaking equivalences, EVEN WHEN BOTH COMPLETE ENDPOINT CODES RETAIN
THE GRAPH. Retention of structure and enforcement of structure preservation are
different obligations.

This is now a fresh Agda result using the existing native modules, not just a
finite symmetry model. A source-specific adapter consumes an incidence-respecting
filler, applies the existing comparison rule, and retains the endpoints, complete
filler (including both incidence proofs), and native derivation in a next-level
package with exact recovery.

## Recovered native interface

The sources are:

- `research/nima/agda/WholePackageResolution.agda`
- `research/nima/agda/WholePackageSigmaPi.agda`
- `research/nima/agda/BoundaryGeneratedQuestions.agda`
- `research/nima/boundary-generated-questions.md`

The last source already abstracts the missing pointed-comparison fields, applies
the actual comparison rule, proves positive and negative filler examples, and
warns that coherence does not choose a signature. This audit reuses that
implementation rather than introducing a competing WG calculus.

For a fixed seed policy S, the exact family of FORMED rule applications is

    Extensions(S) = Sigma(r:Rule) Pi(i:Arity(r)) Resolve(S,input(r,i)).

The new AllApplications module maps this directly to

    (output(r), apply(r,premises)) : Closure(S)

and reifies the entire application in the next universe, with exact recovery.
A formed Rule already contains its parameters and witnesses. Constructing this
Sigma type neither discovers them nor enumerates all of its inhabitants.

For a fixed comparison boundary a,b, the missing evidence is exactly

    K(a,b)=Sigma(e:El(a)~=El(b)) (e(value(a))=value(b)).

With endpoint derivations supplied, an inhabitant compiles through the existing
`Boundary.Application.perform`. Nothing in that rule requires e to preserve
additional fields merely because the fields occur in the retained Code.

## Concrete seed and declared admission policy

The new module defines the six directed edges AB,BC,CA,BA,AD,DB. Every pointQ(v)
retains the entire six-edge list in its code and selects v in its interpreted
four-vertex carrier. A recovery theorem returns the graph package from each code.

The explicit seed family supplies pointQ(A), pointQ(B), pointQ(C), pointQ(D).
This is a declared source policy, not a derivation of four seeds from an empty
source or from an unspecified unpointed initial package.

Two different equivalences both carry A to B:

    sigma=(A B)(C D),
    tau=(A B), fixing C,D.

Both are implemented as involutive equivalences. The actual existing comparison
rule derives both packages from the same A and B seed derivations. Both endpoints
retain the graph. Yet:

- sigma carries every seed edge to a seed edge, in both directions;
- tau carries BC to AC, and Edge(A,C) is empty.

Agda proves the absence of a forward incidence witness for tau, not merely failure
of one candidate implementation. It also proves the two native fillers distinct.

Sigma is NOT a pointed self-comparison at A, since sigma(A)=B. The source-derived
comparison is between the A-pointed and B-pointed packages. Conflating an
unpointed graph automorphism with a pointed self-filler would reject or misstate
the actual boundary.

Exact permutation enumeration independently gives six underlying pointed
bijections A->B, only one of which preserves seed incidence: sigma. This counts
maps at a fixed finite boundary, not all native rules, histories or arbitrary
proof-relevant extension fibers.

## Source-specific lift and actual retained adapter

Define the refined fiber

    SeedFiller(a,b) = Sigma(f:K(pointQ(a),pointQ(b)))
      (PreservesEdges(f.e) x PreservesEdges(f.e^-1)).

This is an explicit strengthening of the native signature, justified by the
chosen directed-incidence source contract. It is NOT a claim that the generic
comparison rule was defective or already enforced the strengthening.

The checked `compile-structured` consumes:

- a,b;
- the complete refined filler f;
- actual derivations of pointQ(a) and pointQ(b).

It returns a record containing a,b,f and the native comparison derivation.
`retain-structured` reifies that whole record as a Complete in the next universe.
`structured-record-recovered` recovers it exactly. The positive sigma instance
is implemented, with both incidence witnesses. A deliberate attempt to reuse
sigma's incidence witness for tau is rejected by the kernel.

The reified record is an available next-level object. No additional claim is
made that it automatically has a Resolve derivation under some new-level seed
policy, or that its next extension witness exists. Those remain separately typed
admission obligations.

## Where generation is already present, and where choices remain

The other native schemas include E, Pi, composition, higher paths, path lift,
distribution, and E/Pi congruence. They are not all equivalence-only constructors.
The existing BoundaryGeneratedQuestions module derives unit-indexed and
Bool-indexed E packages from the unit seed and proves that the latter cannot be
pointedly equivalent to the unit package. Its closure was freshly rechecked as
a dependency here. Thus genuine interpreted-type generation already exists in
the actual calculus; it need not be inferred from symmetry-record counting.

However, E's index type/family and selected index are explicit rule parameters.
A higher-rule likewise requires its actual higher witness. The generic calculus
does not derive a unique index family, boundary policy, or arbitrary filler from
source retention alone.

The sharpened general architecture is therefore:

    native extension evidence
      + source-required structure-preservation evidence
      -> actual native application
      -> whole-record reification.

Its comparison, preservation and recovery portions have a concrete checked
instance here. To obtain a source-driven generative synthesis theorem one must
still show how the native source/admission contract determines the allowed
families and constraints across subsequent boundaries. The present proof does
not manufacture that selection theorem by wrapping the record again.

## Verification

    python research/strominger/checkers/check_native_extension_family_audit.py

Fresh headless `agda --ignore-interfaces` closure passes under Agda 2.8.0.1 and
Cubical 0.9. The module uses `--safe --cubical --guardedness`; no postulates or
holes were introduced. The negative control exits 42 at the expected sigma/tau
edge mismatch. Exact candidate counts are 6 unrestricted versus 1 incidence
preserving at the fixed A->B boundary. Source hashes are checked unchanged
across the run.

Artifacts:

- `agda/NativeExtensionFamilyAudit.agda`
- `agda/negative/NativeBadIncidenceAdmission.agda`
- `checkers/check_native_extension_family_audit.py`
- `results/native-extension-family-audit.json`
- `results/native-extension-family-audit-positive.log`
- `results/native-extension-family-audit-negative.log`

Only Strominger-owned sources/reports/checkers were edited. Fresh Agda checking
may refresh generated dependency interfaces. No physical process, graph
publication, commit or push is claimed.
