---
id: 432
date: 2026-08-17
title: The Conductor Ring Square Has the Opposite Variance from the V-Map
---

# The Conductor Ring Square Has the Opposite Variance from the V-Map

Entry 431 constructed the global finite conductor cospan and isolated its left
ringed-morphism gate. That gate cannot be closed by an ordinary ringed finite
space: the geometric and algebraic arrows have opposite variance.

The forced exceptional map uses the order
\[
c<e_-,\qquad c<e_+,
\]
because \(h<r_-,h<r_+\) maps to \(c<e_-,c<e_+\). An ordinary Alexandrov
structure sheaf on this order requires generization maps
\[
\mathcal O_c\longrightarrow\mathcal O_{e_-},
\qquad
\mathcal O_c\longrightarrow\mathcal O_{e_+}.
\]

Normalization–conductor gluing has the reverse ring diagram. In the standard
node model it is
\[
A_+\xrightarrow{\epsilon_+}C
\xleftarrow{\epsilon_-}A_-,
\qquad
A_{\rm node}=A_+\times_C A_-.
\]
For the degree-\(n\) truncations of \(A_+=k[x]\) and \(A_-=k[y]\), this fiber
product has rank \(2n+1\). By contrast, the covariant diagram
\(C\to A_\pm\) imposed by the forced topology has compatible global tuples
determined by one element of \(C\); its rank is one. It does not reconstruct
the singular ring or its conductor extension.

Reversing the finite-space order to \(e_\pm<c\) permits the correct ring maps
\(A_\pm\to C\), but then the required image of \(h<r_\pm\) is not
order-preserving. Hence neither orientation of a single ordinary ringed poset
supports both the geometric V-map and the normalization fiber-product square.

This proves that the missing left leg is intrinsically mixed-variance. It must
be represented by a recollement/bimodule kernel combining restriction
\(A_\pm\to C\) with the exceptional shriek or Borel–Moore direction, exactly
as anticipated in Entries 144 and 146. Calling it a ringed-space projection
would erase one of its two essential variances.

The next gate is therefore algebraic rather than topological: write the
explicit normalization–conductor bimodule complex, pull it across the unique
V-to-conductor map, and verify that its derived fiber gives the endpoint swap,
the Tor-zero/Tor-one pair, and the ordinary-forgetting contraction.

The executable audit is
`research/voevodsky/check_conductor_ring_variance_no_go.py`.
