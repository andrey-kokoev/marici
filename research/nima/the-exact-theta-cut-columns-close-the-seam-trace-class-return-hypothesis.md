# The exact theta-cut columns close the seam trace-class return hypothesis

## Seam coefficient metric

Use the prime coefficient Hilbert space with

\[
\langle x,y\rangle_{\rm seam}
=
\sum_p(\log p)\overline{x_p}y_p.
\]

The source adjoint of a column incidence \(Bx=\sum_pb_px_p\) is

\[
(B^\dagger f)_p
=
\frac{\langle b_p,f\rangle}{\log p}.
\]

After identifying this coefficient space with ordinary \(\ell^2\), the
Hilbert--Schmidt columns are \(b_p/\sqrt{\log p}\).

## Exact primitive columns

The theta-cut identity gives a label-independent vector norm

\[
\|u_{p,1}\|_{\rm cut}^2=\|\Phi\|_2^2.
\]

After primitive Euler half-density loading,

\[
b_p=p^{-1/2}u_{p,1}
\]

up to the fixed source orientation.  Therefore

\[
\|B_1\|_2^2
=
\sum_p\frac{\|b_p\|^2}{\log p}
=
\|\Phi\|_2^2
\sum_p\frac1{p\log p}
<\infty.
\]

The convergence is the standard prime-density improvement over the divergent
sum \(\sum_n1/(n\log n)\).

## Square and connected columns

The square columns carry coefficient \(\frac12p^{-1}\), so their
Hilbert--Schmidt budget is bounded by

\[
\frac{\|\Phi\|_2^2}{4}
\sum_p\frac1{p^2\log p}<\infty.
\]

The connected grades satisfy the stronger nuclear estimate

\[
\sum_p\sum_{k\ge3}
\frac1k p^{-k/2}\|u_{p,k}\|<\infty.
\]

Hence adding square and connected columns preserves the
Hilbert--Schmidt property of the full seam incidence \(B\).

The wall-extended cut norm adds the same label-independent finite constant to
each unweighted atom.  It changes only the common multiplicative bound and not
the summability thresholds.

## Trace-class boundary return

Let \(G\) be the bounded reciprocal boundary propagator on the centered seam.
Then

\[
R=B^\dagger GB
\]

is trace class and

\[
\|R\|_1\le\|G\|\,\|B\|_2^2.
\]

For the centered prime loop

\[
L(1/2)e_p=p^{-1/2}e_p,
\]

one has

\[
\|L(1/2)\|=2^{-1/2}<1.
\]

Thus

\[
K_{\rm rel}(1/2)
=(I-L(1/2))^{-1}R
\]

is trace class and has a source-typed ordinary relative Fredholm determinant.

## Parameter neighborhood

For \(\operatorname{Re}s\ge1/2\), the primitive column estimate is no worse
than the centered estimate, and

\[
\|(I-L(s))^{-1}\|
\le\frac1{1-2^{-\operatorname{Re}s}}.
\]

Therefore the same construction is locally trace class on the right-hand
closed half-strip away from any separately declared parameter boundary. The
reflected reciprocal chart supplies the analogous estimate on the left using
\(1-s\).

The successor packet
`the-relative-seam-return-needs-det2-to-create-an-open-reciprocal-overlap.md`
shows that these ordinary Fredholm regions meet only on the centered line and
therefore cannot be glued as holomorphic charts. Passing to the
\(\mathcal S_2\) relative return gives the open overlap
\(1/3<\operatorname{Re}s<2/3\), at the cost of a first-trace anomaly.

## Separation from the bare Euler determinant

The relative return \(K_{\rm rel}\) is trace class because it passes through
the seam-weighted Hilbert--Schmidt incidence.  The bare prime loop \(L(s)\)
still carries the primitive, square, and connected determinant-three
filtration and is not trace class near the critical line.

Thus the completed scalar architecture may contain both:

- the boundary factors and \(\det_3\) associated with the bare Euler loop;
- an ordinary Fredholm determinant for the relative seam return.

They must not be conflated or double-counted.

## Disposition

The previously conditional residual-tail hypothesis for the seam-weighted
return is satisfied by the exact theta-cut columns.  The centered and
right-chart relative boundary return is trace class with an explicit ideal
bound.

Still open are reciprocal determinant-chart gluing, the archimedean factor,
the closed-loop boundary cone, comparison with \(\Xi\), and multiplicity
preservation.  No RH conclusion is authorized.
