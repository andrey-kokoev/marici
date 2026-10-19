# Local four-photon Ward/Bose tensor basis through degree four

## Question and scope

Can EF-WB4 start from a genuine covariant multilinear tensor rather than forward amplitudes, without erasing its three forward-invisible local directions?

[Contract](contracts/photon-local-ward-basis-v1.json) · [checker](checkers/check_photon_local_ward_basis_v1.py) · [tests](checkers/test_photon_local_ward_basis_v1.py) · [receipt](results/photon-local-ward-basis-v1.json). The active SCC obligation is forward realization in an explicitly imported photon EFT, then forward readout restriction. No native spacetime or scattering law is derived.

The candidate is an eight-generator local tensor jet through Mandelstam degree four. Rivals are a scalar parametrization with no Ward lift, loss of the single-minus sector, and Ward-compatible terms that fail Bose symmetry. The predicted test is full coefficient rank eight but forward-jet rank five. Removing h3 must leave forward data unchanged while destroying a nonzero off-forward helicity response. A one-pair f2 term must remain Ward but violate Bose symmetry. The result below constructs the local basis and survives these tests; the nonlocal loop and window lifts are not part of this result.

## 1. Source conventions and full multilinear construction

Use four null all-in momenta with sum zero. Write q_i=p_i.sigma and e_i=epsilon_i.sigma/sqrt(2), and E=[[0,1],[-1,0]]. Contractions are complex bilinear, not Hermitian probability pairings. Define

    F_i^+ = sym(q_i E e_i^T),
    F_i^- = sym(q_i^T E e_i),
    D(F)=E F E^T,     C(F,G)=sum_ab F_ab D(G)_ab.

