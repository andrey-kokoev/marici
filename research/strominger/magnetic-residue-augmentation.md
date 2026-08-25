# Global residue augmentation and its integral index

Let `T` be the set of visible positive pole depths at fixed grade `g`.  After
the combinatorial kernel classification, the tower lattice is

\[
L_T=\bigoplus_{a\in T}\mathbb ZD_{g,a}.
\]

Rational exactness is controlled by one global weighted augmentation

\[
\rho_g:L_T\longrightarrow\mathbb Z\eta,
\qquad
D_{g,a}\longmapsto r_{g,a}\eta,
\]

\[
r_{g,a}=-g(g+1)C_{g+1}a^{\overline{g-1}}.
\]

This map couples tower components that are disconnected in the exponent
lattice graph.  Rational exactness therefore has no purely componentwise
shadow.  Its combinatorial shadow is the kernel of a global augmentation
attached after the component classification.

Over `Q`, if `T` is nonempty, there is a short exact sequence

\[
0\longrightarrow K_g^{rat}\longrightarrow K_g
\xrightarrow{\rho_g}\mathbb Q\eta\longrightarrow0.
\]

Each new positive depth after the first adds one rational-exact relative
class.  For two depths `a,b`, its primitive integral coordinate is

\[
\frac1{\gcd(r_{g,a},r_{g,b})}
\left(r_{g,b}D_{g,a}-r_{g,a}D_{g,b}\right).
\]

This is a genuine circuit, but it differs from the grade-two magnetic
exceptions.  The exceptional circuits are local dependencies inside one
parity component.  Residue circuits are global relations created only after
mapping disconnected tower components to the common divisor class `eta`.

Pairwise primitive circuits are not, in general, an integral basis of the
full kernel.  For example, at grade three and depths `{4,6,8}`, removing the
common transport factor leaves the row

\[
(10,21,36).
\]

The two primitive circuits obtained by pairing everything with the first
entry span an index-five sublattice.  They miss the primitive relation

\[
(-12,4,1).
\]

## Unimodular kernel construction

For an arbitrary ordered residue row

\[
r=(r_1,\ldots,r_n),
\]

construct a unimodular matrix `U` inductively.  Suppose the first `k-1`
entries have already been reduced to `(d_{k-1},0,...,0)`.  Choose Bezout
coefficients

\[
x_kd_{k-1}+y_kr_k=d_k,
\qquad d_k=\gcd(d_{k-1},r_k).
\]

On coordinates `1,k`, multiply by

\[
B_k=
\begin{pmatrix}
x_k&-r_k/d_k\\
y_k&d_{k-1}/d_k
\end{pmatrix}.
\]

Its determinant is one and

\[
(d_{k-1},r_k)B_k=(d_k,0).
\]

After all depths are processed,

\[
rU=(d_{g,T},0,\ldots,0),
\qquad U\in GL_n(\mathbb Z).
\]

The final `n-1` columns of `U` are therefore a saturated integral basis of
`ker rho_g`.  The first column is a source combination attaining the minimal
accessible residue `d_{g,T}*eta`.  This construction is ordering-dependent as
a basis, but its kernel lattice and Smith divisor are invariant.

## Smith invariant

Over the integral lattice, the one-row augmentation matrix has Smith form

\[
\operatorname{SNF}(\rho_g)=
\begin{pmatrix}d_{g,T}&0&\cdots&0\end{pmatrix},
\qquad
d_{g,T}=\gcd_{a\in T}|r_{g,a}|.
\]

Hence

\[
L_T/\ker\rho_g\simeq d_{g,T}\mathbb Z\eta\simeq\mathbb Z,
\]

while its embedding into the primitive ambient residue lattice has cokernel

\[
\mathbb Z\eta/\rho_g(L_T)\simeq\mathbb Z/d_{g,T}\mathbb Z.
\]

The torsion belongs to the ambient accessibility comparison, not to the tower
quotient itself.  Rationalization erases this index.

If `T` is enlarged, rational cohomology rank remains one and

\[
d_{g,T\cup\{b\}}=\gcd(d_{g,T},|r_{g,b}|).
\]

Thus increasing pole-depth resolution can only refine the accessible residue
step.  This is the stable-limit law at the arithmetic layer.

## Infinite-depth stable index

For the full positive even-depth constructor, put `n=g-1` and define the fixed
divisor

\[
\delta_n=\gcd_{a\in2\mathbb Z_{>0}}a^{\overline n}.
\]

Its closed form is

\[
\boxed{
\delta_n=
\begin{cases}
n!,&n\text{ even},\\
n!\,2^{\nu_2(n+1)},&n\text{ odd}.
\end{cases}}
\]

For every odd prime `p`, multiplication by two permutes the residue classes
modulo every power of `p`.  Restricting the start of the consecutive product
to an even integer therefore does not change its minimal `p`-valuation, which
is `nu_p(n!)`.  At `p=2`, an even-start interval of odd length contains one
additional even site.  Minimizing its valuation gives the extra
`nu_2(n+1)`; for even length there is no extra factor.  Combining the prime
valuations gives the formula.

Consequently the stable integral residue step at grade `g` is

\[
\boxed{
d_g^{\mathrm{stable}}
=g(g+1)C_{g+1}(g-1)!
\begin{cases}
1,&g\text{ odd},\\
2^{\nu_2(g)},&g\text{ even}.
\end{cases}}
\]

The parity of the grade enters only through this 2-adic constructor memory.
It disappears after tensoring with `Q`.

If the constructor is enlarged from positive even depths to all positive
integer depths, the fixed divisor becomes simply `(g-1)!`.  Therefore the
index ratio between the original and enlarged constructors is

\[
\frac{d_g^{\mathrm{even}}}{d_g^{\mathrm{all\ integer}}}
=\begin{cases}
1,&g\text{ odd},\\
2^{\nu_2(g)},&g\text{ even}.
\end{cases}
\]

Odd depths do not activate another rational cohomology class.  They refine
which integral multiples of the existing class are constructible.  This is a
pure constructor signature.

Finally, the fixed-divisor theorem is finite.  Since
`a^(rising n)` has degree `n`, its fixed divisor on the even progression is
already detected by `n+1` consecutive admitted starts.  At grade `g`, the
depths

\[
2,4,\ldots,2g
\]

therefore suffice to reach the infinite-depth arithmetic index.  This
arithmetic stabilization cutoff is independent of the Laurent cutoff
`m_min<=-(g+a_max-1)` required to make those towers visible.
