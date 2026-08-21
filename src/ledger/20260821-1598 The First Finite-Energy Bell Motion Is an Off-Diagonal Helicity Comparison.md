# 1598 — The First Finite-Energy Bell Motion Is an Off-Diagonal Helicity Comparison

Date: 2026-08-21

Sequence claim: `seqclaim-499b3d677672d450adb99d80`

## Result

The parity-even photon EFT basis through six derivatives types the first
higher-energy correction as

\[
\Phi_1=g_2s^2+g_3s^3,
\qquad
\Phi_2=f_2(s^2+t^2+u^2)+f_3stu,
\qquad
\Phi_5=h_3stu.
\]

At the transverse angle, the exact lower Bell-saturation branch is

\[
r_-(s)=\frac23\left[
(1+as)\left(\sqrt2-
\sqrt{1-\frac{h^2s^2}{8(1+as)^2}}
\right)-\frac14bs
\right],
\]

where

\[
a=\frac{g_3}{g_2},\qquad
b=\frac{f_3}{g_2},\qquad
h=\frac{h_3}{g_2},\qquad
r=\frac{f_2}{g_2}.
\]

Its expansion begins

\[
\boxed{
r_-(s)=\frac23(\sqrt2-1)
+s\left[
\frac23(\sqrt2-1)\frac{g_3}{g_2}
-\frac16\frac{f_3}{g_2}
\right]
+\frac{s^2}{24}\left(\frac{h_3}{g_2}\right)^2
+O(s^3).
}
\]

Therefore the first finite-energy displacement is not controlled by a single
Wilson coefficient. It is the off-diagonal comparison between the (g_3)
and (f_3) helicity sectors. The mixed-helicity coefficient (h_3) is absent
at linear order and first raises the boundary quadratically.

This sharpens Entry 1595's universal sensitivity statement using the actual
source-typed EFT basis. The separate angular audit was subsequently completed
in Entry 1599.

## Evidence

- Dutta Chowdhury et al., arXiv:2112.11755v4, Appendix F.
- `research/nima/check_photon_d10_bell_boundary.py`
- `research/nima/results/photon-d10-bell-boundary.json`
- `research/nima/photon-d10-bell-boundary.md`
- epistemic-graph event:
  `ev-000000001779-c298edb2-0ba4-4858-b263-3e2d22cd1338`.
