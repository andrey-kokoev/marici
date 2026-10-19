# Interaction continuation — iteration 6: bound modes versus incoming scattering

## Quantitative follow-up

Iteration 7, `native-port-retained-weights.md`, now supplies certified bound
spectral weights including the infinite tails, and exact bandwidth/contact
controls. The fixed-law spectrum below remains valid; retention is not forced
independently of that environmental law.

## Result

The declared lead-coupled interface has **five distinct square-summable bound
modes above its lead band [0,4]**. They are certified by exact metric inertia,
not a finite-chain approximation or floating eigensolver.

| Preparation sector | Approximate bound energies |
|---|---|
| Symmetric | 7.4651524, 25.6917416 |
| Antisymmetric | 7.2159150, 9.7244532, 25.6916735 |

Every value has a rational certified interval of width at most 10^-7. All five
intervals are disjoint, including the close pair near 25.6917.

All **19 exact checks** pass. The retained source is the stationary, one-excitation
port fixture of iterations 4–5, not a physical particle binding model.

## 1. Why incoming flux conservation did not settle retention

Iteration 5 normalized incoming propagating lead waves. That does not imply
that an arbitrary initially localized central excitation eventually leaves.
A time-independent self-adjoint operator can have both propagating continuum
states and localized bound states. They are different spectral subspaces.

This audit finds the discrete subspace and certifies which named central
preparations overlap it. It does not compute the numerical retained probability
weights yet.

## 2. Exact decaying lead solution

For an energy above the lead band, parameterize

    E = 2+r+1/r,    0<r<1.

The outgoing decaying branch has eta=-r. A central port amplitude u_j continues
into the lead as

    psi_(j,n) = (-r)^n u_j.

Eliminating these tails gives the nonlinear secular equation

    M(E)u = [E I-K-(1+r)P]u = 0.

The full state is square summable, with norm

    ||u||_central^2
      + [r^2/(1-r^2)] sum_j h_j |u_j|^2.

The tail contribution must be included when normalizing a bound eigenvector or
calculating overlap probabilities. A unit-normalized central vector alone would
not be a unit-normalized state of the lead-coupled system.

## 3. Global counting by monotone inertia

Since

    dr/dE = -r^2/(1-r^2),
    dM/dE = I + [r^2/(1-r^2)]P,

the secular matrix is strictly increasing in energy in the positive source
metric. Each eigenvalue crossing is upward. This supplies a global root count,
including multiplicity, rather than a scan that might miss roots.

At the upper threshold E=4 (r=1), the full weighted secular matrix has inertia

    (positive, negative, zero) = (6,5,0).

At r=1/32, E=1089/32, its inertia is

    (11,0,0).

Strict monotonicity excludes further roots above that upper cutoff. Therefore
there are exactly five above-band bound modes. Exact congruence elimination
handles positive, negative and zero pivots, including off-diagonal pivot cases.

## 4. Symmetric and antisymmetric preparation blocks

The previously retained joint generator splits into two metric-orthogonal
invariant spaces:

- dimension 5, containing the belt character and the carrier-character sum;
- dimension 6, containing the carrier-character difference.

The lead contact projector preserves both spaces. Their active port ranks are
two and one, respectively. Exact restriction confirms that the lead elimination
respects the same decomposition; this is not inferred from input names alone.

Their threshold negative counts are two and three. Adaptive rational brackets
isolate one root per interval. All endpoints are nonsingular, and root counting
is exact at every subdivision. Midpoints in the table are merely readable
approximations of these certified intervals.

## 5. Which internal preparations overlap the bound modes?

| Initially localized central preparation | Bound modes with nonzero overlap |
|---|---:|
| Native belt character | Both symmetric modes: **2** |
| Sum of carrier characters | Both symmetric modes: **2** |
| Difference of carrier characters | All antisymmetric modes: **3** |
| Proton-port character alone | **5** |
| Electron-port character alone | **5** |

This establishes a strictly nonzero retained bound-state component for each
listed nonzero preparation. It does not establish its magnitude or that all of
the input is retained.

### Overlap certificates

