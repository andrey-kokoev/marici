# The backward Hankel witness is a rigged transpose, not an executable reverse incidence

## Retyping the no-path obstruction

The executable constructor graph has no authorized path from the forward tail
state back into the forcing state. That result remains correct. The `3+2+1`
architecture shows that such a path is not what the backward witness requires.

Forward and backward compositionality have opposite variance. The backward
witness should live in the rigged dual category rather than masquerade as
writable feedback in the forward category.

## Exact mate of the history operator

Let the source Hankel history map be

\[
(\mathsf H_f\varphi)(q)
=\int_0^\infty f(q+a)\varphi(a)\,da,
\]

and let `E_0` be endpoint evaluation at `q=0`. The topological transpose gives

\[
\mathsf H_f^\times E_0
\in F^\times.
\]

For every test vector `varphi`,

\[
(\mathsf H_f^\times E_0)(\varphi)
=E_0(\mathsf H_f\varphi)
=\int_0^\infty f(a)\varphi(a)\,da.
\]

Thus the backward endpoint witness is exactly the source covector. No Riesz
identification, chosen Hilbert metric, or executable arrow from tail to forcing
is required.

On the character `e_z(a)=exp(za)`,

\[
(\mathsf H_f^\times E_0)(e_z)
=E_0\mathsf H_fe_z
=F(z).
\]

The forward Evans construction and backward source functional are therefore
strict mates.

## Meaning of a zero

At a transform zero,

\[
e_z\in\ker(\mathsf H_f^\times E_0).
\]

The source covector itself does not vanish. Nor does a state travel backward
through an executable feedback edge. Scalar nullity is orthogonality of the
distinguished character to the pulled-back source covector.

This resolves an ambiguity in the earlier reverse-incidence programme:

```text
forbidden demand:
  executable tail state -> forcing state

canonical backward witness:
  endpoint covector -> source covector
  through the rigged transpose
```

## What remains missing

The backward witness is now constructed at the continuum source level, and
its mate relation with the forward history map is taut-free: both descend from
the integral kernel before zeros are inspected.

It still has no RH force by itself. Positive even sources can have off-seam
characters in the kernel of their source covector. The missing final `+1`
cell must compare this pulled-back covector with the complete typed arithmetic
Ward defect:

```text
source covector on the character orbit
<-> primitive, square, connected, seam, and archimedean defect packet
```

That comparison must be natural in cutoff and completion. It cannot be formed
by applying a Riesz map and calling the result feedback, because that would
reintroduce metric dependence and the previously exposed autocorrelation
substitution.

## Scope correction

The no-executable-path theorem remains a valid prohibition against forward
feedback. It is no longer a blocker for construction of the contravariant
backward witness. Under `3+2+1`, the open RH layer is the final mate between
the source covector and arithmetic defect tower, not existence of a reverse
state-transition arrow.

## Durable verification

- Checker: `checkers/check_hankel_endpoint_transpose_mate.py`
- The checker verifies in an arbitrary finite Hankel truncation that endpoint
  evaluation after forward history equals evaluation by the transposed
  endpoint covector.
