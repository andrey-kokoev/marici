# Exceptional attachment, retained normal complex, and the trace obstruction

## Scope and input

This calculation starts from the supplied native logarithmic blowdown

\[
b:\widetilde C\longrightarrow C.
\]

Here \(\widetilde C\) is the complete 245-generator native normal complex of
the stellar subdivision at \(\{03,13\}\), and \(C\) is the 215-generator
original normal complex. All sixteen endpoint states and seven quotient
states are retained. The coefficient ring is

\[
R=\mathbb Z[X_d,u_d:d\in\mathcal D],\qquad q_d=1+u_d,
\]

or its localization at the monodromy units \(q_d\). No occurrence \(X_d\) or
normal \(u_d\) is inverted in any map constructed below. The existing
finite-to-Cech map is used only in the target modules where its inverses are
permitted.

Put

\[
a=03,\quad b=13,\quad c=04,\quad d=35,\qquad
f=u_a+u_b+u_au_b=q_aq_b-1.
\]

The exceptional monodromy relation is source-defined. The new matrix is an
ordinary covariant native-normal comparison. Neither a normalization-sheet
input map nor a mixed-variance physical Gysin identification is assumed.

All chain degrees below are homological. Thus \(A[2]\), for a module \(A\),
means a complex with \(A\) in homological degree two. This is unrelated to
regrading an external Cartier filtration.

## 1. Retain the ten-state exceptional packet

The input kernel retraction identifies \(\ker b\) with a free complex \(N\)
having ranks \((0,2,5,3)\) in degrees zero through three. Use bases

\[
N_1=R\langle p_c,p_d\rangle,
\]
\[
N_2=R\langle r_0,r_c,r_d,y_c,y_d\rangle,
\qquad
N_3=R\langle z_0,z_c,z_d\rangle.
\]

Its complete differential is

\[
\begin{aligned}
d r_0&=-X_c p_c-X_d p_d,&
d r_c&=-u_c p_c,&d r_d&=-u_d p_d,\\
d y_c&=-f p_c,&d y_d&=-f p_d,\\
d z_0&=f r_0-X_c y_c-X_d y_d,\\
d z_c&=f r_c-u_c y_c,&
d z_d&=f r_d-u_d y_d.
\end{aligned}
\]

Both \(p\)-boundaries are zero. This is the tensor factorization

\[
N\simeq K_R(f)\otimes_R P_{\mathrm{link}}[1],
\qquad
P_{\mathrm{link}}=
\left[R^3\xrightarrow{\left(\begin{smallmatrix}X_c&u_c&0\\X_d&0&u_d\end{smallmatrix}\right)}R^2\right],
\]

with the signs specified by the displayed differential. The link has the two
incompatible residual diagonals \(04\) and \(35\); it is not legitimate to
make both inverse normals available on a single existing marked face.

Define

\[
g=u_cu_d r_0-X_cu_d r_c-X_du_c r_d,
\qquad
Z=u_cu_d z_0-X_cu_d z_c-X_du_c z_d.
\]

Then

\[
dg=0,\qquad dZ=fg,\qquad H_2(N)=R/(f)\langle[g]\rangle.
\]

The lower homology \(H_1(N)=\operatorname{coker}(d_{P_{\mathrm{link}}})\otimes_R R/(f)\)
is retained; it is not discarded in the trace calculation.

## 2. The actual attaching map

Let \(j:C\to\widetilde C\) be the previously constructed graded polynomial
section of \(b\). Let \(p:\ker b\to N\) be the kernel retraction. The
attaching map is the actual defect of that graded section:

\[
\delta=p(d_{\widetilde C}j-jd_C):C_n\longrightarrow N_{n-1}.
\]

It satisfies \(d_N\delta+\delta d_C=0\). Its only nonzero columns are

| Target-complex input | Exceptional output |
|---|---|
| \([\{03\},\{03\}]\) | \(-X_{13}r_0\) |
| \([\{03,04\},\{03\}]\) | \(+X_{13}p_c\) |
| \([\{03,04\},\{03,04\}]\) | \(+X_{13}r_c\) |
| \([\{03,35\},\{03\}]\) | \(+X_{13}p_d\) |
| \([\{03,35\},\{03,35\}]\) | \(+X_{13}r_d\) |

These are attaching columns of the full blowdown extension. They are not the
five \(13\)-marked incoming rows of the earlier mixed-Chern radial defect.
Both calculations are retained separately in their respective artifacts.

Define the normal-retaining complex \(\widehat C\) on the graded direct sum
\(N\oplus C\) by

