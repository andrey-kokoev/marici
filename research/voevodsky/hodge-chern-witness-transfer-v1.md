# Global iteration 12 (new series 2/10): normalized higher-Chern witness transfer

## Result

The previous turn identified all 14 middle Hodge directions of A=X x B, with an eight-dimensional exceptional sector and a complete four-channel cycle test. Here we audit the actual higher-Chern route rather than presume that normalization in dimension eight behaves like normalization on X.

For an algebraic bundle G of rank n on X, and an algebraic line bundle M on B with c1(M)=D1, put

    H=(pX*G tensor pB*M) direct_sum O_A.

If w=P6 kappa3(G) is nonzero, then

    Pi_exc kappa4(H)=(w external D1)/(n+1).

This is a licensed construction from a **supplied** bundle, not a construction of the missing G. Tensoring alone gives zero exceptional normalized fourth class. The direct sum is essential; normalization is not additive.

Consequently alpha algebraic is equivalent to existence of an algebraic bundle on A with nonzero exceptional normalized fourth Chern class. Neither existence nor nonexistence has been decided. The old rank-two P8 filter kills the displayed D1-transfer sector, so the full four-channel test is necessary for this construction.

We also construct a genuine rank-two reflexive sheaf control on the fixed X with nonzero kappa3, but with zero Weil projection. This prevents confusing bundle rank bounds with rank bounds on singular sheaves.

## 1. Newton identities and normalization at the actual targets

For any positive-rank bundle V of rank r define

    kappa(V)=ch(V) exp(-c1(V)/r).

No root of the determinant line bundle is being asserted: the exponential defines rational characteristic classes. In degrees three and four Newton's identities give

    ch3=(c1^3-3c1 c2+3c3)/6,
    ch4=(c1^4-4c1^2 c2+2c2^2+4c1 c3-4c4)/24,

    kappa3=ch3-(c1/r)ch2+c1^3/(3r^2),
    kappa4=ch4-(c1/r)ch3+(c1^2/(2r^2))ch2-c1^4/(8r^3).

These are identities in the rational Chow ring and its cohomology image. On the fixed X, c1 is proportional to E_X, and P6 kills E_X times any degree-four class. Therefore

    P6 kappa3(V)=P6 ch3(V)=P6 c3(V)/2.

On the fixed A, every rational Hodge class of codimensions one and two is divisor-generated, by the full Hodge table proved previously. Thus every expression using only c1,c2 is in the divisor sector. The exceptional degree-four formula is

    Pi_exc kappa4(V)
      =(r-3)/(6r) Pi_exc(c1(V)c3(V)) - Pi_exc(c4(V))/6.

Unlike on X, normalization can erase the sought component: c1*c3 can itself have a nonzero exceptional part on A. It is invalid to replace projected kappa4 by projected ch4 without checking that term.

The checker implements the Newton and exponential expressions in the weighted polynomial ring Q[c1,c2,c3,c4], truncated only above codimension four. It runs exact rank controls 1 through 16. The displayed symbolic derivation supplies the all-rank identity, not the finite list.

## 2. Necessary locally free rank bounds, not existence or optimality claims

For a locally free sheaf, c_j=0 for j greater than its rank. Hence:

- On X, every rank-one or rank-two bundle has kappa3=0. A nonzero projected third-Chern bundle witness must have rank at least three.
- For a locally free sheaf of rank at most three, the normalized Newton identities give

      kappa4=kappa2^2/12.

  For rank one both sides vanish. On the fixed A, kappa2 is divisor-generated, so every such bundle has Pi_exc kappa4=0. An exceptional normalized-fourth bundle witness must have rank at least four.

The second rank restriction is about normalized fourth data, not raw ch4. The rank-three formula allows an exceptional raw fourth component coming from c1*c3, even though normalization cancels it. No actual example with that component on the fixed A is asserted.

These are necessary bounds. We do not prove that a rank-three witness on X or a rank-four witness on A exists, even conditionally on alpha algebraic with an arbitrary unbounded-rank bundle realization. We also do not infer c_j=0 for j greater than the rank of an arbitrary coherent or reflexive sheaf.

## 3. A genuine rank-two reflexive control with nonzero third data

Choose an ample line bundle for the fixed polarization and take a sufficiently high tensor power L that is very ample. By Bertini, three general sections s1,s2,s3 have smooth nonempty codimension-three zero locus Z. Put t=c1(L). Define F using the initial part of the Koszul resolution:

    0 -> L^-3 --(s1,s2,s3)--> (L^-2)^3 -> F -> 0.

Signs and the ordering of the Koszul coordinates do not affect the calculation. The subsequent Koszul map embeds F in (L^-1)^3. Thus F is torsion-free of rank two. Outside Z one section is locally a unit, so F is locally free. At Z the source map is minimal and F requires three generators, so it is not locally free there.

At a point of Z the regular local ring has dimension at least three and F has projective dimension one. Auslander--Buchsbaum gives depth at least two. Together with local freeness away from Z, this gives S2; a torsion-free S2 sheaf on the smooth normal X is reflexive. Equivalently F is the relevant second syzygy in the Koszul resolution. These standard geometric facts license the sheaf; the checker does not numerically supply its sections.

