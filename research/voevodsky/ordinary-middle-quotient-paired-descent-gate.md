# Ordinary middle-quotient paired descent gate

## Scope

Finite-dimensional linear-algebra reduction for the ordinary sector of the six-prime common cell. This does not construct its actual analytical observation or prove coarse Green isometry.

Inputs:
- `../grothendieck/the-six-prime-associativity-cell-retains-the-derived-middle-block.md`
- `../grothendieck/the-six-prime-shifted-attachment-has-a-function-valued-paired-comparison.md`
- `../nima/the-critical-joint-seam-green-form-reduces-to-local-function-valued-pairings.md`

## The quotient to be paired

For each retained ordered pair partition set

    T = R1 tensor E2 tensor R3,
    K = R1 tensor R2 tensor R3,
    H0 = T/K = R1 tensor B2 tensor R3.

Summing the 90 labels gives dimensions 2880, 720, and 2160 respectively. The root carrier is tensored once throughout. These are coefficient dimensions, not full receiver dimensions.

Let F:T -> Y be a candidate ordinary analytical observation and let q_Y be conjugate-linear in its first argument. For an ambient observer y the proposed functional is

    [t] -> q_Y(F(t), y).

It is independent of the lift t exactly when q_Y(F(k),y)=0 for every k in K. Thus the maximal allowed observer space for this proposal is

    A = {y : q_Y(F(K),y)=0}.

If all ambient observers are allowed and q_Y is nondegenerate, descent is equivalent to F(K)=0. Source multiplication modulo I^3 proves a quotient identity, not this analytical vanishing condition.

A self-pairing q_Y(F(t),F(u)) descends in both variables exactly when F(K) is orthogonal to F(T). Hermitian symmetry supplies the other variable. Merely having zero self-pairing on K is insufficient.

## Detection after restricting observers

At a fixed finite-dimensional nondegenerate ambient envelope, A-perpendicular equals F(K). Therefore the descended observation against A detects T/K exactly when

    F^{-1}(F(K)) = K.

In particular an injective F suffices. This constructs a quotient-versus-annihilator pairing, not a metric on T/K and not permission to discard the shifted K channel. That channel remains separately present in degree -1 of the derived common object.

This is a possible route, conditional on constructing the actual F. No injectivity of an ordinary F follows here from the previously proved shifted map j3.

## Comparing groupings

Once actual ordinary maps F_L,F_R and their observer identification are specified, test lift independence first. With a common Y and observer space A, equality is precisely

    q_Y((F_L-F_R)(t),y)=0 for every t in T and y in A.

For A=F(K)-perpendicular this means their difference lies in F(K). Equality after source quotient alone does not identify the analytical ambient spaces or their Green forms.

Keep middle vertices, root pairing, independent memory/seam weights, and individual spectral denominators in constructing these maps. The shifted connecting observation is zero on H0 and cannot serve as a faithful ordinary observation.

## Next concrete gate

Specify F_L,F_R on the eight middle endpoint paths and both outer relation types, using the admitted analytical carrier. Compute their values on the two middle relations. Then either prove full-observer vanishing or justify the common annihilator observer space and its detection criterion. Do not select a section and call its pullback an inherited quotient form.

Verification: `uv run --with sympy python research/voevodsky/checkers/check_ordinary_middle_quotient_descent.py`. Fixtures test only the descent criteria, not actual Clark traces or the 2160 analytical coordinates.