For each simple root in its preparation block, inspect the principal minor that
removes an active port coordinate. That minor is also strictly monotone in E.
Its inertias agree at both ends of the root bracket, with no zero direction.
Thus it is nonsingular throughout the bracket, including at the full root.
The corresponding diagonal cofactor is nonzero, proving that the bound mode has
nonzero amplitude at that port.

The belt vector is exactly orthogonal to the entire antisymmetric block. Each
individual carrier vector is half the sum, plus or minus half the difference.
Orthogonality of the blocks prevents cancellation of their spectral overlaps.

A claim that every internal excitation must scatter completely is therefore
false for this fixture, despite the earlier exact unit-flux scattering matrix.

## 6. No below-band negative-energy bound state

The whole lead/contact quadratic form is positive. More directly, below the
band use 0<r<1 and E=2-r-1/r<0. The secular matrix is

    E I-K-(1-r)P,

which is strictly negative in the positive metric. It has no zero vector.
Exact representative controls also pass.

The five localized modes are therefore **above-band modes**, not negative-energy
binding below a vacuum reference. Their existence depends on the finite-band
lead law. Wider bands or additional multi-object decay channels can change this
conclusion and must not be assumed absent in a physical interpretation.

## 7. Thresholds are not ordinary bound states

At E=0, the central K has a one-dimensional nullspace. Its port projection is
nonzero. The corresponding lead tails are constant, not square summable.
This is a bounded **threshold resonance**, not a normalizable stored mode.

At E=4, the secular matrix is nonsingular. There is no corresponding bounded
threshold mode of this coupled fixture.

Inside (0,4), an L2 lead solution would have zero propagating amplitudes. It
would require an invisible central eigenvector. The previous cyclic-closure
certificate excludes such an eigenvector in the coupled eleven-state space.
This statement does not remove independent spectator modes from the larger
retained model.

## 8. Zero-energy scattering limit

Let v be the central zero mode and v_P its port projection. Near k=0,

    M(E) = -K + i k P + O(k^2).

The simple zero mode gives the limiting coefficient scattering matrix

    S_0 = I - 2 v_P v_P^* H_port/(v_P^* H_port v_P).

This is a metric Householder reflection. Its metric unitarity and probability
normalization are checked exactly. For belt incidence, the limiting
probabilities are approximately

    reflection: 0.06762774765,
    each output: 0.46618612617.

These are limits as E approaches zero from the propagating band. At E=0 itself
the group velocity vanishes; this is not a finite-flux probability assignment
that bypasses the threshold restriction in iteration 5.

## 9. What this says about indication or storage

The same conditional interface supports both transport and localized spectral
components. That is closer to a functional question than merely counting holes.
But a nonzero bound component is not yet a protected memory or an indication
mechanism:

- its actual retained fraction has not been calculated;
- superpositions of bound modes accumulate relative phases;
- local occupation can oscillate through interference;
- perturbations, noise, moving ports and additional output sectors have not been
  included;
- high-energy trapping in finite-band leads is not a topology-only prediction.

Incoming asymptotic scattering states do not autonomously populate an orthogonal
bound subspace in this time-independent model. An initially central preparation
can already have bound-state overlap. Capture from an incident wave would need
another admitted operation, time dependence, dissipation, or an additional
energy-exchange channel.

## 10. Next executable continuation

Quantify the bound spectral weight of the named central preparations, using the
full tail-normalized residues rather than central normalization alone. Also test
how the bound-mode count depends on the declared lead bandwidth/contact law.
For leads and contacts scaled together by t, the upper-threshold secular matrix
is

    t(4I-2P)-K.

This gives an exact spectral way to audit whether retention survives opening a
wider continuum. The empirical reaction interpretation, full spinor coupling and
multi-object output dictionary remain separate unresolved obligations.

## Reproduction

```sh
python research/voevodsky/checkers/check_native_port_bound_spectrum.py
```

Receipt: `results/native_port_bound_spectrum.json`, retaining exact source hashes,
inertia counts, rational root intervals, port-overlap certificates, preparation
blocks and the threshold-limit matrix. No numerical retained fraction is claimed.
