# Covariance tomography fixes a projection, not automatically the full observable

## Fresh source boundary

Read ledger2215 and2216 against ledger2218/2219 and2231. They supply normalized response identities and contact-normal mixed readouts, while warning about raw backgrounds and operational scope. The inspected statements do not specify a unique full Gaussian L2 representative of the projected contact observable.

Use independent baseline real coordinates X_i with variance1 and deformed variances g_i. This is the normalized three-mode model, not an assertion that arbitrary polynomials below are admitted cosmological operators.

## Canonical lift of the actual contact polynomial

For missing edge i and remaining j,k, define

    O_C=8C X_j^2 X_k^2(1-X_i^2).

Then for every positive diagonal covariance,

    E_g O_C=8C g_j g_k(1-g_i).

At baseline g=1, E O_C=0 and

    ||O_C||_2^2=64 C^2 *3*3*(1-2+3)=1152 C^2.

Since S_i=(X_i^2-1)/2,

    O_C=-16C S_i(1+2S_j)(1+2S_k).

Thus O_C lies in the complete finite product-score span. The preceding tower calculation is exactly its full L2 norm, not just a lower bound for this particular lift. For this lift every test L with uniformly bounded L2 norm has |E(O_C L)|<=sqrt(1152)|C| ||L||, which vanishes at contact infinity.

## Severe ambiguity: even the whole diagonal covariance family can miss a component

Let Z=X_i X_j. Every centered independent diagonal Gaussian has E_g Z=0, while baseline ||Z||_2=1. Also Z is orthogonal to every function even separately in each coordinate, including O_C and all covariance scores. Hence

    E_g(O_C+Z)=E_g O_C for all g,
    ||O_C+Z||_2^2=1152 C^2+1,
    E((O_C+Z)Z)=1.

Even global field-sign parity does not remove this example: Z is even under simultaneous sign reversal. Separate coordinate parity, or a source constraint of comparable strength, is needed. This does NOT prove that Z is allowed by momentum conservation, the contact-normal channel or the original physical action. It proves that Gaussian response identities alone cannot exclude it.

There is also a weaker finite-tower ambiguity within the separately even sector. H4(X_i)=X_i^4-6X_i^2+3 is orthogonal to every square-free product score in the eight-slot tower, has squared norm24, but E_g H4=3(g_i-1)^2. Thus eight moments alone do not establish uniqueness even after imposing separate parity. The entire covariance-family identity is stronger than finite first-per-edge moments.

## Conditional uniqueness theorem

If a source supplies BOTH (a) a separately even baseline L2 observable and (b) its full expectation identity E_g O=8C g_j g_k(1-g_i) on an open covariance neighborhood, then O=O_C almost everywhere.

Proof: apply the identity to the difference. Gaussian likelihood ratios for variances near1 and all their derivatives belong to baseline L2. Differentiating yields orthogonality to all products of even Hermite polynomials. These are complete in the separately even Gaussian L2 subspace, so the difference vanishes. This is a written analytic argument; the finite checker verifies examples, not Hermite completeness.

For a general observable the same argument identifies only its projection onto that separately even subspace. Its orthogonal complement remains unobserved by diagonal covariance variation.

## Decision

The all-bounded-test obstruction is proved for the canonical lift and, conditionally, for a source-certified separately even full-family lift. It is NOT yet proved for the complete physical observable. The finite-tower obstruction remains valid without promoting it to this stronger claim.

Next locate a primary-source contact-normal operator lift and its symmetry/admissibility conditions. Specifically determine whether the source supplies separate parity and the full covariance-family identity at the operator level, or permits a complementary non-covariance port. The explicit Z example is a falsifier of insufficient data, not a proposed physical rescue. No owner artifacts are changed.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_contact_gaussian_lift.py` integrates polynomials by exact Gaussian moments, verifies the canonical lift for arbitrary diagonal covariance, its norm, the invisible Z component and the H4 finite-tower control. It does not authorize either perturbation physically.
