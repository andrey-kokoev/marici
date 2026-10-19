# The positive-axis collision is internal: the plane survives, but a positive-unitary step does not

**Iteration 6 of the requested ten-turn work-net run.**

**Strength:** exact real-root isolation and cyclicity certificates, with standard spectral-projector continuation. Not a physical parameter calibration, global graph-coordinate formula or source metric derivation.

[Previous local plane](MOVING-BOUNDARY-PLANE.md) · [Checker](check_positive_spectral_collision.py) · [Receipt](results/positive-spectral-collision.v1.json)

## 1. Fresh polynomial family

The checked graded four-carrier has characteristic polynomial

    chi(lambda,z)=lambda^4-z^4 lambda^2-(z^4+z^5)lambda-z^5.

At z=1, its selected pair is the reference omega/conjugate-omega pair; the complementary roots solve lambda^2-lambda-1=0. A local moving rank-two plane already exists. This turn tests its continuation along the positive real z-axis.

No identification of z with physical time, energy or frequency is made.

## 2. Exactly one positive collision parameter

For z>0, zeros of the discriminant are zeros of

    d(z)=4z^7-8z^6-23z^5+36z^4-2z^3+36z^2-27z-256.

The exact Sturm sequence has degrees 7,6,5,4,3,2,1,0. Its sign variations are three at zero and two at positive infinity. Hence d has exactly **one positive root**, z_c. The constant final remainder also proves d is squarefree.

Rational bisection with Sturm counts isolates it in

    49381557/16777216 < z_c < 24690779/8388608,

an interval of width 1/16777216. For display only,

    2.9433701634 < z_c < 2.9433702231.

The decimal values are not the certification; the rational interval and exact root counts are.

## 3. Identify which roots meet

Two useful exact identities hold for every z>0:

    chi(-1,z)=1,
    chi(0,z)=-z^5<0.

There is always a root in (-1,0). Descartes' sign rule gives exactly one positive root, counting multiplicity. Exact quartic Sturm counts at z=1 and z=2 show one negative root in (-1,0), one positive root and a nonreal conjugate pair. At z=3 they show two further negative roots below -1.

There are no other positive discriminant zeros, and no eigenvalue can cross -1 or zero. A simple discriminant zero represents one ordinary double-root collision, not a triple root or two simultaneous double collisions. Together these facts identify the sectors throughout the positive axis:

| Parameter range | Selected sector | Complementary sector |
|---|---|---|
| 0<z<z_c | One nonreal conjugate pair | One root in (-1,0), one positive root |
| z=z_c | A double negative root below -1 | The same two simple, separated roots |
| z>z_c | Two distinct negative roots below -1 | One root in (-1,0), one positive root |

Thus the collision is **inside the selected pair**. It is not a collision between that pair and its complement.

## 4. The selected plane continues on all z>0

At every positive z, the selected two-root cluster is separated from the complementary roots. A contour enclosing that cluster defines a local analytic Riesz projector, including at the internal double root. Patching these local projectors along the positive interval continues the original rank-two plane as a real-analytic subspace on **all z>0**.

This uses the full generalized eigenspace at the double root, not two falsely assumed independent eigenvectors. The individual eigenvalues/eigenvectors do not remain analytic through the ordinary collision.

No uniform spectral gap as z approaches zero or infinity is claimed. No extension through z=0 is claimed. Nor does this prove that the original graph chart (I;X(z)) works globally: a chart may fail while the underlying subspace remains regular. Complex-parameter global monodromy is outside this positive-axis result.

## 5. The collision has a genuine Jordan block

The checker forms exact Krylov matrices from the actual four-by-four M(z). For the second coordinate vector, its determinant is

    det[e_2, M e_2, M^2 e_2, M^3 e_2]
        = -z^6 (z-1)^2 / 8.

It is nonzero at z_c, since z_c lies between two and three. Thus M(z_c) is cyclic: its minimal polynomial equals its characteristic polynomial. The double selected root therefore has a nontrivial two-by-two Jordan block.

This produces a useful boundary independent of coordinate chart:

- At z_c, no nonzero scalar rescaling can make the selected step unitary in any positive-definite inner product. Such an operator would be diagonalizable, but scalar rescaling does not remove the Jordan block.
- Above z_c, the selected eigenvalues are distinct negative reals with different magnitudes. One scalar cannot put both on the unit circle.

These statements do not identify a physical metric or reject every possible altered evolution law. They concern scalar normalization of the existing selected step in a positive-definite metric. Indefinite forms and other source operations are different questions.

## 6. Updated gate

The earlier local plane now has a justified positive-axis continuation. The full discriminant was not a reason to discard it. But persistence of a plane is weaker than persistence of an oscillatory or positive-unitary mode.

The next executable test lies on 0<z<z_c: examine whether determinant normalization admits a conditional positive invariant metric, how that metric degenerates near z_c, and which parts would be additional supplied structure rather than a native source metric. Keep the distinction between constructing such a conditional metric and deriving a physical norm or clock.

The dictionary/control, correlated preparation, retained residuals, geometry and independent physical outputs remain open. Existing work-net contracts and formal outcomes are unchanged.

## Reproduce

```sh
python research/scattering/seed-composition/check_positive_spectral_collision.py
python research/scattering/seed-composition/check_positive_spectral_collision.py --check
python research/scattering/seed-composition/check_moving_boundary_plane.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The checker uses exact rational polynomial division, Sturm counts and Krylov determinants. It recomputes the preceding polynomial family and writes only its own receipt. `--check` compares read-only. The analytic projector consequence uses the stated standard spectral argument; no machine-formal or physical admission is claimed.