\[
d_{\widehat C}(n,t)=(d_Nn+\delta t,d_Ct).
\]

This is a complex because the attaching map anticommutes with the two
differentials. It has 225 generators and chain ranks

\[
(14,65,98,48).
\]

After removing both endpoint packets, its rank is 209, compared with 229
for the endpoint-relative native source.

### Explicit homotopy equivalence

Write \(N_{\mathrm{old}}=\ker b\), and let
\((p,i,h)\) be the input strong deformation retraction onto \(N\), with

\[
dh+hd=1-ip,\qquad pi=1,\qquad ph=hi=h^2=0.
\]

In the graded splitting \(\widetilde C=N_{\mathrm{old}}\oplus C\), write
\(\delta_0=dj-jd\). Define

\[
P(n,t)=(pn,t),\qquad
I(n',t)=(in'-h\delta_0t,t),\qquad
H(n,t)=(hn,0).
\]

Direct substitution proves

\[
PI=1,\qquad dH+Hd=1-IP,
\qquad dI=Id,\qquad dP=Pd.
\]

The executable verifies these identities on every basis element and exports
all three matrices. In native bases the maps have shapes \(225\times245\),
\(245\times225\), and \(245\times245\).

Every homotopy component into an endpoint or a Q state is zero. Endpoint
packets are mapped identically, and both endpoint connecting squares
commute. Thus this replacement removes only the twenty explicitly
contractible generators; it does not remove the resonant kernel.

Projection \(\widehat C\to C\), followed by the source-defined finite-to-Cech
map \(\Lambda\), recovers the old \(K^{\check C}\) matrix exactly. This does
not claim that \(\Lambda\) is an equivalence.

## 3. The Q attachment is determined in this native model

Let \(L=\{03,14,25\}\), and use the following primitive top cycle of the
seven-state Q quotient:

\[
\theta=\left(\prod_{l\in L}u_l\right)[\varnothing,\varnothing]
-\sum_{l\in L}X_l\left(\prod_{m\in L\setminus\{l\}}u_m\right)[\{l\},\{l\}].
\]

Its graded lift \(\widetilde\theta\) to \(C\) need not be a cycle; write
\(\beta=d_C\widetilde\theta\). The new exceptional attachment is

\[
\delta\widetilde\theta=X_{03}X_{13}u_{14}u_{25}\,r_0.
\]

The retained complex has the full boundary

\[
d_{\widehat C}(0,\widetilde\theta)
=(X_{03}X_{13}u_{14}u_{25}r_0,\beta).
\]

Its next differential is zero because
\(d_N\delta\widetilde\theta+\delta\beta=0\). Deleting the exceptional term
is not a compatible change to this native comparison. The expression is a
chain attachment, not a cohomology class in isolation.

Changing the graded section changes the attaching map by a chain homotopy.
It does not erase the extension class computed next. This follows either
from the displayed formulas or from the termwise-split extension construction
in Stacks Project, tag 014D.

## 4. The full top-cycle lift is obstructed at exceptional resonance

The complete target top cycle is

\[
\Omega=\sum_{F}(-1)^{|F|(|F|+1)/2}
\left(\prod_{a\in F}X_a\right)
\left(\prod_{a\notin F}u_a\right)[F,F].
\]

All 45 faces occur. The top differential equations force all top cycles to
be polynomial multiples of \(\Omega\): already the one-face equations
force the empty-face coefficient to be divisible by every independent
\(u_a\), and then the other coefficients are fixed uniquely. Hence
\(H_3(C)=R\langle\Omega\rangle\).

Define the following coefficient, as computed from the full matrix:

\[
\mu=X_{03}X_{13}u_{02}u_{13}u_{14}u_{15}u_{24}u_{25}.
\]

Then

\[
\delta\Omega=\mu g.
\]

Thus the connecting map on homology is

\[
R\langle\Omega\rangle\longrightarrow R/(f)\langle g\rangle,
\qquad 1\longmapsto\bar\mu.
\]

The ring \(R/(f)\) is a domain. For example,
\((1+u_{03})(1+u_{13})=1\) identifies its two displayed monodromy variables
with a single Laurent coordinate. The element \(\bar\mu\) is nonzero.
Therefore the kernel of the displayed connecting map is exactly \((f)\).
Consequently

\[
\operatorname{im}(H_3(\widetilde C)\xrightarrow{b}H_3(C))=fR\langle\Omega\rangle.
\]

The native top generator is explicit:

