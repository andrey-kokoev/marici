# Closure specializes within the control base; pushforward does not extend transversely

## Fresh task and supplied classes

Execute control-spread-specialization-boundary. Retain the smooth connected four-dimensional level/monodromy cover S0, its smooth projective abelian scheme pi:mathcal X0->S0 of relative dimension6, and the global flat determinant sections R_S,I_S. The preceding construction supplies Xi_R,Xi_I in CH^3(mathcal X_U)_Q over a nonempty dense open U of S0, with the required fiber classes.

We extend the CHOW CLASSES on the same smooth total space. We do not assume that arbitrary closures of the chosen representatives are flat over the omitted fibers.

## Chow localization provides extensions on the same total space

The total space mathcal X0 is smooth of dimension10. Let Z=mathcal X0 minus mathcal X_U. Localization gives the exact sequence

    CH_7(Z)_Q -> CH_7(mathcal X0)_Q -> CH_7(mathcal X_U)_Q -> 0.

Here CH_7(mathcal X0)=CH^3(mathcal X0). Thus each Xi_j admits an extension barXi_j in CH^3(mathcal X0)_Q. Concretely one may take the closures of its finite rational cycle summands. Their total dimension remains seven. This extension is not canonical; different choices differ by classes supported over S0 minus U.

No universal Hilbert family at the omitted points has been manufactured by this surjectivity. The conclusion is extension as a rational cycle class on the total space.

## Refined fiber restriction handles excess intersections

For every s in S0(C), the fiber inclusion i_s:mathcal X_s->mathcal X0 is a regular embedding of codimension4. Its refined pullback gives

    i_s^!:CH_7(mathcal X0)_Q -> CH_3(mathcal X_s)_Q
          =CH^3(mathcal X_s)_Q.

This is well defined even when a closure has excess-dimensional intersection with that fiber. Ordinary set-theoretic intersection or the assertion that closure is flat would not justify the same operation.

Cycle-class compatibility gives

    cl(i_s^! barXi_j)=i_s* cl(barXi_j).

A global ordinary cohomology class on the smooth total space restricts to a flat section of R^6 pi_*Q: on a local differentiable trivialization of the proper smooth family, the fiber restrictions are locally constant. This uses the edge restriction to H^0(S0,R^6 pi_*Q), not an asserted splitting of the whole Leray filtration.

The section from barXi_j agrees with j_S on U. Since S0 is connected, it agrees on all of S0. Therefore

    cl(i_s^! barXi_R)=(R_S)_s,
    cl(i_s^! barXi_I)=(I_S)_s

for EVERY control fiber s, including those omitted from U. The same argument shows that differences between extensions have zero cohomology class after restriction to every fiber. No uniqueness of their Chow classes is claimed.

This is an actual theorem-backed construction of fiber cycle classes via localization and refined pullback. It is not a canonical effective or flat relative representative. All fibers considered here remain in the smooth abelian scheme; compactification fibers with singular total spaces are outside this statement.

## Why this is not extension into the full Weil base

The full Weil base S has dimension9. The displayed product-control locus has dimension4, hence codimension5. A level cover of that locus is not automatically a global closed embedding in S. Whenever discussing proper pushforward, first work on a chart where the locus is closed, or use a proper generically finite cover of its image. If no proper map is supplied, the proposed pushforward is not licensed at all.

Even when a suitable proper map is supplied, dimension is decisive. Its full family total space has dimension15; mathcal X0 has dimension10. A barXi_j cycle has total dimension7. Proper pushforward preserves dimension for a generically finite image, so its image is in

    CH_7(mathcal X_S)=CH^8(mathcal X_S),

NOT CH^3(mathcal X_S). The codimension increases from3 to8 because the base locus has codimension5. A degree normalization for a finite cover changes coefficients, not codimension.

Refined restriction of this pushed class to a fiber of the full smooth family has codimension8, and therefore lies in

    CH^8(mathcal X_s)=0

since the fiber has dimension6. Equivalently CH_7 maps to CH_(7-9)=CH_(-2). The visible three-dimensional support over a special control fiber is an excess intersection; it is not the refined degree-six class one sought. The pushed cohomology class has degree16, not degree6.

A genuine transverse extension would instead require a class Omega in CH^3(mathcal X_S)_Q, or a relative cycle-parameter component dominating an ambient neighborhood, whose fiber classes give the desired flat section. Localization across an OPEN subset of mathcal X0 does not prove surjectivity of restriction from the different total space mathcal X_S to its CLOSED control subfamily.

Nor would failure to extend one selected Chow representative prove failure of every possible representative of its cohomology class.

## Disposition and next infinitesimal comparison

Constructed: extensions of the relative Chow classes across all omitted fibers of the same smooth control base, with refined restriction realizing R and I there. Rejected: using closure or proper pushforward over the codimension-five control locus as a transverse codimension-three cycle family on the full base.

The original fixed X remains outside the decomposable control, and its alpha is still unresolved. No pointwise-algebraicity or dominance conclusion on the full Weil base is obtained.

Next bounded task: type the first-order DIFFERENTIAL of the relative cycle-parameter map in transverse directions. For a supplied smooth embedded cycle, construct the Kodaira-Spencer-to-normal-bundle obstruction and compare it with the first-order Hodge condition via semiregularity; retain the limitations for unknown or singular representatives. Use a high-degree complete intersection as an actual positive lifting control. Vanishing of the class-level Hodge derivative must not be assumed to kill the entire embedded deformation obstruction.

Verification separates exact degree/localization controls from the written Chow localization, refined-Gysin and smooth-family cohomology facts. These are imported standard results; no proof-assistant certification or Hodge verdict is claimed.
