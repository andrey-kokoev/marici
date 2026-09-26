# Restore deletion-edge factors before making loop-integrability claims

## Fresh source read and conventions

Read primary2401.05207 eq:CGUnInt and its dash rule (local TeX lines1098–1129): each erased edge contributes1/y_e and shifts both endpoint energies by y_e. Read ledger2136 to distinguish the relative-Landau normal nu_i from an ordinary energy denominator, and retain ledger2159's ratio C1 C3/P13=q13/y31.

Use the primary universal-integrand dash convention1/y_e, and the ledger's displayed4,-8 coefficient convention. Do not silently identify these constants with a bare product of Gaussian covariances1/(2y_e): real-part/component normalizations also enter that dictionary. The power counting below is unaffected by fixed nonzero convention factors.

## A compatible pre-grade route representative

For deletion S={12,23}, the isolated component is2 and the retained connected component is13. Define

    ell1=X1+y12+y31, ell2=X2+y12+y23,
    ell3=X3+y23+y31,
    q13=X1+X3+y12+y23,
    C_i=1/ell_i, P13=y31/(q13 ell1 ell3).

The source row is4P13 v13-8C1C3 v123. The factor

    H=C2/(y12 y23 y31)

restores a component/dash representative with

    H P13=1/(y12 y23 q13 ell1 ell2 ell3),
    H C1 C3=1/(y12 y23 y31 ell1 ell2 ell3)=D.

The first has precisely the two deleted-edge factors and the connected spectator; the second has three deleted edges and three isolated contacts. This is an explicit algebraic reconstruction consistent with the source component ratio. It is NOT a proof that H is the inverse of the source's relative-Landau/normal-grade operation on integrated periods.

For the source-normalized moving kernel v13=2q13/y31, v123=1, the restored signed route values are8D and-8D. The unweighted graph itself is not asserted to vanish: this is the selected kernel packet, with its source coefficient vector retained.

## Preserve deletion masks during covariance variation

The common baseline factor H is only a convenient factorization. It does not mean the retained edge31 was deleted in the first route. At fixed source kinematics and coefficient vector, the multiplier family is

    F(g)=8D g12 g23(1-g31).

It has first final-edge response-8D. Assigning g31 to both terms merely because H contains1/y31 would incorrectly preserve cancellation and give zero. Source incidence labels survive algebraic common-factor extraction.

External-leg restoration gives -8 L_ext D under the same contracted-level assumptions as the previous note. The complete uncontracted operator lift and normalization dictionary remain distinct obligations.

## Fixed-external positive-energy loop behavior

Use the physical routing from the preceding audit with fixed positive external energies and distinct norm centers. At l=r n,

    y_e=r+O(1), ell_i=2r+O(1), q13=2r+O(1),
    D=(1/8)r^-6+O(r^-7),
    H=(1/2)r^-4+O(r^-5).

Hence the restored response -8L_ext D behaves as -L_ext r^-6, whereas the reduced two-contact response behaves as -2L_ext r^-2. With Cartesian d3l the restored radial tail is O(r^-4)dr and converges. Integrating the reduced response alone would instead have a constant radial tail. These are different integrands, not contradictory UV conclusions.

Near a single loop-norm center, only one y_e vanishes, while the other y factors remain nonzero and positive ell_i stay bounded below by X_i. D is O(1/rho), locally integrable against rho^2 drho. Thus this particular positive-energy reconstructed kernel-density representative is absolutely integrable. This does not prove all graph sectors, site-energy coupling transforms, differentiated densities or analytically continued chains are integrable.

## What has been gained

We now have a source-compatible full deletion-factor representative, a correct mask-preserving susceptibility, and its elementary UV/local integrability argument. It is consistent with the prior positive-energy finite-readout evidence.

The remaining comparison is not just another scalar asymptotic estimate: establish how the actual contact-normal extraction acts on this integrable representative and whether it commutes with integration in a declared topology. Source nu_i=P_i^2-X_i^2 is not ell_i, so multiplication by H must not be called that operator without proof. Existing source-owner handoff remains active; no owner artifact is modified.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_contact_route_density.py` checks the route factors, moving-kernel cancellation, distinct masks, physical UV constants and the convergent radial power. Uniform asymptotic estimates and local integrability above are written arguments, not machine-formalized integration theorems.
