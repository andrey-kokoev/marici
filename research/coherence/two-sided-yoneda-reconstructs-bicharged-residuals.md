# Two-sided Yoneda reconstruction of bicharged residuals

## Behavioral matrix

For typed residual primitives \(X_i\), retain incoming and outgoing charges. Their complete contextual pairing table is

\[
B_{ij}=q_{\rm out}(X_i)q_{\rm in}(X_j).
\]

This combines the two profiles

\[
Y_{\rm out}(X)=\operatorname{Hom}(X,-),
\qquad
Y_{\rm in}(X)=\operatorname{Hom}(-,X)
\]

through composition.

## Reconstruction theorem

If the behavior is nonzero and rank one, the matrix \(B\) determines both charge families up to the unavoidable line gauge

\[
q_{\rm out}\mapsto\lambda q_{\rm out},
\qquad
q_{\rm in}\mapsto\lambda^{-1}q_{\rm in}.
\]

Choose any nonzero pivot \(B_{i_0j_0}\) and the gauge \(q_{\rm out}(X_{i_0})=1\). Then

\[
q_{\rm in}(X_j)=B_{i_0j},
\]

and

\[
q_{\rm out}(X_i)=\frac{B_{ij_0}}{B_{i_0j_0}}.
\]

Every entry is reconstructed exactly.

Thus the two-sided behavior determines the bicharged residual object modulo change of basis in its one-dimensional state line.

## Representability criterion

A proposed contextual behavior belongs to this primitive type precisely when

\[
\operatorname{rank}B\le1
\]

and its orientation and zero-sector typing are retained. A rank-two behavior cannot be represented by one bicharged residual line; it requires a higher-dimensional residual state.

This gives a concrete validity test:

```text
valid one-line residual
iff
all contextual pairings factor through one incoming/outgoing state line
```

## Relation to Isbell duality

Incoming and outgoing profiles are contravariant and covariant views of the same residual. Their composition pairing identifies compatible pairs of profiles. In a larger category, the corresponding fixed objects belong naturally to an Isbell envelope.

At the finite scalar level constructed here, this reduces to rank-one factorization modulo gauge. Calling it “Yoneda squared” is useful intuition, but the precise operation is two-sided representability.

## Caveat

If every pairing vanishes, behavior alone cannot distinguish a zero incoming charge from a zero outgoing charge. The typed zero sector must therefore be supplied separately. This is the smallest failure of unqualified behavioral reconstruction.

## Verification

The checker reconstructs 180 nonzero rational behavior systems up to gauge and rejects a rank-two hostile matrix:

```text
python research/coherence/check_two_sided_yoneda_reconstruction.py
```

Artifacts:

- `check_two_sided_yoneda_reconstruction.py`
- `two-sided-yoneda-reconstruction.v1.json`
