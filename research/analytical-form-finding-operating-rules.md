# Analytical form-finding operating rules

Use these rules when constructing analytical realizations, comparison maps, determinant packets, boundary forms, completions, or scalar readouts.

## Governing sequence

Work in this order:

1. source operation;
2. type declaration;
3. composition law;
4. transport law;
5. finite falsifier;
6. completion topology;
7. packet sewing;
8. noncollapse test;
9. scalar readout.

Reversing this sequence risks importing the desired readout into its proposed source.

## Rules

### 1. Start from an independent source operation

Derive each form from incidence, translation, convolution, boundary restriction, graph composition, functional calculus, valuation refinement, or a declared completion functor. Do not reconstruct the source backward from a desired scalar identity, divisor, sign, or cancellation.

### 2. Type objects before calculation

Declare the carrier, base state, variance, grading, domain, cutoff dependence, topology, reciprocal action, and scalarization map. Similar formulas on different carriers are not interchangeable.

### 3. Preserve the full response packet

Retain all independent response coordinates through sewing. Quotient a coordinate only after proving that it lies in the relevant radical. A convenient scalar projection is not evidence that the omitted channel is null.

### 4. Separate absolute and relative claims

A cancellation in an absolute complex does not automatically hold in a relative cone. Construct the comparison cell between source boundaries, endpoint terms, and determinant or Tate lines before transporting the cancellation.

### 5. Base state-dependent comparisons

If a boundary value depends on a state `G`, its realization must retain that base, for example

\[
\kappa_G:Q_a\longmapsto K_{G,a}.
\]

Reject a universal unbased map when its proposed trace or boundary value varies with `G`.

### 6. State the actual composition law

For state-indexed operations, composition occurs over the transported base. A representative law is

\[
K_{G,a+b}=K_{G,a}\star K_{S_aG,b}.
\]

Do not replace a translation-groupoid cocycle by an unbased algebra homomorphism.

### 7. Separate grades before completion

Keep primitive, square, connected, endpoint, archimedean, and relative-anomaly channels distinct. Equal scalar degree or regularization order does not identify their source types.

### 8. Assign regularized determinants only their supported grades

For `K` in the third Schatten class,

\[
\det(I+K)=\det_3(I+K)
\exp\!\left(\operatorname{Tr}K-\frac12\operatorname{Tr}(K^2)\right).
\]

Treat the first trace, square trace, and connected determinant as separate typed data. Do not ask the regularized tail to reconstruct the removed low grades.

### 9. Do not infer an operator from finitely many moments

Matching `Tr K` and `Tr(K^2)` does not determine the spectrum or `det_3(I+K)`. Require independent connected spectral data or a source construction of the complete operator.

### 10. Test whether an anomaly is already a coboundary

Normalize an exact anomaly once and use the resulting strict module law. Do not add independent pair and triangle coherencers when one source-derived counterterm generates them.

### 11. Scalarize last

First construct labelled operators, determinant lines, reciprocal transitions, archimedean transitions, and monodromy. Select a scalar section only after these data sew. A local scalar coordinate is not automatically a global function.

### 12. Do not continue a primitive current through the target section

A logarithm of the completed target, a branch cut selected from its divisor, or cancellation checked only after scalar aggregation is not a source construction. Continue primitive data as labelled operators, transition cocycles, connections, or line-valued sections.

### 13. Preserve monodromy rather than hiding it

When a global logarithm is obstructed, retain a determinant line with connection or a groupoid-valued section. Branch dependence is geometric data, not a nuisance to erase.

### 14. Interpret Euler projectors as refinement boundaries

For

\[
\Pi_P=\prod_{p\in P}(I-S_p),
\]

regard `Pi_P` as the total Möbius boundary of the finite prime-refinement cube. A finite prime set leaves infinitely many prime-free cores; isolation of a unique primitive vertex requires a controlled all-prime limit.

### 15. Distinguish finite coherence from completed coherence

A compatible cutoff family defines a pro-object. Completion additionally requires a declared realization topology, Cauchy or compactness control, a source-derived boundary value, and exclusion of phantom compatible families. Uniform boundedness alone is insufficient.

### 16. Determine cutoff variance before defining bonding maps

Establish whether refinement forms a direct system, inverse system, correspondence, or common pre-quotient core. Shrinking radicals naturally produce inverse quotient maps; forcing direct inclusions can make the construction ill-defined.

### 17. Prove transport before quotienting

Construct forward and contragredient transport on the common carrier first. An early quotient can erase a detectable direction or require noncanonical lifts at finer cutoffs.

### 18. Classify every scalar factor by function

Record whether a factor is a frame normalization, anomaly, endpoint contribution, index, kernel or cokernel term, or invertibility defect. Nonvanishing exponential factors change frames but not divisors.

### 19. Require packet sewing, not scalar coincidence

Compare energies, endpoint currents, forcing currents, determinant lines, reciprocal transport, and archimedean terms. Agreement of one scalar projection is not a comparison theorem.

### 20. Test noncollapse after sewing

Verify that sewing has not annihilated transverse response, reciprocal orientation, determinant monodromy, source-state dependence, or primitive boundary data. Formal closure can otherwise be vacuous.

### 21. Attach a finite falsifier to every proposal

Name the smallest computation that can reject the form: an incompatible state pair, failed refinement square, non-Cauchy tower, chart mismatch, equal low moments with unequal determinants, or a forbidden-sign tail.

### 22. Prefer exact finite arithmetic

Use rational spectra, symbolic traces, exact determinants, algebraic cocycle identities, and certified residual signs where possible. Numerical calculations scout candidates; they do not authorize identities.

### 23. Require naturality before promotion

A local formula becomes a geometric object only after compatibility with the applicable interval composition, source-state transport, prime refinement, reciprocal involution, Tate-line transport, and cutoff bonding maps.

### 24. Localize unresolved content by grade and cell

Record exactly which grade, comparison cell, convergence claim, or positivity statement remains open. Do not report the whole architecture as unresolved when transport, connected tails, or anomaly coherence are already closed. Do not infer global completion from those local closures.

### 25. Label theorem strength

Classify each result as a formal identity, finite-cutoff theorem, convergence theorem, source realization, comparison theorem, positivity theorem, or an equivalence-strength gate. The label determines which downstream uses are authorized.

## Master rule

Construct on the richest faithful source carrier, preserve all typed boundary data through composition and completion, and scalarize only after naturality, convergence, packet sewing, and noncollapse are proved.

## Review checklist

Before accepting an analytical form, answer:

- What source operation constructs it?
- On which carrier and over which base does it live?
- What is its variance and composition law?
- Which coordinates and grades are retained?
- What transports it across charts and refinements?
- What finite test can falsify it?
- In which topology does its cutoff system complete?
- Which packet components are sewn?
- What proves that the sewn object does not collapse?
- Which final map produces the scalar readout?
