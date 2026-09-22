# Alternative balanced sectors reduce cubic response amplification to sharp Gaussian order

## Result and measurement boundary

The response amplification exp(904 pi A^2) is NOT intrinsic to the cubic source functional. The answer depends on which existing labelled outputs are available:

1. With ONLY the original four selected sectors, the exact minimal extension norm is given in section 3 and has Gaussian order exp(901 pi A^2).
2. With the FULL labelled balanced output of the same six-event, two-feature corner, an explicit alternative observer has norm of order

       A^(-2y-5) exp(101 pi A^2).

   A matching lower bound proves this full-output growth order is optimal. An exact finite-A minimizing constant is not claimed in this second setting.

The new observer agrees with the OLD functional on the ENTIRE actual cubic source corner, not just on the positive witness. It uses an additional already existing balanced sector, changes no pairing or source ideal, and does not merge or discard response labels.

Inputs:
- `../nima/translated-cubic-observers-have-sharp-gaussian-source-growth.md`
- `two-residual-gaps-detect-the-adjacent-cubic-attachment.md`
- `../nima/the-two-slot-residual-attachment-has-a-rigged-tate-comparison.md`

## 1. Fix the functional and the response norm

Keep the translated background A, the six event primes (2,3,5,7,11,13), the spectral point iy, and the actual two-feature I^3 corner. Let Lambda_A be the supplied cubic residual-gap functional.

Use the existing full five-label one-feature response O. At the record level use the labelled l1 sum of ordered projective response tensors, retaining every balanced seam and memory shape in this homogeneous corner. Feature tensors are UNSCALED, exactly as in the supplied four-sector response-noise norm; the functional itself carries w_seam^2. Fixed event/graph weights, if included, only change location-independent constants at this fixed shape. No source Gamma norm is substituted for this response norm.

The full output Y_A is D3 followed by actual response substitution and forward balancing. We minimize over continuous scalar tests on this declared response carrier whose restriction to Y_A of the actual source is Lambda_A. Scalar variance follows the existing conjugate-linear first-slot observation convention.

The supplied source enumeration gives 270 disjoint-support basis products. Only two have nonzero Lambda_A:

    v_0=mixed(2,3) mixed(5,7) forgotten(11,13),
    v_x=mixed(2,5) mixed(3,7) forgotten(11,13).

Their values are

    S_0=w_seam^2/(2y^2) gap_A gap_B,
    S_x=-w_seam^2/(2y^2)(mu(A,2)-L_0)(mu(30A,7)-L_0).

These values, including the crossed product, are retained exactly in everything below.

## 2. Size of one actual response on this family

Put e=exp(-yu), h=||e||_(H_-gamma)=1/sqrt(2(y+gamma)). For a positive window F,

    O(Psi(F))=sqrt(2)X_F [c_even+(mu_F-L_0)v_e],

where c_even=O(e,0) is fixed, and v_e has e only in the weak residual coordinate. Since that coordinate is zero in c_even, the sum response norm is exactly

    ||O(Psi(F))||=sqrt(2)X_F [C_even+|mu_F-L_0|h].

C_even is finite and independent of A. The supplied theta asymptotics give, for each fixed k,p,

    X(kA,p) ~ pi(kA)^(y+5/2) exp(-pi k^2 A^2),
    mu(kA,p)=log(kA)+o(1).

Thus the weak residual coordinate dominates the one-feature norm asymptotically. This accounts for the logarithmic factors below; treating every response norm as merely proportional to X_F would give the wrong polynomial/logarithmic calculation.

## 3. Exact optimum when only four old sectors are measured

Let z_ij be the actual response tensor in old sector (A_i,B_j), and put n_ij=||z_ij||_pi. These are nonzero elementary tensors, so n_ij is the product of their one-feature response norms.

The four-sector images of v_0 and v_x are

    z_0=(z_11,z_12,z_21,z_22),
    z_x=(0,z_12,0,0).

All other cubic basis products have zero projection to these four sectors. Set K=n_11+n_21+n_22 and B=n_12. For coefficients a,b, the image norm is exactly

    |a|K+|a+b|B,

while the desired functional is a(S_0-S_x)+(a+b)S_x, with conjugates when using the first-slot convention. Weighted l1 duality and continuous norm-preserving extension therefore give the exact optimum

    t_4,min=max(|S_0-S_x|/K, |S_x|/B).

This is an optimization of the SAME source functional, not of arbitrary four independently prescribed scalar values.

The K term is dominated by sector (A_1,B_1), whose theta exponent is 1+6^2=37. The B term has exponent 1+30^2=901 and dominates the maximum. In particular

    t_4,min ~ [w_seam^2(y+gamma)/(2y^2 pi^2 30^(y+5/2))]
                 A^(-2y-5) exp(901 pi A^2).

So 904 is avoidable even on those four measurements, but their crossed-source direction forces 901. No test using only those four outputs can attain the smaller order proved next.

## 4. Two private balanced sectors in the full output

Retain the forgotten seam 210A->2310A. Use these two balanced sectors, with vacuum buffers:

    row_0: retained A->2A and 6A->30A,
    row_x: retained A->2A and 10A->30A.

The second row was not among the old four. It is an EXISTING sector of the same actual source, not a new measurement label invented by a fitted form.

Enumeration of all 270 actual minimal cubic products gives:

- row_0 has coefficient +1 on v_0 and zero on every other basis product;
- row_x has coefficient +1 on v_x and zero on every other basis product.

The source reason is that their first and third retained event positions and intermediate vertices fix the two preceding pair blocks. The checker verifies this exhaustively with the existing marked-path recorder and balanced normalization.

