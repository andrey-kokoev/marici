# Photon dimension-ten Bell-boundary packet

## Question

Which first higher-derivative photon EFT coefficients move the Bell-violation boundary obtained at dimension eight?

## Source-typed amplitude

The parity-even photon basis through six derivatives is

\[
\Phi_1=g_2s^2+g_3s^3,
\qquad
\Phi_2=f_2(s^2+t^2+u^2)+f_3stu,
\qquad
\Phi_5=h_3stu.
\]

Write

\[
a=\frac{g_3}{g_2},\quad
b=\frac{f_3}{g_2},\quad
h=\frac{h_3}{g_2},\quad
r=\frac{f_2}{g_2}.
\]

At the transverse angle, (t=u=-s/2), and therefore

\[
z=\frac{\Phi_2}{\Phi_1}
=\frac{\frac32r+\frac14bs}{1+as},
\qquad
c=\frac{\Phi_5}{\Phi_1}
=\frac{\frac14hs}{1+as}.
\]

For real coefficients the normalized Bell readout is

\[
I=\frac{4\sqrt2z}{1+z^2+2c^2}.
\]

## Exact lower saturation branch

The lower positive solution of (I=2) is

\[
z_-=\sqrt2-\sqrt{1-2c^2}.
\]

Consequently the exact transverse coefficient boundary is

\[
r_-(s)=\frac23\left[
(1+as)\left(\sqrt2-
\sqrt{1-\frac{h^2s^2}{8(1+as)^2}}
\right)-\frac14bs
\right].
\]

Its small-energy expansion is

\[
r_-(s)=\frac23(\sqrt2-1)
+s\left[
\frac23(\sqrt2-1)\frac{g_3}{g_2}
-\frac16\frac{f_3}{g_2}
\right]
+\frac{s^2}{24}\left(\frac{h_3}{g_2}\right)^2
+O(s^3).
\]

Thus the infinitesimal boundary motion is controlled by one typed comparison between the (g_3) and (f_3) sectors. The mixed-helicity (h_3) sector is invisible to first order and raises the lower threshold only quadratically.

## All-angle promotion

Put (p=x(1-x)), so (0\le p\le1/4). The exact lower threshold at fixed (p) is

\[
r_-(p,s)=\frac{(1+as)L(p)-bsp}{2(1-p)},
\qquad
L(p)=\sqrt2-\sqrt{1-2k^2p^2},
\qquad
k=\frac{hs}{1+as}.
\]

After multiplying its derivative by the positive factor (2(1-p)^2), its sign is the sign of

\[
(1+as)\left[L(p)+\frac{2k^2p(1-p)}{\sqrt{1-2k^2p^2}}\right]-bs.
\]

The bracket is increasing because its derivative is

\[
\frac{2k^2(1-p)}{(1-2k^2p^2)^{3/2}}\ge0.
\]

Therefore, on the explicit domain

\[
1+as>0,qquad
1-2k^2p^2>0,qquad
bs<(1+as)(\sqrt2-1),
\]

the threshold increases throughout (0\le p\le1/4). Its maximum is exactly the transverse point. Thus the transverse formula above is the all-angle lower Bell boundary throughout this controlled EFT neighborhood.

## Reproduction

Run:

```text
/home/andrey/miniforge3/envs/sage/bin/python research/nima/check_photon_d10_bell_boundary.py
```

The result packet is `research/nima/results/photon-d10-bell-boundary.json`.
