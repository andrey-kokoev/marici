# Deutsch--Popper conjecture: physical ports are constructible records

## Problem

Entry 2128 says that source-added relational structure may reduce the physical
groupoid and make a relative observable descend. That is still too permissive
unless the source can physically create and interrogate the relation.

A mathematical marking may reduce an automorphism group on paper while no
admitted operation can establish that marking as a persistent record.

## Conjecture

A reference port \(R\) is physical only if the sector source supplies a
constructor protocol

\[
\text{prepare }R
\longrightarrow
\text{couple }R\text{ to the target}
\longrightarrow
\text{preserve/transport the correlation}
\longrightarrow
\text{interrogate the record}.
\]

Equivalently, the port must be realized by an admitted interaction whose
induced action on the intended physical quotient is nontrivial. Merely naming
a smaller stabilizer group does not establish constructibility.

## First exact attack: toric support threshold

In the periodic toric chain code, a logical reference port must distinguish
classes in

\[
H_1=\ker\partial_1/\operatorname{im}\partial_2.
\]

An edge-supported operation can do so only if its residue-free chain is not a
face boundary. Exact enumeration for \(L=2,3,4\) proves that every residue-free
operation of weight less than \(L\) is a local repair,

while the first nontrivial logical cycles occur at weight exactly \(L\). There
are \(2L\) minimum straight representatives.

Therefore an operation confined below the code distance cannot construct,
read, or orient a logical loop port. The coordinate exists mathematically,
but it is inaccessible to the declared local constructor class.

## Explanation

The marked homology basis of Entry 2128 is physical only when the experiment
contains a resource spanning a noncontractible support: a Wilson-loop
interaction, a suitably extended ancilla protocol, a boundary construction,
or equivalent dynamics. The required resource is not arbitrary additional
metadata. Its support must reach the capability it claims to reference.

This produces a three-level distinction:

\[
\begin{array}{c|l}
\text{definable port} & \text{a mathematical functional exists},\\
\text{descending port} & \text{it is invariant under the declared framed groupoid},\\
\text{constructible port} & \text{an admitted physical task realizes that frame and readout}.
\end{array}
\]

Only the third level supplies an explanation of why the port belongs to the
world rather than to our description.

## Falsifiers

The conjecture fails if:

1. a subdistance local protocol distinguishes toric logical classes without
   adding a boundary or nonlocal resource;
2. a source-derived reference record exists but induces no nontrivial action
   or pairing on the proposed quotient;
3. two claimed implementations have the same relational groupoid reduction
   but inequivalent operational capabilities, with no retained constructor
   datum distinguishing them;
4. the port remains observable after deleting every source operation capable
   of preparing or interrogating its record.

## Next attack

Promote support size to a sector-neutral resource condition. Given an
operational algebra \(\mathcal A_{\mathrm{adm}}\) and protected quotient
\(\mathcal C\), define the accessible readout algebra as the image of
\(\mathcal A_{\mathrm{adm}}\) on \(\mathcal C\). A proposed port is physical
only if its readout lies in that image or in a source-derived completion with
an explicit limiting protocol.

Then test the same criterion on:

- flavor weak-basis invariant measurements;
- cosmological source-normalized Leray pairings;
- Strominger's magnetic kernel witnesses;
- framed Berry/open-transport experiments.

## Verification

- `research/nima/checkers/check_constructible_reference_port.py`
- dependency-free invocation:
  `python research/nima/checkers/check_constructible_reference_port.py`
