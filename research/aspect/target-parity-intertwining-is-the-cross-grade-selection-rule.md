# Target-parity intertwining is the cross-grade selection rule

## Question

Can opposite source parity of primitive and square route amplitudes force their physical cross pairing to vanish before constructing the complete return?

## Selection theorem

Let \(P\) be source grade parity and \(U\) a unitary involution on the physical route target. Let

\[
T:V_{\rm source}\longrightarrow W_{\rm phys}
\]

be the route map, and assume the intertwining law

\[
TP=UT.
\]

For source vectors \(v_+,v_-\) with

\[
Pv_+=v_+,
\qquad
Pv_-=-v_-,
\]

their target images satisfy

\[
UTv_+=Tv_+,
\qquad
UTv_-=-Tv_-.
\]

Because \(U\) preserves the target pairing,

\[
\langle Tv_+,Tv_-\rangle
=
\langle UTv_+,UTv_-\rangle
=-\langle Tv_+,Tv_-\rangle,
\]

so

\[
\langle Tv_+,Tv_-\rangle=0.
\]

This vanishing kills the reciprocal Pauli \(X\) coefficient in the Gram return.

## Hostile without intertwining

Opposite source labels alone are insufficient. Take source parity basis \(e_+,e_-\) and a route map satisfying

\[
Te_+=Te_-=f
\]

for one nonzero target route \(f\). Then

\[
\langle Te_+,Te_-\rangle=\|f\|^2\ne0.
\]

The map collapses opposite source sectors and cannot intertwine any target parity assigning opposite signs to the common image.

## Relation to reciprocity

Reciprocity and parity act independently. Reciprocity removes the quadrature-odd \(Y\) channel. Target-parity intertwining removes the real symmetric \(X\) channel. If both hold, the return is diagonal in the primitive-square basis, but the diagonal eigenvalues still require a strict bound below one.

## Source gate

The source parity \((-1)^N\) is already defined on the primitive-square frame. The missing objects are:

1. a physical route map \(T\);
2. a target involution \(U\);
3. proof that \(U\) preserves the physical pairing;
4. the intertwining identity \(TP=UT\).

This is weaker than constructing every entry of the return but stronger than assigning parity labels to source vectors.

## Verification

`research/aspect/checkers/check_route_parity_selection.py` verifies orthogonality of opposite target-parity routes and a nonintertwining collapse with nonzero cross pairing using exact rationals.

## Disposition

A route-level parity selection rule can eliminate cross-grade mixing before a full return calculation, but only after target parity and intertwining are source-derived. Without them, the \(X\) channel remains admissible.
