# A positive cubic radius and a sharp common-ray cut modulus

## Result, extra hypothesis and open scope

[Contract](contracts/photon-common-ray-modulus-v1.json) · [checker](checkers/check_photon_common_ray_modulus_v1.py) · [tests](checkers/test_photon_common_ray_modulus_v1.py) · [receipt](results/photon-common-ray-modulus-v1.json).

There is a **quartic-free positive cubic-radius observable for every leading direction**, not just the exact axis. It gives a universal single-source cut-magnitude bound at zero transport. Using this observable, compared source pairs on an **exact common leading ray** with a positive normalized leading single-minus trace have a uniform half-power cut modulus, retaining arbitrary h3 and all quartics. The half-power exponent is sharp uniformly over this paired-ray domain, even on a positive-discriminant-margin subset.

This is an explicit scoped improvement with an additional pairwise common-ray hypothesis. It does **not** settle the original double-margin question for arbitrary sources on different leading rays. A common ray is not inferred from approximate collinearity or a physical branch convention. The source box, ray condition and margin are conditional mathematical assumptions; no native/UV/physical matching is licensed. All eighteen finite local matching directions remain free.

The domain remains the imported real parity-even eight-leading-contact photon model and retained quadratic two-photon degree-six order, with the same normalized joint13/cut13 max norms.

## 1. General positive cubic-radius observable

Let n=(n_g,n_f) be a unit vector parallel to a nonzero leading pair, and c=(p,q,h)=(g3,f3,h3). For zero leading pair any unit n may be used. Write B for the six common-log coefficients and define

    Wg=(0,49/8,49/4,0,0,0),
    Wf=(2,83/4,409/12,0,0,0),
    Wc=(0,0,0,274/3,-131/18,0),
    I_n(B)=(n_g^2*Wg+n_f^2*Wf+n_g*n_f*Wc) dot B.

Then **all three quartic nuisance contacts cancel identically**, and

    I_n(B)=c^T P(n)c,
    P_pp=7*n_g^2/256+989*n_f^2/8064,
    P_qq=49*n_g^2/7680+5*n_f^2/256,
    P_pq=P_qp=-n_g*n_f/192,
    P_hh=49*n_g^2/640-11*n_g*n_f/40+203*n_f^2/720,
    P_ph=P_qh=0.

The checker proves the quartic cancellations coefficientwise as twelve polynomial constraints in n_g,n_f and verifies all eighteen cubic coefficient identities. It does not simply test a few ray samples. No kinematic denominator or source coupling is fitted to create the cancellation.

