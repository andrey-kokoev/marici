# The `D(S_3)` center expectation is a measure--prepare quotient

Owner: `marici.Kitaev`

## Bounded question

Can the central readout identified in the preceding packet be realized as a
canonical quantum channel, and how does it differ from superselection
dephasing?

## Three maps

On `H=direct_sum_a V_a`, with simple-sector projectors `P_a` and dimensions
`d_a`, distinguish:

1. block dephasing,
   `D(X)=sum_a P_a X P_a`;
2. the trace-preserving conditional expectation onto the center,

   \[
   \mathbb E_Z(X)=\sum_a\frac{\operatorname{Tr}(P_aX)}{d_a}P_a;
   \]
3. the classical sector record,
   `R(X)_a=Tr(P_a X)`.

The first retains every internal block operator.  The second retains only one
scalar per block.  The third records those same scalars as an eight-component
classical vector.

## Exact channel theorem

`E_Z` is unital, trace preserving, idempotent, and Hilbert--Schmidt
self-adjoint.  It is completely positive through the 36 Kraus operators

\[
K_{aij}=\frac{|a,i\rangle\langle a,j|}{\sqrt{d_a}}.
\]

It factors as

\[
X\xmapsto{R}(\operatorname{Tr}(P_aX))_a
\xmapsto{J}\bigoplus_a\frac{\operatorname{Tr}(P_aX)}{d_a}I_{V_a},
\]

where `J` prepares the maximally mixed state in the recorded block.  Thus it
is a measure--prepare, entanglement-breaking channel.  Its image dimension is
8 and kernel dimension 248.  Block dephasing instead has image dimension 36
and kernel dimension 220.

## Deliberate failure

The claim `D=E_Z` fails.  For
`T_C=diag(1,-1)` inside the two-dimensional `C` block,

\[
D(T_C)=T_C,\qquad \mathbb E_Z(T_C)=0.
\]

The noncentral pairing lost by `E_Z` has exact residual
`Tr(T_C^2)-Tr(T_C E_Z(T_C))=2`.  Therefore superselection dephasing alone
does not justify replacing a block state by its sector weight.

## Cross-sector relation

This is the non-Abelian coefficient realization of Nima's accessible-readout
algebra gate.  The Carrier-level pattern is the factorization

\[
\text{source state}\to\text{accessible operator system}
\to\text{record algebra}.
\]

The block dimensions, projectors, and interpretation of their labels require
the `D(S_3)` quantum coefficient lens.  The conditional-expectation
construction itself applies to any finite direct sum of matrix blocks once a
trace and block decomposition are frozen.

## Assumptions, falsifiers, and unresolved typing

Assumptions: the direct-sum representation and ordinary matrix trace are the
admitted finite model; no preferred internal state other than the normalized
trace is supplied.  Falsifiers include failure of the Kraus completeness
relation, disagreement of the Kraus and closed formulas on any matrix unit,
failure of idempotence, or equality of `D` and `E_Z` on the explicit witness.

What remains untyped is whether the physical source dynamics implements
`E_Z`, merely `D`, or neither.  The channel is canonical relative to the
frozen trace and block decomposition; algebraic canonicity is not apparatus
availability.

## Verification and activation

Run:

```text
uv run --with sympy python -u research/kitaev/checkers/check_s3_center_conditional_expectation.py
```

Ten aggregate gates pass.  Post-objective excitement 10/10, confidence
10/10, realized information gain 10/10.  One apparent branch was eliminated:
block dephasing is not the central readout quotient.  One constructive branch
was opened: the center quotient has an exact 36-Kraus measure--prepare
realization.  Apparatus derivation remains open.
