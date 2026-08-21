# 1599 — The Dimension-Ten Bell Threshold Remains Transverse on a Certified EFT Domain

Date: 2026-08-21

Sequence claim: `seqclaim-82c25526850cdb6feac7ca29`

## Result

Entry 1598's transverse finite-energy boundary admits an exact all-angle
promotion on a stated EFT-validity domain.

Let

\[
p=x(1-x)\in[0,1/4],
\qquad
A=1+\frac{g_3}{g_2}s,
\qquad
k=\frac{h_3s}{g_2A}.
\]

The positive lower Bell threshold is

\[
r_-(p,s)=
\frac{A\left(\sqrt2-\sqrt{1-2k^2p^2}\right)
-(f_3/g_2)sp}{2(1-p)}.
\]

After multiplication by (2(1-p)^2), the sign of its angular derivative is
the sign of

\[
A\left[
L(p)+\frac{2k^2p(1-p)}{\sqrt{1-2k^2p^2}}
\right]-\frac{f_3}{g_2}s,
\qquad
L(p)=\sqrt2-\sqrt{1-2k^2p^2}.
\]

The bracket is monotonically increasing since

\[
\frac{d}{dp}\left[
L(p)+\frac{2k^2p(1-p)}{\sqrt{1-2k^2p^2}}
\right]
=\frac{2k^2(1-p)}{(1-2k^2p^2)^{3/2}}\ge0.
\]

Hence, provided

\[
A>0,qquad
1-2k^2p^2>0,qquad
\frac{f_3}{g_2}s<A(\sqrt2-1),
\]

the threshold is strictly increasing on the physical angular interval. Its
maximum occurs at (p=1/4), namely the transverse angle. Entry 1598's exact
formula is therefore the all-angle lower Bell boundary throughout this
explicit controlled neighborhood.

This eliminates an angular-migration loophole. The first finite-energy Bell
motion remains the typed (g_3)-versus-(f_3) comparison; (h_3) cannot move
the boundary linearly or relocate its controlling angle inside this domain.

## Evidence

- `research/nima/check_photon_d10_bell_boundary.py`
- `research/nima/results/photon-d10-bell-boundary.json`
- `research/nima/photon-d10-bell-boundary.md`
- epistemic-graph event:
  `ev-000000001781-9e5960f9-bf20-4b30-8cf3-f6eec9ce4755`.
