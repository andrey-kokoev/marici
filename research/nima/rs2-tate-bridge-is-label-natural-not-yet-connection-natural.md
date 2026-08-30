# RS-2: the Tate bridge is label-natural, not yet connection-natural

## Established naturality

The canonical bridge

\[
\tau_{\rm Tate}:
I_{\mathbb F_3}/(g-1)I_{\mathbb F_3}
\xrightarrow{\sim}
I_{\mathbb Z}/(g-1)I_{\mathbb Z}
\]

is natural for the frozen \(D_3\) symmetry action. Rotation is trivial and
reflection acts by \(-1\) on both sides. Combined with occurrence forgetting,
this is a genuine map of source label/coinvariant objects.

## Connection-level gate

Entry 764 gives the source-derived cosmological coefficient transition

\[
S(z)=\operatorname{diag}(z^{-2},z^{-1},z,z).
\]

To extend the label bridge by a constant projection of the rank-four
cosmological coefficient fiber to the trivial cyclic road line, a nonzero row
\(\ell\) would have to satisfy

\[
\ell S(z)=\ell
\]

as a generic Laurent-polynomial identity. Since all four weights are nonzero,
the only solution is

\[
\boxed{\ell=0.}
\]

At the equal-energy fixed point \(z=1\), \(S=1\), so every row satisfies the
equation. The fixed fiber therefore supplies no canonical coefficient
projection at all.

## Verdict

\[
\boxed{
\text{canonical label-level Tate bridge}
\not\Rightarrow
\text{horizontal cross-sector coefficient map}.
}
\]

This is not a failure of the bridge. It identifies its exact categorical
home: the shared \(C_3/D_3\) trace/augmentation calculus. The rank-four
Gauss--Manin coefficient object and the filtered road coefficient object
remain sector-specific lenses.

A connection-level comparison requires a source-derived \(z\)-dependent
localization, Gysin functional, or mixed-variance kernel. Choosing a row at
\(z=1\) and transporting it backward would fit precisely the datum that is
missing.

## Programme consequence

The immediate cross-sector result should close at label-level naturality.
The next scientific frontier is not to force a direct map between unrelated
sector bases. It is to test whether the shared trace/augmentation calculus
acts functorially inside each sector's independently derived localization
diagram.

## Durable evidence

- Entries 410, 436, 764, 1552, and 1553;
- research/nima/checkers/check_rs2_tate_bridge_transport_gate.py;
- research/nima/results/rs2-tate-bridge-transport-gate.json.
