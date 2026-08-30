# RS-1 physical \(C_3\) norm and extension realization

## Correction to the first source census

The initial vocabulary search for a physical nonsemisimple deck
specialization returned no result. Entry 1553 shows that this was a search
false negative, not absence of an object. The programme already contains two
independent physical order-three realizations.

## Cosmological norm channel

At the positive equal-energy cyclic fixed point, the six physical
occurrences form two regular \(C_3\)-orbits. On each orbit,

\[
T(1)=(1,1,1)^T,\qquad R=(1,1,1),\qquad N=TR,
\]

and source geometry gives

\[
RT=3,\qquad N^2=3N.
\]

Modulo three, \(N\) is a nonzero square-zero differential. For one orbit,

\[
H(N)=\ker N/\operatorname{im}N
\quad\text{has dimension }1;
\]

for the two physical orbits its dimension is \(2\). The all-positive
occurrence sum is the source readout, and the coefficient transport is
horizontal at the fixed locus.

However, \(N=TR\) gives \(\ker N=\ker R\). Consequently the declared
all-positive readout induces the zero map on \(H(N)\). This is a complete
physically sourced nonsemisimple *coefficient packet*, but not yet a
physically activated relative syndrome.

## String road/contact channel

Independently, the integral road recollement gives

\[
0\to A_2\to\mathbb Z[C_3]\xrightarrow{\epsilon}\mathbf1\to0,
\qquad
H^1(C_3,A_2)\cong\mathbb Z/3.
\]

Entry 436 supplies the physical gate: the unique primitive integral
positive-sheet class reaches road augmentation \(+1\). Here prime three is
not norm homology but the nonsplitting class that glues primitive and contact
grades.

## RS-1 verdict

The hard core survives and becomes sharper:

\[
\boxed{
\text{shared trace/transfer calculus}
+\text{source-specific coefficient object}
+\text{physical readout}
\Rightarrow
\text{typed coefficient packet}.
}
\]

A further supported or relative readout must be nonzero on the homology
before the latter can be called a physical syndrome.

The two sectors share the order-three calculus but not the coefficient
object:

\[
\begin{array}{c|c|c}
\text{sector}&\text{object}&\text{order-three residue}\\
\hline
\text{cosmology}&\mathbb F_3[C_3]^{\oplus2}&H(N),\ \dim=2\\
\text{string road}&0\to A_2\to\mathbb Z[C_3]\to\mathbf1\to0
&\operatorname{Ext}^1\cong\mathbb Z/3.
\end{array}
\]

This does not vindicate the free decoder. Its three-channel augmentation
kernel happens also to have dimension two, but it is one reduced
representation, whereas the cosmological object is the norm homology of two
independently declared physical occurrence orbits. The equality of dimensions
is a hostile negative control.

## Updated frontier

RS-2 must first derive a supported readout that does not vanish on the
cosmological norm homology. Only then should it test naturality under a
genuine factorization or specialization map between source sectors. The
target is not another rank:

\[
\tau:
H(N_{\rm occurrence})
\longrightarrow
\operatorname{Ext}^1_{\mathbb Z[C_3]}(\mathbf1,A_2)
\quad\text{or a common relative target}.
\]

Such a map must be derived from a declared cross-sector kernel. No map is
currently established, and matching the prime three does not create one.

## Durable evidence

- Entries 410, 436, 1552, and 1553;
- research/nima/checkers/check_rs1_physical_c3_norm_packet.py;
- research/nima/results/rs1-physical-c3-norm-packet.json.
