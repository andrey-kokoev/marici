# Primitive-Current Reflection under Aspect's Germ Tester

## Question

Does the scale-free completion selector of WP836 become a source selector when
the primitive Ward current (q=(1,2,3)^T) is retained and used to fix the
mixing orientation?

## Candidate construction

The normalized current projector and its Householder reflection are

\[
P_q=\frac{qq^T}{q^Tq},\qquad H_q=I-2P_q.
\]

The reflection is self-adjoint, satisfies (H_q^2=I), has trace one, sends
(q) to (-q), and fixes (q^\perp). Conversely, any self-adjoint involution
on the three-state carrier with trace one and (Hq=-q) equals (H_q). Thus,
after the current attachment is retained, the rule fixes the mixing
orientation left open by WP836. The alternative equal-singular minimizer
reflecting the all-ones line fails the current condition.

## Marked germ and native relation

The marked carrier is not (D) alone. It is the attached pair ((q,D)), with
the current identity, its Ward/inflow provenance, and the comparison port to
the declared completion family retained. The target has two layers:

1. compare the candidate with every admitted finite completion using
   \(\Phi_\lambda\);
2. on the minimal three-state fiber, require the negative eigenspace of the
   normalized spectral operator to equal the retained current line.

Consequently the minimization is family-relative, not a unary predicate on an
isolated packet. Forgetting either the comparison family or the attachment
map fails Aspect's native-arity gate.

## Full-fiber gate

For an orthogonal change of carrier frame (U), transport both fields:

\[
q\mapsto Uq,\qquad D\mapsto UDU^T.
\]

Then (P_{Uq}=UP_qU^T) and (H_{Uq}=UH_qU^T). The construction therefore
descends through the simultaneous orthogonal-frame fiber. It does not descend
through a quotient that retains (D) but forgets the current attachment:
distinct current lines select distinct reflections. Nor has descent through
the full complex weak-basis groupoid been established, because the present
real self-adjoint spectral carrier has not been derived as a covariant object
of the flavor source theory.

The absolute scale remains a complete fiber:

\[
D_m=mH_q,\qquad m>0.
\]

Every (D_m) has the same scale-free score and current-aligned normalized
reflection. The pair (m=1,2) is the smallest exact hostile to any claim that
this structure predicts a threshold mass.

## Authority gate

The algebra proves a unique equivariant section only after supplying three
things: the primitive current, the direct-completion grammar, and the
reflection law. WP820 authorizes the first conditionally. No admitted source
action currently derives minimization of \(\Phi_\lambda\) or the rule that the
spectral negative line must equal the current line. A natural equivariant
formula is not itself a constructor.

There is also no realization arrow from this comparison to RG preparation,
finite-threshold survival, or a calibrated `physical16` detector record.
Aspect's authority gate therefore rejects promotion to a physical selector.

## Verdict

The structure passes the exact algebraic and simultaneous-frame fiber tests
and conditionally removes WP836's mixing-orientation ambiguity. It fails the
source-authority and physical-realization gates, and it leaves the positive
scale fiber untouched. Its present type is an equivariant presentation
rigidifier attached to a conditional finite-completion selector, not yet a
source-generated selector on `physical16`.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp837_primitive_current_reflection_aspect_germ_audit.py
```
