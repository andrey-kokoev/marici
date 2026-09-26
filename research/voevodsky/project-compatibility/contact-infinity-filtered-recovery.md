# Contact infinity: retain labelled grades, not an undifferentiated boundary value

## Fresh evidence and scope

Ledger Entries2224 and2225 derive the source response R_jk=-8 s_j s_k/(hat_l_j hat_l_k), with l_i=hat_l_i/s_i. They select its Cartier coefficient from the already constructed mixed correlator, not by fitting a normalization. Entry2225 states order independence for the independent normal-crossing coordinates. The checker `research/benincasa/checkers/contact_infinity_score_cartier.rs` only verifies a constant numerator/denominator example; it does not test continuity in a readout norm.

Use this source-prescribed coefficient and the retained direct-score matrix, not a new physical realization. Work in a chart with nonzero hat_l_i and independent s_i, and a finite occurrence packet x with a continuous boundary value. No global contour continuation is inferred.

## Whole labelled packet

Let the occurrence order be(12,23,31), and put

    g=(s1*s2,s2*s3,s3*s1), G=diag(g),
    h=(1/(hat_l1*hat_l2),1/(hat_l2*hat_l3),1/(hat_l3*hat_l1)),
    B=Q^T, Q=[[1,2,0],[1,-1,-1],[1,-1,1]].

The source contact-weighted direct readout is

    z=-8 B G diag(h) x.

In the interior, demix using the constant source matrix B, then take the labelled Cartier grades:

    z_hat=B G^(-1) B^(-1) z=-8 B diag(h) x.

Division here means coefficient extraction on the specified divisible source sections and their shifted filtration modules. It is not a claim that every boundary vector admits this operation or that an arbitrary normal may be inverted in another sector.

The retained data must include the occurrence labels and their multidegrees. Each pairwise grade commutes in the declared normal-crossing chart; the formula follows directly from factorization. Limits of continuous x and h then give the corresponding boundary packet.

## Hostile path: one common leading grade loses routes

Take s1=t,s2=t,s3=t^2 and hat_l_i=1. Then

    G=diag(t^2,t^3,t^3).

All three ordinary readouts vanish. Even retaining the single common leading coefficient t^(-2)z retains only the12 occurrence. The23 and31 contributions first appear one order later. The labelled multigrade recovers all three.

This is not a failure of Entry2225's pairwise order independence. It is a failure of replacing a labelled normal-crossing filtration by one undifferentiated leading boundary coefficient.

## Which topology makes recovery stable?

Use Euclidean norms on the retained finite packets. Since B has least singular value sqrt(2),

    ||z_hat|| >= 8 sqrt(2) min_e|h_e| ||x||.

This is uniform on chart domains with min|h_e| bounded below. Equivalently, on interior readouts define the filtered norm

    ||z||_filtered,s = ||B G^(-1) B^(-1) z||.

In the corresponding retained-grade coordinates, recovery has a bounded inverse and extends to their finite-dimensional boundary values. This is a precise candidate completion tied to the source-selected asymptotic coefficients.

It is NOT equivalent uniformly to the ordinary unweighted port norm. For x=e23 and the hostile path above, z=-8 t^3 B e23 tends to zero while x remains nonzero and z_hat=-8 B e23 does not vanish. Thus coefficient extraction cannot extend continuously through this degeneration using only the ordinary raw-output topology. Arbitrary additive readout error is amplified by G^(-1).

The source selects an asymptotic observable; that fact alone does not prove that an experimental noise norm, Gaussian statistical norm, or full infinite-dimensional physical topology supplies the required weighting. No uniform finite-precision observability is claimed.

## Structural synthesis

The source realization supports three separate conclusions:

1. ordinary infinity restriction loses the contact routes;
2. the already source-selected labelled Cartier coefficients preserve them;
3. stable recovery requires the retained-grade topology or independently established equivalent control, not merely formal division.

This is an actual-source instance of the filtered comparison/readout contract. It complements the previous Gram-wall result: an alternate port removes Gram projection loss, whereas contact infinity requires retaining different asymptotic grades. Neither operation adds a Carrier incidence or proves the triangle continuation bridge.

Next test the source's Gaussian score/correlation metric against this filtered norm. If the raw noise remains of fixed size while contact responses vanish, identify the resulting precision cost rather than claiming uniform physical stability.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_contact_infinity_recovery.py` verifies the full packet identity, both orders of each pairwise grade, the anisotropic leading-grade loss and finite exact instability samples. These checks do not establish a physical measurement topology. Owner sources remain unchanged.
