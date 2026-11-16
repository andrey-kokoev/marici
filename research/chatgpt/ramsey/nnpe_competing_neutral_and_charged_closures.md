# NNPE: charged-return failure and a competing neutral closure

Date: 2026-11-02. Continuation of `nnpe_feedback_closure_and_open_boundary.md`.

## Result

The previously studied six-port open construction has a second way to complete.
After joining P from one four-leg NNPE primitive to E on the other, its boundary
is NNNNPE. Closing the remaining P/E pair gives NNNN. Closing a free N/N pair
instead gives NNPE.

Thus an alternative **closed** realization can expose P and E while keeping four
external legs overall. It need not remain an unfinished six-port object. This is
an exact consequence of the new four-external-port convention, the retained
N-self-dual/P–E-dual rule, and an explicitly permitted feedback join. It is not
an operation admitted by the current tree-only repository implementation.

The comparison test is equally specific. Let A be the retained passage between
the two primitive payload spaces. Let B be the attempted charged return, and let
D be an independently available neutral return in the same endpoint frames.
The condition

    B A != I,     D A = I

rejects the charged identity-return completion but admits the neutral one.
That supplies a concrete candidate for NNNN -> NNPE **boundary rerouting**.
It does not establish its physical occurrence, select an actual D from Marici,
identify the exposed ports as particles, or supply a rate.

## Source authority and input distinctions

The current `research/realization-tower/sulfur-nnpe-composition.mjs` was inspected
through the GitHub connector. It defines `nnpeDual={N:'N',P:'E',E:'P'}` but uses an
N centre plus only three external ports N/P/E. It rejects every join within an
already connected component. The source contains no payload-comparison matrices,
identity-return test, dynamics, or particle-production rule.

The executable source control imports the unchanged 2,406-byte module copied
from the immediately preceding attached audit. Its SHA-256 is recorded in
`source_composer_results.json`. The currently retrieved remote text has the same
implementation. Both a second charged join and a second neutral join are rejected
with `That join would create a loop.` No repository source was altered or a wider
upstream test suite rerun.

New assumptions retained from the user's proposal and the previous audit:

* Each primitive has four external ports N0,N1,P,E, not three ports plus a centre.
* A feedback join may connect ports already in the same component, retaining
  both original vertices and the full construction history.
* The primary census permits joins between different original vertices. Joining
  two neutral ports of the very same original vertex is tested separately.
* A full-state identity-return contract is used for the payload examples. This
  is stronger than requiring one prepared state to be fixed. Nonidentity return
  does not universally preclude a nonzero fixed subspace.

A typed comparison B and a typed comparison D cannot be compared just because
their displayed matrices have the same size. Their source/target spaces and
frame transports must first be supplied. The finite fixtures explicitly give
those common types; the repository NNPE module does not yet do so.

## 1. Competing complete graphs

Write the two vertices as v0 and v1. Retain the first charged join

    A: v0.P -- v1.E.

The remaining charged join would be

    B: v1.P -- v0.E.

There are four cross-vertex neutral alternatives

    D_ij: v0.Ni -- v1.Nj,    i,j in {0,1}.

The six-port intermediate has the free flags

    v0.N0, v0.N1, v1.N0, v1.N1, v1.P, v0.E.

Its five possible cross-vertex completions have these boundaries:

| Second join | Free boundary | Retained vertices | Internal edges | Cycle rank |
|---|---|---:|---:|---:|
| B | NNNN | 2 | 2 | 1 |
| Any D_ij | NNPE | 2 | 2 | 1 |

For a neutral completion, one N remains on each vertex, alongside v1.P and
v0.E. Two N flags have become an internal connection; no flag or original vertex
has been erased. The two completed graphs have the same total external valence
and the same internal cycle count, but different boundary types.

The two same-original-vertex neutral joins also yield NNPE boundary counts, but
the internal neutral loop is placed on one vertex. They are kept as separate
controls rather than identified with the cross-vertex completions.

