# Falsification attempt: is the printed measure the ordinary loop measure?

## Conjecture under attack

The working conjecture was that source-authorized completion is the principal obstacle and that the local corner dependence reflects information the physical prescription must retain or resolve. Test an earlier bridge: does the literal normalization used in our calculations identify the ordinary spatial loop measure at all?

Freshly inspected method.tex eq:ukchi and cosmologicalintegrals.tex eq:constant. Under the ordinary Euclidean simplex-volume meanings used throughout our pilot, the answer is NO without an additional, explicitly kinematic normalization. This defeats the unqualified measure identification; it does not invalidate the conditional integrals we actually computed.

## An independent derivation, not another check of our expected answer

Place the three distance centers at(0,0), (a,0), (p,v), with a,v>0. Write the loop point as(X,Y,z_perp), rho=|z_perp|. Let r,s,t be its three distances, D the squared base area and K the squared tetrahedral volume. Then

    D=a^2*v^2/4, K=D*rho^2/9.

In three dimensions, direct differentiation gives

    det d(r^2,s^2,t^2)/d(X,Y,z)=8avz.

Accounting for both signs of z and converting squared lengths to r dr s ds t dt gives

    d^3 loop = [1/(3sqrt(K))] r dr s ds t dt.

No external-volume factor remains. This calculation uses elementary Cartesian volume, not the paper's coefficient formula.

More generally, angular integration in the(d-2)-dimensional transverse space gives

    d^d loop = mu_geom * r dr s ds t dt,
    mu_geom = pi^((d-2)/2)*3^(d-4)/Gamma((d-2)/2)
                 * D^((3-d)/2) * K^((d-4)/2).

Derivation: the sphere area is2*pi^((d-2)/2)/Gamma((d-2)/2); changing rho to rho^2 contributes1/2; the Jacobian from(X,Y,rho^2) to(r^2,s^2,t^2) is4av; and d(r^2)d(s^2)d(t^2)=8r dr s ds t dt. Substituting rho^2=9K/D yields the formula. A conventional dimension-only factor such as(2pi)^(-d) can be added separately and does not change the external-volume exponent.

## Compare with the formula actually used

The printed coefficient combined with eq:ukchi gives, for this triangle,

    mu_print = 48*pi^((d-3)/2)*3^(d-6)/Gamma((d-3)/2)
                  * D^((5-d)/2) * K^((d-4)/2).

Consequently

    mu_print/mu_geom
      = [16D/(3sqrt(pi))] * Gamma((d-2)/2)/Gamma((d-3)/2).

This ratio depends on the external geometry. It cannot be absorbed in a dimension-only convention or ordinary Fourier-measure normalization.

Two independent severe checks:

1. **Homogeneity:** including the three y dy factors, mu_geom has total scaling degree d, as d^d loop must. The literal printed measure has degree d+4. This is an external-volume discrepancy, not a boundary-continuation effect.
2. **A regular dimension:** at d=5 the ratio is(8/3)D. Two geometries with D=1 and D=4 give ratios8/3 and32/3. No regulator singularity or delicate order of limits is involved.

At d=3+2epsilon,

    mu_print/mu_geom = (16/3)*epsilon*D + O(epsilon^2).

In particular the ordinary Euclidean measure has no simple zero at epsilon0. The zero that canceled our local profile pole belongs to the literal printed normalization.

## A compact-interior hostile control

Choose a compact integration patch strictly inside the nondegenerate real domain, away from all rational poles. The ordinary d3 loop density is positive and finite there. The printed density tends uniformly to zero there as epsilon→0+.

Thus an ultraviolet or endpoint divergence cannot explain away their local mismatch. A compensating external factor or a different definition of the period could reconcile them, but that is new interface data that must be exhibited. Merely choosing the order of E and epsilon limits does not reconcile two different measures on this regular patch.

## Verdict on the conjecture

- **Falsified under the stated conventions:** an identification of the literal printed weighted measure with the ordinary Euclidean loop measure, up to a dimension-only constant.
- **Not falsified here:** the conditional local corner theorem for the literal printed family. Its calculation explicitly assumed that normalization.
- **Undermined:** the inference that its finite coefficient and path dependence must already be information in the physical loop observable. The finite regulator cancellation may belong to a differently normalized object.
- **Traversal correction:** normalization/measure identification is an earlier concrete obstruction than completion order. Do not spend the next turn extending endpoint charts or merely waiting for an owner. Reconcile the measure map using primary sources and independent geometry first.

The broad recommendation to prioritize source validation survives this attack; the stronger physical interpretation does not. We do not yet know whether the discrepancy is a typo, an implicit external normalization, a volume convention, or a different intended object. No paper or owner artifact is silently corrected.

The source itself cites arXiv:2402.06558 and arXiv:2401.05207 for loop-measure details. Those derivations, together with the owner's convention, are the next discriminating sources. A reconciliation must explain the D factor AND the Gamma-index shift, not merely acknowledge the previous result.

## Verification

`check_triangle_measure_audit.py` independently checks32 exact Cartesian squared-distance Jacobian fixtures, the two-sheet d3 density, homogeneity at four dimensions, and the d5 geometry-dependent ratio. Receipt: `triangle-measure-audit.json`, with unchanged source hashes. A passing test means the mismatch was reproduced; the receipt explicitly reports `printed_measure_matches_euclidean: false`.

The general-dimensional angular derivation and interpretive verdict are written mathematics, not a machine-formalized theorem about the authors' intended conventions.
