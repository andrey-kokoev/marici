# A Generator-Filtered Labelled Total Complex Is Dual-Number Linear

Entry 513 shows that truncating the image span does not produce a
dual-number module.  The repair is to truncate the labelled
principal-gradient total complex at its generators over

\[
R=\mathbb Q[u]/(u^2).
\]

For scalar cutoff `D`, take

\[
B_{\le D},\qquad G_{\le D-3},\qquad P_{\le D-4},
\]

and, in sector `(e_a,e_b)`, admit labelled source monomials only through

\[
\deg f\le D-3-e_a-e_b.
\]

Each declared generator denotes a free `R`-generator, so both `f` and `uf`
are retained before the differential is applied.  With Entry 511's maps

\[
D_{-1}(f,p)=
\bigl(d(f)+Kp,\widehat H(f)+Ep\bigr),
\]

\[
D_0(b,g)=b-\nabla K\mathbin\cdot g\pmod K,
\]

the shifted cutoffs are preserved.  The executable audit checks every
labelled sector, both orbit lattices, both `p/q` operators, and every source
monomial at `D=12,16,20,24`.

\[
\begin{array}{c|r|r|r}
D&\operatorname{rank}_R A_D&\operatorname{rank}_R P_D&
\text{checked generators}\\\hline
12&452&45&497\\
16&1060&91&1151\\
20&1924&153&2077\\
24&3044&231&3275
\end{array}
\]

For every checked generator,

\[
D_0D_{-1}=0,
\qquad
D_{-1}(ux)=uD_{-1}(x).
\]

Thus this is a genuine finite complex of `R`-modules, unlike the quotient
span in Entry 513.  No homology rank or nearby-cycle interpretation is
claimed yet.  The next calculation must diagonalize the deck action on the
paired orbit-labelled source, form the plus subcomplex, and compute its
actual homology and specialization by base change.

## Evidence

- `research/benincasa/check_soft_axis_labelled_total_truncation.py`
- Entries 511 and 513.