### Complete finite matching census

Among the eight flags there are six allowed cross-vertex dual edges: four N/N
edges and two P/E edges. Checking all 64 subsets gives 28 disjoint-port matchings:

| Internal edge count | Valid matchings |
|---:|---:|
| 0 | 1 |
| 1 | 6 |
| 2 | 11 |
| 3 | 8 |
| 4 | 2 |

At two edges, all graphs are connected with one cycle. Their boundary types are:

    NNNN: 1 matching
    NNPE: 8 matchings
    PPEE: 2 matchings.

The eight NNPE matchings comprise either initial charged edge and any of the four
neutral edges. Holding A fixed reduces these to four alternatives. The remaining
two-edge PPEE graphs use two neutral joins and neither charged join.

These are counts of labelled graph fixtures, not branching probabilities. A
cyclic/ribbon order, spatial embedding, or fixed exterior attachment can impose
further restrictions not specified by the port colours.

## 2. An actual comparison-dependent distinction

Let A:X0->X1 and B,D_ij:X1->X0 be reversible maps in retained endpoint frames.
The earlier strong identity-return contract admits the charged graph when

    B A = I_X0,

and admits a neutral graph when

    D_ij A = I_X0.

A failed B comparison therefore does not imply that every completion fails.
Neither does it imply that any D is available or correct.

An exact noncommuting example is

    A = X = [[0,1],[1,0]],
    B = Z = [[1,0],[0,-1]],
    (D_00,D_01,D_10,D_11) = (X,I,Z,-I).

Both A and B are involutions, so A^2=B^2=I. Nevertheless

    B A = [[0,1],[-1,0]],
    det(I-B A)=2.

There is no nonzero payload fixed by this charged return. Exactly one neutral
candidate passes: D_00 A=X^2=I. The resulting graph has NNPE boundary. All maps
were supplied as a finite comparison fixture; D_00 was not recovered from a
native physical constructor.

### Exhaustive noncommuting controls

The main finite comparison set is Q8={+/-I,+/-iX,+/-iY,+/-iZ}. The program checks
all 8^6=262,144 assignments to A, B and the four D values. Every valid neutral
completion is retained; the program does not choose one by ordering or priority.
The conditional census is independently checked against

    charged passes: 8 * binomial(4,k) * 7^(4-k),
    charged fails:  8 * 7 * binomial(4,k) * 7^(4-k),

for k valid neutral returns. This tests the implication and its countercases
without treating a uniform fixture census as a law of nature.

All 32,768 independent Q8 endpoint-frame changes also preserve admission. With
frame changes g0,g1,

    A' = g1 A g0^-1,
    B' = g0 B g1^-1,
    D' = g0 D g1^-1,
    (BA)' = g0 (BA) g0^-1.

Thus the test does not depend on an arbitrary matrix basis once the endpoint
bindings are present.

## 3. Exact retention of the failed charged comparison

Set H=BA. If a neutral completion passes, D=A^-1, so

    B=H D.

The retained A, selected neutral route/address, and based discrepancy H recover
the attempted B exactly. The unselected D witnesses and other construction
records are retained as well. The census checks 131,072 such recoveries.

Changing the active connection does not require discarding the wrong return,
resetting it, or declaring that the mismatch itself is a particle. The old H
can remain a local construction record. The distinction between archival
retention and a currently active passage is explicit.

For a missing B value, algebraically computing A^-1 remains possible. For an
incorrect recorded B, replacing it by A^-1 changes the proposed operation and
must retain its old data. For a missing certification, a correct BA has not
become false. None of these cases is automatically the decay branch.

## 4. What is and is not forced

The exact candidate is an admissibility relation, not a time-evolution rule:

    after the first charged join, enumerate the available closures;
    reject the charged closure if its required comparison fails;
    retain every neutral closure whose required comparison succeeds.

If B fails, at least one D passes, every candidate neutral flag is actually free,
and the allowed next step must be one of these successful closures, then every
admissible next boundary is NNPE. A unique D additionally supplies a unique
labelled completion in that restricted menu.

