# Deutsch--Popperian conjecture: full abstraction of explanatory contexts

## Status

This packet asks when admissible interventions and readouts recover exactly the
authorized equivalence class of a realization. It turns the distinction between
observational agreement and explanatory agreement into a full-abstraction test.

## 1. Contextual observation

Let \(\mathbf E\) be a class of source-typed realizations and let \(\mathbf C\)
be a class of admissible experimental contexts. A context may initialize a
source, compose constructors, couple an ancillary reference, and apply a typed
readout.

For a realization \(R\), define its contextual record

\[
N(R)(c)=\operatorname{Obs}(c[R]),
\qquad c\in\mathbf C.
\]

The assignment \(N\) is the experimental nerve of the realization. Two
realizations are contextually equivalent when

\[
N(R)=N(R').
\]

## 2. Authorized equivalence

Write

\[
R\simeq_{\mathrm{src}}R'
\]

when an authorized typed equivalence intertwines initialization, every admitted
constructor, every readout, and every independently sourced structural datum.

The experimental interface is sound when

\[
R\simeq_{\mathrm{src}}R'
\Longrightarrow
N(R)=N(R').
\]

It is fully abstract when the converse also holds:

\[
N(R)=N(R')
\Longrightarrow
R\simeq_{\mathrm{src}}R'.
\]

Full abstraction says that the interface forgets presentation gauge and nothing
else.

## 3. Four distinct failures

### Unsound context

An authorized gauge change alters an observation. The readout depends on a
coordinate convention that was declared unphysical.

### Inadequate context

A declared observable behaviour cannot be represented by the model's
observation map.

### Incomplete context

Two source-inequivalent realizations have the same contextual record. The
interface has a hidden explanatory kernel.

### Unauthorized context

A proposed discriminator separates the models only by using an intervention or
reference absent from source authority.

The last case may be mathematically informative but cannot close the explanatory
gap in the programme.

## 4. Joint conservativity

The context family is jointly conservative on authorized equivalence classes if

\[
N(R)=N(R')
\]

forces a source equivalence. Thus full abstraction is precisely the claim that
the admitted contexts form a jointly conservative family.

This exposes the operational meaning of a source reference. A new reference is
useful exactly when adjoining its contexts strictly refines the experimental
nerve:

\[
N_{\mathbf C}(R)=N_{\mathbf C}(R'),
\qquad
N_{\mathbf C\cup\{c_*\}}(R)
\neq
N_{\mathbf C\cup\{c_*\}}(R').
\]

The reference does not merely add data. It kills a specific contextual kernel.

## 5. Relation to the kernel-reference theorem

For a linear readout \(L:S\to Y\) and a candidate reference
\(R:S\to Z\), the pair is faithful precisely when

\[
R|_{\ker L}
\]

is injective. This is the one-object linear instance of joint conservativity.

The categorical formulation adds composition: contexts may insert the unknown
realization into different source-derived words, ancilla couplings, or boundary
ports. A family can therefore be conservative even when no single static
readout is faithful.

## 6. Three-lens hierarchy

Let one carrier history admit additive, determinant-line, and ordered-holonomy
evaluations. Their context families generally form a strict hierarchy:

\[
\mathbf C_{\mathrm{add}}
\subseteq
\mathbf C_{\mathrm{phase}}
\subseteq
\mathbf C_{\mathrm{ord}}.
\]

Additive contexts can identify histories whose total current agrees while their
phase and order differ. Phase contexts can identify histories with the same
determinant but different noncommutative holonomy. Ordered contexts can retain
the complete word up to the authorized representation kernel.

Therefore a scalar completed section cannot be presumed fully abstract for an
operator-valued plant. It is fully abstract only if a separate theorem proves
that its kernel equals the authorized operator gauge.

## 7. Toric-code witness

Local syndrome contexts are not jointly conservative on logical sectors. Four
logical classes remain in one contextual fibre.

Adding two independent noncontractible loop probes makes the context family
jointly conservative modulo local stabilizer repairs on the smallest torus.
The reference extension kills the two-dimensional homological kernel.

This does not make the interface fully abstract for decoder mechanisms. To
separate decoders one must admit contexts probing repair locality, fault
propagation, cost, or behaviour under an enlarged noise family.

Thus full abstraction is always relative to the typed object being claimed:
logical state, decoder, controller, or physical implementation.

## 8. Quantum correction

Classical output probabilities need not be jointly conservative on quantum
processes. Ancilla-assisted and compositional contexts may be necessary to
separate channels. Likewise a central Wilson readout separates fewer objects
than the endpoint block algebra.

The correct experimental nerve must therefore specify whether contexts may use:

- coherent superpositions;
- entangled ancillas;
- sequential insertion;
- controlled interference;
- endpoint-resolved algebra;
- a phase or sheet reference.

Changing this list changes the explanatory equivalence relation.

## 9. Finite audit

For a finite realization family \(\{R_i\}\), construct a context matrix

\[
M_{ci}=N(R_i)(c).
\]

Then:

1. quotient the columns by authorized source equivalence;
2. compare the remaining columns over the current context family;
3. every repeated column is an explicit full-abstraction failure;
4. search authorized candidate contexts for a smallest set separating all
   remaining columns;
5. report any pair separable only by unauthorized contexts.

For linear operator spaces, replace columns by the induced measurement map and
compute its kernel. Full abstraction requires that kernel to equal the tangent
or linearized authorized-gauge directions, with a separate global audit when
the gauge action is nonlinear.

## 10. Minimal falsifier

A full-abstraction claim is falsified by:

\[
R\not\simeq_{\mathrm{src}}R',
\qquad
N(R)=N(R').
\]

The certificate must contain:

- the two typed realizations;
- the source invariant proving they are inequivalent;
- the complete admitted context family or its finite completeness theorem;
- equality of every contextual response;
- the smallest additional context known to separate them, if one is
  authorized.

## 11. Strengthened DPC

An explanatory interface is adequate only when its experimental nerve is fully
abstract for the source claims being made: contextual equivalence must coincide
with authorized source equivalence.

Consequently an explanation consists of two proofs:

1. a realization proof showing how constructors generate observations;
2. a full-abstraction proof showing that the admitted criticism can detect every
   non-gauge change relevant to the claimed explanation.

Without the second proof, success under all current tests may still be the
success of a shadow.

## 12. Critic

Full abstraction can be impossible or prohibitively expensive. A physically
available interface may be permanently too weak to distinguish the complete
source realization. Demanding full abstraction for every microscopic detail
would turn explanation into inaccessible tomography.

The repair is problem-relative typing. Declare the exact quotient the problem
needs and require full abstraction only for that quotient. Details outside it
must be reported as deliberately unclaimed, not silently inferred.

## 13. Bottom line

Predictive memory asks whether the record answers every admitted question.
Generative realization asks whether reusable constructors produce those
answers. Full abstraction asks whether the available criticism distinguishes
every non-gauge change to the claimed realization.

The deepest programme-level question is therefore:

> Does the admitted interface observe the explanation itself, or only one of
> its shadows?
