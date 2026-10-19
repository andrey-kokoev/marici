# H4 — closed positive form and self-adjoint open-hinge Hamiltonian

## Claim and source boundary

This is an analytic proof for the fixed unstrained open-hinge model of `pentachoron_open_product_flux_note.md`, sections 2 and 5–6. The kinetic coefficients are kappa_O=kappa_F=1 and kappa_C=1/2, and epsilon=ell=hbar=1. It is not a claim about the later square-root radial kinetic operator, a continuum limit of its grids, or scattering completeness.

The source data are finite unitary spin comparisons, their seam/cycle Gram energies, the rank-two entrance projector P, the bounded unitary spin transport F(theta)=exp(i theta A), and the explicitly retained endpoint records. The contact equations below use the full source terms; none of their diagonal terms is subtracted as an energy offset.

## Hilbert and form domains

Put I=[-s_star,s_star], with 0<s_star<infinity. The Hilbert space is

    H = L2(R;C20) ⊕ L2(I;C20)
        ⊕ C168 ⊕ C168
        ⊕ L2(R+;C28) ⊕ L2(R+;C28).

Write u=(psi,chi,(eta_-,w_-),(eta_+,w_+),zeta_-,zeta_+), where each eta has eight C20 sectors and w lies in C8. The form domain V replaces each L2 field by H1 on the same interval and leaves all finite records unrestricted. The hinge's Hilbert space is L2, not H1; H1 is its **form domain**.

There is no imposed equality between a field trace and a finite record. The source uses finite positive penalties, not infinite-coupling constraints or Dirichlet conditions. Smooth compactly supported fields together with arbitrary finite records give density of V in H. V with the direct-sum H1/Euclidean norm is complete.

## The actual quadratic form

Let H_C(s)=F(theta(s)) H_C F(theta(s))*; the arc coordinate is continuous and theta(s) ranges over a compact interval. Define q as the sum of:

1. integral_R [||psi'||² + psi*H_O psi];
2. integral_I [(1/2)||chi'||² + chi*H_C(s)chi];
3. the original entrance term 2||P(psi(0)-chi(0))||²;
4. at each endpoint e, sum_b eta_e,b*H_e,b eta_e,b + w_e*M_e w_e;
5. at each endpoint, 2 sum_cube_edges ||Q_e,f(eta_e,b-eta_e,b')||², with each undirected edge once;
6. at each endpoint, 2||chi(e s_star)-eta_e,000||²;
7. at each endpoint, 2||zeta_e(0)-U_e(eta_e,111,w_e)||²;
8. for each output, integral_R+ [||zeta_e'||² + zeta_e*H_F,e zeta_e].

P is an orthogonal projector, so the source's matrix contact 2[[P,-P],[-P,P]] equals item 3. H1 gives the same equality for the face-projector contacts. The source solver's `defect` construction includes all four blocks of items 6–7. In non-unit sampling units the stated sqrt(ell) factors are restored; here ell=1 as fixed by H4.

## Positivity and boundedness of the native terms

Each native seam contribution is ||x_j-U_ji x_i||². The cycle contribution is 2I-T-T*=(I-T)*(I-T), since T is unitary. Re-pairing changes the comparisons, not the Gram construction. Thus H_O,H_C,H_e,b are positive Hermitian finite matrices. This uses the model's supplied comparison law, not an inference from approximate eigenvalues.

H_C(s) is positive and uniformly bounded, since F(theta) is unitary. M_e= D_e D_e* is positive (H3 additionally proves its eigenvalues are 1 and 3). The outgoing H_F,e is the direct sum of the remaining seam/internal-cycle Gram matrix and M_e, hence is positive too. Its difference from U_e H_pre U_e* does not affect positivity or closure; equality between them is neither assumed nor required.

All native terms are bounded on H: use the maximum of the finitely many matrix norms and ||H_C||. Finite graph-switch terms are nonnegative bounded forms on the finite records. Every remaining contact is a squared norm with a positive coefficient. Therefore q>=0.

## Trace bounds, form-norm equivalence and closure

For f in H1([a,b];C^d), L=b-a and any x in [a,b], the fundamental theorem of calculus and Cauchy–Schwarz give, for almost every y,

    ||f(x)||² <= 2||f(y)||² + 2L integral_a^b ||f'||².

Averaging y yields

    ||f(x)||² <= (2/L)||f||_L2² + 2L||f'||_L2².

The same estimate applies to line and half-line traces using a length-one subinterval containing the evaluation point. Thus every sampled field trace in q is bounded in its H1 norm. The elementary inequality ||a-Bb||²<=2||a||²+2||B||²||b||² bounds every trace-to-record term. No bound on a derivative trace is needed for the form domain.

Let q_kin be the sum of the four derivative-square integrals, with their positive kinetic coefficients. The norm

    ||u||_V,kin² = ||u||_H² + q_kin[u]

is equivalent to the direct-sum H1/Euclidean norm, since the smallest kinetic coefficient is 1/2. Positivity gives the lower bound, and the trace/native bounds give a finite upper bound:

    ||u||_V,kin² <= ||u||_H²+q[u] <= C ||u||_V,kin².

Hence the q-form norm is complete on precisely V. This proves q is closed, densely defined and nonnegative. The proof needs boundedness in the form norm and positivity, not a falsely asserted small relative perturbation bound.

## Self-adjoint realization and conservation

Polarize q using the complex inner product conjugate-linear in its first argument. The representation theorem for densely defined closed lower-bounded forms supplies a unique nonnegative self-adjoint H with

    Dom(H)={u in V: there is f in H with q(v,u)=<v,f> for all v in V},
    Hu=f.

This definition includes the source contact boundary conditions and finite-record equations without guessing extra boundary constraints. For example, on an outgoing half-line, integration by parts yields -zeta_e'(0)+2[zeta_e(0)-U_e(eta_e,111,w_e)]=0. At a hinge endpoint the outward derivative term has coefficient 1/2 and the corresponding trace-to-eta penalty. The entrance on the full line produces derivative jumps, not two independent boundary values: H1(R) has one trace at zero.

By the spectral theorem, exp(-itH) is a strongly continuous unitary group. It preserves the full Hilbert norm for all initial states and the form energy on V. This proves the stated conservative realization. It does not establish wave operators, asymptotic completeness, a product flux value, physical particle identification, or any convergence/error bound for source solvers.

## Verification status

`check_open_hinge_form.py` verifies pinned source payload hashes, the contact inventory and dimensions, and runs supplementary floating consistency checks on the supplied native/projector/generator arrays. The **analytic argument above**, not the floating eigenvalue test or Markdown hash, establishes closure and self-adjointness. The checker is not a proof assistant and does not mechanically verify the representation theorem. H1/H3 exact checks remain separately replayable.
