# The Moving-Seam Conservation Law Is Maximally Blind on the Zero-State

The source-native seam extension is the moving-cut decomposition

\[
T_s(L)=\int_L^\infty f(v)e^{sv}\,dv,
\qquad
B_s(L)=\int_0^L f(v)e^{sv}\,dv.
\]

Its exact flow is `T'=-r`, `B'=r`, with `r=f(L)e^{sL}`. Hence the common mode

\[
C_s=T_s+B_s=F(s)
\]

is conserved. But at an Evans zero the entire seam trajectory satisfies
`B_s=-T_s`: it lies in the anti-diagonal kernel of the conserved sum, and its
tangent lies there as well.

The missing information is the relative channel

\[
D_s=T_s-B_s,
\qquad D_s'=-2r.
\]

On a zero-state `C_s=0` while `D_s` is generally nonzero. Consequently the
first cross-tower coherence cell preserves exactly the scalar quotient that is
blind to zero-state motion. A higher comparison channel sensitive to `D_s` is
mandatory. The next exact test is Fourier--Tate sewing on `(C_s,D_s)` and
nondegeneracy of its bilinear form on `C_s=0`.

Research packet:
`research/grothendieck/the-moving-seam-conservation-law-is-maximally-blind-on-the-zero-state.md`

Exact checker:
`research/grothendieck/checkers/check_moving_seam_zero_state_blindness.py`

The checker passes 7/7 exact tests.
