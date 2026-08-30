# Deutsch--Popperian remote/local operational-module conjecture

## Independently suggested architecture

Sonar separates an authoritative `RemoteEntityName` from a constructed
`LocalEntity`. A local entity is not a cached copy: it adds state, columns,
validation, controlled actions, operating mode, and readout behavior. Several
local entities may realize one remote relation. Its RPC boundary separately
types the operated-on object `T` and returned object `R`.

This suggests the Marici factorization

\[
\boxed{
\text{Carrier}
\longrightarrow
\text{sector source relation}
\longrightarrow
\text{local operational module}
\longrightarrow
\text{physical readout}.
}
\]

The analogy is structural, not an identification. The Carrier corresponds
more nearly to schema/composition machinery than to one remote table. A
sector source relation is already a realization of it.

## Cosmology specialization

For the five-mark residue packet, freeze:

- remote/source relation: the common numerator space, Cayley--Menger quartic,
  five marked divisors, and unsplit physical source
  \(q_{g_{23}}+q_{g_{31}}\);
- generic local module: quotient by \(R_5\);
- physical local module: quotient by \(R_{-1/2}\);
- constructor/adapter: dimensional specialization or limiting-lattice
  transport;
- readout: pairing with the canonical physical Leray germ.

The two local modules may have equal rank without sharing coordinate
identifications. Their operational histories, not array positions, must type
their comparison.

## Preregistered prediction

The five replaced relations should be generated entirely by the
\(\gamma\)-dependent twisted-de-Rham/IBP differential over the unchanged
source geometry. They may change degrees, parity, or filtration placement,
but must not require:

- a new carrier polynomial or marked divisor;
- a new source numerator;
- a post-hoc projection selected from the desired readout;
- identification by matching finite-field coordinate indices.

The same source was initially predicted to remain cyclic in both modules. A
valid adapter was therefore expected to send the source to itself and
intertwine the source-defined operations. The higher-pole audit below
falsifies the cyclicity clause while preserving the module-family clause.

## Falsifiers

The conjecture fails in this case if any of the following occurs:

1. physical specialization requires new geometric support;
2. the common source ceases to generate the physical module;
3. the changed relation packet cannot be expressed inside the frozen
   twisted-de-Rham presentation;
4. no source-preserving operation-intertwiner exists;
5. an intertwiner exists only after choosing a coordinate splitting or the
   desired period values.

Success requires more than an abstract rank-26 isomorphism. It requires a
natural constructor from shared source operations, followed by an independently
defined Leray readout.

## Immediate test order

1. classify the invariant degree/parity/support profile of
   \(R_5\cap R_{-1/2}\) and both five-dimensional replacement packets;
2. derive the common source-word comparison;
3. test source preservation and connection intertwining;
4. only then pull back the Leray period covector.

## First test result: survived

The relation classifier replicated over \(\mathbf F_{32003}\) and
\(\mathbf F_{32009}\). In the common 36-dimensional numerator space,

\[
\dim R_5=\dim R_{-1/2}=10,
\quad
\dim(R_5\cap R_{-1/2})=5.
\]

For each five-dimensional replacement packet, the intrinsic degree-filtration
profile is

\[
(0,0,0,0,0,0,1,5)
\]

through degrees zero to seven. Neither packet contains a nonzero class inside
any single \((\deg_a\bmod2,\deg_b\bmod2)\) coordinate-parity subspace. Thus
the marked arrangement mixes parity, but generic and physical specialization
have identical filtered shape.

No new polynomial, marked divisor, denominator, or source generator occurs.
The change is wholly internal to the top two grades of the frozen operational
relation lattice. This is precisely the preregistered local-module behavior,
not a Carrier mutation.

The result does not yet prove that a natural constructor exists. It authorizes
the next test: the source-preserving connection intertwiner.

## Constructor typing correction

A direct fixed-fiber intertwiner was initially proposed as

