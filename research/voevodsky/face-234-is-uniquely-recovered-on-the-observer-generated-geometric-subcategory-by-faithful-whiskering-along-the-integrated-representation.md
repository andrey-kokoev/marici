# Face 234 is uniquely recovered on the observer-generated geometric subcategory by faithful whiskering along the integrated representation

## Tetrahedral pasting equation

For the four realization functors, orient the face modifications as

\[
H_{123}:
\eta_{23}\eta_{12}
\Rrightarrow
\eta_{13},
\]

\[
H_{124}:
\eta_{24}\eta_{12}
\Rrightarrow
\eta_{14},
\]

\[
H_{134}:
\eta_{34}\eta_{13}
\Rrightarrow
\eta_{14},
\]

\[
H_{234}:
\eta_{34}\eta_{23}
\Rrightarrow
\eta_{24}.
\]

The tetrahedral equation is

\[
\boxed{
H_{124}
\circ
(H_{234}*\eta_{12})
=
H_{134}
\circ
(\eta_{34}*H_{123}).
}
\]

Here `*` denotes whiskering and `circ` vertical composition, with convention adjusted if the ambient bicategory uses the opposite order.

Thus the whiskering map that must be inverted to recover face `234` is

\[
\boxed{
R_{12}:
H
\longmapsto
H*\eta_{12}.
}
\]

The other whiskering operation is

\[
L_{34}:
H
\longmapsto
\eta_{34}*H.
\]

## Observer-generated geometric category

Let

\[
\mathsf{Obs}_S
\]

be the admitted convolution-observer category and let

\[
\eta_{12}=U_S:
\mathsf{Obs}_S
\longrightarrow
\mathsf{Geom}_S
\]

be the integrated semilocal representation

\[
U_S(h)
=
\int_{C_S}
h(u)U_S(u)d^*u.
\]

Define the observer-generated subcategory

\[
\boxed{
\mathsf{Geom}_S^{obs}
=
\operatorname{EssIm}(U_S)
\subseteq
\mathsf{Geom}_S.
}
\]

Corestricting the codomain gives

\[
U_S^{obs}:
\mathsf{Obs}_S
\to
\mathsf{Geom}_S^{obs}.
\]

It is essentially surjective by definition.

## Faithfulness of the integrated regular representation

On the regular scaling representation, the integrated convolution representation is faithful on the admitted test algebra. After Fourier transform on the abelian group `C_S`,

\[
U_S(h)
\longleftrightarrow
M_{\widehat h}.
\]

Therefore

\[
U_S(h)=0
\Longrightarrow
\widehat h=0
\Longrightarrow
h=0.
\]

The same argument applies to polarized morphisms, provided the observer category retains the full operator-valued representation rather than only its scalar trace.

Hence `U_S^obs` is faithful. With morphisms in `Geom_S^obs` defined as represented observer intertwiners, it is full by construction. Consequently

\[
\boxed{
U_S^{obs}:
\mathsf{Obs}_S
\simeq
\mathsf{Geom}_S^{obs}
}
\]

is an equivalence of the observer presentation with its geometric essential image.

This is a corestriction statement. It does not assert that every semilocal geometric operator comes from one observer.

## Whiskering is invertible on the essential image

Precomposition with an equivalence induces an equivalence between functor categories and therefore a bijection on modification spaces up to the ambient higher equivalence.

Thus

\[
\boxed{
R_{12}^{obs}:
H
\longmapsto
H*U_S^{obs}
}
\]

has a unique inverse on the observer-generated subcategory.

The nonabelian horn criterion is therefore satisfied there:

- existence: the required target lies in the image of `R_12^obs`;
- uniqueness: each fiber of `R_12^obs` is contractible/singleton at the truncated level.

## Recovered face 234

Solving the pasting equation yields

\[
\boxed{
H_{234}^{obs}
=
(R_{12}^{obs})^{-1}
\left[
H_{124}^{-1}
\circ
H_{134}
\circ
(\eta_{34}*H_{123})
\right],
}
\]

with inverses/order changed according to the chosen vertical-composition convention.

Objectwise, for a represented observer `U_S(h)`, this says:

1. recover its unique observer label `h` by faithfulness;
2. apply the source--spectral face `H_123`;
3. apply the spectral--trace comparison `eta_34` and face `H_134`;
4. compare with the geometric cutoff route through `H_124`;
5. descend the resulting modification back to `Geom_S^obs`.

No arbitrary new value of `H_234` is chosen.

## What this proves

For every observer-generated cell, face `234` is formally and uniquely determined once the other three faces and `eta_34` are fixed.

In particular, the seventh edgewise subdivision does not require 343 independent choices of `H_234`. All translated copies are generated functorially from the single recovered modification.

Thus, at the algebraic observer-generated level,

\[
\boxed{
343/343
\text{ face-234 horn values are uniquely forced.}
}
\]

## What this does not prove

### Extension beyond the essential image

The functor

\[
U_S:
\mathsf{Obs}_S
\to
\mathsf{Geom}_S
\]

is not asserted to be essentially surjective onto all cutoff, prolate, or affiliated geometric operators. Hence whiskering need not be invertible on the full geometric category.

### Analytic admissibility

The recovered formula uses `H_124^{-1}` and the spectral comparison. One must still verify:

- domains of affiliated operators;
- continuity in the cutoff parameter;
- compatibility with finite-part limits;
- preservation of adjoints and Hermitian polarization;
- extension to the relevant trace ideals.

### Positivity

Faithful whiskering proves uniqueness of the coherent face, not positivity of its value. The recovered `H_234^obs` may be a signed relative-trace modification.

## Important scalarization warning

If `eta_12` is replaced by its scalar trace readout, faithfulness is lost. Distinct geometric operators can have the same trace. Then `R_12` can have non-singleton fibers and horn recovery becomes ambiguous.

Therefore face `234` must be recovered before applying the scalar finite-part trace.

## Revised status count

There are three distinct counts:

\[
\boxed{
343/343
\text{ formal horn fillers in the universal invertible-whiskering model},
}
\]

\[
\boxed{
343/343
\text{ uniquely forced observer-generated }H_{234}
\text{ values},
}
\]

and

\[
\boxed{
0/343
\text{ currently certified positive analytic tetrahedral fillers}.
}
\]

The second count is now tied to the actual semilocal integrated representation rather than only to the finite `S_3` toy model.

## Next gate

The next nonformal step is to prove that the recovered modification is bounded/admissible in one explicit cutoff row. Because all rows are functorial translates, a uniform estimate there can propagate to all 343 elementary tetrahedra.
