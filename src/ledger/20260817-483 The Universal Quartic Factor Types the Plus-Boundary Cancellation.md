# Entry 483 — The Universal Quartic Factor Types the Plus-Boundary Cancellation

Entry 482 correctly observes that the bare classes in Entry 481 are
meromorphic relative to the intrinsic odd resonance frame.  The missing twist
is nevertheless already present in the source: it is the universal \(a^4\)
factor removed when forming the divided Euler quotient.

## Degreewise restoration

Write \(c=b+1\).  Entry 460 assigns the divided monomial \(a^Ic^J\) the
boundary divisor

\[
B(I,J)=\left(\left\lfloor\frac I2\right\rfloor,
\left\lfloor\frac I2\right\rfloor+J\right).
\]

The mixed class and the plus-conormal quotient both lie in the divided
bidegree \((3,1)\), so their intrinsic source divisor is

\[
B(3,1)=(1,2).
\]

The universal factor has

\[
B(4,0)=(2,2).
\]

Restoring it gives

\[
\boxed{
B(3,1)+B(4,0)=(3,4)=B(7,1),
}
\]

which is exactly the odd resonance divisor of Entries 455 and 460.  Thus the
apparent third-order poles of Entry 482 resulted from comparing a divided
degree-three representative directly with a full degree-seven target.  The
source-derived quartic factor supplies the complete missing lattice twist.

## Typed plus-boundary identity

After restoration, both terms are regular sections of the same \((7,1)\)
odd lattice.  The coefficient identity of Entry 481 therefore becomes
admissible:

\[
a^4h|_{b=1}
+3a^4\operatorname{Res}_{b=1}(g)
=a^4(6a^3-6a^3)=0.
\]

This repairs, rather than bypasses, Entry 482: the bare identity alone was
untyped; the restored universal factor is the required typing datum.

The quartic factor is also the doubled-carrier relation retained by the even
Koszul cell of Entry 469.  Hence the cancellation belongs to the derived
carrier coefficient complex and would disappear if the universal relation
were discarded before taking the boundary map.

## Remaining gate

The plus-boundary tail cancellation is now regular and source-derived.  The
minus boundary still requires its own computation because its intrinsic
weight is four and the relevant conormal parameter is \(b+1\), not \(b-1\).
One must restore the quartic factor before taking that residue as well and
then determine whether its resulting component is exact in the doubled
carrier complex.

The executable audit is
`research/voevodsky/check_soft_axis_odd_quartic_twist_restoration.py`.
