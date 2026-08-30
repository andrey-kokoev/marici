# Port-dimension counting cannot derive the RH seam carrier

Author: `marici.Nima`

Date: 2026-08-26

Status: correction and no-go for deriving seam multiplicity from squareness

## The invalid inference

At a finite labelled cutoff with forcing dimension (N), the raw quadrature
presentation has (N+1) incoming feature coordinates and (N) outgoing
quadrature coordinates. This gives a dimension deficit of one.

It does not follow that the physical seam is one scalar output per sector.
That conclusion confuses a port-only contraction with its complete state-space
colligation.

## The actual defect carrier

For a contraction $T_X$, the minimal isometric dilation uses the defect
space

\[
\mathcal D_X
=
\overline{\operatorname{Ran}(I-T_X^*T_X)^{1/2}}.
\]

Its multiplicity is

\[
r_X=\operatorname{rank}(I-T_X^*T_X),
\]

which is not determined by the difference between raw input and output
dimensions.

In the tail-flow identity, the defect Gramian is already factored by the
retained state feature (G). After Cayley rescaling, this state feature is the
one adjoined by the lurking isometry. It is not automatically the independent
seam carrier.

## Correct conservative signature

A conservative colligation acts on state plus port:

\[
\mathcal H\oplus\mathcal E_{\mathrm{in}}
\longrightarrow
\mathcal H\oplus\mathcal E_{\mathrm{out}}.
\]

The same state type occurs on both sides. Counting only endpoint and
quadrature coordinates omits this state channel and cannot establish the
dimension of either external port space.

Abstract unitary dilation may also add defect and co-defect spaces of ranks
larger than one. Matrix squareness is therefore only a consistency check after
all source types have been constructed.

## What still forces the seam

The seam remains independently required by valid earlier theorems:

- it cannot be reconstructed boundedly from the retained tail;
- it carries translated source norm that survives when the tail norm escapes;
- its boundary trace participates in modular reciprocal sewing;
- its omission changes the source operation rather than merely its
  presentation.

These facts establish a primitive seam carrier. They do not yet determine its
input-output variance, multiplicity, or relation to the passive defect space.

## Directed traces remain a hypothesis

A geometric interface normally has incoming and outgoing traces, and the two
causal sectors suggest two oriented seam appearances. But this must be derived
from the Green boundary form or Tate sewing operator.

It cannot be inferred from the numerical deficit (N+1-N=1).

The next legitimate seam theorem must construct the boundary trace map and
compute its Gramian. Only then can one decide whether:

- the seam equals the passive defect carrier;
- it is an external port;
- it is a larger independent reservoir;
- it splits into two directed traces under reciprocal sewing.

## Finite falsifier

For the actual cutoff operator, compute both

\[
I-T_X^*T_X
\]

and the proposed seam Gramian. A mismatch in rank, kernel, or labelled support
disproves the identification. Dimension agreement alone is never sufficient.
