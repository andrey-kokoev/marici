# Opposite circulation gives a neutral paired belt

## Computed result

For the tested mode-derived radial flux:

| Mode configuration | Flux |
|---|---:|
| Original outward proton mode | +1 |
| Complex-conjugated proton mode | −1 |
| Original all-same-branch belt | approximately +0.496291453572 |
| Belt with opposite circulation in every paired sector | exactly 0 |

The neutral belt keeps its **1836-arrow intrinsic core**: L=432, G=108, N=1296. It retains one coherent collective mode and the positive fixed-weight deletion certificate.

The working distinction is **opposite circulation**, not the openings by themselves.

## Observable and its source

For each generated small triangle (F,a,b), write its existing cyclic mode as

```text
v = F + ω a + ω² b = r + i sqrt(3) s,
r = F − (a+b)/2,
s = (a−b)/2.
```

The exact identity

```text
r × s = ((a−F) × (b−F))/2
```

identifies the mode bivector with the triangle's oriented area. Thus the local orientation is read from the coefficient mode rather than separately assigned to a named particle.

The tested flux is the oriented solid angle divided by 4π, using the radial field x/|x|³ about the common center, at unit collective amplitude. More generally, for local field w=r_w+i sqrt(3)s_w and reference area A_t, its contribution is

```text
Q_t(w) = Ω_t/(4π) × A_t·(r_w × s_w)/|A_t|².
```

This is a declared quadratic flux observable. It is not an independently derived electromagnetic field equation or a claim that the unprojected flux operator has the coherent state as an eigenvector.

Multiplying a local mode by a phase cannot change the sign: its bivector is multiplied by |z|². Complex conjugation does reverse the bivector. Therefore phase offsets alone cannot neutralize the original all-positive belt.

## Why the original belt was not neutral

All six outward belt faces have positive radial solid angle. Their total is about 0.496291453572 of 4π. The two omitted cap cones account for the remainder.

The ordinary vector-area sum is zero for both the closed proton and the belt, so it does not distinguish the two. Nor does simply leaving the caps open make the radial flux zero.

## The alternating belt rule

The shared-face adjacency of the six tetrahedral belt pieces is C6. Requiring opposite circulation across every shared face has exactly two +/- solutions, exchanged by overall reversal:

```text
faces 0,1,2: − ; faces 3,4,5: +,
or the opposite assignment.
```

These are the actual face indices of the checked geometry. Every one of the three adjacent-face sector pairs contains one + and one − member. The six faces are congruent under the exact proper rotation group, hence have equal solid angles. Each pair cancels exactly, independently of decimal evaluation of the angle.

The proton's four-piece shared-face adjacency is K4. It contains odd cycles and admits no assignment alternating across all six interfaces. This is a structural distinction between the carriers. It does not by itself select the proton's original positive branch; that branch remains the source's specified cyclic mode.

## Coherent neutral implementation

Conjugate all three small-triangle modes on each negatively signed face. In the intrinsic representation, the geometry, orthonormal plane frames and denominator factors remain unchanged; only the selected coordinate numerators change.

The 120-degree spatial rotation preserves the assignment, so all three paired sectors still have identical twelve-coordinate reference vectors. Rebuild L and N from this reference and retain the existing alignment G. Exact computation verifies

```text
GL = LG = N,
N² = N,
rank(N) = 1.
```

No support disappears. Of the existing coefficients, 180 L coefficients and 540 N coefficients change; G is unchanged. All 1836 transfers retain their positive closed-cycle deletion certificate.

The old local selectors reject the conjugated modes on all nine affected small triangles. The opposite-circulation state is therefore a new branch choice, not a hidden rephasing of the old one. Its count is the intrinsic core count; the previously counted ambient conversions are unchanged in support.

## What is now specified, and what remains

We have a precise cancellation mechanism compatible with the six-piece geometry and the (3,12) coherent return. The branch pattern can be obtained from the connected shared-face graph once the alternation rule is declared.

The remaining generation question is whether the endpoint/gluing protocol itself requires opposite branches on those interfaces. That requirement is not in the old all-same-branch constructor; this experiment adds and tests it explicitly.

## Verification

```text
python research/voevodsky/checkers/check_mode_flux_charge.py
```

Sixteen checks pass. Area, branch, adjacency, operator and cancellation identities use exact arithmetic; the displayed nonzero belt flux uses numerical solid angles. The zero result is certified by equal-face rotation witnesses and the exact signed count, not rounding.

Artifacts:

- `results/mode_flux_charge.json`
- `results/opposite_branch_belt_store.json`

Existing source artifacts remain unchanged.
