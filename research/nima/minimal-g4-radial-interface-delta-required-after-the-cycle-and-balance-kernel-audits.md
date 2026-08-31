# Minimal G4 radial interface delta required after the cycle and balance kernel audits

## Question

What is the smallest testable extension of SCC's `g4_common` descriptor that can decide radial–G4 conformance without asserting the missing mathematics?

## Claim boundary

The current five-field descriptor cannot distinguish retained labels, common-history quotienting, state-retaining recovery, endpoint–Wronskian balance, or a downstream Green radical. The following fields and laws are necessary and jointly sufficient to run the already-derived kernel tests. This is a proposed interface delta in the Nima locus, not a mutation of Aspect-owned SCC files.

## Current descriptor gap

SCC v2 exposes only:

- `coefficient_object`;
- `completion`;
- `topology`;
- `quotient`;
- `authority`.

Its contract contains no radial state, Wronskian, codiagonal, recovery, observer, radical, or metric field. `all_interfaces_checked: true` therefore checks only reuse of the coarse descriptor.

## Required fields

### Carrier placement

`radial_carrier` must declare whether G4 retains:

- labelled oriented histories;
- common unlabelled histories;
- complete states \(\rho_\pm\);
- only wall and transform readouts.

### Source synthesis

`radial_source_map` must identify

\[
U:C\longrightarrow X
\]

and expose whether

\[
\ker U=Z_1(G)
\]

or labels make \(U\) faithful.

### Directed feature packet

`radial_feature_map` must locate the complete maps producing

\[
(-\rho(0),E_+,W_+;+\rho(0),E_-,W_-)
\]

and state whether the entire transform families or only selected values are retained.

### Codiagonal

`radial_codiagonal` must expose the coefficient and signs in

\[
D=E_++E_--\frac12(W_++W_-).
\]

### Recovery

`radial_recovery` must provide either complete state retention or a map

\[
\mathcal QP_\rho x=x
\]

on \(\operatorname{ran}U\), with topology and continuity witness.

### Cycle treatment

`cycle_policy` must select exactly one of:

1. labels retained;
2. quotient by \(Z_1(G)\);
3. reciprocal-equivariant cycle observer retained.

### Green form

`green_form` must identify the form, variance convention, metric, and feature stage on which it acts.

### Radical and quotient

`green_radical` must provide a feature or form definition and the quotient map. It may equal \(Z_1(G)\) only after nondegeneracy on the common-history range is proved.

### Return placement

`return_map` must state whether return occurs before or after label codiagonalization, cycle quotienting, and endpoint–Wronskian balance.

## Required laws

A conforming witness must prove or explicitly leave open:

1. source typing of \(U\);
2. reciprocal covariance of \(U\), \(D\), and any cycle observer;
3. the exact kernel sequence
   \[
   0\to\ker U\to\ker(DU)\to\operatorname{ran}U\cap N_{\rm bal}\to0;
   \]
4. state recovery, if the collapsed-kernel theorem is invoked;
5. nondegeneracy of the Green form on its declared feature range;
6. quotient compatibility with prime, grade, shell, and ordered-pair projections;
7. continuity on the declared projective completion.

## Hostile fixtures

The interface checker must reject:

- `all_interfaces_checked` used as radial conformance;
- a readout-only carrier claimed to retain full radial state;
- pairwise collision freedom claimed as polarized faithfulness;
- interval cycles renamed a Green radical without a form;
- source-ray faithfulness promoted to polarized-carrier faithfulness;
- endpoint–Wronskian balance identified with interval cycles;
- a forest observer chosen after inspecting source coefficients or Xi zeros;
- a nondegenerate metric inferred from one real return scalar;
- return prime diagonality inferred after undeclared codiagonalization.

## Decision table

- If labels are retained, require labelled recovery and a separately defined Green radical.
- If common history retains full radial state, the pre-metric composite kernel is exactly \(Z_1(G)\).
- If common history is readout-only, require an explicit audit of \(\operatorname{ran}U\cap N_{\rm bal}\).
- If a cycle observer is retained, require reciprocal and cutoff intertwining.
- In every case, Green-radical equality requires downstream range nondegeneracy.

## Disposition

This delta is sufficient to turn the current architectural ambiguity into executable conformance questions while preserving every open proof obligation. Adoption, SCC mutation, and witness authoring remain Aspect-owned. No RH conclusion is authorized.