\[
\widetilde\Omega=\sum_{\widetilde F}
(-1)^{|\widetilde F|(|\widetilde F|+1)/2}
\left(\prod_{a\in\pi\widetilde F}X_a\right)
\left(\prod_{j\notin\widetilde F}v_j\right)
[\widetilde F,\widetilde F],
\]

where the last product is over the ten native rays, \(v_E=f\), and
\(v_j=u_j\) on old rays. Its image is exactly \(f\Omega\).

The old top class \(\Omega\) therefore has no integral lift with coefficient
one across \(f=0\). This obstruction concerns the full native top cycle,
not the claim that each quotient generator has no preimage: the matrix is
still degreewise surjective and is the identity on the native Q graded
states.

## 5. The secondary relation is a nonzero two-extension

In \(\widehat C\), the two primitives of multiples of \(g\) are

\[
W_f=(Z,0),\qquad W_\mu=(0,\Omega),
\qquad dW_f=fg,\quad dW_\mu=\mu g.
\]

Their compatibility is a closed top chain:

\[
fW_\mu-\mu W_f=( -\mu Z,f\Omega ).
\]

Under the explicit inclusion \(I\), this equals the native cycle
\(\widetilde\Omega\) exactly, not merely up to cohomology. The certificate
exports both full native primitives and verifies the identity on all 245
source coordinates. The \(W_\mu\) primitive retains the native endpoint
corrections; they are not set to zero by hand.

The three-generator subcomplex spanned by \(W_f,W_\mu,g\) has differential

\[
R^2\xrightarrow{(f,\mu)}R
\]

in degrees three and two. Its top cycle is \((-\mu,f)\). It embeds into
\(\widetilde C\); on top homology it maps isomorphically to
\(H_3(\widetilde C)\). Its degree-two homology is \(R/(f,\mu)\), and the long
exact sequence of the full blowdown identifies this with the image of the
exceptional \(H_2(N)\) in \(H_2(\widetilde C)\). In particular, the
annihilator of that image is exactly \((f,\mu)\).

The coefficient exact sequence is

\[
0\longrightarrow R
\xrightarrow{(-\mu,f)^T}R^2
\xrightarrow{(f,\mu)}R
\longrightarrow R/(f,\mu)\longrightarrow0.
\]

The sequence \((f,\mu)\) is regular: \(R\) is a domain, \(R/(f)\) is a
domain, and \(\bar\mu\ne0\). Its ideal is proper, including after all
monodromy units are inverted. Thus this is the Koszul resolution of the
quotient. Dualizing gives

\[
\operatorname{Ext}^2_R(R/(f,\mu),R)\cong R/(f,\mu).
\]

With the displayed ordered bases, the two-extension represents \(1\).
Changing \(W_f,W_\mu\) by closed native three-chains changes the coefficient
of the secondary top class by an element of \((f,\mu)\), so its unit residue
is invariant under those changes. No degree-four native chain exists to
supply an additional boundary.

This is a source-derived secondary class in the ordinary native complex. It
is not an identification with the proposed physical conductor--Morse class:
the second defining function \(\mu\) is the computed product above, not an
independently established physical normal coordinate.

## 6. Classify all scalar traces on the exceptional packet

Write \(A=R/(f)\). This is the resonance-supported scalar target; using the
free target \(R\) would already force the value on \([g]\) to be zero.
Because \(N\) is a bounded free complex, chain maps modulo chain homotopies
compute all maps \(N\to A[2]\) in \(D(R)\), not just a restricted family.

A chain map has only a row on \(N_2\). The \(N_3\) equations modulo \(f\)
force its values on \(y_c,y_d\) to be zero: \(u_c\) and \(u_d\) are
nonzerodivisors in \(A\). Thus every map is represented by
\(\alpha=(\alpha_0,\alpha_c,\alpha_d)\in A^3\) on \(r_0,r_c,r_d\).
Homotopies change this row by combinations of

\[
(X_c,u_c,0),\qquad (X_d,0,u_d).
\]

Its value on the exceptional generator is

\[
\tau(g)=u_cu_d\alpha_0-X_cu_d\alpha_c-X_du_c\alpha_d.
\]

This evaluation identifies the complete ordinary derived-map group with

\[
\operatorname{Hom}_{D(R)}(N,A[2])\cong
\mathfrak a=(u_cu_d,X_cu_d,X_du_c)\subset A.
\]

### Proof of injectivity

