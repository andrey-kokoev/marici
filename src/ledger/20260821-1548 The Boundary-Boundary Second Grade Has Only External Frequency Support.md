# 1548 — The Boundary--Boundary Second Grade Has Only External Frequency Support

## Hard-to-vary claim

After restoring the source scale factor \(a_0^2\), the exact
boundary--boundary sector at order \(\eta_0^2\) has frequency support

\[
\boxed{\{-2p,0,2p\}}.
\]

No phase involving the internal momenta \(q\) or \(k\) survives.

## Derivation

Expand each factor as a finite Laurent--exponential sum in \(\eta_0\):

- two boundary weights \(a_0^2C_K\);
- two external Wightman functions;
- the two equal-time internal Wightman functions.

Multiplication is performed while preserving the integer frequency label.
Equal labels are combined only after the complete four-branch sum.

At a generic kinematic sample, the quadratic-grade coefficients are

\[
c_{-2p}=-0.439721471588898+0.00129575843102391i,
\]

\[
c_0=0.879446761472728,
\]

\[
c_{2p}=-0.439721471588898-0.00129575843102391i.
\]

Thus

\[
c_{-2p}=c_{2p}^*,
\qquad c_0\in\mathbb R,
\]

and the sector is real.

These values include the common spatial factor
\((p^2+q^2+k^2)^2\) and the boundary--boundary perturbative weight
\(-\tfrac12\). The original checker version omitted both factors; that
omission changed the displayed normalization but not the support or reality
claims.

## Artifacts

- `research/benincasa/checkers/finite_time_boundary_boundary_grade.rs`
- `research/benincasa/results/finite-time-boundary-boundary-grade.json`

## Narrow conclusion

The first exact \(\eta_0\)-graded sector has the frequency type required by
Eq. (19).  This does not prove the Eq. (19) coefficient: the mixed and
bulk--bulk grade packets must still be added, and only their sum can be tested
against the \(J_i\) combination.

## Next falsifier

Compute the two mixed-sector grade packets with the same labelled algebra.
Require cancellation of every frequency outside \(\{0,\pm2p\}\) before
combining with the bulk--bulk endpoint expansion.
