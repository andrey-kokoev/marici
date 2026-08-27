# Aspect's germ tester requires a primitive integral comparison span

## Target under test

The proposed target is not merely the integer seven.  It is the physical
Smith residue of a comparison between an independently quantized charge
lattice and the affine magnetic observation family.

Aspect's updated tester applies three gates:

1. constancy on complete fibers of every proposed quotient;
2. evaluation at the target's native arity;
3. independent source authority for realization and selection.

The charge/affine proposal fails all three unless its germ is enlarged.

## Fiber gate: primitive normalization cannot be forgotten

Let a quotient retain only the real observation capability of an integral
matrix and forget its primitive integral port unit.  The one-dimensional
presentations

\[
P_1=(1),\qquad P_7=(7)
\]

have the same real rank, kernel, and reconstruction capability.  They lie in
one fiber of that quotient.  Their Smith cokernels differ:

\[
\operatorname{coker}P_1=0,
\qquad
\operatorname{coker}P_7\cong\mathbb Z/7.
\]

Therefore the Smith target is not constant on the fiber.  A germ adequate for
real faithfulness is too coarse for integral index.  Primitive state and port
units must remain marked.

## Arity gate: two lattices do not determine their comparison

The target depends on a span, not on the separate objects:

\[
\Lambda_h\longrightarrow\Lambda_{\mathrm{common}}
\longleftarrow\Lambda_{\mathrm{obs}}.
\]

Even with the same abstract charge lattice \(\Lambda_h\cong\mathbb Z^2\) and
the same affine frame \(F\), distinct attachments of the observation lattice
to the common carrier can change the index.  For example, the primitive
attachment gives \(|\det F|=7\), whereas precomposing the observation
attachment with \(\operatorname{diag}(1,7)\) gives index \(49\).  The separate
lattice objects have not changed; their relative attachment has.

Thus the proposed target is at least a binary relational target, and in a
constructor presentation it is naturally ternary:

```text
charge lattice
observation lattice
primitive comparison/attachment cell
```

Auditing helicity and the affine frame independently cannot establish its
Smith index.

## Grade-locality gate

The affine matrix has a further marked input: its grade variance.  It records
the slope and intercept of the cross-grade family

\[
v_g=F(g,1)^T.
\]

The physical magnetic charge lives at grade three.  A valid comparison germ
must therefore declare either:

- `grade_scope = fixed(3)` and use a fixed-grade pairing; or
- an authorized grade-changing constructor.

Deleting this mark places cross-grade and fixed-grade presentations in one
fiber even though their index targets differ.  This is another fiber failure,
not merely missing interpretation.

## Authority gate

Particle helicity supplies an independently authorized integral charge
lattice.  The magnetic row calculation supplies the affine family.  Neither
source supplies:

- a common primitive integral carrier;
- a physical attachment between helicity charges and observation rows;
- a grade-changing charge operation;
- a selector identifying a physical generator with the affine residue.

Transporting both inputs into one written diagram does not authorize the
missing comparison cell.

## Smallest adequate germ

Aspect's theorem replaces the earlier `common_integral_carrier` placeholder by
the more precise object

```text
PrimitiveIntegralComparisonGerm
  charge_lattice
  charge_primitive_unit
  observation_lattice
  observation_primitive_unit
  grade_scope
  common_integral_carrier
  charge_attachment
  observation_attachment
  comparison_variance
  smith_target
  source_authority
```

The Smith index is a function of this complete marked germ.  It is not a
function of the two endpoint lattices or their realifications.

## Tester result

The new no-go survives Aspect's germ tester, but its diagnosis becomes
stronger:

- the normalization-forgetting proposal fails the fiber gate;
- the endpoint-only proposal fails the native-arity gate;
- the hand-inserted comparison span fails the authority gate.

The current source has not produced a failed index-seven comparison.  It has
not yet produced an object on which a physical Smith index is defined.

This also gives a clean reopening criterion: supply the complete marked germ
from source data.  Then the Smith calculation is deterministic and can return
seven, another index, or no torsion without further choices.
