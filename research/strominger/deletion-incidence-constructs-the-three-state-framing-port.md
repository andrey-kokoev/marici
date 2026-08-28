# Deletion Incidence Constructs the Three-State Framing Port

## Source incidence object

Forget the reflection response and retain only the typed deletion table of the
three cabling generators:

\[
\begin{array}{c|cccc}
&d_1&d_2&d_3&d_4\\
\hline
c_{31}&c_{21}&c_{21}&c_{21}&1\\
c_{13}&1&c_{12}&c_{12}&c_{12}\\
c_{22}&c_{12}&c_{12}&c_{21}&c_{21}.
\end{array}
\]

Its automorphisms may permute the three generators and four faces and may
exchange the two typed outputs \(c_{12}\) and \(c_{21}\). Exhaustive exact
enumeration gives precisely two automorphisms:

1. the identity;
2. endpoint reversal, which swaps \(c_{31}\leftrightarrow c_{13}\), reverses
   the face order, exchanges \(c_{12}\leftrightarrow c_{21}\), and fixes
   \(c_{22}\).

Therefore \(c_{22}\) is intrinsically the unique through-going generator: it
is the only row with no identity face. Its exceptional role is not a basis
label fitted from the response.

## Oriented refinement

When the through-going generator is repeated, the two remaining endpoint
generators carry signs \(\epsilon_0,\epsilon_1\). Their product

\[
\chi=\epsilon_0\epsilon_1
\]

is invariant under endpoint reversal. It is the relative orientation
character of the two endpoint deletion lines.

The source incidence object therefore constructs three states before any
response computation:

\[
\begin{array}{c|c}
A&\text{an endpoint generator is repeated},\\
B&\text{the through-going generator is repeated and }\chi=+1,\\
C&\text{the through-going generator is repeated and }\chi=-1.
\end{array}
\]

## Equivariant response factorization

The complete \(32\)-presentation census verifies

\[
A\mapsto(5,9,13;7,12),
\]

\[
B\mapsto(8,8,14;8,14),
\]

and

\[
C\mapsto(8,12,16;11,12).
\]

The classifier is invariant under both automorphisms of the source incidence
object. Hence it is a source-constructed equivariant port, not a compressed
lookup table.

## Boundary

This theorem proves covariance under the complete automorphism group of the
finite typed deletion table. It does not assert covariance under arbitrary
Nielsen transformations of the free group, which generally do not preserve
that source incidence object.

The three-state port is not the complete orbit quotient of signed
presentations. Endpoint reversal has sixteen orbits on the thirty-two legal
signed presentations, partitioned as eight, four, and four across (A,B,C).
Thus incidence and endpoint orientation define the three-state quotient, but
the response law is what proves that this quotient is sufficient and minimal
for this response. In particular, the sign of the repeated generator is an
endpoint-reversal invariant that the three-state port intentionally forgets.

## Replay

```powershell
python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
