# Aspect Germ Tester Audit of the RG Curvature Triplet

## Question

Does the WP827 curvature-anchor construction have the structure required by
Aspect's marked-carrier germ calculus?

## Retyping

WP827's list of ten ingredients is not a native ten-argument relation. The
ingredients describe a proposed implementation stack. The target relation has
native arity three:

\[
(u_-,u_0,u_+)\longmapsto t_+-2t_0+t_-=0.
\]

Its marked carrier germ is one oriented logistic RG trajectory with:

- a type: an RG trajectory with two intrinsic curvature anchors;
- an identity token: the same trajectory with lower, portal, and upper labels;
- a provenance interface: beta field to acceleration to jerk-zero anchors;
- an unconsumed comparison port: the shared RG clock and common calibration
  epoch.

The three events are not primitive germs. A separate realization map must bind
the carrier to three ordered detector records.

## Fiber gate

Let the adjacent time gaps be

\[
d_- = t_0-t_-,\qquad d_+=t_+-t_0.
\]

The map from three event times to \((d_-,d_+)\) is constant on every common
translation orbit. Likewise, the map from three event energies to their two
adjacent ratios is constant on every common-gain orbit. These are full-fiber
statements, not merely tangent-kernel checks.

Independent event gains fail the fiber gate. Therefore calibration cannot be
completed separately at the three events and sewn afterward. The common
comparison port must be retained until both ratios are formed.

## Arity gate

Equal spacing is a ternary relation. It can be presented as equality of two
binary gaps only if both gaps retain the identical portal record and the same
trajectory provenance. Without that shared identity, two numerical gaps do
not establish one curvature triplet. Thus the binary factorization is
conditional, not automatic.

## Authority gate

The source beta field conditionally selects the three state values and their
ordering inside the logistic model. It does not yet provide:

- threshold survival of those events;
- descent to one `physical16` trajectory;
- a map to ordered detector records;
- an instrument demonstrating one common calibration epoch.

Consequently the construction is a conditional source-trajectory event
selector and a relational rigidifier. It is not yet a selector on the
admissible `physical16` lens family.

## Smallest exact hostile

The same marked ordering with \(\kappa=1\) and \(\kappa=2\) gives respectively

\[
2+\sqrt3,
\qquad
\sqrt{2+\sqrt3}.
\]

This proves that the carrier type without beta-normalization provenance does
not determine the scale ratio. A second hostile assigns independent gains to
the three records; then neither adjacent physical ratio descends.

## Verdict

WP827 passes Aspect's germ structure only after retyping its target as a
marked ternary carrier with an unconsumed same-trajectory comparison port. It
passes the common-translation and common-gain fiber gates. It fails the
physical realization authority gate. The earlier `native_arity = 10` field is
withdrawn as a typing error.

WP829 adds a stricter descent result. Although the ternary carrier is well
typed abstractly, the acceleration-extremum labels are not constant on regular
coupling-coordinate fibers. The germ therefore remains a chart object until a
physically normalized running observable and matched instrument are supplied.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp828_aspect_germ_tester_audit.py
```
