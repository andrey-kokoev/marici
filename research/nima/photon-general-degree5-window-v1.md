# General degree-five photon log/window lift and single-minus scale transport

## Question and bounded result

Can all six coordinates of the general degree-two/degree-three Born cut be lifted regularly without losing the induced single-minus response or identifying source directions hidden by the cut readout?

[Contract](contracts/photon-general-degree5-window-v1.json) · [checker](checkers/check_photon_general_degree5_window_v1.py) · [tests](checkers/test_photon_general_degree5_window_v1.py) · [receipt](results/photon-general-degree5-window-v1.json).

**Yes in the declared real parity-even photon-contact stratum.** A covariant polynomial-times-log representative matches all channel/helicity coefficients, restricts exactly to the R-family tensor, and admits an exact forward Cauchy window extension with a derived two-variable analytic difference. The h5 scale direction is generally nonzero. Neither physical finite matching nor a full physical IR inventory is selected.

## 1. Six source coordinates, regular channel tensors

Use the [general cut](photon-general-degree5-cut-v1.md) and [twelve local generators](photon-local-degree5-v1.md). Keep source order

    m=(g2*g3,g2*f3,g2*h3,f2*g3,f2*f3,f2*h3).

These are products of five real leading Born couplings, not six independent physical parameters. Define

    a=m0/16+m4/60, b=m4/240,
    o=-m1/96-5*m3/48, h=-m2/80-m5/480.

With the previous chiral pair products P_I, symmetric pair invariants x_I and crossed products w_I, the mixed-chirality part of pi^2*M5_log is

    sum_I P_I*[-(a*x_I^3+b*x_I*w_I)*ell_I
                +(m0/96)*sum_(u in I,v in complement I) suv^3*ell_(uv|complement uv)].

Here ell_x=Log(-rho*x), rho>0, with upper positive rim log(rho*x)-i*pi. The other two helicity sectors are

    o*[(F4/4)*sum_x x*ell_x+(F5/2)*sum_x ell_x+F3*sum_x x^2*ell_x],
    h*H3*sum_x x^2*ell_x.

The final line is the new single-minus sector. Its s-log coefficient is h*H3*s^2, giving pi*Im Phi5=-h*s^3*t*u, exactly the coupled Bose-cut result. It is not inferred from the restricted R-family zero.

Every channel coefficient is polynomial in momenta and polarizations, with constant rational denominators only. There is no division by s, t, u or S2. Field strengths give Ward identities; complete subset sums and common scalar branches give Bose/parity covariance; invariant spinor contractions give Lorentz covariance. The all-same-helicity formula follows from x^5=(S2^2/4)*x+(S2*stu/2)+stu*x^2. These are documented algebraic arguments, not machine-formalized proofs or native dynamics.

## 2. Complete common-log transport, including H5

Holding leading couplings fixed and shifting every ell_x by delta gives

    pi^2*Delta M5 = delta*[
        -(m0/12+m4/60)*G5
        +(m0/16-m4/240)*G5prime
        -(5*m1/192+25*m3/96)*F5
        -(m2/80+m5/480)*H5 ].

In particular the single-minus coefficient is

    -h3*(6*g2+f2)/480.

A fixed total amplitude requires the opposite compensating local shift divided by pi^2. No integration constant or numerical h5 is thereby selected. H5 is forward invisible, so forward matching alone cannot recover this direction.

The four-by-six transport map has rank four and precisely the same two-dimensional bookkeeping kernel as the cut. The checker verifies the identity on all 256 polarization matrix-unit tuples. Dotting every channel coefficient with either kernel vector vanishes, but the Born source variables are still retained. Separately, the local twelve-coefficient jet has a six-dimensional **forward-matching** kernel. These are different spaces and must not be conflated.

The R-family weights (1/16,-3/16,0,-1/16,3/16,0) give the previous scalar coefficients (-1/120,1/320,65/3072,0) exactly, including all tensor components and the window shifts. There is no refitted normalization or extra coupling-strength factor.

## 3. General Cauchy window and analytic difference

Let

    U=m0/24+m4/60, V=m0/12+m4/60, W=m1/96+5*m3/48.

The minimal forward-visible lower extension is

    J_tau=(tau^3/3)*(U*G2+W*F2)
          +(tau^2/2)*V*G3+tau*(U*G4+(W/2)*F4).

Its unfixed forward-invisible additions are a representative choice, not forbidden interactions. Set

    pi^2*D5_lift=sum_x C_x*[ell_x-Log(1-x/tau)-log(rho*tau)]+J_tau.

With all-in conserved null momenta, physical forward coefficients obey C_u=-Gamma(C_s). Degree-five polynomial division and the two rims show that this restricts to the entire prescribed twice-subtracted Cauchy representative for each source coordinate, not merely its cut. The h3 monomials have zero physical forward cut but nonzero off-forward channel coefficients; their window extension remains explicit.

Subtracting M5_log yields

    pi^2*(D5_lift-M5_log)
      =J_tau-log(rho*tau)*(the four-generator transport above)
        +sum_(n>=1,x) C_x*x^n/(n*tau^n).

The series begins at degree six. For u=-s-t and |s|,|t|<=a with 2a<tau, it converges absolutely and uniformly in two complex variables. Polynomial coefficients preserve holomorphy; on compact covariant momentum/polarization charts the same argument applies to pair invariants. The unsubtracted threshold-log amplitude is not analytic at zero.

A conservative bound on the coupling-coordinate l1 coefficients of each source helicity scalar is K*r^5, with K=11/32 and r=2a. The generated tail after degree N>=5 is bounded by

    K*r^5*(r/tau)^(N-4)/[(N-4)*(1-r/tau)].

This is not a bound on unknown matching, arbitrary boosted tensor components, all-order amplitudes or an unretained IR spectrum. The artificial endpoint is not a physical threshold.

## 4. Verification and next question

Controls cover all 16 helicities at four CM configurations, every retained channel coordinate, 72 Bose permutations, 4608 scalar component Ward constraints, 256 full-component scale and R-restriction comparisons, exact source-kernel annihilation, and per-coordinate forward Cauchy division/series/rim checks. Eight tests, scoped SCC and fresh headless closure accompany the stored receipt. Identity/analytic derivations remain documented mathematics, not a proof-assistant certificate.

This completes the scoped general quadratic degree-five log/window lift, with twelve local matching coefficients still free. C1–C12 dispositions and C12's exhausted budget are unchanged. Native preparation, physical matching and global UV assumptions are not derived.

A distinct next question is source identifiability from **joint** degree-four and degree-five cuts. The linear six-monomial kernel cannot answer it by itself: the products obey source factorization constraints. Classify actual five-coupling fibres modulo the global sign, retaining zero-leading and single-minus-cancellation strata before claiming an inverse. See the [current frontier](photon-eft-frontier-v2.md).

```text
python -S research/nima/checkers/check_photon_general_degree5_window_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_general_degree5_window_v1.py
```
