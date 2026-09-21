# A weighted Clark-feature history receiver with convergent comparisons

## Constructed strength

The prior Clark source-interface bounds give an explicit analytical receiver for the current finite chamber source and all of its comparison histories. The construction retains ordered tensor slots, evaluates the actual four Clark tails, and represents the full divided-difference kernel at each slot.

The receiver is defined on a weighted analytic subalgebra of the formal history. It is faithful as a linear history representation and has bounded comparison operators. It does not assert that these comparisons preserve one terminal-indexed Green form, or that the source exposes route events experimentally.

## 1. Declared analytical data

Use the completed real forcing Phi normalized as in `research/grothendieck/clark-sewing-to-the-endpoint-gamma-prime-green-kernel.md`. It remains distinct from the single-label Phi_1 used by the earlier raw theta observation.

Let I_1,...,I_15 be the existing divisor shells in [log 2,log 420]. For v in V=C^15, put

    f_v(x)=sum_i v_i 1_(I_i)(x) Phi(x).

Fix a compact disk Omega in the upper half-plane, with positive area and

    0<eta<=Im z<=Y<beta,       z in Omega.

Use Lebesgue area measure mu on Omega. Define

    ||v||_V = ||exp(beta x)(1+x) f_v(x)||_L2,
    M = ||exp(beta x)(1+x) 1_[log 2,log 420](x) Phi(x)||_L2.

For the intended completed theta forcing the shell integrals are strictly positive, so this is a Hilbert norm on V and M>0. Every event incidence v(n,p) has norm at most M, since its shell union is a subset of the full interval.

One concrete choice is the disk centered at 2i with radius 1/4 and beta=3. The construction does not treat this spectral localization as a uniquely selected physical norm.

## 2. The actual one-letter Clark feature

For sigma in {+1,-1} and j=0,1, define the existing source tails and traces

    G_(sigma,j)(f_v;z;x)=integral_x^infinity exp(sigma i z(t-x)) t^j f_v(t) dt,
    h_(sigma,j)(f_v;z)=G_(sigma,j)(f_v;z;0).

Write h_v(z) in the order (+,0),(-,0),(+,1),(-,1). Set

    k_z(t)=exp(izt),       t>=0,
    L(v)(z,t)=h_v(z) k_z(t),
    E=L2(Omega x R_+, C^4; dmu(z) dt).

The existing trace bound gives, with a=beta-Y,

    |h_(sigma,j)(f_v;z)| <= ||v||_V/sqrt(2a),
    ||k_z||_2^2=1/(2 Im z).

Summing the four components and integrating gives

    ||L(v)||_E <= C_0 ||v||_V,
    C_0=sqrt(mu(Omega)/(a eta)).

For the concrete disk above, C_0=sqrt(pi/21).

This uses the actual first-moment source x f_v before tail completion, preserving the source operation order. No derivative-delta port is introduced.

The map L is injective. If L(v)=0, the zeroth forward trace vanishes for almost every z in Omega. It is entire because f_v has compact support, so it vanishes identically. Uniqueness of the Fourier transform yields f_v=0, and the disjoint nonzero shell densities yield v=0.

Since V is finite dimensional, L has a bounded left inverse on its image. No numerical lower bound is claimed.

## 3. Exact signed-kernel retention

Let C be the previously fixed four-by-four Clark coefficient matrix. For any two shell combinations u,v and upper-half-plane parameters w,z, the pointwise features satisfy

    <h_u(w) k_w, (C tensor I) h_v(z) k_z>
      = h_u(w)* C h_v(z) / [-i(z-conjugate(w))].

This is the full divided-difference expression. It includes every cross-orientation entry of C and every cross-shell entry produced by the source combination. The numerator is precisely the B_uv+R_uv derived by shell-resolved Green integration.

The E-valued realization integrates the diagonal spectral feature pairing over Omega. It also retains the entire z-indexed feature function, so the cross-spectral formula above is still available. Point evaluation in z is used on this finite-dimensional analytic feature image, where it is bounded; it is not asserted bounded on arbitrary elements of E.

For arbitrary labelled shell pairs there may be uncanceled meromorphic diagonal terms outside this upper-half-plane feature domain. Here Im z,Im w>0 ensures z-conjugate(w) is nonzero. Reconstructing the full completed source requires the omitted outer shells and completed label normalization, as recorded in the previous audit.

## 4. An analytical history algebra

Use projective tensor norms induced by ||.||_V and define

    A_rho(V)={h=(h_r): sum_(r>=0) rho^r ||h_r||_projective < infinity},
    ||h||_rho=sum_(r>=0) rho^r ||h_r||_projective.

Concatenation is submultiplicative, so A_rho is a unital Banach algebra. Its coefficient sequence embeds injectively in the full formal history H(V). Polynomial histories are dense in the analytic norm.

Take

    rho=1/(2M).

Every event satisfies ||v(n,p)||_rho<=1/2. Therefore

    (1+v)^(-1)=sum_(r>=0)(-v)^r

converges in A_rho, with norm at most 2. Every forward route and every comparison S_w^(-1)S_w' belongs to this one analytic algebra. Formal coefficients agree with the compatible inverse jets.

