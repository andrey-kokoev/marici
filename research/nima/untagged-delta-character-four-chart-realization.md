# Untagged delta/character realization of the four-chart Catalan carrier

Even Gaussians remove channel tags within each chart but collapse Fourier square to the identity. They therefore retain only `C2`. A faithful untagged `C4` model is obtained from point masses and their Fourier characters.

Assign to every channel `d` the positive integer

\[
x_d=2^{\iota(d)}.
\]

For a triangulation `T`, set

\[
S_T=\sum_{d\in T}x_d.
\]

Binary uniqueness makes `T -> S_T` injective. In chart zero, convolution of channel atoms is

\[
R_0(T)=*_{d\in T}\delta_{x_d}=\delta_{S_T}.
\]

With Fourier convention `F(delta_x)=chi_{-x}`, the four charts are

\[
\delta_{S_T}
\xrightarrow{\mathcal F}
\chi_{-S_T}
\xrightarrow{\mathcal F}
\delta_{-S_T}
\xrightarrow{\mathcal F}
\chi_{S_T}
\xrightarrow{\mathcal F}
\delta_{S_T}.
\]

Pointwise multiplication of characters adds frequencies, so the odd charts realize the same channel union law as the convolution of deltas in the even charts. Every tree has a full four-element analytic orbit, and different trees have disjoint orbits.

This realizes the **four-chart enlargement** `C4 x H_n`, not merely the polygon-rotation representation on `H_n`. A half-turn-symmetric triangulation can have a size-two polygon orbit while still carrying four distinct presentation phases. This matches the eight-lattice separation between chart index and geometric lattice coordinate.

`check_untagged_delta_character_c4_realization.py` verifies at `n=4,8,12`:

- no channel tags;
- no collisions between triangulations;
- exact Fourier transport;
- full length-four chart orbits;
- 67,184 distinct analytic states at `n=12`.

The construction lives naturally on the Schwartz/tempered-distribution rigging already used by the oriented Fourier realization. The next source question is whether the powers-of-two support assignment can be replaced by arithmetic channel positions supplied by the Tate data while preserving subset-sum separation.
