# 1841 — Soft-to-Polar Comparison Requires the Gram Root Cover

## Inertia mismatch

Entry 1836's generic active-soft singular term is

\[
\delta^2\log\delta.
\]

Its semisimple monodromy character is \(+1\); the logarithm supplies a
unipotent extension.

Entry 1840's true polar object scales as

\[
\Omega^{-1/2}
\]

on a generic Gram normal \(\Omega\).  Its semisimple monodromy character is
\(-1\).

Therefore

\[
\boxed{
\operatorname{Hom}_{I}
(\mathcal L_{m soft},\mathcal L_{m polar})=0
}
\]

for ordinary inertia-equivariant maps.  A direct Cartier/Gysin comparison on
the unramified Gram base is mistyped.

## Canonical repair supplied by the coefficient geometry

Pass to the source-defined root cover

\[
z^2=\Omega.
\]

One loop in \(z\) winds twice in \(\Omega\), so the polar character becomes

\[
(-1)^2=+1.
\]

Only on this \(\mu_2\) cover can the soft and polar objects enter the same
semisimple inertia block.  The remaining comparison must retain:

- the Rees/weight shift;
- source residue orientation;
- the \(\mu_2\)-trace back to the Gram divisor.

## Architectural result

No carrier modification is required.  The Gram divisor was already frozen in
Entry 1839.  What is required is a sector-specific coefficient enlargement:

\[
\boxed{
\text{Kummer twist}
+
\text{ramified nearby cycles}
+
\mu_2\text{ trace}.
}
\]

This is precisely the distinction between shared carrier calculus and
sector-specific coefficient characters predicted by H2.

## Next falsifier

Construct the comparison on \(z^2=\Omega\), derive its Rees shift, and push it
down with the normalized \(\mu_2\)-trace.  A surviving trace-independent
cofiber would be the candidate coefficient excess; failure before pullback
would merely repeat the inertia type error.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_soft_polar_monodromy_gate.py`
- `research/benincasa/results/five-site-region-pair-soft-polar-monodromy-gate.json`
- Entries 1836, 1839, and 1840
- allocator claim: `seqclaim-f6a17ef148914ebba71536c3`
