# The Cayley--Menger determinant supplies the global del Pezzo surface

The missing global surface equation was already implicit in the source-normalized Cayley--Menger geometry.

On the residue `q_G12=0`, put

\[
c=-(x+y+z)
\]

in the five-by-five Cayley--Menger determinant \(K(a,b)\). Homogenizing its two loop-distance variables with \(h\) gives a quartic \(K^h(a,b,h)\). The normalized double cover

\[
S:\quad W^2=G(a,b,h),\qquad G=-\frac12K^h,
\]

lies in \(\mathbb P(1,1,1,2)\). For a smooth branch quartic this is the degree-two del Pezzo surface itself, not merely its infinity section.

Restricting to \(h=0\) and writing \(t=a/b\) gives exactly

\[
G(t,1,0)=x^2t^4-(x^2+y^2-z^2)t^2+y^2.
\]

Thus the previously studied elliptic quartic is the inverse image of the projective line at infinity.

Crucially, the full homogeneous polynomial is even separately in \(a,b,h\). Therefore the boundary reflection \(t\mapsto-t\) does extend globally:

\[
r_a:[a:b:h:W]\longmapsto[-a:b:h:W].
\]

It is distinct from the Geiser involution \(W\mapsto-W\).

The fixed locus of \(r_a\) consists generically of:

- the genus-one double cover above the fixed line \(a=0\);
- two isolated points above the fixed base point \([1:0:0]\).

Its Euler characteristic is therefore two. Topological Lefschetz gives

\[
\operatorname{tr}(r_a^*|H^2(S))=0.
\]

Since \(\operatorname{rk}H^2(S)=8\), the integral involution has rational eigenspace multiplicities \((4,4)\). It fixes the canonical class, hence on the \(E_7\) algebraic kernel the multiplicities are

\[
\dim E_7^+=3,
\qquad
\dim E_7^-=4.
\]

This changes the status of the automorphism route: the global surface lift is no longer missing, and it is neither identity nor Geiser integrally. What remains is a marking problem, not an existence problem: identify the invariant rank-three sublattice of \(E_7\) and place the source-supported plane \(\langle e_6,v_{\rm alg}\rangle\) in the same blow-up marking.

Evidence and executable derivation:

- `research/benincasa/derive_nine_master_residue_connection.py`;
- `research/benincasa/generic-infinity-boundary-genus.json`;
- `research/voevodsky/checkers/reconstruct_global_del_pezzo_double_cover.py`;
- `research/voevodsky/results/global_del_pezzo_double_cover.json`.
