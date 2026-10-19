# A local moving invariant plane exists, but its phase and modulus deform

**Iteration 5 of the requested ten-turn work-net run.**

**Strength:** exact characteristic/discriminant identities, a local analytic existence result using the finite-dimensional implicit-function theorem, and a checked rational Taylor jet. Not global continuation, a physical clock change or a derived normalization.

[Previous graded carrier](GRADED-BOUNDARY-TRANSPORT.md) · [Checker](check_moving_boundary_plane.py) · [Receipt](results/moving-boundary-plane.v1.json)

## 1. Fresh operator and spectrum

The preceding turn constructed the minimal constant four-dimensional carrier for

    M(z)=z A4+z^2 C4.

Its original fixed reference two-plane leaks at generic z. This turn tests a moving plane rather than enlarging the carrier again or imposing a target eigenvalue.

The actual polynomial family has characteristic polynomial

    chi(lambda,z)=lambda^4-z^4 lambda^2-(z^4+z^5)lambda-z^5.

At z=1 it factors exactly as

    (lambda^2+lambda+1)(lambda^2-lambda-1).

Thus the reference conjugate pair is separated from the two complementary eigenvalues at the base point. This factorization is derived from the matrices, not selected as an ansatz.

## 2. Construct the moving plane locally

Set epsilon=z-1 and split M into two-by-two blocks, with the original reference coordinates first:

    M = ((P,Q),(R,S)).

Seek a plane represented as the graph

    U(epsilon) = (I_2; X(epsilon)),    X(0)=0.

Its invariance is equivalent to the matrix Riccati equation

    R+S X-X P-X Q X=0.

The induced step on graph coordinates is T(epsilon)=P+QX. At the base point it is the original reference T.

The derivative of the graph equation with respect to X at the base point is

    L(Y)=S0 Y-Y T.

The exact four-by-four matrix representing L has determinant **4**. Hence the analytic implicit-function theorem supplies a unique analytic graph X(epsilon) in some neighborhood of zero. This is local uniqueness near this initial plane, not a classification of all invariant planes globally.

The first coefficient is

    X(epsilon) = epsilon * ((-1/8, 5/8),
                            ( 1/4,-1/4)) + O(epsilon^2).

The checker recursively computes rational coefficients through order four and verifies that every corresponding Riccati residual coefficient vanishes. The receipt contains the full jet.

A fourth-order jet is not an exact polynomial frame. Convergence and local existence follow from the nonsingular analytic equation; no explicit convergence radius has yet been certified.

## 3. Continuation does not preserve exact C3 or unit modulus

The induced two-by-two step has

    trace T(epsilon) = -1 - 2 epsilon + O(epsilon^2),
    det   T(epsilon) =  1 + (5/2) epsilon + O(epsilon^2).

The checker also verifies that the first derivative of T^2+T+I is nonzero. Therefore the moving plane does not retain the unchanged oscillatory C3 step merely by being invariant.

For real z sufficiently close to one, the selected eigenvalues remain a nonreal conjugate pair. Their common modulus is

    |lambda| = sqrt(det T)
             = 1 + (5/4)(z-1) + O((z-1)^2).

Thus even a local interpretation as a phase-only change would require an additional amplitude normalization. This calculation does not authorize that normalization, attach a physical inner product or identify z with time or frequency. Selecting a moving invariant subspace is not itself a native preparation mechanism.

## 4. Exact candidate collision locus

An independent Sylvester-determinant computation gives the quartic discriminant

    Delta(z)=z^15 * (
        4z^7 - 8z^6 - 23z^5 + 36z^4
        - 2z^3 + 36z^2 - 27z - 256).

At z=1, Delta=-240, consistent with the separated base spectrum. Its zeros are the candidate locus of full-spectrum collisions.

They are **not automatically singularities of the selected rank-two plane**. Two eigenvalues inside that plane may collide while its span remains separated from the complementary pair. Conversely a graph-coordinate chart may become singular even when the underlying subspace remains well-defined. These possibilities must be checked separately.

No global rational factorization, global rank-two frame, real-parameter collision classification or bundle monodromy result is claimed here.

## 5. Updated conjecture-net gate

**Positive result:** the reference plane has a unique local analytic invariant continuation in the checked four-dimensional graded family.

**Boundary:** its reference phase and modulus are not preserved, and no physical clock or source weighting follows from analytic continuation.

The next executable task is to track this selected sector along positive real z. Isolate the discriminant roots, identify which eigenvalues collide, and distinguish internal collisions from loss of separation from the complementary sector. Do not turn the full discriminant into a false no-go for the plane itself.

The supplied dictionary/control, correlated input preparation, retained rejection records, physical metric and independent photon outputs remain open. Existing work-net contracts and formal outcomes are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_moving_boundary_plane.py
python research/scattering/seed-composition/check_moving_boundary_plane.py --check
python research/scattering/seed-composition/check_graded_boundary_transport.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker uses only standard-library exact rational/polynomial arithmetic. It independently verifies the characteristic polynomial, Sylvester discriminant, invertible graph linearization and Taylor identities. It writes only its own receipt; `--check` compares read-only. The analytic implication uses the stated standard theorem, not a claim of new machine-formal proof admission.
