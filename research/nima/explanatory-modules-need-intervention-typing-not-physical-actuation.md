# Explanatory modules need intervention typing, not physical actuation

## Correction

Modular explanation requires meaningful variation of one mechanism while the
others remain fixed. It does not require every variation to be physically
executable by the investigator.

Three levels must be separated:

1. formal substitution;
2. source-admissible counterfactual intervention;
3. physically executable actuation.

## Formal substitution

Given

\[
E=\mathcal I(M_1,\ldots,M_k),
\]

one can write

\[
M_i\leftarrow M_i'
\]

for any syntactically compatible object. This has no explanatory force if the
replacement violates the laws defining the source family.

A type-correct symbol replacement is not yet a possible-world claim.

## Source-admissible intervention

A counterfactual replacement is source-admissible when the theory supplies:

- a stable interface for the replaced module;
- laws defining the permitted replacement family;
- a splice or transport operation into the unchanged Carrier;
- inherited domains and boundary conditions;
- a rule for which other modules remain fixed;
- derived consequences after replacement.

This is enough for explanatory criticism even when no experimenter can enact
the replacement directly.

Natural variation, comparative systems, simulations derived from the same
laws, and indirect observations may test such counterfactuals.

## Physical actuation

An executable intervention additionally requires:

- an actuator port;
- a control protocol;
- preparation and reset conditions;
- isolation or disturbance bounds;
- a readout instrument;
- fault and common-mode typing.

These are constructor obligations of an implementation programme. Their
absence blocks experimental execution, not necessarily explanatory content.

Possessing a canonical mathematical replacement does not construct the
actuator that realizes it.

## Control-theoretic analogue

Structured robust control studies uncertainty blocks

\[
\Delta=\operatorname{diag}(\Delta_1,\ldots,\Delta_k)
\]

even when the individual perturbations are not command inputs. The block
structure states which plant variations are admitted and which interconnection
channels they occupy.

An actuator input \(u\), by contrast, is an executable port in the plant
equations. Treating every uncertainty block as an actuator invents control
authority.

Thus structured uncertainty can support explanation of sensitivity without
supplying a constructor for controlled replacement.

## Module equivalence

Module decompositions should not be compared by coordinate equality. Two
decompositions are explanatorily equivalent when an authorized equivalence
transports:

- module objects;
- stable interfaces;
- admissible replacement families;
- interconnection;
- change/invariance signatures;
- lower-lens readouts.

If two state-space similarities preserve the aggregate transfer but only one
preserves these replacement semantics, they are behaviourally equivalent but
not equivalent as modular explanations.

Conversely, distinct-looking decompositions may be the same explanation when
their intervention categories are equivalent.

## Toric-code classification

Changing periodic attachment or replacing the Pauli coefficient lens is a
source-admissible comparative variation of the model family. It need not be a
command executable on one already fabricated toric-code device.

Changing a decoder table or noise-control policy may be physically executable,
depending on the hardware interface.

The distinction is:

- topology and coefficient ablations test explanatory dependence;
- decoder commands test implementation control;
- neither licenses the other.

## Hostile cases

- A purely syntactic replacement is called physically possible.
- An uncertainty block is treated as an actuator input.
- Lack of direct actuation is used to dismiss every counterfactual
  explanation.
- A canonical frame is mistaken for an implementation protocol.
- Two module decompositions are identified because their scalar transfer
  agrees while their replacement semantics differ.
- Equivalent intervention categories are treated as rival explanations
  because their coordinates differ.
- A physically executable command is assumed to isolate one module despite
  uncontrolled common-mode coupling.

## Revised conjecture

Explanatory modularity requires a source-typed category of counterfactual
replacements and a predicted pattern of invariance and change. Physical
actuation is a stronger, separately typed constructor.

The abstract distinction, canonical counterfactual frame, and physical
implementation remain three different achievements.
