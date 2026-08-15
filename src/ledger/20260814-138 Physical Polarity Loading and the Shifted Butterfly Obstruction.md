# Physical Polarity Loading and the Shifted Butterfly Obstruction

## Record

Date: 2026-08-14

Status: exact character and integral group-cohomology theorem. The physical
polarity loading removes the carrier-level mod-two choice **if and only if**
the endpoint comparison carries the polarity line relatively, once. The
loaded existence class itself is not yet defined because the two loaded
two-extensions have not been constructed in one support-PC mapping category.

Entries 134--136 left a nonempty carrier lift space whose connected
components form a torsor under

\[
H^1(D_3;\mathbb Z_{\rm or})\simeq \mathbb Z/2.
\]

The natural next move looked like choosing its reflection parity and only
then adding the scalar polarity conductor. That order is unnecessarily
strong. The polarity line changes the coefficient module of the comparison.

## Claim

Let \(\rho\) be one-step rotation and \(\sigma_0:j\mapsto-j\) reflection
of the six fusion labels. The transport symmetry of the three long channels

\[
(F_{14},F_{03},F_{25})
\]

is

\[
D_3^{\rm triad}
=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle,
\qquad
r=\rho^2,\quad s=\rho^3\sigma_0.
\]

Here \(r\) cycles the three channels, while \(s\) fixes \(F_{03}\) and
exchanges \(F_{14}\) and \(F_{25}\). This is a transport group for the
three-channel orbit, not the literal stabilizer of the single \(D03\)
channel.

The road-orientation and polarity characters restrict as

\[
\chi_{\rm or}(r)=+1,
\qquad
\chi_{\rm or}(s)=-1,
\]

and

\[
\chi_{\rm pol}(r)=+1,
\qquad
\chi_{\rm pol}(s)=-1.
\]

The second identity is forced by entry 93: one six-label rotation exchanges
the normalization sheets. Thus two rotations preserve the sheets, whereas
the physical reflection \(\rho^3\sigma_0\) exchanges them. Consequently

\[
\boxed{
\chi_N\big|_{D_3^{\rm triad}}
=\chi_{\rm or}\chi_{\rm pol}
=1.
}
\]

If the butterfly comparison is loaded by this relative polarity line
exactly once, its coefficient module changes from the sign line to the
trivial line. The low-degree groups change exactly as follows:

\[
\begin{array}{c|cc}
&H^1(D_3;-)&H^2(D_3;-)\\
\hline
\mathbb Z_{\rm or}&\mathbb Z/2&\mathbb Z/3\\
\mathbb Z_{\chi_N}=\mathbb Z&0&\mathbb Z/2.
\end{array}
\]

Therefore polarity loading should precede carrier pointing. If the loaded
comparison exists, its connected component is unique. Existence, however,
is now controlled by a binary obstruction rather than inherited from the
already-vanishing carrier obstruction.

## Exact calculation

Use the extension

\[
1\longrightarrow C_3\longrightarrow D_3
\longrightarrow C_2\longrightarrow1.
\]

Rotation acts trivially on both coefficient lines. The standard cyclic
resolution of \(C_2\) gives

\[
H^1(C_2;\mathbb Z_{\rm sign})=\mathbb Z/2,
\qquad
H^2(C_2;\mathbb Z_{\rm sign})=0,
\]

and

\[
H^1(C_2;\mathbb Z)=0,
\qquad
H^2(C_2;\mathbb Z)=\mathbb Z/2.
\]

Moreover \(H^2(C_3;\mathbb Z)=\mathbb Z/3\). Reflection acts on this
class by inversion times its coefficient character. It is invariant for
the road sign line and anti-invariant for the loaded trivial line. Since
positive \(C_2\)-cohomology of a three-primary module vanishes, the
Lyndon--Hochschild--Serre sequence has no differential or extension
ambiguity in total degree at most two. This gives the displayed table
integrally.

The executable independently constructs the normalized inhomogeneous bar
differentials

\[
\mathbb Z\longrightarrow\mathbb Z^5
\longrightarrow\mathbb Z^{25}
\longrightarrow\mathbb Z^{125}.
\]

Their characteristic-zero ranks are

\[
(1,4,21)
\quad\text{for }\mathbb Z_{\rm or},
\qquad
(0,5,20)
\quad\text{for }\mathbb Z_{\chi_N}.
\]

