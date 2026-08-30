# The reduced RH pencil must be assembled from a common invariant form core

## Form-first constructor

The missing reduced pencil should not be manufactured by normalizing pointwise matrices. Begin with one dense source test core
\[
\mathscr D\subset\mathcal H
\]
that is invariant under:

- the ambient Mellin generator \(Q\);
- every finite cutoff inclusion;
- reciprocal Real transport;
- the complete typed boundary incidence.

On \(\mathscr D\), construct parameter-dependent sesquilinear forms:

- a closed nonnegative Green form \(b_s\);
- an arithmetic synthesis form \(f_s\).

The residual form is
\[
r_s=b_s-f_s.
\]
The distinguished generalized eigenvalue is therefore forced. A generalized eigenvector \(u\) satisfies
\[
f_s[u,v]=\lambda\,b_s[u,v]
\quad\text{for every }v\in\mathscr D.
\]
For a nonradical \(u\), the residual equation \(r_s[u,v]=0\) for every \(v\) is exactly the case \(\lambda=1\).
No extra source physics is needed to select the spectral point \(1\).

## Relative form bound

Require \(f_s\) to be relatively \(b_s\)-bounded on the common core:
\[
|f_s[u,v]|
\le
C_s
\bigl(b_s[u,u]+\|u\|^2\bigr)^{1/2}
\bigl(b_s[v,v]+\|v\|^2\bigr)^{1/2}.
\]
For analytic dependence, the closed form domains must remain fixed and \(s\mapsto b_s[u,v]\), \(s\mapsto f_s[u,v]\) must be analytic or norm-\(C^1\) for every \(u,v\in\mathscr D\), with compact-local control of the form bounds.

This gives a common-domain family before any operator representation.

## Stable radical reduction

Let
\[
\mathcal N_s=\{u\in\mathscr D:b_s[u,u]=0\}.
\]
Form domination must imply
\[
\mathcal N_s\subseteq\operatorname{rad}(f_s),
\]
so both forms descend to the Green quotient. But parameterwise descent is insufficient. The source theorem must provide either:

1. a fixed radical \(\mathcal N_s=\mathcal N\) over the patch; or
2. source-authorized parallel identifications of the quotient family with uniform angle and determinant control.

Cutoff and Real maps must preserve \(\mathcal N_s\). Otherwise there is no common reduced carrier and the assembly stops before the representation theorem.

## Associated generalized pencil

On the reduced form Hilbert space \(\mathcal H_s^{\mathrm{red}}\), apply the representation theorem to \(b_s\) and \(f_s\). The primary object is the associated generalized pencil
\[
\mathfrak T_s(\lambda)=F_s-\lambda B_s,
\]
or its form realization, not \(B_s^{-1/2}F_sB_s^{-1/2}\).

Only if strict positivity and bounded inverse square-root control are independently proved may one pass to a Birman–Schwinger operator. Semidefinite Green geometry must remain in pencil form.

The first assembly theorem is therefore:

> A common invariant form core, stable radical reduction, closed analytic Green forms, and relatively Green-bounded arithmetic forms determine a closed analytic reduced generalized pencil with distinguished spectral value \(1\).

## Two separate missing gates

The packet now separates two absences:

    missing_pencil_assembly:
      common_invariant_form_core
      stable_radical_reduction
      closed_analytic_green_form
      relatively_bounded_arithmetic_form
      representation_theorem_realization

    missing_gap_or_contour_isolation:
      compact_local_resolvent_annulus_around_1
      finite_algebraic_multiplicity
      cutoff_and_real_stability
      completion_spectral_exactness

The second gate cannot be tested before the first exists.

## Contour is auxiliary after isolation

Once the reduced pencil has a resolvent annulus
\[
0<|z-1|<\delta
\]
with no spectrum except the tracked cluster, any positively oriented contour around \(1\) inside that annulus defines the same Riesz projection. If \(\Gamma_0\) and \(\Gamma_1\) are homotopic there,
\[
\frac{1}{2\pi i}\int_{\Gamma_0}(z-K_s)^{-1}\,dz
=
\frac{1}{2\pi i}\int_{\Gamma_1}(z-K_s)^{-1}\,dz.
\]
Thus the contour is diagnostic auxiliary data. Source authority chooses the residual problem and hence the point \(1\); the analytic theorem supplies isolation. Extra authority is needed only for a larger or moving cluster not fixed by \(B-F\).

## Mandatory contour hostile

Choose two contours around \(1\) lying in the same declared resolvent annulus. If the resulting packets differ in:

- Riesz projection;
- algebraic rank;
- determinant factor;
- cutoff or reciprocal transport;

then at least one of the following is defective:

1. the functional-calculus implementation;
2. the claimed resolvent annulus;
3. the base-carrier identification;
4. the transport intertwining law.

Contour-homotopic packets cannot legitimately differ.

## Transport theorem

If cutoff inclusion and reciprocal Real maps preserve the common core and intertwine both forms,
\[
b_s(\iota u,\iota v)=b_s(u,v),
\qquad
f_s(\iota u,\iota v)=f_s(u,v),
\]
with the corresponding conjugate relation for \(J\), then they descend through the radical and intertwine the associated pencil. Resolvent and Riesz naturality follow by representation and functional calculus.

This order is compulsory:

1. source core;
2. forms;
3. radical quotient;
4. associated pencil;
5. gap at \(1\);
6. Riesz bundle;
7. compressed connection;
8. cubical coherence audit.

## Decisive frontier

The next source calculation is no longer “find an operator \(K_s\).” It is:

> place the complete Green boundary energy and arithmetic synthesis form on one Mellin-, cutoff-, and Real-invariant theta test core, prove stable radical reduction and relative form boundedness, and invoke the representation theorem.

That is the smallest non-manufactured route from the existing pointwise \(B_s,F_s\) data to the reduced RH pencil.
