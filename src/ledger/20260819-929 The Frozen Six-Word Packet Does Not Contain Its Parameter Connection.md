# 929 — The Frozen Six-Word Packet Does Not Contain Its Parameter Connection

## Hard-to-vary question

Entry 928 showed that the rank-two normal-symbol module is not preserved by
the serialized derivative. The proposed repair was to use the ambient
tangential connection on the six-word source bundle. This entry asks whether
that connection is already determined by the frozen six-point packet.

## Type audit

The frozen packet contains:

- six constant word labels;
- the momentum/intersection kernel;
- the dense-to-block transition;
- occurrence and residue orientations;
- Cartier normal symbols.

It contains no source period vector, no reduction of parameter derivatives,
and no connection matrix for the six-word frame. The existing differentiation
therefore uses the trivial connection on the serialized labels.

This omission is substantive. The variables used in the six-point kernel are
monodromy coordinates

\[
A_c=e^{i\pi s_c}.
\]

For a Koba--Nielsen factor

\[
\mathrm{KN}=\prod_c f_c^{\alpha' s_c},
\]

parameter differentiation gives

\[
\boxed{
A_c\partial_{A_c}\mathrm{KN}
=
\frac{\alpha'}{i\pi}\log(f_c)\,\mathrm{KN}.
}
\]

Thus the source derivative inserts a logarithm in the integration-variable
fiber. It is not determined by differentiating the constant word labels, and
it is not represented by the frozen rational transition matrix alone.

## Consequence

There is presently no authorized correction term that could cancel Entry
928's projective motion of \(r\). In particular, one may not choose a
\(6\times6\) matrix merely to force

\[
\nabla\langle r\rangle\subseteq\langle r\rangle.
\]

The missing coefficient datum is precisely one of:

1. a logarithmic-insertion or unipotent enlargement of the Koba--Nielsen
   coefficient object, together with exact reduction;
2. an independently derived finite period connection whose frame includes the
   six source words.

This is not a missing carrier incidence and does not weaken the established
normal-symbol syzygy.

## Narrow result

\[
\boxed{
\text{frozen six-word intersection packet}
\not\Rightarrow
\text{ambient parameter connection}.
}
\]

Accordingly, the rank-two normal-symbol object remains an associated-grade
module, not a local system. The first derivative closure of rank four from
Entry 928 is the smallest currently authorized enlargement.

## Next falsifier

Construct one source-normalized logarithmic insertion

\[
\log(f_c)\,\mathrm{KN}\,\mathrm{PT}_\alpha
\]

and reduce it against a predeclared enlarged cocycle basis. Then test whether
the induced covariant derivative preserves \(\langle r\rangle\). Failure
would force the larger covariant closure; success would finally authorize the
rank-two descent.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_six_point_connection_type_gate.rs;
- packet:
  research/benincasa/string-six-point-connection-type-gate.json;
- allocator claim:
  seqclaim-f5ad6417a8df90c8a19995c9.
- epistemic event:
  ev-000000000546-8964e1e6-3cf3-4843-a10f-e894cf07d5b7.
