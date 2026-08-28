# Threshold Hodge Matching Has a Central Lift Fiber and a Free Gain Jump

## Question

Does the ordered Hodge data on the two sides of a threshold uniquely determine
the matching constructor needed by WP882?

## Projector-level matching

Let ((H_-,J_-)) and ((H_+,J_+)) be ordered Hodge pairs on two real singlet
planes. A matching isometry (M) must obey

\[
MH_-=H_+M,
\qquad MJ_-=J_+M,
\qquad M^TM=I.
\]

After choosing ordered orthonormal representatives (R_-) and (R_+), all
solutions are

\[
M=\sigma R_+R_-^T,
\qquad \sigma\in\{+1,-1\}.
\]

The Hodge pair therefore fixes the orthogonal matching only up to its central
sign. If only (H) is retained, four independent sign choices survive; the
orientation tensor (J) reduces this to the diagonal twofold fiber.

Conjugation of projector or adjoint data cannot see this lift:

\[
(-M)H_-(-M)^{-1}=MH_-M^{-1}=H_+.
\]

Consequently the central sign is not an ambiguity of the transported
`physical16` point. It becomes observable only in a relational amplitude
experiment with an independently retained reference path.

## Portal matching

For (G_-=g_-H_-) and (G_+=g_+H_+), the most general Hodge-compatible
threshold rule is

\[
G_+=\eta M G_-M^{-1},
\qquad \eta=\frac{g_+}{g_-}.
\]

The ordered Hodge geometry fixes the direction (H_+), but it does not fix
the real threshold coefficient (eta). Neither the central lift sign nor
projector conjugation can select it. A completion-specific finite matching
calculation is required.

## Contextual partition

There are three distinct levels:

1. projector/adjoint histories identify (M) and (-M);
2. amplitude histories retain the two central lifts only if a reference path
   is part of the experiment;
3. portal-strength histories additionally retain the continuous parameter
   (eta).

Thus smooth co-moving transport followed by an unspecified threshold factors
through a first nonfaithful arrow at finite matching: the source Hodge pair
does not determine the scalar jump.

## Smallest exact falsifiers

- Lift hostile: (M) and (-M) have identical conjugation action.
- Gain hostile: (eta=1) and (eta=2) transport the same ordered Hodge
  direction but give strengths differing by two and intensities by four.
- Under-typed hostile: retaining (H) but dropping (J) enlarges the lift
  fiber from two to four sign choices.

## Aspect classification

- Realization: the algebraic threshold intertwiner is exact.
- Tester: the (H)-only, Hodge-pair, and gain fibers are enumerated.
- Falsifier: the two central lifts and two gain values are explicit hostiles.
- Ontology: nonorthogonal wave-function matching and channel mixing remain
  fresh terms outside this packet.
- Governance: (eta) is deferred until one matter completion and its finite
  threshold action are source-authorized.
- Portfolio: observing the lift sign requires a new relational reference
  experiment over the corresponding stabilizer groupoid.

## Verdict

The ordered Hodge pair rigidifies the adjoint matching across a sharp
threshold, but does not select a portal-strength jump. The residual central
sign is invisible on the original physical quotient; adding a coherent
reference port defines a new relational experiment rather than recovering an
absolute sign.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp883_threshold_hodge_intertwiner_fiber.py
~~~
