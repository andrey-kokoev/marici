# One precursor trace vector has zero Schur reserve

## Source trace increment

Let

\[
a
=
\int_0^\infty e^{-u/2}\Phi(u)\,du
=
\frac12-\frac14\vartheta(1),
\]

and

\[
b
=
\int_0^\infty e^{u/2}\Phi(u)\,du
=
\frac14\vartheta(1).
\]

Then

\[
a+b=\frac12.
\]

For the single theta precursor \(h\), the relative Wronskian increment is the vector

\[
v_h=
\begin{pmatrix}
a\\
b
\end{pmatrix}.
\]

## Rank-one Gram

If one forms the boundary energy from this one source vector alone, its Gram is

\[
G_h
=
v_hv_h^{*}
=
\begin{pmatrix}
a^2&ab\\
ab&b^2
\end{pmatrix}.
\]

It has

\[
\det G_h=0.
\]

Eliminating either reciprocal trace gives zero Schur reserve. For example, if \(b\ne0\),

\[
a^2-(ab)(b^2)^{-1}(ab)=0.
\]

Thus the two nonzero trace amplitudes do not by themselves generate a positive effective wall coefficient.

## Interpretation

The reciprocal masses partition one wall class. They are not two independent wall-energy directions. Treating them as independent diagonal energies would double-count one precursor degree of freedom and manufacture coercivity.

The result is a finite version of the coherent-mode problem: two visible outputs can still span only one source direction.

## What can create positive reserve

A nonzero wall Schur return requires at least one of:

1. a second independent precursor mode with a non-collinear trace vector;
2. a bulk completion energy coupled to the traces;
3. an independently typed endpoint or archimedean trace;
4. a nontrivial relative Green polarization not equal to the Euclidean outer product of one trace vector.

Each option must be source-derived.

The reciprocal kernel modes \(w_+\) and \(w_-\) are natural candidates for enlarging the precursor domain, but their admissibility and endpoint asymptotics differ. Merely listing both formal solutions does not produce a positive trace Gram.

## Polarized trace criterion

For a precursor test space \(\mathcal E_{\mathrm{pre}}\), define

\[
\mathcal T f
=
\begin{pmatrix}
\Delta\mathcal B_-(f)\\
\Delta\mathcal B_+(f)
\end{pmatrix}.
\]

The complete trace Gram has positive two-dimensional support exactly when

\[
\operatorname{rank}\mathcal T=2
\]

after quotienting the completion radical. Equivalently, there must exist \(f_1,f_2\) such that

\[
\det
\begin{pmatrix}
\Delta\mathcal B_-(f_1)&\Delta\mathcal B_-(f_2)\\
\Delta\mathcal B_+(f_1)&\Delta\mathcal B_+(f_2)
\end{pmatrix}
\ne0.
\]

One precursor \(h\) can never certify this rank.

## Relation to the wall kernel

Adding \(cw_+\) shifts boundary values without changing completed bulk. Depending on whether increments or absolute traces are used, this kernel mode may:

- disappear from the increment map;
- supply an independent absolute wall coordinate;
- or become a gauge direction.

The relative complex must state which. Quotienting \(w_+\) before forming absolute traces may erase precisely the wall needed for rank two.

## Hostiles

1. Use \(a\) and \(b\) as two diagonal wall energies, ignoring their common rank-one source.
2. Compute a nonzero Schur complement by dropping the cross term \(ab\).
3. Add a formal kernel solution as a second vector although it violates the declared decay domain.
4. Obtain rank two at every finite endpoint but lose the second trace direction in the completion limit.

## Next theorem

Freeze the precursor domain and decide whether the relative trace uses absolute endpoint values or increments. Then compute the rank of

\[
\mathcal T:
\mathcal E_{\mathrm{pre}}/\operatorname{rad}\mathcal C
\to
\mathbb C^2.
\]

If the rank is one, the relative wall cannot supply the identity reserve alone and the auxiliary cell must retain an additional bulk or endpoint feature. If the rank is two, its smallest singular value becomes the new completion margin.
