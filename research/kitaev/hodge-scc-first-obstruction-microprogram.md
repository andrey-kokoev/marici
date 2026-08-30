# Hodge–SCC first-obstruction microprogram

## Objective

Determine, in the smallest genuinely higher-codimension regime, exactly which SCC realization cell is not supplied by the known constructor theory:

\[
CH^p(X)_{\mathbf Q}\xrightarrow{\operatorname{cl}}
H^{2p}(X,\mathbf Q)\cap H^{p,p}(X).
\]

The programme does not attempt to prove the Hodge conjecture globally. It seeks the first irreducible missing constructor after all Lefschetz-generated classes have been removed.

## Scope

- Smooth projective complex varieties.
- Rational coefficients.
- First frontier: codimension \(2\) on fourfolds.
- Integral coefficients appear only as a hostile fixture.
- Every result remains typed by variety, codimension, coefficient lens, equivalence relation, and admitted functorial operations.

## Why this is the first frontier

Codimension one is closed by the Lefschetz \((1,1)\) theorem. Hard Lefschetz transports the divisor result through the corresponding low-dimensional cases. The first packet not exhausted by this mechanism is the primitive rational \((2,2)\) sector of a fourfold.

With a chosen polarization \(L\), split the Lefschetz-generated and primitive sectors. The Lefschetz-generated summand has an algebraic constructor. The primitive summand is the live realization fiber.

## Twelve moves

### M1 — Freeze the typed packet

Record \(X\), its polarization \(L\), codimension \(2\), rational coefficients, rational equivalence on cycles, and the cycle-class target. Reject any argument that changes one of these silently.

### M2 — Reproduce the codimension-one closure

Express the divisor–Picard–first-Chern-class bridge as an SCC filler. Identify exactly which exponential-sequence cells make the realization map surjective.

### M3 — Prove the low-dimensional reduction

State the precise Hard Lefschetz transport that closes the relevant threefold packet. Record every hypothesis and coefficient choice. This prevents a known \(p=1\) consequence from being mistaken for higher-codimension evidence.

### M4 — Split off Lefschetz-generated classes

For a polarized fourfold, separate the Lefschetz-generated classes from the primitive \((2,2)\) sector. Transport divisor constructors into the first summand and verify the cycle-class square.

### M5 — Define the primitive realization fiber

For \(h\in\operatorname{Hdg}^2_{\mathrm{prim}}(X)\), define

\[
\mathcal R_X(h)=
\{Z\in CH^2(X)_{\mathbf Q}:\operatorname{cl}(Z)=h\}.
\]

Classify it as inhabited, empty, or unknown. Do not infer a preferred representative.

### M6 — Audit standard intermediate constructors

Test line bundles, vector bundles, coherent sheaves, \(K_0\), and Chern characters. For each, determine whether it enlarges the cycle-class image or merely repackages algebraic cycles already in \(CH^2\).

### M7 — Audit deformation transport

Over a smooth projective family, distinguish:

- a flat cohomology class remaining of type \((2,2)\);
- an algebraic cycle transported in the family;
- a class that is algebraic only on special fibers.

The SCC cell must not replace relative-cycle existence by Hodge-locus membership.

### M8 — Audit monodromy and realization fibers

Compute the action of admitted monodromy on the primitive Hodge sector and on known algebraic-cycle classes. Equal invariant subspaces do not imply surjectivity; require an actual intertwining realization.

### M9 — Insert the integral hostile

Use a known failure of the integral Hodge statement to verify that the checker rejects the rule “integral Hodge type implies integral algebraic cycle.” Then identify exactly which obstruction rationalization removes.

### M10 — Form the constructor-cokernel

Define

\[
\mathcal C_X^2=
\operatorname{Hdg}^2_{\mathrm{prim}}(X)/
\operatorname{cl}\bigl(CH^2(X)_{\mathbf Q}\bigr)_{\mathrm{prim}}.
\]

The Hodge conjecture in this packet is \(\mathcal C_X^2=0\). Treat this quotient as an obstruction classifier, not as evidence that a nonzero class exists.

### M11 — Search for a complete intermediate bridge

For each proposed enrichment—normal functions, variations of Hodge structure, derived objects, or motives—require two arrows:

\[
\text{algebraic cycles}\longrightarrow\text{enriched object}
\longrightarrow\text{primitive Hodge class}.
\]

The enrichment is useful only if its source-authorized realization theorem is stronger than a restatement of Hodge type and descends back to an algebraic cycle.

### M12 — Produce the first-failure certificate

Return exactly one of:

1. a source-derived primitive cycle realizing the selected class;
2. a classified finite torsor of realizations;
3. an empty realization fiber proved by a typed obstruction;
4. an open constructor cell with the earliest unavailable arrow identified.

## Required hostile fixtures

- scalar period agreement with no algebraic-cycle preimage;
- a \(K\)-theory representative whose Chern character merely repackages a known cycle;
- a class remaining \((2,2)\) under observation while no relative cycle is constructed;
- monodromy invariance promoted incorrectly to algebraicity;
- an integral obstruction silently erased without declaring rationalization;
- a proposed motivic or derived filler with no descent to \(CH^2(X)_{\mathbf Q}\);
- equality after projecting away the primitive sector.

## First expected result

The likely first result is a structural reduction:

\[
\text{general Hodge realization}
\longrightarrow
\text{primitive codimension-two realization on fourfolds},
\]

with the divisor-generated sector removed and every proposed intermediate constructor classified as realization-bearing or observational only.

## Falsifier of the microprogram

The programme is incorrectly scoped if either:

- a genuinely lower-dimensional rational Hodge packet survives the Lefschetz reduction; or
- primitive codimension-two fourfold classes are already covered by a general theorem supplying algebraic cycles.

Either finding changes the declared first frontier and requires a scope revision.

