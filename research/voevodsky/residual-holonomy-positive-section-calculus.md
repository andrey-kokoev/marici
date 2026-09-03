# Residual holonomy and positive-section calculus

## Question

What does it mean for residual to be fundamental rather than an error, and which residuals must vanish, be quotiented, be trivialized, or remain positive?

## Claim boundary

This packet types the residual calculus and verifies finite fixtures. The arithmetic observer category's complete generator-and-relation presentation remains open.

## Four residual modalities

| Type | Object | Required disposition |
|---|---|---|
| Presentation | declared gauge or duplicate-label subobject \(G\) | quotient |
| Invisible | \(\ker(\prod_iO_i)/G\) | vanish for joint faithfulness |
| Anomaly | edge residual \(\Omega_f\) | obey composition and have zero directed periods after completion |
| Substantive | \(R=A^*A-B^*B=D^*D\) | remain natural and positive; generally not vanish |

The phrase “zero residual” is therefore ill-typed until the residual modality is named.

## Directed anomaly transport

For a lower-pyramid arrow \(f:x\to y\), define

\[
\Omega_f=K_y-f_*K_x.
\]

Then

\[
\Omega_{gf}=\Omega_g+g_*\Omega_f.
\]

For two parallel directed paths \(p,q:x\to y\), the period is

\[
\kappa_{p,q}=\Omega_p-\Omega_q.
\]

Coherence requires \(\kappa_{p,q}=0\), not \(\Omega_p=0\). Cutoff arrows need not be invertible, so these are comparisons of parallel paths rather than formal loop holonomies.

An enumerable test chooses rooted preferred paths in a generator graph, verifies defining relation cells, and compares each non-tree generator composite with the preferred path to its target. This is sufficient only after the generators and relations are proved to present the intended observer category.

## Cohomology caution

When \(K_x\) is globally assigned at every vertex and

\[
\Omega_f=K_y-f_*K_x,
\]

\(\Omega\) is a formal coboundary. Calling it a nontrivial cohomology class would be false. A genuine obstruction class requires local assignments without a global \(K\), or a specified coefficient system in which no global trivializer exists.

Endpoint and gamma data may provide a missing global trivialization of the prime-only presentation, but this must be stated as an extension of the coefficient object rather than as proof that a tautological coboundary was nontrivial.

## Positive defect section

For a contraction \(C\),

\[
R=A^*A-B^*B
=A^*(1-C^*C)A
=D^*D.
\]

The nonzero part of \(R\) is positive slack. Setting it to zero would force the comparison to be isometric and would generally annihilate the Weil form. The metaobserver instead transports restrictions

\[
R_J|_I=R_I
\]

and requires \(R_I\geq0\).

## Relation to earlier sectors

The same calculus appears as:

- the reachable/observable quotient in minimal control realization;
- syndrome-zero logical operators in quantum error correction;
- the `physical10` kernel resolved by faithful `physical16` coordinates;
- phase or route information invisible to intensity-only optics;
- higher descent obstructions after local overlap agreement.

Each asks whether the observer kernel is exactly the declared quotient or contains an additional global sector.

## Apex object

The corrected apex has three simultaneous coordinates:

\[
(\text{flat anomaly transport},
\text{natural positive section }R,
\text{zero invisible quotient kernel}).
\]

None can replace another. Flat transport does not imply positivity; positivity does not imply joint faithfulness; joint faithfulness does not determine the required anomaly trivialization.

## Disposition

Residual is the organizing object of the architecture. Laws act on residuals by four different operations: quotient, annihilation, trivialization, and cone admission. The final proof must verify those typed dispositions on an enumerable generator presentation rather than demand that every residual equal zero.

## Verification

- `research/voevodsky/residual-holonomy-positive-section-calculus-v1.json`
- `research/voevodsky/checkers/check_residual_holonomy_positive_section_calculus.py`
- `research/voevodsky/results/residual_holonomy_positive_section_calculus.json`
