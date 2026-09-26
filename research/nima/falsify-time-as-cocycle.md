# Falsifying "time = ∫α" and the Jacobi/cocycle observation

## Jacobi identity and fibration phases: not coincidence

The cocycle condition for the phase lift associativity

\[
\omega(g,hk)+\omega(h,k)=\omega(gh,k)+\omega(g,h)
\]

is **the same structure** as the Jacobi identity \[[X,[Y,Z]]+\text{cyclic}=0\] at the infinitesimal level. This is not an accident—it is a mathematical necessity for any consistent central extension of a group or Lie algebra. Our phase transport cannot be associative without it.

**What this does not prove:** every consistent Poisson manifold and every central extension satisfies Jacobi/cocycle identities. Most have nothing to do with time. The similarity is necessary for a temporal interpretation but far from sufficient.

## Falsification of "time = ∫α"

The candidate clock is the path integral of the connection

\[
\alpha = d\varphi - \frac{\beta}{\kappa},\qquad
\int\alpha = \Delta\varphi - \frac{\Delta F}{\kappa} = -\delta.
\]

Two genuine falsifications emerged.

### 1. Gauge dependence (fatal without source selection)

A canonical transformation adds an exact term to the symplectic potential:
\[
\beta\mapsto\beta+dG,\qquad
\alpha\mapsto\alpha-\frac{dG}{\kappa}.
\]
Then
\[
\int\alpha\mapsto\int\alpha-\frac{\Delta G}{\kappa}.
\]

The path integral changes by a boundary term depending on the canonical gauge. If this is elapsed time, the same trajectory gives different clock readings under different symplectic coordinates.

**The conjecture survives only if the source fixes a preferred symplectic potential.** That is exactly the open product/readout admission gate.

### 2. No canonical connection (fatal without source selection)

Every symplectic potential \(\beta\) defines a different connection \(\alpha\). Our construction used \(\beta = p\,dq+s\,dz\) from the declared Clifford realization. Nothing in the model forces this choice. The source must select it.

**Again the same gate:** source admission of the observable algebra and its symplectic structure.

### Surviving conditional predictions

- **Geometric phase unification:** a horizontal loop (\(\alpha=0\)) gives \(\oint\alpha = -\text{area}/\kappa\), which is purely geometric. A dynamical trajectory gives the same type of integral. This is a nontrivial prediction—same \(\kappa\) for both—but requires both protocols to be source-admitted.
- **Orientation:** odd elements flip the sign of \(d\varphi\) in \(\alpha\). This is consistent if orientation is part of the temporal structure (time reversal).
- **Unit scaling:** ordinary conventional dependence, not a physical failure.

## What does NOT falsify it

- **The Jacobi identity:** structurally necessary, temporally silent.
- **Winding ambiguity:** solved by retaining the unwrapped history.
- **Frame erasure (original Test 2):** the integral of \(\alpha\) is geometrically invariant; the earlier confusion was between coordinate expression and geometric object.
- **\(\kappa\) being uncalibrated:** genuine parameter, not a contradiction. A horizontal loop protocol could fix it.

## Bottom line

The conjecture has a plausible candidate (\(\int\alpha\)) and two surviving physical tests (geometric phase, orientation). But its **strongest falsification is gauge dependence**, and that points to the same unresolved gate: the source has not admitted the symplectic gauge, product or observable algebra.

Until it does, the mathematical clock exists conditionally in our declared model but is not source-derived physical time.

**Verification:** `research/nima/try_falsify_time_as_cocycle.py` — exact symbolic checks for each test.