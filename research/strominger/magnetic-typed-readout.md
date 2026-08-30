# Typed forgetting does not create the virtual interference

Let the transported route packet land in a graded direct sum

\[
T:\mathcal S\longrightarrow\bigoplus_\chi\mathcal O_\chi.
\]

Forgetting the grade labels leaves the same underlying direct-sum vector
space.  It is conservative for rank: an injective graded map remains
injective after ordinary forgetting.

The virtual interference appears only after a different operation,

\[
Q:\bigoplus_\chi\mathcal O_\chi\longrightarrow\mathcal O,
\]

which identifies distinct sectors by a codiagonal.  In the smallest model,

\[
T=\begin{pmatrix}1&0\\0&1\end{pmatrix},
\qquad
Q=\begin{pmatrix}1&1\end{pmatrix}.
\]

The underlying map `T` has rank two, while `QT` has the artificial kernel
`(-1,1)`.  Thus the problematic operation is not type forgetting but an
unauthorized cross-type quotient.

For reflected magnetic branches, the codiagonal readout is authorized exactly
when both routes have the same deck type.  On an `N`-fold cover this requires

\[
2Nq=0\pmod N,
\qquad\text{equivalently}\qquad 2q\in\mathbb Z.
\]

Every original integral component satisfies this condition.  Therefore the
ordinary scalar readout is legitimate on the classified magnetic lattice,
which explains why its determinant gives the correct integral theorem.  The
rational components `q=35/3,55/3` fail it, so applying the same scalar pairing
there is a new quotient rather than continuation of the original readout.

The correct rank invariant is blockwise:

\[
M=\bigoplus_\chi M_\chi,
\qquad
\operatorname{rank}M=\sum_\chi\operatorname{rank}M_\chi.
\]

Its determinantal data are the Fitting ideals or exterior-power sections of
the individual blocks.  Coordinates from different `chi` sectors are never
added before rank is evaluated.

This gives the conservativity theorem Deutsch requested:

\[
\boxed{
\text{On the integral magnetic source lattice, the scalar readout pairing is
type-authorized; outside it, rank must be computed in the graded direct sum.}
}
\]

The minimal sufficient type for this question is the reflection distance
modulo the cover pairing condition, equivalently the deck-charge difference
`2Nq mod N`, together with the tensor component type.  The full exponent pair
is needed for support and boundary questions, but not merely to decide whether
the two route outputs may be summed.

## Equivariant descent is not a codiagonal

For a cyclic cover, legal descent to an ordinary base scalar takes the
invariant sector.  In representation notation,

\[
\operatorname{Hom}_{\mathbb Z_N}(V_\chi,V_0)=0
\qquad(\chi\ne0).
\]

The candidate cubic charges are `(2,1,1)`, so none has an ordinary descended
scalar readout.  The incorrect scalar continuation did more than identify two
routes: it supplied non-equivariant maps from both nontrivial representations
to the trivial representation and then added their values.

A homogeneous morphism of charge `c` can map `V_chi` to `V_psi` only when

\[
\psi=\chi+c\pmod N.
\]

Thus a charge-1 cubic source needs a charge-2 readout adapter to land in the
trivial sector, while a charge-2 source needs a charge-1 adapter.  Since the
two branches require different adapters, a uniform twist cannot repair their
relative mismatch.

The lawful alternatives are therefore explicit:

- retain a twisted, nontrivial target local system instead of a scalar;
- provide sector-specific charged adapters;
- insert a branch-supported defect carrying the missing charge;
- break deck equivariance.

Each alternative changes the observable interface.  None is ordinary pullback
and descent of the original magnetic readout.

## Charge compatibility does not fix coherence

Suppose sector-specific charged adapters are introduced:

\[
J_1:V_1\to V_0,
\qquad
J_2:V_2\to V_0.
\]

Their equivariant Hom spaces are independently one-dimensional.  Hence the
most general authorized readout has the form

\[
O=\alpha J_1(A)+\beta J_2(B).
\]

Deck charge determines which maps may exist, but it does not determine the
relative normalization `beta/alpha`.  For an anti-diagonal packet `(A,-A)`,

\[
O=(\alpha-\beta)A.
\]

Cancellation at unit weights is destroyed by the equally admissible rescaling
`(alpha,beta)=(1,2)`.  Therefore a twisted interference zero is not invariant
until some further source datum fixes the relative phase and normalization of
the two charged adapters.

Such a datum could be a normalized defect junction, a fusion law, a Hermitian
pairing, or another source-derived sewing constraint.  Without it, one can
tune a cancellation into or out of existence, so it is not an explanation or
a prediction.

The activation hierarchy gains a fourth independent gate:

\[
\boxed{
\text{state representation}
+\text{charge compatibility}
+\text{tail construction}
+\text{coherence normalization}.
}
\]

## Reflection turns the two charges into a doublet

Reflection sends `chi` to `-chi`.  On the cubic cover it exchanges the
charge-1 and charge-2 sectors, while deck rotation acts within them.  Together
these symmetries generate `D_3`, and the two conjugate charge lines form its
real two-dimensional standard representation.

That doublet has no invariant linear functional:

\[
\operatorname{Hom}_{D_3}(V_{\mathrm{std}},\mathbf1)=0.
\]

Its first invariant readout is quadratic.  In an orthonormal real frame,

\[
Q(x,y)=x^2+y^2.
\]

For the packet previously made dark by a codiagonal,

\[
Q(A,-A)=2A^2\ne0
\]

when `A` is nonzero.  Thus the anti-diagonal packet is not dark to the natural
dihedral invariant; it is only dark to the unauthorized linear projection
`(x,y) mapsto x+y`.

Reflection can relate the normalizations of conjugate sectors, but it does not
create a linear scalar observable.  To obtain one still requires a charged
spurion or defect selecting a direction in the doublet.  Such a choice breaks
the dihedral symmetry and makes the cancellation dependent on that selected
direction.

## Positive invariant completion

The quadratic statement extends to every finite deck group.  Given any
positive Hermitian form `h_0` on a finite-dimensional representation `V`, the
group average

\[
h(v,w)=\frac1{|G|}\sum_{g\in G}h_0(gv,gw)
\]

is `G`-invariant and positive definite.  Consequently

\[
h(v,v)=0\quad\Longleftrightarrow\quad v=0.
\]

A nonzero route packet may therefore be dark to one selected linear
projection, but it cannot be dark to the complete symmetry-preserving positive
readout.  For a complex anti-diagonal packet,

\[
\|(A,-A)\|^2=2|A|^2.
\]

The star/real structure is essential.  The holomorphic polynomial `x^2+y^2`
has the nonzero isotropic vector `(1,i)`; it is not a positive detector over
the complexified algebraic space.  Positivity enters only after reflection or
Hermitian conjugation selects the physical real form.

This gives a final mechanism discriminator:

\[
\begin{array}{c|c|c}
\text{packet}&\text{linear codiagonal}&\text{invariant Hermitian energy}\\
\hline
(0,0)&0&0\\
(A,-A),\ A\ne0&0&2|A|^2
\end{array}
\]

Only a zero packet is invisible to every lawful invariant detector at that
same packet level.  A coherence residue is relative to a linear interface; it
remains present as positive information in the complete typed packet.  This
does not say that the full magnetic exceptional classes have zero sheet
packets: in fact they satisfy `A=B!=0`.  Their local residual carrier loss and
their final equal-sheet magnetic cancellation are distinct stages, as recorded
in `magnetic-two-level-interference.md`.
