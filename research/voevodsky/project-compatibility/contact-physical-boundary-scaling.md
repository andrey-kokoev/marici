# Contact infinity needs a physical momentum lift

## Fresh sources and declared slice

Read primary2401.05207 eq:CC3 and the definition x_s=sum of incident external energies, plus ledger2135's component poles and ledger2223's contact response. Restrict to the three-leg, one-external-leg-per-site momentum-conserving slice, not arbitrary valence. Use the already frozen massless spectral Gaussian source A(p)=|p|, whose normalized real-mode covariance is K(E)=1/(2E).

Let p1+p2+p3=0, Ei=|pi|, and choose internal routing

    y12=|l|, y23=|l+p2|, y31=|l-p1|.

The isolated component normals are

    ell1=E1+y12+y31,
    ell2=E2+y12+y23,
    ell3=E3+y23+y31.

The retained unstripped channel response is

    R23=-8 L_ext/(ell2 ell3),
    L_ext=1/(8 E1 E2 E3).

This is the contact coefficient/readout after external-leg restoration. It is not asserted to be the complete loop integration density: remaining graph factors, coupling transforms, integrations and the operator lift must still be identified.

## Correction to the earlier hostile path

Momentum conservation implies E3<=E1+E2, so

    ell1+ell2-ell3=E1+E2-E3+2y12>=0,

and cyclically. Hence ell=(t^-1,t^-1,t^-2), equivalently s=(t,t,t^2), cannot occur on this physical slice for0<t<1/2.

Our previous anisotropic controls remain valid in an independent algebraic normal chart and establish information-loss/norm statements there. Calling that particular path physically realized would be too strong. This does not make all contact infinity inaccessible, and does not prove the same inequality for higher-valence sites where x_s need not equal one momentum norm.

## Three realizable limits

### Fixed positive external energies, loop UV

For l=r n with |n|=1 and fixed external momenta, each internal norm is r+O(1), and each ell_i=2r+O(1). Thus

    R23=-2 L_ext r^-2+O(r^-3).

External legs are constant. Ordinary readout collapse and a second asymptotic grade persist along a physically realizable route, without the previous anisotropic chart path.

### Uniform hard dilation

Scale every external and internal momentum by r. Then ell_i scales as r, L_ext as r^-3, and

    R23(r p,r l)=r^-5 R23(p,l).

The restored physical contact coefficient has degree-5, rather than the stripped degree-2. This is not an exponent for a fully integrated amplitude.

### Mixed soft–hard corner

Choose, for t>0 and integer a>0,

    p1=(0,t^a,0), p2=(t^-1,0,0),
    p3=(-t^-1,-t^a,0), l=(0,0,1).

Momentum conservation is exact and the external momenta are noncollinear for every t>0. Here ell1 tends to2 while ell2 and ell3 are asymptotic to2/t. External factors instead give L_ext~t^(2-a)/8. Consequently

    R23~-t^(4-a)/4.

It vanishes for a2, approaches-1/4 for a4, and diverges for a6. These are simultaneous soft and contact-infinity limits. They do not contradict uniform bounds restricted to nonsoft compact external domains.

## Programme consequence

There is no single physical asymptotic degree associated merely with the words contact infinity. The momentum lift and other incident strata must be declared. External-leg factors neither universally cure nor universally worsen the stripped suppression.

Retain the fixed-external loop-UV path as the simplest physically realizable collapse control. Keep soft–hard corners separately typed, and do not import the invalid anisotropic chart path as physical evidence. Next restore the remaining source graph factors before assessing integration or score-norm completion on that fixed-external path. The current coefficient power alone is not an integrability theorem.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_contact_physical_scaling.py` checks exact momentum closure, norm routing, the triangle inequality identity, uniform dilation, the fixed-external UV limit and mixed soft–hard coefficients for a2,4,6. No owner artifacts are changed.
