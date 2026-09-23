# The sourced four-mass ψ prefactor is a normalized inverse auxiliary Jacobian

The primary-source starred four-mass ψ class now matches more than the four paired source columns and its TWO auxiliary kinematic solutions. Its explicit ψ prefactor has an exact Jacobian meaning on the same four-dimensional quotient by the fixed nine-point target.

Let the source's two coupled equations for the auxiliary twistors `A=z7+α z8` and `B=z3+β z4` be

    f(α,β)=α<8,5,6,B>-<5,6,B,7>=0,
    g(α,β)=β<4,1,2,A>-<1,2,7,A>=0.

Alternation of the quotient four-brackets gives FOUR exact derivative identities:

    ∂β f = <A,4,5,6>,        ∂α g = <B,8,1,2>,
    ∂β g = -<A,4,1,2>,      ∂α f = -<B,8,5,6>.

Therefore

    det(∂(f,g)/∂(α,β))
      = <A,4,1,2><B,8,5,6> - <A,4,5,6><B,8,1,2>,

and the source's OWN prefactor is exactly

    ψ = <A,4,1,2><B,8,5,6> / det(∂(f,g)/∂(α,β)).

The checker confirms every alternating sign with exact four-brackets from the moment-curve data and the rational observed `Y`, then checks the identity symbolically in `(α,β)`. After substituting the previously matched `α(q),β(q)`, both the source prefactor's numerator and denominator are coprime to the graph quadratic. Hence ψ is finite and nonzero at BOTH exact algebraic solution branches; its two branch values are distinct. A vanishing discriminant would instead signal a singular auxiliary Jacobian when the two solutions collide, subject to the numerator and chart factors.

A subsequent formal calculation proves the stronger universal two-branch identity `ψ(α+)+ψ(α-)=1`, independently confirmed by the fixed-target quadratic-field trace; see `the-sourced-four-mass-psi-prefactors-form-a-two-branch-partition-of-unity.md`. This supplies an exact source-side NORMALIZATION PIECE, not equality of the complete source function with the traced cell form. The source's two super-five-brackets, fermionic component projection, global orientation, and occurrence in the sourced nine-point generalized-R history still need to be carried through. In particular, comparing only the previously certified positive local source lift to the full ψ function would discard the second complex sheet improperly.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_four_mass_psi_jacobian.py

Packet: `research/nima/results/nine-point-four-mass-psi-jacobian.json`.
