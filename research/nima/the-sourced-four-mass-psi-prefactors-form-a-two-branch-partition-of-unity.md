# The sourced four-mass ψ prefactors form a two-branch partition of unity

An exact calculation of the sourced four-mass prefactor at the rational nine-point target found an unexpectedly simple result: the two algebraic branch values are distinct, but their **sum is exactly one**. This is NOT a coincidence of the chosen moment-curve data. It holds universally for the primary source's TWO SIMPLE auxiliary solutions, wherever their denominators are nonzero.

Write the two primary-source coupled equations in formal four-bracket coefficients as

    f(α,β) = α(e0+β e1)-f0-β f1 = 0,
    g(α,β) = β(d0+α d1)-n0-α n1 = 0.

Eliminate `β=(n0+α n1)/(d0+α d1)` and write `P(α)=A α²+B α+C`. The earlier exact alternating-bracket calculation established

    ψ = (∂α f)(∂β g) / det(∂(f,g)/∂(α,β)).

At a simple solution, implicit differentiation gives `det(∂(f,g)/∂(α,β))=P'(α)`, while `(∂α f)(∂β g)=H0+A α` with `H0=e0 d0+e1 n0`. Hence

    ψ(α) = (H0+A α)/(2A α+B)
          = 1/2 + (H0-B/2)/P'(α).

For the two distinct quadratic roots, `P'(α+)=-P'(α-)`. The odd terms cancel, yielding the **universal exact identity**

    ψ(α+) + ψ(α-) = 1.

A formal-symbol checker proves this without specializing the eight bracket coefficients; a separate exact quadratic-field computation on the certified rational nine-point target independently gives `Tr(ψ)=1`, nonzero branch coefficient, and a nonzero branch norm. There the source α quadratic has one positive and one negative root, corresponding to the positive four-pair cell lift and its nonpositive algebraic conjugate.

The identity concerns the SOURCE ψ PREFACTOR, not the complete four-mass ψ times its two super-five-brackets. In particular, it does not say that the traced differential-form coefficient is one, nor that the two branch superfunctions agree, nor that a nine-point generalized-R history contains this cell. It explains how an algebraic per-solution Jacobian weight can consistently accompany a two-solution sum, while preserving the distinction between positive-real membership and algebraic trace.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_source_psi_field_trace.py
    uv run --with sympy python research/nima/checkers/check_four_mass_psi_universal_partition.py

Packets: `research/nima/results/nine-point-source-four-mass-psi-field-trace.json` and `four-mass-psi-universal-partition.json`.
