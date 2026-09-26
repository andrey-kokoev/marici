# Triangle normalization: continuation order is part of the source contract

## Source discovery

Freshly inspected `sections/cosmologicalintegrals.tex`, equations eq:mCM and eq:constant, in the frozen arXiv:2408.16386v2 source. The named coefficient c_(d,n_e,L) contains an explicit factor Vol(external simplex). It is NOT independent of external kinematics merely because its name displays only d,n_e,L.

Combine this with `sections/method.tex`, eq:ukchi:

    gamma=(d-n_s-L)/2,
    kappa0=c_(d,n_e,L) D^(-gamma),
    D=Vol^2(external simplex).

For n_s=3,L=1,d=3+2epsilon, the literal printed formulas imply

    gamma=-1/2+epsilon,
    c_(d,3,1)=C(d)*D^(1/2),
    kappa0=C(d)*D^(1-epsilon).

C(d) includes regulator-dependent constants; no epsilon→0 limit, phase convention or independent physical validation of this printed normalization is asserted. An owner/source normalization check is requested before treating it as a physical asymptotic.

## Two different parameter maps

The general source distinguishes site energies X_i from spatial invariants P_i. The applications section then restricts to one external state at each site and identifies |P_i| with X_i, reducing six scales to three.

There are now two DIFFERENT continuation problems:

1. Stay in that reduced family and set X3=E-X1-X2. The spatial external triangle degenerates with E.
2. Return to independent energies/spatial invariants and continue E while holding P_i fixed. Its external volume D stays fixed.

They cannot be interchanged silently. The first is a specified algebraic chart; the second is a different map in the larger source parameter space. Neither choice by itself supplies the intended physical continuation path/sheet or E0 relative chain.

## Exact external degeneration in the reduced chart

Write a=X1, b=X2, c=E-a-b. For the canonical external triangle with side-length parameters a,b,c, let H=16D. The Cayley–Menger determinant gives exactly

    H=E(E-2a)(E-2b)(2a+2b-E).

At generic a*b*(a+b)≠0,

    H=8ab(a+b)E + O(E^2).

Consequently, on a chosen local branch at fixed generic regulator, the displayed kappa0/E factor has order E^(-epsilon), not an automatic simple E pole. This statement is about that prefactor in that chart. If K and all remaining factors are regular and nonzero at a fixed generic integration point, they do not change this order; that hypothesis need NOT hold on the limiting physical support.

In the fixed-P continuation, this argument does not apply: D is fixed and the displayed1/E factor is not canceled by this external-volume dependence. Source selection of the continuation map is therefore essential to the purported residue constructor.

## Exact internal degeneration and support constraint

Use a canonical tetrahedron whose base edges are a,b,c and whose apex distances are r,s,t. This is the source simplex geometry up to labeling; no rational-denominator incidence dictionary or physical chain identification is inferred from this relabeling.

Set

    G=a^2+b^2-c^2,
    U=a^2+r^2-s^2,
    V=b^2+r^2-t^2,
    M=[[2a^2,G,U],[G,2b^2,V],[U,V,2r^2]],
    K=det(M)/288.

The exact degeneration is

    B=a*V+b*U,
    K|_(E=0)=-B^2/144.

For a real nonnegative-volume representative, a bounded limiting point must therefore lie on B=0. An unrestricted fixed-y coefficient calculation generally lies OFF that limiting support.

There is also an exact transverse identity:

    Hface=4a^2*r^2-U^2,
    C=2a^2*V-G*U,
    2a^2 det(M)=H*Hface-C^2.

On bounded real patches with the relevant face inequalities, a≠0 and H=O(E)>0, nonnegative K forces C^2≤H*Hface. Hence C=O(sqrt(E)), and since C|_(E=0)=2aB, the support approaches B=0 at a controlled transverse scale on such patches.

This is NOT a specialization theorem for the complex continued physical cycle. It does not control unbounded ends, pole intersections, regulator removal, phases or total period normalization. It identifies an actual source-geometric boundary layer that a valid completion map must account for, rather than importing the interval model's delta measure by analogy.

## Implication for the pilot

The next necessary choice is earlier than an interchange estimate: specify which source parameter map, normalization and cycle continuation define the desired observable boundary. Only then can one calculate a source-derived pullback density/Jacobian, test its transverse limit and determine whether a boundary contribution survives.

The primary source does state the general flat-space-amplitude expectation at total energy zero. That prose is not being refuted here. It does not alone provide the normalized target, chosen continuation or interchange construction for this particular reduced, regulated edge-weight period. The earlier amplitude-typing perimeter remains relevant at that specific interface.

Benincasa/Nima owner-input branch remains active. Ask explicitly whether the external-volume factor in c_(d,n_e,L) is intended in the active normalization and whether the intended E0 operation stays on the reduced family or lifts to independent energies at fixed spatial invariants.

## Verification boundary

`check_triangle_normalization.py` checks exact sparse rational polynomial identities for the external Cayley–Menger determinant, its generic leading coefficient, the internal Gram degeneration, the transverse identity and affine regulator exponents. All four inventoried source/checker files remained unchanged. Receipt: `triangle-normalization.json`.

The source reading, branch-dependent fractional-power valuation and positivity-based support argument are written mathematics, not a formalized analytic continuation theorem. No owner source was edited.