Thus these rows separate precisely the two nonzero values of Lambda_A without contamination from the other source basis directions.

## 5. An explicit continuous observer, not just an extension argument

On a one-feature output let kappa read only its weak residual coordinate through

    kappa(w)=sqrt(2(y+gamma)) integral_0^infinity
                 exp(-(y+2gamma)u) w_res(u)du.

The test has H_gamma norm one, so kappa has response norm one. It satisfies kappa(v_e)=h. This is an admitted test in the prescribed five-label test space, not an arbitrary tensor-dual element.

For F with mu_F!=L_0,

    kappa(O(Psi(F)))=sqrt(2)X_F(mu_F-L_0)h.

All needed differences are nonzero for sufficiently large A. Let E_0 and E_x be the products of these values on row_0 and row_x respectively. Explicitly,

    E_0=2h^2 X(A,2)X(6A,5)(mu(A,2)-L_0)(mu(6A,5)-L_0),
    E_x=2h^2 X(A,2)X(10A,3)(mu(A,2)-L_0)(mu(10A,3)-L_0).

Use the scalar test

    Lambda_new(y)=(S_0/E_0) conjugate((kappa tensor kappa)(y_row0))
                 +(S_x/E_x) conjugate((kappa tensor kappa)(y_rowx)).

The coefficients are real in this imaginary-spectral setup. By section 4, Lambda_new Y_A equals Lambda_A on EVERY source basis product, hence on the entire source corner. Forward balancing is already included in the row definition; the tests are continuous on the resulting labelled balanced carrier. They do not redefine its quotient.

If one also wants an original residual-port observer representation on this prepared fibre, put h_test=sqrt(2(y+gamma))exp(-(y+2gamma)u). The port

    (h_test,-[L(1/2+y)+L(1/2+y+2gamma)]h_test)

has Q_res observation equal to <r,h_test> on u proportional to e. This follows from the two independently known exponential eigenvalues. It shows compatibility with the existing form without changing that form. Its ambient norm need not equal the optimal unit residual-coordinate test norm.

For finitely many small backgrounds where an E denominator vanishes, the original observer remains available. The asymptotic optimization concerns sufficiently large admitted A and claims no uniform numerical onset.

## 6. Sharp full-output growth order

Because the two rows are independent l1 sectors and kappa tensor kappa has projective dual norm one,

    ||Lambda_new||=max(|S_0/E_0|,|S_x/E_x|).

The first term has order exp(37 pi A^2)A^(-2y-5)(log A)^(-2). The crossed term dominates and satisfies

    |S_x/E_x|
      ~ [w_seam^2(y+gamma)/(2y^2 pi^2 10^(y+5/2))]
           A^(-2y-5)exp(101 pi A^2).

This is an explicit upper bound of the claimed order for the full-output optimum t_full,min.

For the matching lower bound, ANY representing test must obey

    ||test|| >= |S_x|/||Y_A(v_x)||.

Expand the actual 32 marked paths of v_x and their at most 20 ordered three-cut terms. Their two retained windows start at or after A and 10A respectively. Each one-feature response has norm at most a fixed constant times log(A) times X(A,2), or X(10A,3), for all sufficiently large A. This follows uniformly over the finitely many event-window choices from section 2. Forward concatenation/balancing retains its fixed-shape bound, independent of the translated background.

The projective triangle inequality consequently gives

    ||Y_A(v_x)|| <= C (log A)^2 X(A,2)X(10A,3).

No cancellation is assumed in this upper bound. Since |S_x| is comparable to (log A)^2, every representing test has norm at least a positive constant times A^(-2y-5)exp(101 pi A^2). Combined with the construction,

    t_full,min is comparable to A^(-2y-5)exp(101 pi A^2).

This proves the optimal growth ORDER, including its polynomial power. It does not determine the exact best finite-A norm or leading constant of all possible full-output representatives.

## 7. Noise and source priors

For total independent full-output noise epsilon, the new observer's scalar error is at most ||Lambda_new||epsilon. Thus, up to source-independent asymptotic constants, a fixed scalar tolerance permits

    epsilon of order A^(2y+5)exp(-101 pi A^2),

rather than the old calibrated test's order A^(2y+5)exp(-904 pi A^2). With only four old outputs the intrinsic order is instead exp(-901 pi A^2). Access to row_x is essential for the full improvement.

These are asymptotic orders, not certified finite numerical tolerances. Enclosing the new amplitudes and coefficients would require a separate calibration. The shared-template certificate in Grothendieck's supplied two-feature transport note is compatible but answers a different question: it controls a structured approximation of the positive witness, not a uniform norm on this complete source corner.

The SOURCE functional has not changed. Its source norm remains the supplied A^(-2beta-7)exp(101 pi A^2), and its source-prior threshold remains exactly the one proved there. Equality of the Gaussian exponents does not identify source and response norms; their polynomial powers still differ.

The adjacent nonzero attachment observation is unchanged on the actual source image. No metric, ideal, arithmetic coefficient or root-state factor has been modified to obtain the improvement.

## Verification

`uv run --with sympy python research/voevodsky/checkers/check_optimized_cubic_response_observer.py`

The checker verifies the old and new projections on ALL 270 actual cubic products, exact equality of the two functionals on that basis, the four-sector coordinate formula, the residual test's port realization, and the distinct 904/901/101 exponent algebra.

The supplied `certify_two_feature_escape_transport.py` also passes its symbolic and Arb checks. Actual asymptotic optimality here follows from the specified response norms, source enumeration, and the supplied theta boundary estimates, not from sampled window values.
