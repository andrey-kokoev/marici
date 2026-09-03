# Opposed infinity domains in the four-pyramid RH diagram

## Question

Why do limits appear to travel in opposite directions, and how do the four pyramids react to each infinity domain?

## Claim boundary

The table types the limit directions and their compatibility conditions. It does not prove the missing contraction or positivity estimate.

## Fundamental variance

The source side is covariant: enlarging finite support, derivation depth, or approximation range adds generators and constructs a direct system.

The verification side is contravariant: every new identity or observer adds a constraint, so the admitted cone becomes smaller. Finite observer sets form a directed index category, but their solution cones form an inverse system.

Thus the same refinement arrow \(i\to j\) produces

\[
X_i\longrightarrow X_j
\qquad\text{and}\qquad
C_j\longrightarrow C_i.
\]

This is not a contradiction. Construction takes a colimit; conformance and positivity take intersections or inverse limits.

## Four-pyramid table

| Pyramid | Prime-support infinity | Identity/derivative infinity | Analytic cutoff/completion infinity | Observer-rank infinity | Heat-scale boundary |
|---|---|---|---|---|---|
| **P1: prime atomic** | Finite prime sets enlarge toward the Euler source by direct colimit. | Local Euler and Frobenius identities generate further relations. | No completed scalar is taken here. | Finite prime probes see only bounded support and are nonfaithful. | No primitive heat direction; smoothing is added only after a transform. |
| **P2: prime-derived transforms** | Prime powers and von Mangoldt packets enlarge covariantly with common cutoffs. | Jets, moments, and transform identities grow with order; the conformance equalizer shrinks as each identity is imposed. | Finite transforms may converge only after source estimates; absolute PNT bounds lose signed cancellation. | Moment/Hankel tests form descending necessary cones; every bounded order is nonfaithful. | Heat recurrence propagates toward broader smoothing, while recovery of narrow probes travels oppositely. |
| **P3: completed coupling** | Endpoint, gamma, and prime channels must enter one object before the support limit. | Mellin–Poisson, reciprocal, and polar identities identify one completed distribution. | Theta/Mellin approximants converge covariantly to the completed apex; sector limits do not commute separately through singular boundaries. | Restrictions of the completed kernel to finite packets are compatible, but positivity is not inherited from sector restrictions. | With \(\tau=1/(4t)\), forward heat increases \(\tau\); increasing \(t\) moves backward and does not preserve positivity. |
| **P4: order-enriched metaobserver** | Restricts the completed object back to every finite source stage and checks compatibility. | Takes the inverse limit of all conformance equalizers and all-order heat cones. | Requires one continuous apex map so every finite observation is a restriction of the same completed object. | Takes the inverse limit over all finite Gram packets; one fixed width is enough only when all ranks are retained. | Global scalar faithfulness requires every \(t>0\) and every derivative order; no one-parameter or finite-order slice is faithful. |

## Douglas factorization at the interface

Write the completed source form as

\[
Q(f)=\|Af\|^2-\|Bf\|^2.
\]

The infinite conformance identities must first prove

\[
\ker A\subseteq\ker B.
\]

Only then is

\[
C(Af)=Bf
\]

well defined on \(\operatorname{ran}A\). Positivity is a separate order statement:

\[
Q\geq0
\quad\Longleftrightarrow\quad
\|C\|\leq1.
\]

When the contraction exists, Douglas factorization gives the common certificate

\[
Q(f)=
\left\|
(1-C^*C)^{1/2}Af
\right\|^2.
\]

Every finite Gram certificate is then a restriction of this one apex certificate. This is the desired compatibility between the direct source colimit and inverse observer limit.

## Failure modes exposed by the table

- Taking positivity before completed coupling wrongly asks endpoint or prime sectors to be positive separately.
- Passing from finite source stages to the colimit without a uniform contraction loses order control.
- Treating more observers as more source data reverses variance.
- Using a finite observer truncation replaces the inverse limit by a nonfaithful projection.
- Running heat smoothing backward attempts to infer a stronger narrow-probe statement from a weaker broad one.

## Disposition

Four pyramids are useful here: prime atomic, prime-derived, completed coupling, and the order-enriched metaobserver. The first three construct by direct limits; the fourth reflects them through inverse limits. Final RH closure is a Beck–Chevalley-type compatibility condition: completion followed by observation must agree with finite observation followed by restriction, while one uniform contraction preserves the positive cone across the crossing.
