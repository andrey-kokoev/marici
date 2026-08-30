# Radial-mass collision splits a positive one-atom source off seam

## Minimal positive family

Take the one-atom positive half-source

`rho_m=m delta_1`, with `m>0`.

Its faithful coordinates are

`M_m(z)=m cosh z`,

`N_m(z)=m sinh z`,

`S_m(z)=1/2+m(z^2-1/4)cosh z`,

`A_m(z)=m(z^2-1/4)sinh z`.

Reciprocity, positivity, the Lorentz conic, and the hyperbolic-to-Fourier Wick
rotation hold for every positive `m`.  Only the radial normalization changes.

## Exact seam collision

On the seam `z=i tau`, a double scalar zero satisfies

`1/2-m(tau^2+1/4)cos tau=0`

and

`2tau cos tau-(tau^2+1/4)sin tau=0`.

The first positive noncentral solution is

`tau_*=1.00960335011549266...`,

`m_*=0.74017432572687309...`.

This is the collision at which a reciprocal pair of seam zeros changes
orientation.  Lowering the radial mass to `m=1/2` produces the explicit
off-seam zero

`z=0.43157676846226198-1.07873572392581855 i`.

It lies inside `|Re z|<1/2`.  Its antisymmetric port is

`A=-0.57818682243820985+0.49415749887908327 i`,

whose forbidden real quadrature is large.

## What this isolates

No multi-atom interference is required to violate confinement.  A single
positive rapidity ray already leaves the seam when its radial mass crosses a
source collision threshold.  Therefore:

- positivity does not select the radial normalization;
- the Lorentz conic does not prevent the collision;
- rapidity linearity `chi=z` does not prevent it;
- the missing theta law must constrain radial mass relative to the fixed
  completion carrier `C=1/2`.

This is a cleaner hostile than perturbing the shape of `rho`: it changes one
scalar source parameter and preserves every kinematic identity.

## Optical experiment

Program a single log-delay mode and sweep its coherent weight `m`.  Track the
three-port zeros as `m` passes through `m_*`:

- at the threshold, the scalar port has a double seam null;
- below threshold, the nulls form an off-seam reciprocal-conjugate quartet;
- the real quadrature of `A` turns on as the radial witness;
- the control port remains fixed by the completion carrier.

This is a directly falsifiable exceptional-point experiment.  It models the
precise failure mode that a theta-specific radial conservation law must
forbid.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_one_atom_radial_mass_collision.py
```
