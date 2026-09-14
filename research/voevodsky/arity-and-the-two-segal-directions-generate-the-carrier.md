# Free linearization of the endpoint-direction orbit produces a carrier

## Question

Can the rank-three real carrier and its two coherence planes be constructed from the two-directional 2-Segal model?

## Arity line

The simplex degree supplies the arity monoid \(\mathbb N\). Group completion and realification give

\[
A=
\mathbb R\otimes_{\mathbb Z}\mathbb N^{\mathrm{gp}}
\cong\mathbb R.
\]

This is the shared arity line.

## Direction space

After choosing the usual orientation of the simplex category, the two endpoint path-space constructions form a labelled pair. Reversal removes any intrinsic preference for either endpoint. The invariant datum is therefore, at most, the unordered reversal orbit

\[
D=\{\triangleleft,\triangleright\}.
\]

This orbit is genuinely two-element only if the model retains the two endpoint constructions as distinct structured objects. Take its free real vector space

\[
V=\mathbb R[D].
\]

It has canonical basis vectors \(\nu_{\triangleleft}\) and \(\nu_{\triangleright}\). Simplex reversal exchanges them.

## Carrier and planes

Define

\[
E=A\oplus V.
\]

Then \(E\) has rank three. Define the two plane tangents by

\[
T_{\triangleleft}=A\oplus\mathbb R\nu_{\triangleleft},
\qquad
T_{\triangleright}=A\oplus\mathbb R\nu_{\triangleright}.
\]

Since the two free basis lines are independent,

\[
T_{\triangleleft}\cap T_{\triangleright}=A.
\]

Thus the shared rank-one incidence and the two transverse planes are generated directly by arity plus the two path-space directions.

## Reversal

Extend simplex reversal linearly. It fixes \(A\), exchanges the two basis vectors of \(V\), exchanges the planes, and squares to the identity.

Once the free-linearization functor is chosen, the free vector space on \(D\) carries a canonical permutation-invariant Euclidean metric for which its basis is orthonormal. Consequently this particular realization makes the transverse directions meet at \(90\) degrees. The angle is canonical relative to free Euclidean linearization, not relative to the 2-Segal axioms alone.

## Disposition

For the endpoint-marked model, free linearization gives a consistent geometric enrichment:

- arity generates the common line;
- the unordered endpoint orbit generates the normal plane;
- their direct sum generates the rank-three carrier;
- reversal generates the plane exchange.

This does **not** derive two planes from the 2-Segal axioms. It assumes that the endpoint constructions remain a noncollapsed two-element orbit and chooses free Euclidean linearization. If the endpoint objects are identified, or if no endpoint marking is retained, the proposed normal plane is not source-derived.

## Verification

```text
python research/voevodsky/checkers/check_carrier_from_arity_and_path_directions.py
```

The checker verifies all ranks, exact plane intersection, and the involutive reversal action.

Artifacts:

- `research/voevodsky/checkers/check_carrier_from_arity_and_path_directions.py`
- `research/voevodsky/results/carrier_from_arity_and_path_directions.json`
