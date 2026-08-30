# BSD–SCC rank-realization microprogram

## Objective

Locate the first irreducible constructor-coherence gap between the analytic jet of an elliptic-curve \(L\)-function and the global arithmetic realization carried by rational points, heights, local defects, and the Tate–Shafarevich group.

For an elliptic curve \(E/\mathbf Q\), the rank conjecture is

\[
\operatorname{ord}_{s=1}L(E,s)
=
\operatorname{rank}E(\mathbf Q).
\]

The refined conjecture compares the first nonzero analytic jet with the period, regulator, Tamagawa factors, torsion correction, and \(\Sha(E)\).

## Scope

- Elliptic curves over \(\mathbf Q\).
- The completed, modular \(L\)-function.
- Analytic ranks \(0\) and \(1\) as theorem-backed fixtures.
- Analytic rank at least \(2\) as the first general open frontier.
- Rank equality, finiteness of \(\Sha\), and the leading-coefficient formula remain separate gates.

## SCC objects

| Role | Object |
|---|---|
| arithmetic constructor | \(E(\mathbf Q)\) |
| constructor multiplicity | Mordell–Weil rank |
| viewing form | Néron–Tate height pairing |
| separation volume | regulator |
| local instruments | reduction, Euler, conductor, Tamagawa, and local-solubility data |
| analytic observer | completed \(L(E,s)\) and its jet at \(s=1\) |
| hidden local-to-global defect | \(\Sha(E)\) |
| terminal comparison | rank equality and refined leading coefficient |

Analytic zero order is an observer multiplicity. Mordell–Weil rank is constructor multiplicity. Their equality must be witnessed; it is not definitional.

## Twelve moves

### M1 — Freeze one elliptic-curve packet

Record a global minimal model, conductor, discriminant, torsion subgroup, reduction type at every bad prime, real period convention, and completed \(L\)-function normalization.

### M2 — Derive the Euler observer

Construct the good-prime factors from \(\#E(\mathbf F_p)\), attach the bad-prime factors with declared reduction typing, and include the archimedean factor. Reject finite-prime agreement as authority for the completed analytic object.

### M3 — Certify the functional equation

Record analytic continuation, conductor normalization, gamma factor, root number, and the involution about \(s=1\). Separate a numerically observed central zero from a rigorously certified order of vanishing.

### M4 — Reproduce the analytic-rank-zero fixture

For a theorem-qualified curve with \(L(E,1)\ne0\), record:

- Mordell–Weil rank \(0\);
- finiteness of \(\Sha(E)\);
- which parts of the refined leading-coefficient formula are proved and which require further hypotheses.

Do not promote this fixture beyond its hypotheses.

### M5 — Reproduce the analytic-rank-one fixture

Use the Gross–Zagier height formula and Kolyvagin’s Euler-system theorem to connect \(L'(E,1)\ne0\) to a non-torsion rational point, rank \(1\), and finite \(\Sha(E)\).

The SCC filler is not merely the scalar equality \(1=1\). It includes the Heegner-point constructor and its positive height.

### M6 — Isolate the rank-two frontier

For analytic order \(r\ge2\), define the analytic jet line

\[
\mathcal J_E^{(r)}
=
\mathbf Q\cdot \frac{L^{(r)}(E,1)}{r!}
\]

with its normalization data. On the arithmetic side define the free Mordell–Weil lattice and its height Gram form. Record that equal dimensions, if known in a case, do not yet imply the refined comparison.

### M7 — Separate rank from realization

Audit three statements independently:

1. analytic rank is at least algebraic rank;
2. algebraic rank is at least analytic rank;
3. a source-derived comparison pairs analytic zero directions with independent rational-point directions.

Reject a numerical rank match that supplies no comparison constructor.

### M8 — Audit the regulator

Given independent rational points \(P_1,\ldots,P_r\), compute the Néron–Tate Gram matrix

\[
G_{ij}=\langle P_i,P_j\rangle_{\mathrm{NT}}
\]

and regulator \(\det G\). Distinguish:

- full rank;
- positive separation;
- a completion-stable lower height margin;
- basis-dependent coordinates versus the invariant covolume.

### M9 — Audit local-to-global failure

Use a torsor that is locally soluble everywhere but has no rational point as the hostile showing that local instruments can be jointly coherent while the global realization fiber is empty. Type its obstruction through \(\Sha(E)\), not through Mordell–Weil rank.

### M10 — Freeze the refined product

Form the typed arithmetic packet

\[
\frac{\Omega_E\,\operatorname{Reg}(E)\,|\Sha(E)|
\prod_p c_p}
{|E(\mathbf Q)_{\mathrm{tors}}|^2}.
\]

Every factor retains its source and normalization. Scalar compensation between an incorrect regulator, \(\Sha\), period, or Tamagawa factor is forbidden.

### M11 — Test the leading-coefficient comparison

Compare the arithmetic packet with \(L^{(r)}(E,1)/r!\). Require:

- rank equality first;
- finiteness of \(\Sha(E)\);
- compatible period and measure conventions;
- exact local factors;
- a constructor-level comparison, not decimal agreement.

### M12 — Issue the first-failure certificate

Return exactly one:

1. closed rank-and-leading-coefficient realization for the selected curve;
2. rank equality established but refined coherence open;
3. analytic and algebraic ranks not yet identified;
4. a typed local, height, \(\Sha\), or normalization obstruction;
5. insufficient rigorous analytic-rank certification.

## Required hostile fixtures

- identical finite sets of Euler factors with different global behavior;
- numerical vanishing mistaken for certified analytic rank;
- equal analytic and algebraic ranks without a point-to-jet comparison;
- full Mordell–Weil rank with a nearly singular height Gram matrix;
- everywhere-local solubility with no global point;
- scalar leading-coefficient agreement produced by compensating mistyped factors;
- finite \(\Sha\)-approximations promoted to a proof of finiteness;
- omission of the archimedean completion;
- rank-zero or rank-one theorems silently generalized to rank two.

## First expected result

The first structural reduction should be

\[
\text{BSD}
\longrightarrow
\begin{cases}
\text{rank comparison},\\
\text{height/regulator realization},\\
\text{local-to-global defect finiteness},\\
\text{typed leading-coefficient identity}.
\end{cases}
\]

The first generally open constructor comparison begins at analytic rank at least \(2\), after the rank-zero and rank-one Heegner/Euler-system fixtures are frozen.

## Falsifier of the microprogram

Revise the programme if a general theorem already closes the declared rank-two packet with finite \(\Sha\) and the refined leading coefficient, or if the rank-zero/rank-one fixtures require hypotheses omitted from their SCC typing.

## Source anchors

- Gross and Zagier, *Heegner points and derivatives of L-series*.
- Kolyvagin, *On the Mordell–Weil and Shafarevich–Tate groups for Weil elliptic curves*.
- Clay Mathematics Institute formulation of the Birch and Swinnerton-Dyer problem.

