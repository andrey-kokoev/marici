# The Prime-Two Additive Incidence Does Not Descend to the Valuation Seam

## The finite local analogue

At a finite place, additive differentiation has no literal infinitesimal
counterpart. Its source-native replacement is an additive difference. For
\(h\in\mathbb Q_p\), let

\[
(\tau_hf)(x)=f(x+h),
\qquad
\Delta_h=\tau_h-I.
\]

With the self-dual additive Fourier transform,

\[
\mathcal F_p\tau_h
=
M_{\chi_h}\mathcal F_p,
\]

where \(\chi_h(\xi)=\chi_p(h\xi)\). Consequently,

\[
\mathcal F_p\Delta_h
=
(M_{\chi_h}-I)\mathcal F_p.
\]

This is the exact finite-place derivative--coordinate square. It is defined
on the additive local source before any valuation or Euler compression.

## Prime-two descent test

Let

\[
v_2:\mathbb Q_2^\times\longrightarrow\mathbb Z
\]

be the valuation quotient and choose the first inverse-integral displacement
\(h=\tfrac12\). The two points

\[
x=\frac12,
\qquad
y=\frac32
\]

have the same valuation:

\[
v_2(x)=v_2(y)=-1.
\]

After the authorized additive translation,

\[
x+h=1,
\qquad
y+h=2,
\]

and hence

\[
v_2(x+h)=0,
\qquad
v_2(y+h)=1.
\]

Therefore translation by \(h\), and thus the induced difference
\(\Delta_h\), does not descend through the valuation quotient. There is no
map \(T_h\) on valuation labels satisfying

\[
v_2(x+h)=T_h(v_2(x))
\]

for all admissible \(x\), even before passing from point transport to
operators on functions. In particular, no valuation-only
\(P_{\mathrm{fin}}\) can implement this additive difference.

## Consequence for the Green forcing defect

The archimedean operator

\[
P=e^{-q}\left(\partial_q-\frac12\right)
\]

generates the horizontal Green coefficient through an even--odd additive
incidence. Its finite local mate lives on the full additive residue chart.
The Euler primitive loop and its powers live on the coarser valuation chart.

The two constructions therefore cannot be joined by declaring a
valuation-only \(P_{\mathrm{fin}}\). Such a declaration would erase residue
data on which additive translation acts nontrivially. The forcing defect in
the doubled Green identity cannot be cancelled directly by primitive and
prime-square valuation currents through the proposed square.

## Categorical interpretation

This is a descent obstruction, not a failure of local Fourier coherence.
The additive square closes exactly before quotienting. Failure occurs only
when one asks it to factor through

\[
\mathbb Q_p^\times\longrightarrow\mathbb Z.
\]

The required comparison object must retain both:

1. the additive residue or germ coordinate carrying \(\Delta_h\);
2. the multiplicative valuation coordinate carrying the Euler loop.

The natural home is therefore the full local recollement or an equivalent
residue-aware correspondence. The scalar Tate determinant line may compare
their final readouts, but it does not manufacture the missing descent.

## Scope

The witness closes the naive valuation-only finite incidence already at
prime \(2\). It does not rule out a larger local correspondence retaining
residue classes, nor a global boundary current constructed on that larger
object. It also does not establish its restricted-product completion.

The next admissible gate is to construct the smallest residue--valuation
correspondence on which additive translation and the primitive Euler return
are both defined, then test whether their commutator is a source boundary
2-cell.
