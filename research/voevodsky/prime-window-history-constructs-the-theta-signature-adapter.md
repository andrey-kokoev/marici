# Prime-window history constructs the theta signature adapter

## Independently specified arithmetic update

Use the existing prime multiplication n -> np and the retained divisor-window restriction. For the squarefree packet (2,3,5,7), rooted at label 2, let v(n,p) be the incidence vector of chambers contained in

    [log n, log(np)].

This is computed from the integer labels and the arriving prime. It does not look up the completed route or its parity class.

Let T_<=4(C^15) be the truncated noncommutative tensor algebra, with degree-zero unit. Retain a history z in this algebra and update

    (n,z) -> (np, z (1+v(n,p))).

Prime multiplication and interval restriction come from the prior arithmetic source constructions. The tensor history is explicit added record memory. Its update is independently defined before any selected parity readout.

## Exact signature comparison

Starting from (2,1), induction on the arriving events gives

    z_r = sum_(j_1<...<j_r) v(n_(j_1-1),p_(j_1)) tensor ... tensor v(n_(j_r-1),p_(j_r)).

Thus z_r is exactly the event-segmented K_r coordinate of the route. Each event contributes zero or one tensor letter; same-event powers are absent from the forward update. No scalar history is tensor-powered after aggregation.

The independent checker defines its windows by arithmetic inequalities between adjacent numerical divisor labels, then compares with the existing mask-based implementation. It verifies all 168 admissible paths from all sixteen starting divisor labels, at every degree zero through four.

For the 24 full routes it reconstructs the selected 24-by-24 matrix M directly from this online recorder. The determinant is one and the previously recorded parity readout obeys

    R M = K*/2.

Applying the existing bounded theta atom map H at each tensor slot gives exactly F. This closes the mathematical generator comparison from an event-accessible arithmetic history source to our theta packet.

## An arithmetic operation on the comparison edges

Every event element 1+v is invertible in the truncated algebra:

    (1+v)^(-1)=1-v+v^2-v^3+v^4.

For a word w, define its arithmetic history element

    S_w = product_(events in w) (1+v_event).

The product is in event order; its inverse is the reverse product of the displayed event inverses. Define the right comparison on history memory by

    C_(w,w')(z) = z S_w^(-1) S_w'.

This is an explicit bounded linear map on the finite-dimensional history algebra. It satisfies

    C_(w,w')(S_w)=S_w',
    C_(w',w'') C_(w,w')=C_(w,w''),
    C_(w,w)=I.

Hence every commuting square, every braid hexagon, and all their pastings have identity holonomy on this declared history carrier. The identities follow from associativity and cancellation; the ingredients S_w are computed from the independently specified prime-window updates.

This realizes the discrete permutohedral comparisons by arithmetic history operations. It uses the known source and target word labels of each edge. It does not define a word-blind transport on an already aggregated mixture, nor identify the earlier barycentric interpolation inside the three-cell with a physical evolution.

## Why history cannot be recovered from the terminal base

Prime multiplication commutes on integer labels. The two words (2,3) and (3,2), rooted at 2, both end at 12. Their degree-one chamber totals agree, while their degree-two history difference is

    e_0 tensor e_1 - e_1 tensor e_2 - e_1 tensor e_3.

The checker verifies this exact nonzero difference using the fixed fifteen-chamber alphabet.

Consequently there is no section assigning a single history s(n) to each terminal integer, initialized at s(2)=1, and intertwining every prime update. The two orders would force incompatible values for s(12).

Forgetting history gives an intertwiner back to ordinary prime multiplication, but there is no compatible reconstruction from that base alone. This is an extension of the arithmetic state, with an explicit obstruction to treating it as a mere coordinate change on terminal labels.

## Positive-mixture acceptance test

The checker also tests the previously constructed strictly positive mixtures

    c_plus=(1/24)1+K_0/48,
    c_minus=(1/24)1-K_0/48.

Their accumulated records agree through degree three and differ at degree four. The reconstructed normalized parity difference is e_0/12. Thus the online recorder separates the collision when it is permitted to accumulate the degree-four record before mixing routes.

For classical random routes, accumulate each route record and then average. For complex route amplitudes, use the linear extension over route histories; a physical realization requires a coherent history register and an appropriate amplitude measurement. Classical route counts alone do not implement that latter map.

## Remaining admission and metric conditions

The construction requires access to each arriving prime and the current arithmetic state, plus memory retained across events. Its existence as a finite transducer does not prove that a previously specified terminal theta source exposes those events or admits this interaction.

No noise covariance or signed Green form on the new memory has been inferred. The original raw theta observation norm and its decoder lower bound remain unchanged.

The remaining physical/source-interface question is now concrete: does the owning source admit the transition

    |n> tensor z -> |np> tensor z(1+v(n,p))

with the declared classical or coherent interpretation? If it does, the adapter and its finite coherence follow from the formulas above. If only the terminal integer or aggregated history is available, the exact two-order and positive-mixture obstructions apply.

## Verification

Fresh command:

    uv run --with sympy python research/voevodsky/checkers/check_arithmetic_window_signature_adapter.py

All checks passed: 168 path comparisons, selected determinant, parity reconstruction, invalid-transition rejection, noncommuting history over the commuting base, and the positive-mixture collision test. Certificate: `results/arithmetic-window-signature-adapter.json`.

The comparison-edge identities are algebraic proofs in the truncated tensor algebra; the checker verifies their arithmetic signature ingredients rather than executing all full-algebra edge operators.
