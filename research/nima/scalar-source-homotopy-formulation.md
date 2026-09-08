# Bounded source-derived homotopy formulation

## Question

Does a homotopy algebra derived from the scalar action explain the measured failure of triangle-weight quadrics? Operator authorized one bounded comparison, with a stop if the formulation reproduces amplitudes but supplies no residual-to-boundary map.

## Claim boundary

Use the declared massless real scalar source, not an authenticated external publication. With boundary terms discarded for compactly supported variations, write

\[
S=\frac12\int\phi K\phi-\frac g{3!}\int\phi^3-\frac\lambda{4!}\int\phi^4,\qquad K=-\Box.
\]

Fourier convention gives K(p)=p^2. Its equation is E(phi)=K phi-g phi^2/2-lambda phi^3/6. The algebra below is formal on smooth fields with products defined; no multiplication of singular distributions is asserted.

### Graded construction and identities

Use the shifted symmetric convention L-infinity[1]: V^0 is the field space, V^1 a separate copy for equations, and all other degrees vanish. Maps b_n are graded symmetric of degree +1. On degree-zero inputs define

\[
b_1(f)=Kf,\qquad b_2(f_1,f_2)=-g f_1f_2,\qquad b_3(f_1,f_2,f_3)=-\lambda f_1f_2f_3.
\]

Set b_n=0 for n>3 and every map to zero if an input lies in V^1. The Maurer-Cartan expression b1(phi)+b2(phi,phi)/2!+b3(phi,phi,phi)/3! is exactly E(phi). Each nested bracket in every homotopy identity vanishes individually: an inner output lies in V^1, and any outer bracket with that input is zero. This proves the identities with the stated grading, rather than importing an associativity convention from the triangle variables.

In particular b3 is NOT compensating a nonzero b2-composition here. The quadratic composition already vanishes by type, and lambda is an independent source coupling. Deleting b3 would leave an algebra satisfying the identities but change the source equation and amplitudes.

### Propagator recursion and comparison

On internal off-pole momentum sectors use h=K^-1 from equation degree to field degree, with h zero on fields. There b1 h+h b1=id. This is a local algebraic contraction away from K=0, not a global contraction of the physical on-shell complex. Write phi=phi_free+J with K phi_free=0 and solve formally

\[
J=h\left(\frac g2(\phi_{\rm free}+J)^2+\frac\lambda6(\phi_{\rm free}+J)^3\right).
\]

Polarize in distinct external source labels. The permutations of two or three distinct child blocks cancel the 2! or 3!, so each unordered partition supplies respectively a cubic vertex g or a quartic vertex lambda. Apply h at every non-root internal branch and amputate the root. This is the source equation's tree recursion. It does not require division by g and remains meaningful in the pure quartic limit.

At four points it gives the full labelled tree sum g^2(1/s+1/t+1/u)+lambda. The specified planar subset retains two exchange channels. At six points it gives 105 cubic trees, 105 one-quartic trees and 10 two-quartic trees. Selecting contiguous internal channels leaves 14,21,3. The checker matches every planar denominator set and its coupling monomial to the independent source-dissection enumeration, not just these counts. The common -i convention and A3=g are unchanged.

## Disposition

A separately action-derived homotopy formulation exists and reproduces the source tree contributions exactly. The measured triangle-weight quadric defect nevertheless remains nonzero in the prior refinement. The algebra's identities are nested maps on fields and equations; the defect is a polynomial in coefficients of a chosen graph presentation. No comparison turning that polynomial into a b1-boundary has been constructed, and the identities above neither require nor supply one.

Thus this bounded investment passes the formulation/amplitude test and fails to establish the proposed explanatory bridge. There is no derived next cubic coherence failure in this construction. Stop elaborating this interpretation until a separately justified multiplicative comparison identifies the particular defect. Do not set h(Q) by fiat: h acts on typed equations, not arbitrary weight polynomials, and its off-pole domain matters.

The surviving explanation remains that quartic contact information is independent of cubic triangle weights. This does not rule out richer source-derived BV or other formulations, but it gives no reason to invoke one merely to repair this presentation. The already admitted correlated-allocation test is a distinct executable rival, not a homotopy promotion.

Verification: checkers/check_scalar_source_homotopy.py and results/scalar_source_homotopy.json. Exact source derivative and tree matching pass; the nonzero quadric is deliberately retained as a control. Git prohibition remains active; no Git operations occurred.