If the displayed value is zero, reduction modulo \(u_c\) forces
\(\alpha_c=u_c\ell\), because \(X_cu_d\) is a nonzerodivisor modulo
\(u_c\). Dividing the resulting polynomial identity by \(u_c\), and then
reducing modulo \(u_d\), forces \(\alpha_d=u_dm\). The remaining equation
is \(\alpha_0=X_c\ell+X_dm\). This is precisely a homotopy row. Surjectivity
onto \(\mathfrak a\) follows by taking the three coordinate rows.

The ideal is proper: at \(X_c=X_d=u_c=u_d=0\), all three generators vanish,
while every \(q_j\) can remain invertible and \(f=0\). Therefore

\[
1\notin\mathfrak a.
\]

No ordinary resonance-valued scalar trace on the full exceptional packet
sends \([g]\) to the primitive unit. Tensoring with a framed invertible line
changes its line label but does not make this proper ideal contain a unit.

This also explains why the lower link packet cannot simply be dropped: it
is precisely the differential that imposes the two homotopy relations and
the proper trace-value ideal.

## 7. No nonzero scalar exceptional trace extends to the whole native source

Suppose \(\tau:N\to A[2]\) extends to \(\widetilde C\). The extension
triangle forces \(\tau\delta\) to be null-homotopic. Evaluation on the
closed target top cycle gives

\[
\mu\,\tau(g)=0\quad\text{in }A.
\]

Since \(A\) is a domain and \(\bar\mu\ne0\), this forces \(\tau(g)=0\).
Section 6 then forces \([\tau]=0\). Hence the restriction map

\[
\operatorname{Hom}_{D(R)}(\widetilde C,A[2])
\longrightarrow\operatorname{Hom}_{D(R)}(N,A[2])
\]

is zero.

This is an ordinary derived coefficient obstruction. A relative-dualizing
trace with additional support, shifts, and comparison targets is a different
map and is not ruled out. The source's primitive trace on a pulled-back
constant exceptional interval cannot be identified with the present native
normal scalar map by comparing its value \(+1\) alone.

## 8. Relation to the physical Gysin problem

The calculation supplies:

* a complete normal-retaining right-leg model homotopy equivalent to the
  native 245-state source;
* all five exceptional attaching columns, including their native Q effect;
* the exact top-lift obstruction \(\bar\mu\in R/(f)\);
* a nonzero unit two-extension on \(R/(f,\mu)\);
* the full ordinary scalar-trace group and the obstruction to extending a
  nonzero trace across the native source.

It does not supply the missing normalization-conductor-to-native-source map,
nor identify the physical residue with the new two-extension. A genuine
physical comparison must either transport this complete two-extension to
its prescribed support triangle or explain, by a source-defined operation,
why it is removed. Deleting the exceptional sector on grounds of underlying
poset contractibility is incompatible with the explicit complex.

All statements are for the independent coefficient ring and its
monodromy-unit localizations. A substitution \(u_j=t_jX_j\) is a different
base-change calculation; no Rees conclusion is silently inferred here.

## Reproduction and evidence

Run `python check_exceptional_trace.py` beside the `dependencies` directory.
The script reconstructs the old matrix and kernel, writes the retained
matrix and certificate, and checks every map in the deformation retraction.
It also verifies every endpoint and Q component, both native top cycles,
the two annihilating primitives, their secondary relation, and the Hom
presentation identities.

The unbounded classifications use the explicit divisibility, regular-
sequence, and long-exact-sequence arguments above; they are not inferred
from a finite sample of polynomials. The exact rational specializations in
the script are additional nonzero controls only.

Pinned source facts:

- Marici commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`,
  `research/voevodsky/check_d03_normalized_blowdown_counit.py`:
  old-face labels and the marked normalized-blowdown carrier.
- Same commit, `research/voevodsky/check_ringed_alexandrov_pc_target.py`:
  original loaded-cell differential and legal Cech summands.
- Same commit, ledger entry 111: `q_E=q_03*q_1`, with the exceptional
  center separate from the conductor normal `x_3`.
- Same commit, ledger entry 424: the primitive relative-interval trace on
  the pulled-back finite structure sheaf. Its source is not the native
  complex used here.

General homological algebra:

- Stacks Project 014D: a termwise-split sequence and its connecting map.
- Stacks Project 0A8H: mapping-complex differential and homotopies.
- Stacks Project 064B: maps out of bounded-above projective complexes can
  be computed in the homotopy category.
- Stacks Project 0621 and 062F: Koszul construction and exactness for a
  regular sequence.

The exact matrix, its defect, trace ideal, and two-extension are computations
in this package, not assertions attributed to those general references.
