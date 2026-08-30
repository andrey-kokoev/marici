# Cartan–Clifford optical supertrace gate

## Question

Can the proposed normal-displacement identity be turned into a finite optical
test that distinguishes a genuine graded constructor from a visible-subspace
coincidence, and what does completion require?

## Minimal ordered-path instrument

Use one even optical mode and one odd optical mode. In their calibrated field
basis, implement the forward conversion and return conversion

\[
d_a=
\begin{pmatrix}0&a\\0&0\end{pmatrix},
\qquad
Q=
\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]

Two phase-stable routes implement the ordered words separately:

\[
d_aQ=aP_{\rm even},
\qquad
Qd_a=aP_{\rm odd}.
\]

Coherent recombination therefore implements

\[
d_aQ+Qd_a=aI.
\]

The detector must retain signed complex field amplitude. Intensity alone
reports only the square magnitude of `a` and cannot distinguish the two sides
of the critical seam. A comb- or pilot-referenced balanced heterodyne receiver
can recover the sign after the path and detector frames are calibrated.

Both parity inputs must be injected. Testing only the even input measures the
first ordered projector and does not establish the operator identity.

## The completion surprise

Let the carrier be graded into even and odd modes and let both `d` and `Q` be
odd. Cyclicity of the ordinary trace gives the exact identity

\[
\operatorname{str}(dQ+Qd)=0.
\]

If the desired relation is

\[
dQ+Qd=aI
\]

with nonzero `a`, its supertrace is

\[
a(\dim V_{\rm even}-\dim V_{\rm odd}).
\]

Consequently a nonzero Cartan–Clifford contraction requires equal even and odd
dimensions. Completion cannot mean adjoining arbitrary hidden loss, delay, or
memory modes. Every admitted extra mode must arrive in a parity-balanced
contractible pair, or the exact identity is impossible before any numerical
conditioning question arises.

## Smallest hostile completion

Adjoin one hidden even mode and allow forward and return couplings `b` and `c`.
In the order visible-even, visible-odd, hidden-even, take

\[
d=
\begin{pmatrix}
0&a&0\\
0&0&0\\
0&b&0
\end{pmatrix},
\qquad
Q=
\begin{pmatrix}
0&0&0\\
1&0&c\\
0&0&0
\end{pmatrix}.
\]

Their anticommutator is

\[
\begin{pmatrix}
a&0&ac\\
0&a+bc&0\\
b&0&bc
\end{pmatrix}.
\]

An even-input-only experiment still reads `a` and falsely passes. The odd
probe reads `a+bc`; hidden-port monitoring also exposes `ac`, `b`, and `bc`.
For nonzero `a`, no choices of `b` and `c` make this matrix equal to `aI`.
This is the finite optical form of the supertrace obstruction.

## Balanced control

Adjoining one additional even–odd pair and extending `d` and `Q` by a second
two-mode Clifford block preserves the identity exactly. Thus the obstruction
is not “more modes are bad.” It is a graded index condition on completion.

## Experimental falsifier

For each declared cutoff:

1. inventory all accessible and environment modes with their grading;
2. inject calibrated probes spanning both parity sectors;
3. measure `dQ` and `Qd` as separately switched coherent routes;
4. recombine their signed heterodyne amplitudes;
5. compare the full reconstructed anticommutator with `aI`;
6. repeat after adding one controlled parity-balanced mode pair;
7. reject the constructor if an unpaired hidden channel is required or the
   residual lacks a cutoff-uniform bound.

This instrument tests a source-proposed `Q`; it does not authorize one. Nima’s
theta/Tate derivation, the primitive/square/seam/archimedean typing, and a
continuum common-domain theorem remain necessary.

## Verification

Run:

```text
python research/aspect/checkers/check_cartan_clifford_optical_supertrace_gate.py
```

The checker uses an exact polynomial ring over the rationals. It verifies the
two-mode identity, the one-hidden-mode false pass and full failure, and the
parity-balanced four-mode control.
