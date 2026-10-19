# Global iteration 31: eightfold cycle mechanism and corrected secant candidate

## Scoped result, not an algebraic witness

The external research report prompted a fresh primary-source check. Schoen supplies a genuine dimension-eight cycle mechanism **conditional on realizing the appropriate generalized Prym**. Independently, the displayed higher-dimensional secant character in Markman's survey has an arithmetic discrepancy: changing the displayed Theta twist to 3Theta repairs its claimed secant-plane membership. Neither fact supplies a target cover, a transformed sheaf with proved semiregularity, or an exceptional algebraic cycle on our fixed target.

The fixed sixfold X, alpha=R6, auxiliary A and principal Y2 remain unchanged. Earlier scoped exclusions, the conditional polarized bielliptic census0/0, the unpolarized comparison516/258, determinant48i and all four exceptional channels are retained. Three unrestricted research obligations remain open.

## 1. Schoen's theorem is not restricted to sixfolds

Fresh retained primary PDF: C. Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Mathematica65 (1988), 3-32, https://www.numdam.org/article/CM_1988__65_1_3_0.pdf.

Theorem2.0, printed p11, assumes even primitive-character multiplicity h and a simple branch tuple (branch characters paired with their negatives). The unramified case satisfies simplicity. Corollary3.1, printed p24, transfers the algebraic determinant-character space to the primitive abelian factor of the Jacobian. For m=4, h=8, this is a codimension-four cycle mechanism on an eightfold. The written source theorem is an imported mathematical result, not a theorem proved by our arithmetic checker.

For an etale genus17/9/5 cyclic tower, h=8. The missing input is an actual compatible realization/isogeny/correspondence with the target and a verified cycle transfer. The particular principal model Y2 is not the only allowable presentation problem. Signature, determinant or a formal Hodge tensor alone do not establish target matching.

An additional ramified search has a genus-four bottom and branch monodromies1,3. Riemann-Hurwitz gives genera16/8/4, with two ramification points in the top double cover and primitive Prym dimension8. The inverse branch pair supplies the same simplicity condition. These are necessary numerical data for a proposed presentation, not a constructed cover matching Y2. Previous etale genus-nine low-gonality exclusions must not be silently applied to its genus-eight intermediate.

The external report also identifies Lange-Ortega arXiv:1902.00251 and Schoen's addendum. Their further statements are pending primary verification here; they are not imported by this node. A Prym-preserving transformation does not automatically transport an order-four action on covering curves.

## 2. Independent secant-character correction

Fresh retained primary PDF: E. Markman, arXiv:2509.23403v2, section12, PDF pp21-22. The source displays [O -> nu_*O_Ztilde] tensor O(Theta) and claims its character lies in span(exp(sqrt(-d)*t),exp(-sqrt(-d)*t)). It explicitly leaves the proposed weaker deformation criterion unverified. Question11.4 on PDF p20 is not a theorem.

Use the stated generic incidence/partial-normalization geometry on a principally polarized fourfold, t=[Theta], n=(d+9)/2, N=(d+9)(2d-1). The rank-one K-class convention is [O]-[nu_*O_Ztilde]. Inclusion-exclusion has n surfaces, n adjacent curve intersections, n(n-3)/2 nonadjacent pair intersections and n consecutive triple intersections. Since t^4=24[point],

    ch(O_Z)=n*t^2-2n*t^3+n*(55-6n)*t^4/12,
    ch(nu_*O_Ztilde)=n*t^2-2n*t^3+n*(18-n)*t^4/6.

The second identity adds N point classes at the normalized isolated ordinary double points. Therefore the displayed Theta twist has ch2=-(d+8)t^2/2 instead of the required -d*t^2/2. The 3Theta twist gives

    ch(F3)=1+3t-d*t^2/2-d*t^3/2+d^2*t^4/24.

For s^2=-d this equals ((1+3/s)/2)exp(s*t)+((1-3/s)/2)exp(-s*t) through top degree. The checker verifies this by exact rational arithmetic for20 odd parameters and rejects both the displayed twist and omission of the normalization contribution. These finite controls accompany the polynomial identity above; they are not a proof of geometric incidence or deformation.

For d=9 the field is Q(i), n=9, N=306, and

    ch(F3)=1+3t-(9/2)t^2-(9/2)t^3+(27/8)t^4.

This is an independently checked arithmetic correction, **not an author-confirmed erratum**. The candidate is a derived object; a repaired character neither proves properties of its Orlov transform nor supplies an actual sheaf deforming to the target. A valid semiregularity/deformation theorem and its hypotheses remain missing. The old split-sixfold theorem is still not applied to a nonsplit sixfold or to an eightfold.

## 3. Revised executable research queue

1. **Corrected secant:** verify/freeze generic incidence and partial-normalization geometry for d=9; construct the transformed object, compute the actual obstruction maps, and establish a valid deformation argument. Do not promote Question11.4 to a theorem.
2. **Generalized Prym matching:** seek a concrete K-equivariant isogeny or effective correspondence from an appropriate etale or ramified cyclic-quartic primitive Prym. Specify the period/lattice/K-action and verify the cycle-class transfer and exceptional channels. Elliptic theta degrees need not survive arbitrary isogenies.
3. **Pending sources:** verify the Lange-Ortega branch-position/polarization hypotheses and Schoen's addendum, then separately test cyclic-action compatibility.

The existing tetragonal/sextic joint-pencil idea, actual theta computation and direct non-divisor sheaf/threefold geometry on X remain alternatives. The current Y2 already has an actual integral polarized Gaussian automorphism by its Gaussian-stable lattice construction; this prerequisite is not a new obstruction or a curve realization.

## Artifacts and trust

Contract: `research/conjecture_net/contracts/hodge-eightfold-literature-audit.v1.json`.
Checker: `research/voevodsky/checkers/check_hodge_eightfold_literature_audit.py`.
Receipt: `research/voevodsky/results/hodge-eightfold-literature-audit-v1.json`.
Sources: `research/voevodsky/inputs/hodge-eightfold-literature-v1/sources.json`.

    python research/voevodsky/checkers/check_hodge_eightfold_literature_audit.py

Source PDFs/text and their hashes are retained; the checker validates freshness, exact Chern arithmetic, ramification arithmetic and non-promotion boundaries. It does not formally verify Schoen's theorem or geometric/deformation claims. Historical iteration30 and pins v1-v32 are preserved. No Hodge verdict, exceptional target cycle, all-cycle theorem or independent review is supplied.
