# Source-derived extension indices inside the existing native E/Pi calculus

## Constructive result

There is now a source-derived family constructor, rather than another supplied
Boolean or symmetry-choice index. Given the declared task 'retain all endpoint-
compatible attachments', the six-arrow incidence relation determines its index
fiber exactly. These indices feed ACTUAL native E and Pi derivations. Source
symmetry transport and endpoint covariance are proved for every finite structural
depth, and the transported selected E packages have actual native comparison
derivations.

This is a conditional constructive instance of the recursive synthesis
conjecture. It does not prove that source incidence uniquely selects the
attachment task, a depth, or a preferred branch among the admissible attachments.

## Reused source, not a new graph or native signature

The Agda module imports Vertex, Edge, pointQ, Seeds, root, sigma and sigmaEdge
from `NativeExtensionFamilyAudit.agda`. Edge has precisely AB,BC,CA,BA,AD,DB.
The seed family supplies the four graph-retaining vertex-pointed packages.
The native E, Pi, reflexivity, comparison, and history-reification operations
are imported unchanged from the existing WholePackage modules.

Earlier seed work already constructs endpoint-compatible paths and records their
counts. The new contribution is a direct, source-indexed binding to the native
E/Pi rules with all-finite-depth kernel-checked transport, not discovery of those
path counts. `research/nima/native-family-feedback-binding.md` also warns that
family formation must not be confused with native feedback; that distinction is
retained below.

## Deriving W from the chosen attachment task

Define

    Out(v) = Sigma(w:Vertex) Edge(v,w).

For a retained configuration carrier X with endpoint:X->Vertex, set

    Next(X) = Sigma(x:X) Out(endpoint(x)).

No unrelated index set, branch priority, phase or measure is supplied. The
outgoing fibers have respectively 2,2,1,1 inhabitants at A,B,C,D.

The kernel checks the universal mapping property

    (T -> Next(X))
      ~= Sigma(f:T->X) Pi(t:T) Out(endpoint(f(t))).

Thus a map into the extension is exactly an old configuration map plus its
compatible edge witnesses. Once this task is specified, using a strict subset
of the admissible edges would fail this unrestricted mapping property. The
property does not select endpoint attachment over every other possible task.

## Recursive indices and source covariance

Define source-indexed paths structurally:

    PathsFrom(0,v)=Unit,
    PathsFrom(n+1,v)=Sigma(o:Out(v)) PathsFrom(n,target(o)),
    Paths(n)=Sigma(v:Vertex) PathsFrom(n,v).

The index retains each original incidence witness and its position, not merely
the endpoint. No physical time or execution occurrence is assigned to depth or
position.

Sigma transports Out(v) equivalently to Out(sigma(v)). Dependent-sum composition
then constructs, for EVERY finite n, an equivalence of the full Paths(n) index.
The endpoint of the transported path equals sigma applied to the old endpoint.
These are general Agda theorems, not conclusions extrapolated from finite tests.

An independent finite audit checks all paths through depth six, prefix recovery,
source-symmetry transport, and variable attachment fibers. Counts are

    depth:   0  1   2   3   4   5   6
    paths:   4  6  10  16  26  42  68.

These are source path counts, not physical states, spatial dimensions or rung
identifications.

## Actual native E/Pi applications

For every source path p, its endpoint package already has a seed derivation.
Apply the EXISTING reflexivity rule to that complete endpoint package to obtain

    branch(n,p) = path-package(pointQ(endpoint(p)), refl).

All source graph provenance in pointQ remains in the path code. No new atomic
seed containing a fabricated edge or desired index is inserted.

The family p -> branch(n,p), indexed by the source-derived Paths(n), supplies
all required premises of the existing E and Pi rules:

- E resolves any supplied admissible p and retains the whole indexed family.
- Pi builds the complete family WITHOUT selecting p.

Both have native Resolve derivations under the unchanged seed policy. The entire
Pi derivation can be reified in the next universe and recovered exactly.

The interpreted E carrier is PROVED equivalent to Paths(n). Its extra endpoint
reflexivity witness has no hidden multiplicity because Vertex is a set. Thus
these are not merely longer codes around an unchanged interpreted carrier:
the finite counts of the interpreted E types really change from four to six,
ten, etc. At depth one the AB and AD branch values are separately proved unequal.

Transport the E carrier through its equivalence with Paths(n), apply the source
path equivalence, and transport back. This supplies actual native compare-rule
applications between selected E packages at every depth, with both endpoint
derivations. This closes the comparison/generation binding for this instance.

The Pi package has a DIFFERENT interpretation: a family of endpoint reflexivity
witnesses, not the disjoint set of path choices. Its index and complete branch
family survive in Code. The E path counts must not be attributed to Pi's
interpreted value type.

## What remains selected, and what is not yet feedback

The full-family constructor makes no deterministic outgoing-edge choice. Exact
enumeration nevertheless finds TWO different endpoint successor policies that
respect both source incidence and sigma. One selects the shared-edge successors
at A,B; the other gives the existing four-cycle cover. Naturality still does not
select between them. Pi family construction avoids needing that selector; an
individual E application still requires its actual path inhabitant.

The task and structural depth remain explicit inputs. This report does not say
that the generic twelve-schema calculus uniquely chooses endpoint attachment,
all path lengths, or any physical path.

Also, recursive index formation occurs at the source-type level. The new native
derivations compile their branch premises from the original endpoint seeds.
They do NOT consume a previous reified history through an autonomous feedback
procedure that selects the next rule and depth. Whole-history reification is
proved, but automatic next-level admission is not inferred from it.

## Consequence for the conjecture

We now have one concrete chain connecting all three structural goals:

    source incidence -> exact admissible index fibers
      -> native E/Pi construction of retained configurations
      -> source-covariant native comparison and whole-history reification.

The family is no longer an arbitrary externally supplied Boolean fixture.
Its boundary constraints come from the source after declaring the attachment
task. The remaining stronger conjecture concerns selection or derivation of
that task and its recursive admission policy, not the availability of a
coherent source-derived generative example.

## Verification

    python research/strominger/checkers/check_source_indexed_extension_families.py

Fresh headless Agda closure with `--ignore-interfaces` passes under Agda 2.8.0.1 /
Cubical 0.9. The new module uses `--safe --cubical --guardedness`, contains no
postulates or holes, and introduces no unsupported indexed-match warning.
A negative module claiming CA certifies a C->D attachment is rejected at its
Edge boundary (exit 42). Source hashes remain stable through the run.

Artifacts:

- `agda/SourceIndexedExtensionFamilies.agda`
- `agda/negative/SourceBadEndpointExtension.agda`
- `checkers/check_source_indexed_extension_families.py`
- `results/source-indexed-extension-families.json`
- `results/source-indexed-extension-families-positive.log`
- `results/source-indexed-extension-families-negative.log`

Only Strominger-owned sources and reports were edited; generated dependency
interfaces may be refreshed by Agda. No physical claim, graph publication,
commit or push.
