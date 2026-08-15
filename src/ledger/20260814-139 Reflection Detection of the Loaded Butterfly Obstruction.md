# Reflection Detection of the Loaded Butterfly Obstruction

## Record

Date: 2026-08-14

Status: exact integral detection theorem. Once the physical polarity line is
loaded relatively exactly once, the global binary obstruction of entry 138 is
detected by one reflection-square calculation at the \(D03\) channel. The
required loaded reflection connector is not yet constructed, so the theorem
reduces the test without deciding its outcome.

## The reflection subgroup detects the global class

Let

\[
G=D_3^{\rm triad}
=\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle
\]

be the transport symmetry of
\((F_{14},F_{03},F_{25})\), with

\[
r=\rho^2,
\qquad
s=\rho^3\sigma_0=f_3.
\]

The subgroup

\[
H=\langle f_3\rangle\simeq C_2
\]

is the physical stabilizer of \(D03\). Entry 138 proves that, after the
relative polarity line is retained once, the comparison coefficient is the
trivial module

\[
\mathbb Z_{\chi_N}=\mathbb Z.
\]

For a finite group and trivial integral coefficients,

\[
H^2(G;\mathbb Z)
\simeq H^1(G;\mathbb Q/\mathbb Z)
\simeq \operatorname{Hom}(G_{\rm ab},\mathbb Q/\mathbb Z).
\]

Both \(G_{\rm ab}\) and \(H\) are \(C_2\), and the inclusion
\(H\hookrightarrow G\) induces the identity on the nontrivial abelianized
reflection. Therefore

\[
\boxed{
\operatorname{res}_{H}^{G}:
H^2(D_3;\mathbb Z)
\xrightarrow{\sim}
H^2(\langle f_3\rangle;\mathbb Z)
\simeq\mathbb Z/2.
}
\]

This is a detection theorem, not an induction theorem: it applies after the
two global loaded extension points and their restriction functor have been
typed.

## An explicit parity formula

Let

\[
\varepsilon:G\longrightarrow\{0,1\}
\]

be reflection parity. The normalized integral cocycle

\[
\boxed{
c(g,h)=
\frac{\varepsilon(g)+\varepsilon(h)-\varepsilon(gh)}2
}
\]

is inflated from \(G\to C_2\), satisfies the cocycle identity, and has

\[
c(f_3,f_3)=1.
\]

For any normalized integral one-cochain \(b\),

\[
(\delta b)(f_3,f_3)=2b(f_3).
\]

Hence the parity of the reflection-square value is independent of the
cocycle representative. For the still-to-be-constructed loaded obstruction,

\[
\boxed{
\omega_{\rm load}=0
\quad\Longleftrightarrow\quad
\omega_{\rm load}(f_3,f_3)=0\pmod2.
}
\]

Since entry 138 also proves

\[
H^1(D_3;\mathbb Z_{\chi_N})=0,
\]

an even reflection square gives one connected component of loaded lifts,
whereas an odd reflection square proves nonexistence.

## What the physical reflection actually exchanges

The simplification does not make the entry-131 \(x_3\)-edge purity by itself
into the obstruction cocycle. The physical reflection acts on the short
diagonals by

\[
f_3:x_0\longleftrightarrow x_1,
\qquad
f_3:x_3\longleftrightarrow x_4.
\]

Consequently, on the \(D03\) square,

\[
v_{00}=x_0x_3\longleftrightarrow v_{11}=x_1x_4,
\qquad
v_{10}=x_1x_3\longleftrightarrow v_{01}=x_0x_4.
\]

Entry 120 proves the full \(x_3\) road-flag filtered trace with both
\(\operatorname{Tor}_0\) and \(\operatorname{Tor}_1\) grades. Entry 131
proves the positively normalized \(x_3\) target edge purity. Their reflected
target packets are geometrically available, but these results do not provide
the endpoint-coherent comparison between the support/Yoneda and
Tate/Cartier two-extensions. Declaring the reflected local unit to be the
needed connector would assume the equivariance whose square is being tested.

## Sharp blocker and smaller next construction

The first missing datum is one paired reflection connector