Uniformly on the unit circle,

    c0*Id <= P(n) <= Id,  c0=49/7680,
    |I_n(B)-I_n(B')| <= K*||B-B'||,  K=3821/36.

For the p/q block, use |n_g*n_f*p*q|/96<=(n_g^2*p^2+n_f^2*q^2)/192 and compare the remaining coefficients with c0. The h block is a quadratic form in n with determinant 247/92160 and trace 413/1152; determinant/trace>c0 and trace<1. The p/q block trace is also below one. The data gain follows from |n_g*n_f|<=1/2 and the displayed row norms. These exact rational certificates retain the independent h3 mode.

### Universal single-source corollary, without a box or trace margin

For any actual real source, choose n along its leading pair (or any n at zero leading pair). Then

    p^2+q^2+h^2 <=(K/c0)*||B||.

The fixed-M3 cut map has gain 13/3 and its missing coordinate contributes p^2/224. Consequently

    ||C|| <= A*||B||,  A=13/3+K/(224*c0)=80879/1029.

No quartic-source bound is needed for this single-source inequality. It quantitatively strengthens zero-transport/zero-cut equivalence in the declared model. It is **not** the false pairwise inequality ||C_X-C_Y||<=A*||B_X-B_Y||: a difference of source-product vectors need not factor. The earlier equal-transport and unbounded-image examples are consistent with this zero-based magnitude bound. It selects no physical source or native prior.

## 2. Exact common-ray pair domain

Let X,Y lie in the conditional eight-source box of radius M>=1. Require their leading vectors to be collinear; after an entire-source common-sign reversal in the proof, write them r_X*n,r_Y*n with r_i>=0. When a leading vector is nonzero require

    |6*n_g+n_f|>=eta,  0<eta<=1.

Both zero-leading sources are admitted without choosing n. A pair with exactly one zero leading vector is admitted when the other's ray satisfies the trace margin. Zero cubic pairs and cubic single-minus cancellation 10*p+q=0 are not discarded. No discriminant margin is needed for the upper estimate because the exact common ray is supplied; that is stronger information than a discriminant margin alone.

Put m=min(eta,1/15). With delta the full joint-data gap, define

    A=80879/1029,
    B_M_eta=M/(14*c0*m).

Then for all delta>=0,

    cut gap <=min((2713/3360)*M^2, A*delta+B_M_eta*sqrt(delta)).

For delta<=1 this is a Holder-1/2 bound with coefficient A+B_M_eta. It is uniform over eligible common rays, not an assertion that every ray separately has an optimal half-power exponent. The square root is enclosed by exact rational arithmetic in the implementation.

## 3. Quantitative proof

For a fixed common n the lower degree-five vector satisfies

    (u,v,w,z)^T=r*A_n*c,
    A_n=[[n_g,0,0],[0,n_f,0],[10*n_f,n_g,0],[0,0,6*n_g+n_f]].

The p/q block has smallest singular value at least 1/15 by its determinant and trace; the h block is bounded below by eta. Hence the full smallest singular value is at least m. Use the transformed cubic vector V=P(n)^(1/2)*c, whose norm is at most 2*M. A fixed left inverse of A_n gives a transformed measured vector r*V with pairwise gap at most 2*delta/m. The measured squared radius is I_n(B), with gap at most K*delta. No explicit numerical matrix square root is needed for the proof.

Let r=max(r_X,r_Y). If r>=2*sqrt(delta), the other radius is at least r/2: the two leading squared norms differ by at most 2*delta, since both diagonal Gram entries are measured. Normalizing the transformed measured vectors as in the axis argument, and writing p as a linear functional of V with squared norm at most 1/c0, gives

    |p_X^2-p_Y^2| <=[K*delta+32*M*delta/(m*r)]/c0.

This handles a zero transformed cubic vector by its radius difference, rather than dividing by zero. The augmented cut inverse therefore gives

    cut gap <=A*delta+M*delta/(7*c0*m*r)
             <=A*delta+B_M_eta*sqrt(delta).

If r<=2*sqrt(delta), the general surrogate-bias identity gives

    cut gap <=(13/3)*delta+(229/8400)*M*r
             <=(13/3)*delta+(229/4200)*M*sqrt(delta).

Because m<=1/15, B_M_eta is larger than that last square-root coefficient. This covers all zero-leading cases. At delta=0 exact joint-data reconstruction supplies equality of the cuts. The source-box diameter cap completes the estimate.

These are documented real spectral and norm arguments with exact rational coefficient certificates, not proof-assistant formalizations or physical noise estimates.

## 4. Sharpness, retained modes and the remaining cross-ray problem

The earlier bounded axis family is a common-ray family with leading trace margin six and normalized discriminant margin at least 23/37. Its data gap is of order r^2 and cut gap of order r. Thus no uniform exponent above one-half is possible in the present paired-ray class, even if both normalized margins at least 1/2 are also imposed (eta<=1). All quartics are bounded; this is not the unbounded counterexample. The axis proof is now one instance, rather than the only known ray.

The full-box one-third family changes leading rays and is excluded by exact collinearity. The margin-only h3 counterexample has the common cancelled ray f2=-6*g2 and is excluded by the explicit trace margin. Neither exclusion is a physical prior or permission to set a small field to zero. Checkers reject a tiny noncollinearity and an exactly cancelled trace.

There are 3240 positive-radius/coercivity controls over five rays, including the cancelled ray for the identity alone; 64 paired-ray cut controls; an explicit cubic-trace-zero control; and four positive-discriminant sharpness pairs. Eight tests, scoped SCC and a fresh headless receipt accompany them. No fresh full-suite or native scientific-evidence claim is made.

The general double-margin problem **remains open for pairs on different rays**. The positive radius is now available, but its observable coefficients vary with n, so they may not be held fixed across such a comparison. Next control that variation using the supplied discriminant/leading-trace margins, or construct an exact bounded counterexample satisfying both. All native source-box/ray/margin/noise licensing, physical matching and UV inputs remain unearned. C1–C12 and C12's exhausted budget are unchanged. See [frontier v4](photon-eft-frontier-v4.md).

```text
python -S research/nima/checkers/check_photon_common_ray_modulus_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_common_ray_modulus_v1.py
```
