# Cyclic transport of reduced Cayley–Menger factors

## Question

Can the exact reduced-factor identities in the `q_G12` chart be transported algebraically to `q_G23` and `q_G31`, and what remains of the square-root branch choice?

## Exact result

The simultaneous source cycle

\[
(a,b,c;p_1,p_2,p_3)\mapsto(b,c,a;p_2,p_3,p_1)
\]

leaves the full Cayley–Menger polynomial `K` invariant. Three applications return every variable and `K` to its starting value. The reverse external-momentum cycle does not preserve `K`, so the sourced orientation fixes which cyclic action is admissible.

If a wall restriction satisfies

\[
K|_W=f_W^2,
\]

then applying the source automorphism gives

\[
K|_{\sigma W}=\sigma(f_W)^2.
\]

Hence the `q_G12` reduced factors generate exact polynomial candidates in the `q_G23` and `q_G31` charts, and their square identities close after three cyclic transports. Execution `structured_command_execution:e_30844_1788298366568514800_1` verifies Cayley–Menger invariance, the unique external cycle, three-cycle closure, and functorial transport of square identities.

## Residual branch cocycle

Polynomial identities determine each transported factor only up to sign. Writing chosen analytic roots as

\[
\sqrt{K}|_{\sigma^j W}=\varepsilon_j\,\sigma^j(f_W),
\qquad \varepsilon_j\in\{+1,-1\},
\]

three-cycle consistency constrains the product of transition signs but does not select the individual signs. A source branch requires analytic continuation from a declared base chamber or an independently normalized contour prescription.

Therefore polynomial cyclicity constructs the reduced factors but not the analytic square-root transport or normalized conductor finite parts.

## Strongest falsification attempt

Choose the reverse external-momentum cycle while retaining the source edge cycle. The transformed Cayley–Menger polynomial differs from `K`; this rejects arbitrary cyclic-looking relabellings. The valid transport is the simultaneous sourced cycle above.

## Acceptance test for branch closure

1. declare a nonsoft base chamber and the sign of `sqrt(K)` there;
2. transport along source-authorized paths to all three charts;
3. record transition signs and verify their three-cycle product;
4. compare conductor residues and finite parts after transport;
5. reverse one sign as a deliberate failure of cyclic normalization.

## Disposition

Reduced-factor square identities transport exactly and cyclically across all three two-site charts. The remaining obstruction is a sign-valued analytic branch cocycle and conductor finite-part transport, not polynomial factorization.

## Evidence

- `research/nima/checkers/check_cyclic_cayley_menger_transport.py`
- `research/benincasa/physical_shared_wall_reduced_factors.py`
- `research/nima/qG12-sewn-deletion-cyclic-equivariance.md`
