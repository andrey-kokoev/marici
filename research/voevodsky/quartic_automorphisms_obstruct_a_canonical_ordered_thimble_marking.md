# Quartic automorphisms obstruct a canonical ordered thimble marking

## Question

Do automorphisms preserving the currently declared quartic data exchange the two total-energy nodes or the remote wall labels?

## Claim boundary

This proves an obstruction to a canonical ordered thimble marking from the unmarked quartic, base value, symmetric boundary germ, and Cut data. It does not prove that every invariant ambient parity class is impossible.

## Quartic

Let

\[
F(t;x,y,E)=x^2t^4-
\bigl(x^2+y^2-(E-x-y)^2\bigr)t^2+y^2.
\]

It has two exact involutions.

First,

\[
r:t\longmapsto-t
\]

fixes \((x,y,E)\) and satisfies

\[
F(-t;x,y,E)=F(t;x,y,E).
\]

At total energy,

\[
F(t;x,y,0)=(xt^2+y)^2,
\]

so the two nodes are

\[
t_\pm=\pm\sqrt{-y/x}.
\]

The involution \(r\) exchanges \(t_+\) and \(t_-\).

Second, projective reciprocity gives

\[
s:(x,y,t)\longmapsto(y,x,t^{-1})
\]

with

\[
t^4F(t^{-1};y,x,E)=F(t;x,y,E).
\]

It fixes the critical values \(0\) and \(2(x+y)\), while exchanging \(2x\) and \(2y\). The physical base expression \(E_{\rm phys}=x+y+z\) is invariant under exchanging \(x,y\).

The two commuting involutions generate a Klein four action on the unmarked quartic family.

## Obstruction

The Bunch–Davies boundary germ approaches the two total-energy nodes identically, and the known Cut pairing is zero on the elliptic coinvariant information. Hence neither supplies an \(r\)-odd label.

Suppose the currently declared invariant data canonically selected an ordered pair of distinct thimbles \((\mathcal T_+,\mathcal T_-)\) over the two nodes. Naturality under \(r\) would require the selected pair to be fixed, while geometric transport under \(r\) sends it to

\[
(\mathcal T_-,\mathcal T_+).
\]

A fixed ordered pair would imply \(\mathcal T_+=\mathcal T_-\), contradicting their distinct boundaries. Therefore no canonical ordering is defined by those invariant inputs.

Likewise, without preserving labelled \(x\) and \(y\) as asymmetric source data, reciprocity \(s\) prevents a canonical distinction between the two remote middle critical values and between identity versus swapped wall labels.

## Residual scope

Modulo two, invariant and anti-invariant combinations of the local pair coincide. Consequently this automorphism theorem explains the lost local ordering but does not determine whether an unordered global construction might select one invariant ambient parity class.

To obstruct every parity selection, one must compute the induced action of \(r\) and \(s\) on the ambient rank-nine Picard lattice and show that no candidate class is fixed. That action is not present in current source artifacts.

## Disposition

Existing quartic symmetries prove that local and unmarked global data cannot canonically order the paired thimbles; reciprocity also preserves the identity-versus-swap ambiguity unless site labels are retained as asymmetric physical input. The stronger parity-orbit obstruction remains contingent on the missing ambient Picard action.