For full four-event routes,

    ||S_w||_rho <= (3/2)^4,
    ||S_w^(-1)||_rho <= 2^4,
    ||S_w^(-1) S_w'||_rho <= 81.

The reverse comparison has the same bound. These constants refer to the declared analytic history norm, not the earlier output-only theta noise metric.

A_rho is not complete for arbitrary degree-adic Cauchy sequences: some formal histories have infinite analytic norm. Thus the formal universal theorem is not being applied to all of H(V) as a Banach target. Evaluation below is instead proved directly by absolute convergence on A_rho.

## 5. Bounded operator receiver

Let F_tau(E) be the Hilbert direct sum of all tensor powers of E, including the vacuum, with norm

    ||xi||^2=sum_(r>=0) tau^(2r) ||xi_r||^2,
    tau=rho/C_0.

Left tensor creation by L(v), denoted c(L(v)), is bounded and has norm

    ||c(L(v))||=tau ||L(v)||_E <=rho ||v||_V.

The projective universal property and absolute summability define a unital algebra representation

    Pi:A_rho(V) -> B(F_tau(E)),
    Pi(v_1...v_r)=c(L(v_1))...c(L(v_r)),
    ||Pi(h)||<=||h||_rho.

On the vacuum,

    Pi(h) Omega_vac = direct_sum_r L^(tensor r) h_r.

Therefore Pi is faithful: different degrees occupy different tensor summands, and L is injective on V at every finite tensor degree. The inverse bound of L may grow under tensor powers; no bounded inverse of Pi on its entire image is claimed.

Chronological route words are represented with the declared tensor ordering. These operator matrices use ordinary left multiplication; the original memory comparisons use right multiplication. To implement the latter directly, use the bounded right regular operators

    R_a(h)=h a

on A_rho. They have ||R_a||<=||a||_rho, and C_(w,w')=R_(S_w^(-1)S_w') gives the same comparison law as before. On the common analytic history this avoids any convention change about the order of function composition.

All inverse and comparison identities hold by norm-convergent multiplication, not just formally. Their coefficient projections agree with every previously checked finite jet.

## 6. Signed form and the remaining isometry question

The bounded signature operator C on E has norm one. One possible graded signed form on F_tau(E) uses

    J_Fock=direct_sum_(r>=0) C^(tensor r),       C^(tensor 0)=1,

where C acts on the C^4 feature component. Its degree-r pairing is the product of r one-letter Clark feature pairings, with the declared analytic weight tau^(2r). This supplies a definite, bounded candidate form on the receiver. It is an explicitly chosen tensor extension; the earlier scalar arithmetic kernel does not force that extension.

The construction proves no isometry of the comparison operators for this fixed form. The four-jet obstruction already shows why a graded form cannot have the required faithful terminal-invariant restriction if it descends to that quotient. In the full receiver, invariance must be checked with the full infinite comparison, including all higher coefficients.

Thus the receiver supplies convergent histories and actual Clark features, while its terminal Green invariance remains an equation to test. The metric selection has been made explicit rather than inferred from formal universality.

## All-order test: a graded invariant form must lose the comparison direction

The chosen graded form pulled back to A_rho obeys

    q(1,h)=epsilon(h),

where epsilon is the degree-zero coefficient. Let r=S_w^(-1)S_w' and suppose right multiplication R_r is isometric for q. Its bounded inverse is R_(r^(-1)). For arbitrary g, apply invariance to 1 and g r^(-1):

    q(r,g)=q(1,g r^(-1))=epsilon(g).

The last equality uses epsilon(r)=epsilon(r^(-1))=1. Therefore

    q(r-1,g)=0       for every g in A_rho.

By Hermitian symmetry r-1 lies in the full radical. Conversely, any g with q(r-1,g) nonzero explicitly witnesses failure of isometry, through

    q(R_r 1, R_r(g r^(-1)))-q(1,g r^(-1))=q(r-1,g).

This argument is exact at all orders; it does not assume d^3=0 or use a finite Jordan block. It shows that an orthogonal-by-degree Clark extension can be terminal-invariant only by making the actual comparison direction radical. Thus a faithful invariant Green realization must change this graded assembly, use history-indexed forms, or explicitly accept that quotient.

The receiver itself remains faithful as a linear analytical representation. This test concerns its signed form, not storage or convergence.

## Scope and next test

Constructed: a faithful norm-convergent analytical history receiver at the current finite chamber cutoff, whose one-letter data are the source-defined Clark tails and whose slot pairings retain the full divided-difference kernel.

Still separate:

- comparison invariance of the chosen full signed form;
- a source reason selecting the tensor extension and its degree weights;
- uniformity as the prime/chamber cutoff grows;
- replacement of completed Phi by the earlier single-label Phi_1 observation;
- physical access to route events and calibration.

The full receiver's isometry question now has an all-order structural answer: the proposed graded form cannot preserve the comparison faithfully. A source-derived cross-degree sewing or a history-indexed Green family is required. The analytical convergence and one-letter Clark source map are already supplied above; those need not be rebuilt for the next form comparison.