\[
\boxed{
\kappa_{f_3}^{\rm load}:
f_3^*\mathcal E_{03,x_3}^{\rm load}
\Longrightarrow
\mathcal E_{03,x_4}^{\rm load}
}
\]

in the endpoint-pointed support-PC two-extension category. It must retain:

- the nonzero generic \(Q\)-leg of the support/Yoneda extension;
- the polarity conductor exactly once;
- the full \(x_3/x_4\) road-square occurrence system;
- both repeated-normal Tor grades and the graph Bockstein;
- all lower Koszul--Cech terms;
- reciprocal-regular versus original-Borel--Moore variance;
- endpoint maps and the independent positive physical normal.

Its composite with its reflected pullback is the reflection-square defect

\[
\Omega_{03}
=
\kappa_{f_3}^{\rm load}
\circ f_3^*\kappa_{f_3}^{\rm load}.
\]

After placing that loop in the normalized two-extension mapping complex, the
single number

\[
\operatorname{ev}(\Omega_{03})\pmod2
\]

is the global obstruction. No full \(D_3\) bar-cocycle enumeration and no
choice of the carrier \(\mathbb Z/2\) parity are needed.

The construction cannot be replaced by an isolated local edge map. The
restriction theorem detects a global class; it does not manufacture the
global extension points or prove their \(D_3\)-equivariant assembly.

## Evidence

Extended exact certificate:

- research/voevodsky/check_physical_polarity_butterfly.rs
- SHA-256
  b7c68ea7fcb5f4f7850b5588ad7a80fc3051ad83bad284ebb0fea5f767b86bd1

It verifies the normalized cocycle on all triples of \(D_3\), its restriction
value \(c(f_3,f_3)=1\), parity invariance under integral coboundaries, and the
physical exchanges \(x_0\leftrightarrow x_1\) and
\(x_3\leftrightarrow x_4\). The previous exact character and bar-complex
tests remain unchanged.

Verification:

~~~text
rustfmt --edition 2021 --check
rustc --edition 2021 -D warnings -O
executable exit 0
JSON output parses
~~~

Repository-wide pnpm check built the shared UI and then stopped during
Astro content synchronization on the pre-existing untracked entry
20260814-137 Local PC Closure and the Endpoint-Coherent Butterfly Frontier:
its first author is outside the configured content-schema enum. The failure
precedes entry 139; that unrelated file and the schema were left untouched.

Epistemic-graph admission is pending. The Marici site advertises the
epistemic-graph and worker-delegation surfaces, but the loader returned
Transport closed when asked to open the site fabric. No graph storage or MCP
configuration was edited manually.

## Outcome contract

~~~json
{
  "claim": "For the once-polarity-loaded trivial coefficient, restriction from the D3 transport group to the physical D03 reflection subgroup is an isomorphism on H2. A normalized loaded obstruction is therefore zero exactly when its f3-square value is even.",
  "status": "proved",
  "assumptions": [
    "The relative polarity line occurs exactly once in the comparison coefficient, as in entry 138.",
    "The global loaded support/Yoneda and Tate/Cartier two-extension points are constructed before restriction is evaluated.",
    "Entry 93 retains the polarity factor independently; the D03 stabilizer alone sees only its product with road orientation."
  ],
  "factorization_test": {
    "global_loaded_H2": "Z/2",
    "reflection_subgroup_H2": "Z/2",
    "restriction": "isomorphism",
    "normalized_generator": "c(g,h)=(eps(g)+eps(h)-eps(gh))/2",
    "decision_value": "omega_load(f3,f3) mod 2",
    "x3_x4_reflection_connector": "unconstructed"
  },
  "counterevidence": [
    "The entry-131 x3 purity arrow is a target costalk equivalence, not a path between the two global loaded extensions.",
    "f3 exchanges the x3 and x4 edge packets, so one displayed edge cannot be treated as reflection-stable.",
    "Local construction in isolation does not imply global D3 assembly.",
    "The vanishing carrier Z/3 class does not determine this loaded Z/2 parity."
  ],
  "next_experiment": "Construct the endpoint-coherent f3-paired x3/x4 loaded connector and compute its reflection-square parity. If even, use the unique loaded component in d_sp,sc and G03^Cousin; if odd, reject the proposed physical loading."
}
~~~
