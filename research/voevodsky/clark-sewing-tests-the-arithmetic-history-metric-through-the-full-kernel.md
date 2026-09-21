# Clark sewing tests the arithmetic history metric through the full kernel

## Source inputs

This comparison uses:

- `research/grothendieck/closure-generated-arithmetic-history-and-its-terminal-metric-obstruction.md` for the actual arithmetic subspace (1,d,d^2) and its comparison U;
- `research/grothendieck/reciprocal-clark-sewing-leaves-one-explicit-forcing-correlation-row.md` for the four source tails and fixed Clark coefficient matrix C;
- `research/grothendieck/clark-sewing-to-the-endpoint-gamma-prime-green-kernel.md` for the full scalar arithmetic kernel.

The source map from the three history vectors into the full Clark realization is not yet constructed. The calculations below give necessary conditions on it and a domain-correct shell map supplying its degree-one ingredients.

## Full Hermitian invariant form

On (1,d,d^2), the comparison is

    U = [[1,0,0],[1,1,0],[0,1,1]].

Solving U* Q U=Q over all Hermitian matrices gives

    Q = [[a, -e/2+i h, -e],
         [-e/2-i h, e, 0],
         [-e, 0, 0]],       a,e,h real.

Its determinant is -e^3. Thus Q is nondegenerate precisely when e is nonzero. The imaginary parameter h is additional to the real symmetric family in the earlier note.

If Q is positive semidefinite, its zero last diagonal entry forces the last row to vanish, hence e=0. Its zero middle diagonal then forces h=0. The remaining form is diag(a,0,0), a>=0: both comparison directions are radical.

## Fixed-port Clark obstruction

The fixed coefficient matrix is

    C = (1/2) [[0,0,-1,1], [0,0,-1,1], [-1,-1,0,0], [1,1,0,0]].

It has rank two and inertia (1,1,2). For any linear map J:C^3 -> C^4, a pullback J* C J has rank at most two. If it is also U-invariant, the determinant calculation forces e=0. Therefore

    Q = [[a,i h,0],[-i h,0,0],[0,0,0]].

The degree-four vector d^2 is necessarily radical. If h is nonzero, d itself remains paired with 1 and the form has rank two and inertia (1,1,1). Thus an indefinite fixed-port pullback can retain one comparison direction, but cannot retain the nondegenerate three-dimensional invariant form.

This conclusion is conditional on requiring U-invariance in one terminal-indexed metric. A history-indexed family has different covariance equations.

Injectivity of J alone does not evade the obstruction. The checker exhibits an injective J whose d^2 image is a nonzero vector in ker C. Faithful linear storage and a nondegenerate form are separate requirements.

## The full divided-difference kernel passes this rank test

The Clark numerator has the rank-two factorization

    N(w,z)=h(w)* C h(z).

The full kernel is

    K(w,z)=N(w,z)/[-i(z-conjugate(w))].

Entrywise division across a spectral packet is not a fixed diagonal congruence and need not preserve numerator rank. As an exact algebraic fixture, take X(z)=z^3+z. Its Clark kernel is

    K(w,z)=6 conjugate(w)^2 z^2 +2 conjugate(w)^2
           -4 conjugate(w) z +2z^2+2.

At nodes 0,1,2 the numerator matrix has rank two, while the removable-limit kernel matrix is

    [[2,4,10],[4,8,28],[10,28,98]].

It has determinant -128 and inertia (2,1,0). Thus a full Clark kernel can have exactly the dimension and inertia needed by a nondegenerate invariant Jordan form. This example distinguishes the two rank questions; it does not identify the arithmetic kernel or provide the history source map.

## Domain-correct shell ingredients

Fix the completed forcing Phi with the normalization used by the arithmetic crosswalk. On a finite shell I_i=[A_i,B_i], define

    f_(i,0)(x)=1_(I_i)(x) Phi(x),
    f_(i,1)(x)=x f_(i,0)(x),
    G_(i,sigma,j)(z;x)=integral_x^infinity exp(sigma i z(t-x)) f_(i,j)(t) dt.

For fixed z these compactly supported L2 forcings give H1 tails on the half-line satisfying

    (partial_x+sigma i z)G_(i,sigma,j)=-f_(i,j).

The shell indicators themselves need not be H1. First-order integration by parts applies to the tails, which are continuous across shell boundaries and have weak derivatives in L2. This bypasses the earlier failed direct embedding of step densities into a second-order graph.

Let h_i(z) collect their four values at x=0 in the order (+,0),(-,0),(+,1),(-,1). Each pair of shells has a defined numerator

    N_ij(w,z)=h_i(w)* C h_j(z)=B_ij(w,z)+R_ij(w,z).

Here B_ij retains all cross-tail pairings with coefficients

    C_ab i(sigma_b z-sigma_a conjugate(w)),

and the forcing row is exactly

    R_ij=<f_(i,0),G_(j,-,1)(z)-G_(j,+,1)(z)>
         +<G_(i,-,1)(w)-G_(i,+,1)(w),f_(j,0)>.

The moment-one forcing terms cancel by the same fixed matrix identity as in the full source calculation.

## Cross-shell correlation and its orientation

Define

    A_ij(d)=integral_0^infinity (x+d) f_(i,0)(x) f_(j,0)(x+d) dx.

For real Phi, change of variables gives

    R_ij(w,z)=2i integral_0^infinity
        [A_ji(d) sin(conjugate(w)d)-A_ij(d) sin(zd)] dd.

For ordered disjoint shells with i<j, A_ji vanishes on d>=0, while A_ij can be nonzero. Thus cross-shell orientation is explicit in the source row. Summing over all shell pairs recovers the original A(d) formula, whenever the shell partition covers the source and the integrals converge.