\[
T A_i^{(5)}=A_i^{(-1/2)}T.
\]

That equation is too restrictive unless \(T\) is known to be independent of
kinematics. The actual horizontality equation is

\[
\partial_iT+A_i^{(-1/2)}T-TA_i^{(5)}=0.
\]

More fundamentally, twists differing by the noninteger amount \(11/2\) need
not define isomorphic local systems: their monodromy characters may differ.
The Sonar analogy therefore points to a constructor over a parameter base,
not necessarily an RPC-style isomorphism between two already constructed
local entities.

The corrected object is a source-labelled module \(\mathcal H_\gamma\) over
an open subset of the \(\gamma\)-line, with base-change maps

\[
\mathcal H_\gamma\otimes_{\gamma=5}k,
\qquad
\mathcal H_\gamma\otimes_{\gamma=-1/2}k.
\]

The next finite gate is regularity of this family at \(\gamma=-1/2\): stable
rank, stable source cyclicity, and a pivot/Plücker chart that does not acquire
a pole there. If regular, the physical module is derived by base change even
though its relation lattice differs. If singular, a limiting or nearby-cycle
lattice is genuinely required.

## Plücker regularity result

The bounded family is regular at the physical twist over both tested primes.
The same ten numerator coordinates

\[
(3,2),(3,3),(3,4),(4,2),(4,3),
(5,1),(5,2),(6,0),(6,1),(7,0)
\]

give a full-rank projection of the relation space at both \(\gamma=5\) and
\(\gamma=-1/2\). The relation rank is ten and the quotient rank is 26 in
both fibers. Although elimination chooses different preferred pivot charts,
one common Plücker chart contains both tested fibers.

Because the unreduced twisted differential is polynomial in \(\gamma\), the
nonzero physical Plücker minor defines an ordinary Zariski-open neighborhood
of \(-1/2\) in this bounded presentation. Thus no limiting or nearby-cycle
lattice is required merely to reach the physical twist at pole depth two:

\[
\boxed{
\text{same bounded module family}
\xrightarrow{\gamma=-1/2\text{ base change}}
\text{physical rank-26 presentation}.
}
\]

This does not exclude additional resonant classes first appearing at higher
\(K\)-pole depth. The next hostile check is pole-depth stabilization at the
half twist. If it remains rank 26, the canonical Leray covector may be built
directly in the physical Plücker chart and compared to the generic family by
ordinary base change.

## Higher-pole result: regular module, codimension-one physical source orbit

Complete normal-form reduction was extended from common \(K\)-pole depth two
to depth three. At both tested primes,

\[
\begin{array}{c|cc}
&K\text{-depth }2&K\text{-depth }3\\
\hline
\dim H_{\gamma=5}&26&26\\
\dim H_{\gamma=-1/2}&26&26\\
\dim\langle\nabla^I s\rangle_{\gamma=5}&26&26\\
\dim\langle\nabla^I s\rangle_{\gamma=-1/2}&25&25
\end{array}
\]

Thus no higher-pole cohomology appears through depth three, and the physical
fiber remains an ordinary rank-26 base change. Nevertheless the literal
unsplit source loses exactly one cyclic direction at the physical twist.

The prior rank-26 physical source-orbit report used an incomplete quotient
normal form that stopped at the first free leader. Eliminating every pivot
before free-coordinate projection gives the replicated rank 25.

This is not a Carrier mutation and not a rank singularity. It is a
codimension-one operational residual inside the regular physical module:

\[
\boxed{H_{-1/2}/\langle\nabla^I s_{\rm phys}\rangle\simeq k.}
\]

It is not yet identified as a physical readout class. The next test must
construct its intrinsic annihilator line, classify its filtration/support,
and evaluate whether the canonical Leray covector detects it.

Evidence:

- `research/nima/checkers/check_rank26_gamma_plucker_chart.py`
- `research/nima/results/rank26_gamma_plucker_chart_p32003.json`
- `research/nima/results/rank26_gamma_plucker_chart_p32009.json`

