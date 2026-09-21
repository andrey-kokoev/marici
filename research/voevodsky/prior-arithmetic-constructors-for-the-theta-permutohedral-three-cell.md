# Prior arithmetic constructors for the theta permutohedral three-cell

## Search conclusion

Prior research supplies independently defined prime multiplication, moving-window restriction, adjacent-prime comparison, and braid coherence. The most direct arithmetic identification is the divisor-chamber refinement. Its four-prime instance is exactly the interval catalogue used by our theta packet, after translation by log 2.

The remaining distinction is between the arithmetic comparison of route presentations, which has an explicit source construction, and access to a distribution or coherent superposition of route-conditioned multipoint records, which has a separate source contract.

## 1. Exact match: divisor chambers

Source: `research/nima/the-common-refinement-of-prime-factorization-paths-is-the-divisor-chamber-complex.md`.

For n=2*3*5*7=210, all prefix products of all factorization words are exactly the divisors of n. Their logarithms give the minimal common refinement on [0,log n]. After translation by log 2, the endpoints are

    2,4,6,10,12,14,20,28,30,42,60,70,84,140,210,420

in exponential coordinates. These are precisely our existing sixteen endpoints and fifteen interval atoms.

For a route w and its prefix products d_j, its j-th event is the interval

    [log(2 d_(j-1)), log(2 d_j)].

Let v_(w,j) be its fifteen-entry chamber incidence row. The prior source restriction/reaggregation supplies these rows directly. They are the same event vectors used by `research/grothendieck/theta_interval_signature.py`. Consequently

    K_r(w) = sum_(j_1<...<j_r) v_(w,j_1) tensor ... tensor v_(w,j_r).

Thus the arithmetic interpretation of the route vertices, swap edges, and interval columns is explicit. The path signature retains the event segmentation before summing over routes.

The prior refinement acts by restricting an actual source function to disjoint intervals. It preserves its L2 energy by orthogonal decomposition. This is a source operation already defined independently of the parity reconstruction.

## 2. Adjacent swaps need ratio windows

Source: `research/nima/adjacent-prime-transport-requires-the-signed-ratio-window.md`.

For p<q, the common refinement of the orders pq and qp has pieces of lengths

    log p, log(q/p), log p.

The two ordered stage readouts on (x,y,z) are

    P_pq(x,y,z)=(x,y+z),
    P_qp(x,y,z)=(x+y,z).

They agree on the total but have different kernels. The retained middle ratio window is therefore needed for swap transport. A two-port permutation cannot supply it.

This explains the arithmetic content of our permutohedral edges: they compare different aggregations of one retained divisor-chamber source.

## 3. The braid comparison already exists at the refined source

Source: `research/nima/three-prime-braid-coherence-holds-only-on-the-retained-common-interval-refinement.md`.

Both three-swap routes from pqr to rqp act by reaggregation of the same retained atomic source and reach the same final packet. The recorded exact fixture uses lengths 1,2,4; the proof is the common-refinement construction. It includes a quotient-before-transport counterexample.

The general divisor-chamber note extends the same source description to all factorization words. For our four primes, retaining the fifteen chambers supplies the common source for every square and braid hexagon. The resulting comparison system is flat. This is a natural arithmetic interpretation of the face coherence of our P4 construction, rather than an interpretation inferred from a raw output commutator.

This identifies the discrete comparison operations. It does not identify the interior barycentric probability interpolation of our three-ball with a new arithmetic operation. That interpolation remains a chosen continuous filling in the linear observation carrier.

## 4. Independent prime multiplication and analytic transport

Source: `research/grothendieck/bordered-prime-shift-derives-the-euler-factor-before-scalar-aggregation.md`.

On labelled arithmetic source vectors,

    V_p e_n = e_(pn),
    T e_n = phi_n,
    T V_p = p^(-1/2) tau_(log p) T.

Prime multiplication and its half-density translation are therefore already source-defined. The V_p commute, so their terminal product depends only on the final integer. To retain path-dependent event observations one must also retain intermediate restrictions and their order.

Source: `research/nima/the-valuation-chain-Stein-identity-is-the-source-derived-seam-attachment-before-determinant-sewing.md`.

The source-derived window observation B_p and transported base A_p obey

    G_p - A_p* G_p A_p = B_p* B_p.

The full transported-window family is required; one fixed seam row can miss a source vector with nonzero energy. This is a useful candidate for an operator-level implementation of the moving boundary records, with domains and labels already specified.

## 5. Candidates already ruled out or limited

`research/grothendieck/prime-reciprocal-noncommutativity-is-an-exact-frame-coboundary.md` corrects the earlier raw prime-exchange commutator interpretation. The normalized exchanges become one fixed reflection after source-native frame transport, and the transition cocycle has identity holonomy. Their untransported commutator does not supply an intrinsic higher residual.

`research/aspect/common-forcing-generates-finite-valuation-odd-current.md` supplies a genuine affine forcing reservoir and an exact interval semigroup. It retains a finite odd boundary displacement. For constant common forcing, its total transfer depends only on total interval length, so ordered route information would again require intermediate records.

`research/aspect/constructor-permutohedron-bianchi-closure.md` provides an operational template: compare full constructor transports around a braid hexagon. Products of scalar fringes are insufficient. Its execution is an exact matrix fixture; physical tomography is explicitly unrun.

## 6. Sharp remaining source-access gate

`research/grothendieck/the-raw-theta-inverse-is-severely-conditioned-and-fixed-forcing-does-not-restore-route-correlations.md` audits the relevant source contracts. A fixed-forcing joint graph built from an already aggregated interval history preserves that input, while the route correlation collision has already been erased. Deterministic downstream processing cannot recover it.

`research/grothendieck/prior-research-clues-for-route-access-and-calibrated-correlation-readout.md` and `research/grothendieck/source-stage-parity-instrument-and-calibration-contract.md` give the positive candidate: an event-stage parity accumulator on an accessible ordered route record. They separately treat classical route probabilities and coherent amplitudes. The arithmetic event-access adapter and measured calibration remain undeclared in those packets.

The next independent source comparison can now be stated without inventing a new operation:

1. start from labelled prime multiplication V_p;
2. retain its transported divisor-window observations at each event;
3. specify how ordered event products are recorded before route aggregation;
4. verify that this record equals the K_2 and K_4 packet on every route generator;
5. test it on the strictly positive indistinguishable mixtures from `three-point-bordered-observations-still-miss-all-six-parity-channels.md`.

If only the common terminal product or aggregated history is exposed, the parity adapter fails that test. If the declared source exposes the intermediate route-conditioned record, the existing divisor refinement and theta synthesis provide the mathematical observation map.

## Scope of this audit

The cited notes were read during this search. Their historical checker claims were not freshly rerun here. The new P4 incidence and theta-signature checker was run in the preceding construction. This audit identifies exact matching source formulas and their remaining interface conditions; it makes no new physical-access or signed-form preservation claim.
