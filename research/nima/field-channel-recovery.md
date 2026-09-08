# Channel recovery over a declared field

## Question

What additional test beyond geometric channel-image membership decides recovery over the coefficient field?

## Claim boundary

Let n>=4 and all triangulation weights lie in k*, for a field k. Every contextual polygon flip is included. No zeros, source normalization, or physical interpretation are supplied.

For a flip exchanging x for y record w(T')/w(T). On the connected crossing graph choose a root and assign its relative scale one; propagate relative scales r along a spanning tree. Check every contextual edge equation w(T')/w(T)=r_y/r_x, including parallel edges and edges outside the tree. Failure obstructs any channel representation. If all pass, the quantity

\[
a=\frac{w(T)}{\prod_{c\in T}r_c}
\]

is independent of T by flip connectivity. Channel scales exist in k exactly when a=z^(n-3) for some z in k*: the scales z r_c then reconstruct all weights. Necessity follows because any solution has the same relative scales and therefore differs by one common multiplier.

Changing the graph root rescales r by one field unit b, replacing a by a/b^(n-3). Thus the class of a in k*/(k*)^(n-3) is independent of root. Different paths yield the same r once every edge equation passes. Solutions, when present, form a torsor under the field-valued roots of unity of order dividing n-3; this statement about points does not assert an etale group scheme in positive characteristic.

## Disposition

The checker uses nonconstant rational channel products and their uniform doubling. All nine graph roots and two edge traversal orders yield the predicted power class. The original weights recover; doubled weights fail because their 2-adic valuation class is one modulo three. A local triangle-factor input fails the edge-consistency stage, distinguishing geometric failure from coefficient-field failure. Exact targeted checks passed.
