# Radiative Memory Is a Paired Readout

Entry 1056 gives the leading charge as

\[
Q_f
=
-\frac{1}{8\pi G}
\int_{S^2}d^2z\,\gamma^{z\bar z}
f\,\mathcal O N.
\]

Thus the physical scalar is not the memory field alone.  It pairs the
covariant memory datum with a transported supertranslation detector
\(f\), using the sphere measure and operator \(\mathcal O\).

The exact three-direction \(D_3\) model makes this visible.  On the
difference plane use

\[
r=
\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad
s=
\begin{pmatrix}1&0\\1&-1\end{pmatrix},
\qquad
G=
\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]

Then

\[
h^TGh=G
\]

for every \(h\in D_3\), and

\[
\boxed{
\langle hf,hN\rangle_G
=
\langle f,N\rangle_G.
}
\]

Holding \(f\) fixed while transporting \(N\) fails extensively.  The
checker verifies the invariant pairing for all six group elements and every
pair of bounded detector/memory vectors in \([-3,3]^2\), while retaining
the fixed-detector failures as a hostile control.

This supplies a third positive sector for the paired-readout refinement:

- cosmology: Kummer coefficient paired with the Betti chamber orbit;
- five-point strings: twisted de Rham class paired with the oriented chamber;
- radiative gravity: supertranslation detector paired with memory.

The shared statement is the mixed-variance pairing law, not equality of the
sector-specific coefficient spaces or physical functionals.

Artifacts:

- `research/nima/check_radiative_memory_paired_readout.py`
- `research/nima/results/radiative-memory-paired-readout.json`