For helicity plus choose e_i=lambda_i*rtilde_i^T/[tilde_lambda_i rtilde_i]; for minus choose e_i=r_i*tilde_lambda_i^T/<lambda_i r_i>. These give respectively (F_i^+,F_i^-)=(lambda_i lambda_i^T,0) and (0,tilde_lambda_i tilde_lambda_i^T). Our angle and square brackets denote lambda and tilde-lambda determinants respectively (the source's plub and minb pairings); helicity plus carries lambda. This fixes amplitude normalization; it does not identify the coefficients with Feynman-rule Lagrangian coefficients. The paper's in/out map and structures are recorded in the [attributed primary excerpt](sources/photon-scattering-2024-local-spinor-excerpt.tex), equations (B.88)-(B.112), from the already pinned author source.

For each unordered pair I={i,j} and complement {k,l}, put

    sij=det(q_i+q_j),
    x_I=(sij+skl)/2,
    w_I=(sik*sil+sjk*sjl+ski*skj+sli*slj)/4,
    S2=(1/2)*sum_(i<j) sij^2,
    P_I=C(F_i^+,F_j^+)*C(F_k^-,F_l^-).

On momentum conservation x_I is the pair invariant and w_I is the product of its two crossed invariants. The symmetric definitions avoid choosing a labelled endpoint. Sum P_I over all six size-two subsets. Weights 1, x_I, x_I^2 and w_I define G2, G3, G4 and G4prime.

For F2 sum, over the three pairings, C(F_i^+,F_j^+)*C(F_k^+,F_l^+) plus its parity partner. Weight each pairing by x_I/3 to obtain F3; define F4=S2*F2. The factor 1/3 follows from s^3+t^3+u^3=3stu, not from fitting a forward value.

The single-minority-helicity covariant is essential. For distinct i,j,k,m define

    H(i;j,k|m)=F_i^+ : [D(F_j^+) q_i D(F_m^-) (D(F_k^+) q_i)^T],

where colon is the entrywise bilinear matrix pairing. Define H3=(1/3)*sum_(m,i!=m) H(i;j,k|m) plus the parity-transformed expression (F^+<->F^-, q_i<->q_i^T); j,k are the two remaining labels. For pure three-plus/one-minus input this contracts to ([mi]<ij><ik>)^2 in the declared bracket notation, and agrees with the source's single-minus structure. This is a polynomial contraction, not division by stu.

Contracting momentum conservation gives sum_r <jr>[rm]=0, which identifies the three H anchor expressions on shell. On a generic four-point patch, chiral pair products equal chi*x_I^2 with a common little-group phase chi (the phase identity accompanying source (B.89)); hence the F3 projection is chi*stu. The construction itself has no such ratios, so these polynomial identities extend to degenerate momenta without dividing there.

The full local amplitude is the coefficient combination of (G2,F2,G3,F3,H3,G4,G4prime,F4). It is linear in each of the four polarizations. Thus it defines an uncontracted four-vector tensor by evaluation on four matrix-unit polarization bases. The checker constructs all 256 components for each of eight generators at one exact momentum configuration; it checks 2048 component Ward constraints there, not merely selected helicity zeros.

## 2. Algebraic Ward, Lorentz and Bose arguments

For any 2x2 q, q E q^T=det(q)*E is antisymmetric. Hence F^+(q,q)=F^-(q,q)=0. Every term contains exactly one field strength from each external leg, so replacing any polarization by its momentum kills the full multilinear form. A reference-spinor change adds a multiple of q and therefore does not change it.

Under q,e -> L(q,e)R^T with det(L)=det(R)=1, F^+ -> L F^+ L^T and F^- -> R F^- R^T. All spinor indices in C and H are contracted with the invariant E; the determinants and weights are scalars. This proves complexified Lorentz covariance and hence its real Lorentz restriction within the imported spinor framework.

The G sum runs over all six subsets, the F sum over all three pairings, and the H sum over every minority/anchor pair. The weights are invariant under reordering either pair or interchanging its complement. H(i;j,k|m) is symmetric in j,k because its two field-strength matrices are symmetric. Consequently external permutations permute complete summands; the included parity partners give parity invariance. These are algebraic arguments for the polynomial forms, not general conclusions inferred from positive samples. They are documented mathematics, not machine-formalized proofs.

## 3. Source helicities, rank and the noncollapsed kernel

On shell, the local CM projections are exactly

    Phi1 = g2*s^2+g3*s^3+g4*s^4+g4prime*s^2*t*u,
    Phi2 = f2*(s^2+t^2+u^2)+f3*s*t*u+f4*(s^2+t^2+u^2)^2,
    Phi3 = Phi1(u,t,s),     Phi4 = Phi1(t,s,u),
    Phi5 = h3*s*t*u.

Here all coefficient symbols are photon EFT matching parameters, not the earlier Dirac-current g2/g3. Four exact CM configurations, including forward and backward limits, test all 16 helicities against a separate spinor polynomial evaluator. Additional controls test gauge patches, permutations, Lorentz transforms, parity and homogeneous scaling. Momentum polynomials have no kinematic denominators; polarization reference charts do not introduce amplitude poles.

For coefficient order (g2,f2,g3,f3,h3,g4,g4prime,f4), the derived forward jet with rows (Phi1_s2,Phi1_s3,Phi1_s4,Phi2_s2,Phi2_s4) is

    [1 0 0 0 0 0 0 0]
    [0 0 1 0 0 0 0 0]
    [0 0 0 0 0 1 0 0]
    [0 2 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 4].

Its rank is five and its kernel is exactly span(f3,h3,g4prime). This is a formal forward JET rank, not the rank of a helicity matrix at a single energy. At fixed momenta the eight parameter responses need not be independent. Across the explicitly retained kinematic evaluations an exact eight-row witness has rank eight, proving independence of these eight momentum-polynomial generators. Their completeness is relative to the sourced on-shell local jet (1.6), not an independent exhaustion of all off-shell operators.

At s=1,t=-16/25,u=-9/25, the rows (Phi2,Phi5,Phi1) restricted to columns (f3,h3,g4prime) form (144/625)*I3. Thus each invisible forward direction survives off forward. Dropping h3 keeps the entire forward map but lowers the full witness rank to seven. A Ward-compatible one-pair f2 alternative has a Bose-permutation defect 369/625. Neither error can be cured by a normalization change.

## Claim boundary and disposition

Established: explicit local covariant tensor generators with algebraic Ward/Bose/Lorentz arguments, all-helicity controls, an eight-dimensional coefficient-polynomial witness, and the rank-five forward restriction with its nonzero three-dimensional kernel. Local coefficients are retained, not selected.

Still open in EF-WB4: add the independently verified degree-four logarithmic form factors to the full tensor, reproduce every channel cut without spurious rational kinematic poles, and lift/compare the whole-window analytic shift in two variables. Local polynomial analyticity does not establish joint analyticity of the full loop amplitude. No UV completion, physical coupling selection, native preparation or rate is inferred. C1–C12, the exhausted C12 budget and high-energy pause are unchanged.

```text
python -S research/nima/checkers/check_photon_local_ward_basis_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_local_ward_basis_v1.py
```