Evidence:

- `research/nima/checkers/check_rank26_replaced_relation_profile.py`
- `research/nima/results/rank26_replaced_relation_profile_p32003.json`
- `research/nima/results/rank26_replaced_relation_profile_p32009.json`

## Recurring architecture: obstruction on the ordinary channel

The Sonar comparison exposes a second distinction that is more important
than the remote/local naming.  Its RPC layer separates transport failure from
a successfully transported negative domain result.  A request may reach the
generic controller and return the ordinary typed envelope

```text
{ result: "error", messages: [...], requestedFrontendActions?: [...] }
```

through a successful HTTP response.  The UI may render that value as an
error, but it is not the same thing as failure of the transport itself.  The
same `RpcResponseV1` sum type carries successful data, negative domain
results, messages, and authorized frontend effects.  Controlled-action
records determine which entity/action/field operation is legal before the
controller evaluates it.

This sharpens the Marici analogy:

\[
\boxed{
\text{illegal or untyped attempt}
\;\neq\;
\text{legal operation returning a typed obstruction}.
}
\]

For an admitted operation \(f\), the operational result should be modelled
schematically as

\[
\operatorname{Attempt}_f(X)
\longrightarrow
\operatorname{Success}_f(Y)\sqcup
\operatorname{Obstruction}_f(O_f).
\]

The obstruction is not necessarily an exception or a defect.  It may be a
failed-descent class, boundary residue, extension class, curvature term,
relation cell, or missing homotopy.  Because it was produced by a legal typed
operation, it retains source, target, provenance, support, and composition
data.  A sector adapter or physical readout may display it as a negative
record, annihilate it, transport it, or reveal that it is precisely the next
coherence datum.

### Earlier occurrences of the same pattern

This is a recurrence claim, not an assertion that the following objects are
identical.

| Occurrence | Ordinary channel | Structured negative/residual datum |
|---|---|---|
| Sonar controlled actions and RPC | authorized generic-controller request/response | `result: "error"`, messages, and requested frontend actions |
| Carrier coherence squares | two legal composites of typed maps | their difference, curvature, or required homotopy |
| Generic versus supported coefficient maps | localization/Gysin comparison | the Beck--Chevalley obstruction rather than a fabricated direct map |
| Labelled principal-cell calculations | the full labelled total complex | a principal or extension column that survives although the homogeneous quotient misses it |
| C9 Orlik--Solomon sewing | legal source relation among adjacent charts | a seam relation/coherence cell, not an ordinary period class |
| Labelled Lah constructors | insert/create/freeze histories | augmentation collapses many labelled histories to one scalar coefficient without making the histories identical |
| Physical readout | an admitted coefficient--response pairing | an invisible, killed, or supported channel rather than an untyped absence |

The database/UI analogy anticipated this distinction in the separation of
authority, local projection, capability, and readout.  The controlled-action
example now supplies an independently built software instance in which the
negative result is explicitly first-class and travels through the normal
response contract.  The C9 seam and labelled-Lah results supply later
mathematical instances: a relation cell can carry the unresolved datum, while
augmentation can hide its labelled provenance.

### Falsification boundary

The analogy earns explanatory weight only if the negative branch is itself
typed and composable.  It weakens or fails when:

1. the alleged obstruction is only free-form logging with no source/target;
2. an illegal or unauthorized request is conflated with a legal negative
   result;
3. a local projection is treated as authority for the remote/source object;
4. the residual is fitted after inspecting the desired readout;
5. composition discards the obstruction without a declared augmentation,
   quotient, or annihilating readout.

Thus the proposed recurring architecture is not simply “errors are data.”
It is:

\[
\boxed{
\text{admitted operation}
+\text{normal typed result channel}
+\text{first-class obstruction branch}
+\text{explicit readout/augmentation}.
}
\]

Evidence and provenance:

- `C:/Users/andrey/src/sonar.cloud/src/api/rpc.ts`, especially the separate
  transport-error and response-body branches;
- `C:/Users/andrey/src/sonar.cloud/src/types/rpcInterfaces.ts`, defining
  `RpcResponseV1`;
- `C:/Users/andrey/src/sonar.cloud/src/platform/server/api/implementations/plpgsql/utils/get_applicable_controlled_actions2.pgsql`;
- `research/nima/capability-indexed-instrument-surface.md`;
- `research/nima/cross-sector-source-sewing-annihilates-nondescending-odd-jets.md`;
- epistemic events 2567--2580 for the C9 seam typing and labelled-Lah
  constructor/augmentation sequence.

## First universality attack: one interface, not one obstruction object

The recurrence does **not** justify a single global type

\[
\operatorname{Result}(T,E)
\]

with one fixed error object \(E\).  The examples already falsify that naive
formulation.  Their residues have incompatible mathematical types:

- curvature is a degree-two morphism-valued form;
- a Beck--Chevalley defect is a comparison 2-cell or its obstruction class;
- a principal column is part of an augmented complex;
- an Orlik--Solomon seam is a relation cell;
- an augmentation kernel retains labelled combinatorial provenance;
- a Sonar domain rejection is an application-level response record.

Forcing these into one set or vector space would erase precisely the degree,
support, variance, and authority information that makes them useful.

The surviving universal candidate is instead an **indexed result
architecture**.  Let \(\mathsf{Op}\) be the category of admitted operations.
For each operation \(f\), retain its own success and obstruction fibers
\(Y_f\) and \(O_f\):

\[
\mathsf{Result}_f=Y_f\sqcup O_f.
\]

Globally these form a projection

\[
\boxed{
\pi:\int_{f\in\mathsf{Op}}\mathsf{Result}_f
\longrightarrow\mathsf{Op},
}
\]

not one untyped coproduct.  Composition must supply typed transport from the
chosen branch over \(f\) and the chosen branch over \(g\) into the appropriate
branch over \(g\circ f\).  A readout is a further operation-indexed functor or
pairing; it may not silently identify fibers belonging to different
operations.

This has a close software form.  A generic RPC envelope is reusable, while
each endpoint still owns its response payload, domain rejection vocabulary,
authorization conditions, and follow-up actions.  Parametricity of the
envelope is not equality of its payload types.

### What repeats

The recurring invariant is therefore the four-stage shape

\[
\boxed{
\text{admission}
\to\text{operation-indexed attempt}
\to\text{operation-indexed value/residue}
\to\text{explicit readout or composition}.
}
\]

What does *not* repeat is a universal coefficient space, scalar error code,
or common physical interpretation.  This is the same methodological split as
“shared calculus, sector-specific coefficients,” now applied to negative as
well as positive operational results.

### Decisive next test

Choose two composable source operations \(f,g\) in one established sector and
export all four branch-composition maps

\[
Y_g\circ Y_f,
\quad Y_g\circ O_f,
\quad O_g\circ Y_f,
\quad O_g\circ O_f
\longrightarrow
Y_{g\circ f}\sqcup O_{g\circ f}.
\]

The conjecture survives only if those maps are source-derived and associative
up to already declared coherence.  The filtered jet pilot supplies one exact
positive model: its current value and next-grade Hochschild cocycle compose
associatively after the residue is retained.  A hostile physical-sector test
must now use a genuine localization/Gysin or seam/augmentation pair.

Failure of any mixed branch to type without inventing a corrective target
would show that “normal-channel obstruction” is only a family resemblance,
not an operational calculus.  Successful closure would identify the first
nontrivial piece of the sought universal constructor: not a universal error,
but a fibred algebra of typed attempts and residues.

Related exact pilot:
`research/nima/filtered-interaction-jet-pilot.md` and
`research/nima/checkers/check_filtered_interaction_jet_pilot.py`.
