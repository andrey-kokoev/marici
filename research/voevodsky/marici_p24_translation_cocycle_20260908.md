# Constant endpoint translations and the primitive P24 value

Date: 2026-09-08

## Translation field

For each strict framed cycle

\[
v_{\sigma,T}=b_{\sigma,T}\in D_{k_\sigma},
\]

the additive structure of the GR formal vector prestack defines a constant vector field

\[
X_{\sigma,T}=\partial_{v_{\sigma,T}}.
\]

Unlike the previously considered linear operation fields, this derivation lowers formal symmetric weight by one. For a linear homological field `Q`, the standard translation identity is

\[
[Q,\partial_v]=\partial_{Qv}.
\]

The eight spatial maps are strict cycles, so `Qv=0` and

\[
[Q,X_{\sigma,T}]=0.
\]

On an odd primitive source class—available in the cubic and quintic native sectors—the image `v` and its constant translation have odd parity, as required by the P24 odd infinitesimal-symmetry convention.

## Primitive coordinate and residue evaluation

The framed primitive coefficient one supplies a dual linear coordinate `lambda_v` satisfying

\[
\lambda_v(v)=1.
\]

Use the canonical zero-section distribution trace followed by the normalized sixfold conductor residue. Although this trace kills the Bruce products for weight-preserving fields, it detects the weight-lowering translation. The P24 cochain

\[
\phi_v(f_0,f_1)=
\tau_0\bigl((-1)^{|f_0|}X_v(f_0f_1)\bigr)
\]

has, for odd `lambda_v`,

\[
\boxed{\phi_v(\lambda_v,1)=-1}.
\]

The result holds in all eight endpoint/channel frames. Reflection exchanges `D35` and `D04` and transports this normalized value unchanged; determinant and polarity compensation are already included in the framed coefficient.

## Scope

This proves that the concrete P24 cochain is not the zero cochain. It also supplies the previously missing geometric outer derivation and verifies its supercommutation with `Q`.

It does **not** yet prove that the cochain represents a nonzero derived-cyclic cohomology class. A nonzero cochain may still be a Hochschild boundary. The remaining gate is to rule out

\[
\phi_v=-b\sigma
\]

for every permitted zero-cochain `sigma`, preferably by a reduced/Dorroh-normalized detector that retains the conductor residue line.

## Verification

```sh
python research/voevodsky/check_marici_p24_translation_cocycle_20260908.py \
  --root . \
  --output research/voevodsky/marici_p24_translation_cocycle_certificate_20260908.json
```

The checker performs 40 integration checks and records primitive value `-1` in all eight frames.