The mod-two and mod-three cohomology dimensions agree exactly with the
primary torsion predicted above. No integer or scalar parameter is inverted.

## Simplified formula objective

Do not choose a point of the carrier \(\mathbb Z/2\)-torsor. Instead load
the canonical roof of entry 136 and construct the two loaded endpoint
two-extensions directly. Their difference must define

\[
\boxed{
\omega_{\rm load}
\in
\operatorname{Ext}^2_{\mathbb Z[D_3]}
(\mathbb Z,\mathbb Z_{\chi_N})
\simeq\mathbb Z/2.
}
\]

Then there are exactly two outcomes:

\[
\omega_{\rm load}=0
\quad\Longrightarrow\quad
\pi_0\operatorname{Lift}_{\rm load}
\text{ is a singleton},
\]

because the acting \(H^1\) group vanishes, while

\[
\omega_{\rm load}=1
\quad\Longrightarrow\quad
\operatorname{Lift}_{\rm load}=\varnothing.
\]

Only in the first case should the unique loaded component be inserted into
the total specialization differential and the \(D03\) Cousin map.

## Sharp blocker

The coefficient calculation does not produce \(\omega_{\rm load}\).
The first missing datum is a pair of endpoint-coherent loaded
two-extension maps in one physical-diagonal \(D_3\) support-PC category.
They must retain the polarity conductor, occurrence coefficients,
reciprocal/BM variance, and endpoint maps. Their difference, rather than a
chosen carrier reflection cochain, is the class to evaluate.

This distinction is essential:

- the zero carrier obstruction lies in \(\mathbb Z/3\), a different
  coefficient group, and does not determine the loaded \(\mathbb Z/2\)
  class;
- if \(L_{\rm pol}\) is placed symmetrically on both mapping endpoints,
  it cancels in internal Hom and the old \(\mathbb Z/2\) carrier torsor
  remains;
- the actual stabilizer \(\{1,f_3\}\) of \(D03\) sees only the product
  character and cannot separately certify its two factors;
- \(H^1=0\) proves uniqueness only after existence.

Thus the theorem simplifies the order of construction but does not close
the scalar differential or the Cousin correspondence.

## Evidence

Exact certificate:

- research/voevodsky/check_physical_polarity_butterfly.rs
- SHA-256
  eedebf0e769ee01163214807c549d61b95c2712665b4d0de22b41a272e745008

Verification:

~~~text
rustfmt --edition 2021 --check
rustc --edition 2021 -D warnings -O
executable exit 0
JSON output parses with status=proved
normalized bar differentials square to zero
git diff --check
~~~

Repository-wide `pnpm check` reached Astro content synchronization and
stopped on the pre-existing untracked entry
`20260814-137 Local PC Closure and the Endpoint-Coherent Butterfly Frontier`
because its first author is outside the configured content-schema enum.  The
failure precedes entry 138 and was not repaired or bypassed here.

Epistemic-graph admission remains pending: the project loader returned
`Transport closed` when asked for the Marīci site surfaces.  No graph
storage was edited manually, so this ledger record is published evidence but
not yet an admitted graph consequence.

Dependencies:

- Entry 92: independent road-orientation and polarity characters.
- Entry 93: canonical polarity-odd normalization--conductor symbol.
- Entry 94: loaded primitive \(D03\) associated-grade symbol.
- Entry 134: framed lift-space obstruction and carrier \(\mathbb Z/2\)
  torsor.
- Entry 136: canonical unpointed AW/cap roof.

## Outcome contract

~~~json
{
  "claim": "On the D3 transport symmetry of the long-channel triad, the road-orientation and polarity lines are both reflection-sign modules, so their relative product is trivial. Consequently a once-polarity-loaded butterfly has H1=0 and H2=Z/2, instead of carrier H1=Z/2 and H2=Z/3.",
  "status": "proved",
  "boundary": "The actual loaded two-extension maps and their Z/2 difference class are unconstructed.",
  "consequence": "Load the canonical roof before pointing it. If the loaded obstruction vanishes, the loaded component is unique; if it is nonzero, no loaded lift exists.",
  "next_experiment": "Construct the two endpoint-coherent loaded comparison maps in one support-PC category and evaluate omega_load in Z/2 without choosing a carrier parity."
}
~~~
