# Exceptional Restriction Leaves a Three-Class Mixed-Normal Obstruction

## Result

Restricting the corrected D03 carrier to its literal exceptional open-star
does not make the dualizing complex perfect.  It performs a large and useful
compression: the nine global one-normal obstruction families reduce to
three rank-one **mixed-normal** classes.  But those three classes still carry
derived localization duals and prevent a bounded finite-projective
compression.

Thus bare exceptional support is not yet the category in which the
Entry-176 cap can equal the exceptional dualizing object.  Entry 176 would
have to supply a relative boundary differential or a quotient that kills a
specific three-class packet.

## Literal exceptional sector

Let \(E\) be the new exceptional ray in the blown-up face poset.  The
literal exceptional open-star in the corrected carrier is

\[
\widetilde G_E
=\{(\sigma,H):E\in\sigma_0\}.
\]

Because the faces in \(\sigma\) form an increasing chain, this is equivalent
to requiring every face of \(\sigma\) to contain \(E\).  The exact census is

\[
|\widetilde G_E|=172.
\]

Its blowdown has only three target faces:

\[
\{D_{03},x_1\},\qquad
\{D_{03},x_1,x_4\},\qquad
\{D_{03},x_1,x_3\}.
\]

Accordingly only four of the nine normal labels occur:

\[
D_{03}=(0,3),\quad x_1=(1,3),\quad
x_4=(0,4),\quad x_3=(3,5).
\]

Each target face has three degree-zero exceptional lifts, corresponding to
the three blowup-chart faces with the same blowdown.  Every such lift has
singleton source open, so any one of the three defines a representable
projective witness.

## All one-normal sectors cancel

It is not enough to note that \(D_{03}\) and \(x_1\) occur in every image
face.  A normal-state mark \(H\) can withhold either variable from inversion
and can later be deleted, so all four labels can still produce localization
jumps.

For each of the four labels, filter the target bar dual by terminal states
that have not inverted that label.  The exact chain signatures are:

| label | chain ranks | boundary ranks mod 101 | homology |
| --- | --- | --- | --- |
| \(D_{03}\) | \((6,72,144,78)\) | \((0,6,66,78)\) | \(0\) |
| \(x_1\) | \((6,66,126,66)\) | \((0,6,60,66)\) | \(0\) |
| \(x_4\) | \((18,114,186,90)\) | \((0,18,96,90)\) | \(0\) |
| \(x_3\) | \((18,114,186,90)\) | \((0,18,96,90)\) | \(0\) |

Every one-normal completion quotient therefore cancels on exceptional
restriction.  This positive test is why exceptional support is much closer
to Entry 176 than the full carrier.

## The mixed-normal falsifier

The exceptional source-chain census by degree and localization-jump size is

\[
\begin{array}{c|rrrr}
p&0&1&2&3\\ \hline
0&172&0&0&0\\
1&248&596&281&44\\
2&96&848&1226&424\\
3&0&288&1212&864\\
4&0&0&288&480.
\end{array}
\]

Hence one-variable cancellation cannot decide perfectness.  The checker
filters by every nonempty subset of each of the three target faces.  All
proper subsets are acyclic.  Exactly the three full-face subsets survive:

1. On \(\{D_{03},x_1\}\), the full pair has chain ranks
   \((4,41,78,42)\), boundary ranks \((0,4,36,42)\), and homology
   \((0,1,0,0)\).
2. On \(\{D_{03},x_1,x_4\}\), the full triple has chain ranks
   \((8,37,60,30)\), boundary ranks \((0,7,30,30)\), and homology
   \((1,0,0,0)\).
3. On \(\{D_{03},x_1,x_3\}\), the full triple has the same ranks and
   homology \((1,0,0,0)\).

The corresponding coefficients are the multi-localization duals

\[
R\operatorname{Hom}_A
\bigl(A[(\prod_{u\in U}u)^{-1}],A\bigr),
\]

which retain non-finitely-generated completion cohomology.  The three free
rank-one incidence classes therefore give nonperfect stalk witnesses just
as in Entry 367.  In particular,

\[
\boxed{\omega_{q|\widetilde G_E}\text{ is still nonperfect}.}
\]

## Meaning for Entry 176

Entry 176 is not disproved as a relative exceptional correction.  The new
census specifies what such a correction must do.  It must act on the packet

\[
\mathsf T_E=
\mathsf T_{D_{03},x_1}[1]
\oplus
\mathsf T_{D_{03},x_1,x_4}
\oplus
\mathsf T_{D_{03},x_1,x_3},
\]

with the displayed incidence shifts, and kill it by a relative-boundary
cone or by passage to a quotient.  Merely restricting support to the
exceptional open-star, or checking each normal separately, is insufficient.

The next sharp test is therefore to type the Entry-176 relative cap as a map
into this three-class obstruction packet and compute its cone.  If the cone
is perfect, the cap is the missing exceptional correction.  If the map has
rank below three or the shifts do not match, Entry 176 cannot repair the
actual D03 extraordinary pullback.

## Evidence boundary

`research/voevodsky/check_d03_ringed_carrier_typing.rs` verifies the
172-point exceptional restriction, its three image faces, all four
one-normal acyclicity calculations, the complete exceptional jump census,
all multivariable filtered sectors, and the three surviving homology
classes.  No cap-to-packet morphism is constructed in this entry.