Each qualification matters. Executed controls include:

* B fails and no neutral candidate passes: no closed completion in this menu.
* B fails and four neutral candidates pass: boundary type is NNPE, but the
  labelled history is not unique.
* B and neutral candidates pass: both NNNN and NNPE are admitted.
* A neutral witness is unavailable: it cannot be invented as A^-1.
* Neutral ports are already bound to the exterior: they cannot be reused for
  an internal join.
* Inverse repair is independently admitted: it remains a rival to rerouting.

The rules do not yet require completing rather than waiting, rejecting, retrying
or using a different constructor. Nor does reversibility by itself prioritize
NNNN when both boundary types are admitted. Those selection questions are not
resolved by the successful fixture.

## 5. Three output slots without a third residual object

Under a further **process orientation**, designate one of the two remaining N
ports as the incoming neutral carrier. The other three ports are then N,P,E.
The corresponding local operation would have type

    Gamma: H_Nin -> H_Nout tensor H_P tensor H_E.

This is a type for a possible joint output, not a supplied Gamma matrix or a
proof of physical tensor-factor independence. It uses the actual four-port
boundary; it does not append a fourth output or reinterpret a lost-norm register
as a neutrino.

The two N ports share only a coarse neutral type. They need not carry the same
species, but distinguishing their sectors requires actual retained source data
and readers. Calling Nout an antineutrino would still require the appropriate
spin, charge, flavor and propagation identification. Conversely, if the model
requires every N port to be a neutron, the above type has not described beta
decay. Choosing an incoming leg and independent propagating output systems are
additional obligations, not consequences of an unoriented corolla.

This corrects the earlier research demand that cutting two vertices must somehow
make three disconnected vertices. Three outputs of a process need not be three
new vertices in its interaction graph. That observation does not, however,
turn exposed attachment flags into independently realized particles.

## 6. The precise primitive-level test now available

The branch to test is no longer merely 'leave a failed six-port object open.' It
is **replace a failed charged feedback closure with an admitted neutral feedback
closure**, changing the closed boundary from NNNN to NNPE.

The first missing source input is now very narrow: determine the actual
D_ij return witnesses, their endpoint/frame bindings and their availability from
the same retained NNPE construction that supplies A and B. Compute DA and BA
without choosing D to make the result succeed. Then test whether the native
successor policy consumes that difference in admission.

The inspected tree-only composer has no such witness data and rejects both
loops. The proposed graph calculation therefore supplies an executable target
for a primitive extension, not a recovered physical neutron transition. There
is no new failure probability, fitted lifetime, output spinor projector,
interaction strength, energy threshold or physical energy assignment here.

## Reproduction

    python closure_channel_switch.py
    node check_source_composer.mjs

Python 3.10+ standard library and Node's built-ins suffice. The Python matrices
use only Gaussian integer entries +/-1,+/-i and exact small-integer arithmetic;
no numerical tolerances or eigenvalue approximations enter the decisions.
`closure_switch_results.json` contains the graph and comparison census, selected
counterexample and controls. `source_composer_results.json` records the actual
legacy-function rejection tests. `run.log` records both completed runs.

## Sources

- Marici, `research/realization-tower/sulfur-nnpe-composition.mjs`, retrieved
  November 2, 2026: https://github.com/andrey-kokoev/marici/blob/main/research/realization-tower/sulfur-nnpe-composition.mjs
- Attached preceding audit, `nnpe_feedback_closure_and_open_boundary.md`,
  especially its four-port extension and identity-return comparison contract.
- E. Getzler and M. M. Kapranov, *Modular operads*, Compositio Mathematica 110
  (1998), 65-125, https://arxiv.org/abs/dg-ga/9408003. This supplies background on
  graph-with-loops composition, not the physical or dynamical interpretation
  tested here.

The graph and map tests in this note are independent calculations. No external
paper is credited with the proposed charged/neutral continuation rule.
