# Entry 482 — The Bare Conormal Identity Does Not Define an Intrinsic Boundary Cancellation

Entry 481 records the correct polynomial identity

\[
3a^3(1+b)
+3\frac{a^3(1-b^2)}{b-1}=0.
\]

Its promotion to a derived boundary cancellation was premature.  The identity
was checked in the bare polynomial fraction field, not in the intrinsic odd
Cartier lattice established in Entries 455 and 465.

## Intrinsic valuation audit

The odd lattice generator is

\[
\eta_-=a\,t^3(b+1)
=\frac{a}{8}(b-1)^3(b+1)^4.
\]

Its boundary valuations are therefore

\[
(v_{+},v_{-})(\eta_-)=(3,4).
\]

For the Entry 477 mixed class and the plus-conormal quotient,

\[
h=3a^3(b+1),
\qquad
\frac{g}{b-1}=-a^3(b+1),
\]

the boundary valuations are both \((0,1)\).  Relative to the intrinsic frame,
both have valuations

\[
(-3,-3).
\]

Thus they are meromorphic with third-order poles in the intrinsic odd frame.
Their scalar sum is indeed zero in the common fraction field, but neither term
has yet been shown to be a regular morphism of the source-derived boundary
lattices.  Cancellation of two inadmissible meromorphic expressions does not
by itself construct a differential or homotopy in the relative category.

At the minus boundary the other conormal quotient has relative valuations

\[
(v_+,v_-)\left(\frac{g}{b+1}\Big/\eta_-\right)=(-2,-4),
\]

so the asymmetry cannot be repaired by declaring the same bare formula at both
ends.

## Corrected status of Entry 481

Entry 481 proves a useful **fraction-field identity and coefficient match**.
It does not prove the claimed intrinsic plus-boundary cancellation.  That
claim is withdrawn pending a lattice-valued construction.

The next gate is to derive the domain and codomain twists of the conormal
boundary generator from the complete weighted exact sector.  Only if those
twists supply the missing three powers at \(b=1\) does the coefficient-three
identity become an admissible boundary differential.  The minus-boundary
fourfold weight must then be checked independently.

No new carrier geometry is indicated; the obstruction is the typing of a
coefficient-complex morphism.

The executable audit is
`research/voevodsky/check_soft_axis_odd_intrinsic_boundary_typing.py`.
