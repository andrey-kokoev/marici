# A concrete 1836-arrow phase net

This is an explicit candidate construction, not a deduction of its parameters from the previous incidence tower. Its primitives are directed endpoint pairs. No history tags multiply the count.

## Ports and arrows

Take twelve sites c in Z/12. Each has twelve relation ports R_i and three state ports H_a. These are disjoint kinds of ports, not a triangle subset counted again inside the relation ports.

The relation labels can be the twelve oriented tetrahedral arrows. The three state labels are a separate declared state sector. Specifying twelve sites and both sectors is part of this construction.

For each c, create precisely these arrows:

    (c,R_i) -> (c+1,R_j), for 0 <= i,j < 12;
    (c,H_a) -> (c+1,H_b), for 0 <= a,b < 3.

Site addition is modulo twelve. Source and target always lie at different sites. The net has 180 port-nodes, 1728 R arrows and 108 H arrows: exactly 1836 distinct directed endpoint pairs. Every displayed arrow counts once.

There are no R-H arrows in this version, so it has two connected components, of 144 and 36 port-nodes. Inter-sector dynamics is not supplied by this construction.

## Phase transport

On each sector of size n, assign the normalized Fourier weight

    (F_n)_{b,a} = exp(2*pi*imaginary_unit*a*b/n)/sqrt(n).

All weights are nonzero, so none of the 1836 arrows is merely decorative. Writing S_12 for the cyclic site shift, the full one-step operator is

    U = S_12 tensor (F_12 direct_sum F_3).

Fourier orthogonality gives F_n^2[a,b]=1 when a+b=0 mod n and zero otherwise. Thus F_n^4=I and

    U^12 = I.

No positive step count smaller than twelve returns the full operator to identity, because the site coordinate has not returned. The twelve-step identity is a coherent sum over paths; individual path weights need not equal one.

## Unique-arrow traversal union

Every arrow is on a length-twelve closed walk. For an arrow from (c,s,a) to (c+1,s,b), continue on port b around the sites, then take the final arrow back to port a at site c. Taking the union of these explicit closed-walk witnesses gives exactly the net's 1836 arrows, with repeats deduplicated by endpoint pair.

This proves coverage of the constructed graph by identity-endpoint return walks. Full weighted return additionally follows from U^12=I. It does not assert that a single walk visits all 1836 arrows.

## Checks and limits of the construction

    python research/nima/checkers/check_1836_phase_interaction_net.py

The checker enumerates all endpoints, rejects duplicate arrows and self-loops, verifies the closed-walk union, and propagates every one of the 180 basis vectors through twelve steps. The worst numerical return error is below 2e-14; the Fourier orthogonality argument supplies the exact identity.

A control using only the 180 matching-port arrows also returns after twelve site steps. Consequently, identity closure alone does not prove that the dense 1836-arrow construction is minimal. Its dense Fourier mixing, twelve-site architecture and disjoint sector sizes are explicit design assumptions.

Artifact: `results/1836-phase-interaction-net.json`.

This is a directed phase-weighted interaction graph. A formal port-rewriting interaction-net calculus would additionally require agent signatures, principal ports and local rewrite rules.
