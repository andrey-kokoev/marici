# The shared orientation line supplies the C2 channel torsor

## Question

Can the \(C_2\) channel data be obtained from the shared incidence of the two coherence planes?

## Orientation torsor

Assume the shared incidence has a real rank-one determinant line \(L\). Its orientation type is

\[
\operatorname{Or}(L)
=
(L\setminus\{0\})/\mathbb R_{>0}.
\]

It has two elements. Multiplication by a negative scalar exchanges them, while multiplication by a positive scalar preserves them.

Thus \(\operatorname{Or}(L)\) is a torsor for

\[
\mathbb R^\times/\mathbb R_{>0}
\cong C_2.
\]

The \(C_2\) action is free and transitive. It supplies sign exchange without selecting either sign as preferred.

## Incidence of the two planes

Choose orientations on the forward and backward planes so that their induced orientations on the common line are opposite. The common incidence then occurs once with each element of \(\operatorname{Or}(L)\).

Their signed internal-boundary contributions cancel, but the underlying shared line remains present.

## Dependency chain

Within the right-angle geometric model:

1. the shared axis supplies a real rank-one line;
2. its orientation torsor supplies the \(C_2\) channel action;
3. the nontrivial real character supplies parity;
4. incidence reversal exchanges the two torsor elements;
5. averaging over the generated \(D_4\) action supplies the metric up to scale.

No independent choice of a labelled \(C_2\) set is then required.

## Residual

The construction does not produce a canonical orientation. Reversal has no fixed point on the orientation torsor, so any chosen sign is additional section data.

For the general coherence pyramid, the first missing source object is a real rank-one determinant line attached to the shared incidence. Without that line, the orientation torsor and its \(C_2\) action cannot be formed.

## Verification

```text
python research/voevodsky/checkers/check_shared_axis_orientation_torsor.py
```

The checker verifies the free transitive action, involutive fixed-point-free reversal, opposite induced plane orientations, and internal-boundary cancellation.

Artifacts:

- `research/voevodsky/checkers/check_shared_axis_orientation_torsor.py`
- `research/voevodsky/results/shared_axis_orientation_torsor.json`
