# The relation layer embeds jointly in the derived seam carrier

The four-prime product layer is now connected to the analytical refinement seam complex by an explicit path derivative.

For a marked path, insert at each event its typed seam coordinate and retain prefix, seam, and suffix records. The boundary of this derivative telescopes to the path endpoint difference. Consequently every local diamond relation is a nonzero seam cycle.

For the six two-event middle vertices, the two local relation generators on each side produce

    6 * 2 * 2 = 24

composite relations, exactly the source product layer `I^2`. Each composite is killed by either single-seam derivative: the two seam positions separately cannot see the full product attachment. Retaining both seam coordinates gives a joint typed observation whose selected minor has rank 24. Thus the joint seam carrier separates all of `I^2`.

This supplies the missing comparison for the four-prime nonsplit triangle

    I^2 -> I -> I/I^2 -> I^2[1].

The product inclusion is not an abstract dimension match: its actual source products map to explicit joint seam cycles, while each marginal seam map annihilates them. The attaching data is therefore joint and relation-sensitive.

The path derivative also verifies the expected telescoping law for arbitrary tested marked paths, including two-event and four-event routes. It does not make the single seam derivative faithful, and it does not identify this coefficient seam pairing with the analytical Green form.

Verification:

    uv run --with sympy python research/grothendieck/checkers/check_relation_to_seam_bridge.py

Passed: 24 local relation cycles, 24 product relations, rank-24 joint seam minor, local-cycle closure, product annihilation by each marginal, and path-boundary telescoping.