Its characteristic classes follow from the actual resolution:

    ch(F)=3 exp(-2t)-exp(-3t),
    c1(F)=-3t, c2(F)=3t^2, c3(F)=t^3,
    kappa3(F)=t^3/2.

The normalized third class is nonzero, since L is ample. But t is a multiple of E_X, so its Weil projection is zero. This is an actual singular-sheaf control in the divisor sector, not a witness for alpha.

A related caution is the rank-one ideal sheaf I_Z. It is torsion-free but not reflexive here. Its Koszul character has rank one, c1=c2=0 and

    kappa3(I_Z)=ch3(I_Z)=-[Z]=-t^3.

Rank alone therefore does not justify a locally free Chern truncation. In particular the reflexive F above explicitly refutes extending the rank-two bundle kappa3-vanishing statement to arbitrary rank-two reflexive sheaves. It does not exhibit a rank-two reflexive Weil witness: this F still has zero Weil projection. It invalidates rank-based Chern truncation and leaves singular sheaf constructions with a non-divisor singular Chern class open.

The retained secant paper's rank-two source bundles live on a threefold, and its resulting target sheaf has a different rank and hypotheses. The present rank bounds do not reject that construction. Nor do they repair the previously proved discriminant mismatch for our X or the dimension mismatch for A.

## 4. Explicit conditional bundle transfer

Suppose a genuine algebraic bundle G on X is supplied with

    rank(G)=n, w=P6 kappa3(G) nonzero.

By the source rank bound n>=3. The full Hodge calculation on X says the only exceptional Chern-character component is its degree-three part w; every other even-degree Hodge class on X is a divisor power. Also

    E_X w=0.

This last identity is the primitive determinant support calculation: every native monomial of w already contains one coordinate from every native pair, whereas E_X adds both coordinates of a pair.

Let M=O_B(D1). Tensoring pX*G by pB*M leaves its normalized character equal to pX*kappa(G), so its exceptional fourth component is zero. It is not a witness transfer by itself.

Now add a trivial summand and write N=n+1:

    H=(pX*G tensor pB*M) direct_sum O_A,
    c1(H)=c1(G)+n D1,
    (ch3(H))_exceptional=w,
    (ch4(H))_exceptional=w external D1.

Here the degree-three exceptional part is W6 external 1; multiplying it by the X part of c1 contributes zero. All terms involving only ch1,ch2 are divisor-generated. Thus normalization gives

    Pi_exc kappa4(H)
      =w external D1 - (n/N) w external D1
      =(w external D1)/N.

This holds for every supplied G satisfying the hypotheses; it does not presume that an arbitrary formal Hodge character comes from a bundle. The four channels return w/N in channel zero and zero in the other three. In particular P8 alone kills this whole D1 sector despite its being an effective conditional witness transfer.

The checker uses six arbitrary formal source Hodge characters at ranks 3,4,5,8,16,32 to cross-check the coefficients, the failure of tensoring alone, the n+1 denominator and the four-channel output. Every such record is labelled **formal input only**. None is asserted to be an actual bundle at the specified X.

## 5. Existence equivalence and why it does not solve the positive gate

The prior sixfold resolution argument already proved

    alpha algebraic iff some algebraic bundle G on X
       has P6 kappa3(G) nonzero.

Forward construction above then gives an algebraic bundle H on A with nonzero Pi_exc kappa4(H). Conversely such an H has an actual rational algebraic normalized characteristic class, and a nonzero four-channel image gives alpha by the existing inverse. Consequently

    alpha algebraic iff some positive-rank algebraic bundle H on A
       has Pi_exc kappa4(H) nonzero.

One may additionally twist the supplied bundles by sufficiently ample line bundles to make them globally generated: kappa is unchanged under line-bundle twists. This is still a conditional operation, not a produced witness or a rank-four realization.

It would be wrong to derive the new equivalence by treating normalized kappa as additive along a resolution. It is not additive. The explicit direct-sum calculation is what supplies the missing license; the source existence argument used projected ch3 where the troublesome divisor correction vanishes.

## Disposition and artifacts

Constructed: rank-sensitive higher-Chern audit, a Bertini-Koszul-depth singular control, and the conditional bundle transfer. Not constructed: a bundle or singular sheaf with nonzero Weil component at the fixed point. All-cycle annihilation, the algebraicity branch and independent review remain open.

Next geometry must supply a genuine rank-at-least-three bundle on X, an appropriate singular reflexive sheaf whose Chern class has a Weil part, or a rank-at-least-four bundle on A with nonzero exceptional normalized fourth class. The rank bounds cannot exclude the singular sheaf route, and twists alone cannot produce the missing normalized class.

Contract: `research/conjecture_net/contracts/hodge-chern-witness-transfer.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_chern_witness_transfer.py`.
Receipt: `research/voevodsky/results/hodge-chern-witness-transfer-v1.json`.

    python research/voevodsky/checkers/check_hodge_chern_witness_transfer.py

The rational identities and exterior controls support the written proof. Bertini, Koszul exactness, depth/reflexivity and cycle/characteristic-class functoriality are imported standard mathematics, not proof-assistant certification. No fresh or exhaustive literature assertion is made, and no Hodge verdict follows from these checks.