For our fifteen shells, the omitted regions [0,log 2) and [log 420,infinity) must also be included to reconstruct the full half-line source. In addition, Phi must remain distinguished from our single-label atom Phi_1; the completed normalization and theta-label sum have not been replaced by that atom.

For the single-label, first-slot-localized source alone, the moment row is

    A_i(d)=M_i(d)+d H_i(d),
    M_i(d)=integral_(I_i) x Phi_1(x)Phi_1(x+d) dx.

This identifies the additional moment needed by Clark sewing. It is not the full completed A without the other shells and theta labels.

## A necessary cancellation before regularization

Individual off-diagonal N_ij need not vanish at z=conjugate(w). For real spectral x and real shell forcings,

    N_ji(x,x)=-N_ij(x,x).

Their sum cancels, but each divided off-diagonal row may have a pole. In fact, with X_i(z)=integral f_(i,0)(x)cos(zx)dx,

    N_ij(x,x)=2i[X_i(x)X_j'(x)-X_i'(x)X_j(x)].

Consequently it is unsafe to assign a separately regular positive kernel to every directed shell pair. The common-source sewing and its cross terms determine which singularities cancel. The compact-source fixture in the checker exhibits a nonzero off-diagonal residue and its exact opposing cancellation numerically.

## Remaining comparison, now restricted

The shell map supplies the four moment-tail columns on the actual first-order domain. It does not yet supply an algebra representation sending tensor history multiplication to operators on the Clark source. In particular, mapping the degree-two d and degree-four d^2 requires an admitted multipoint source composition or receiver; summing shell columns loses their order.

The next required data are therefore:

1. a source-derived receiver for the tensor history into the full tail/spectral construction;
2. its images of 1,d,d^2, with all cross-shell terms retained;
3. the full-kernel pullback Q and the residual U* Q U-Q;
4. if the residual vanishes, a source-derived value e different from zero for nondegeneracy.

Fitting a matrix of inertia (2,1) to U would not construct this receiver. The fixed-port obstruction also shows why the full scalar arithmetic identity must not be replaced by its rank-two numerator.

## Degreewise tensor assembly fails the invariant-metric test

A direct way to extend the known shell maps is to apply them tensorwise at each history degree, then form an orthogonal direct sum of the degreewise signed forms. This gives a legitimate chosen graded form wherever its factors are defined. It pairs the vacuum with no positive-degree history vector.

On the actual arithmetic subspace, d has positive degrees two through four and d^2 is purely degree four. Therefore every such orthogonal assembly has

    Q(1,d)=0,       Q(1,d^2)=0.

Combining these two identities with the full invariant matrix above forces e=h=0. Both d and d^2 then lie in the radical of the restricted form. Thus this direct extension cannot simultaneously provide terminal-indexed isometric comparison and a nondegenerate form on the three-dimensional history subspace.

This is a conditional obstruction to that particular assembly, not a failure of tensor histories themselves. A full source sewing can contain cross-degree terms; a history-indexed positive family also avoids the terminal-invariance assumption.

## Exact adjoint and functional needed on the relative history algebra

The actual comparison subalgebra is B=C[d]/(d^3), with r=1+d. If r is to be isometric in a nondegenerate terminal form, its adjoint must be r^(-1). This forces

    d^*=-d+d^2,       (d^2)^*=d^2.

It is an involution on B. It mixes the lower and higher history contributions even though the event records were originally graded.

A Hermitian functional lambda on B has the required values

    lambda(1)=a,
    lambda(d)=L/2+i h,
    lambda(d^2)=L,

with a,L,h real. Defining q(x,y)=lambda(x^* y) gives exactly

    Q = [[a,L/2+i h,L], [L/2-i h,-L,0], [L,0,0]].

This is the preceding invariant family with e=-L; its determinant is L^3. Since B is commutative and r^*r=1, invariance follows directly. Every invariant Hermitian form on this subspace is represented this way.

Thus the required source comparison has a sharply testable highest-grade coupling:

    lambda_Clark(d^2)=Q_Clark(1,d^2)=L != 0,
    Q_Clark(d,d)=-L,
    2 Re Q_Clark(1,d)=L.

The scalar L must be derived from the completed Clark source, including its cross-shell and cross-degree attachments. Choosing L to make the form nondegenerate would specify a new form rather than identify the prescribed one.

Under the stronger requirement that each event 1+v itself be isometric, its adjoint increment would be

    v^*=-v+v^2-v^3+v^4

in the four-jet algebra. A plain degree-preserving sign reversal v -> -v fails already at the quadratic term. The adjacent-history comparison assumption alone does not impose this stronger eventwise requirement.

The new exact checker verifies the relative involution, the functional matrix, its invariance and determinant, the degreewise-assembly obstruction, and the formal event inverse. The actual Clark functional on B remains to be constructed.

## Verification

Fresh commands:

    uv run --with sympy python research/voevodsky/checkers/check_clark_history_jordan_metric_gate.py
    uv run --with sympy --with mpmath python research/voevodsky/checkers/check_shell_resolved_clark_sewing.py
    uv run --with sympy python research/voevodsky/checkers/check_history_clark_cross_grade_requirement.py

All three passed. The first is exact symbolic algebra, including the polynomial rank fixture. The second checks exact Clark coefficients and the endpoint rational identity, then tests all four ordered shell pairs for exp(-x) on [0,2] split at 1 using 35-digit quadrature. Observed Green and correlation errors were below 1e-35. Those numerical tests are regressions of the stated analytic identities, not interval certificates or arithmetic positivity results.
