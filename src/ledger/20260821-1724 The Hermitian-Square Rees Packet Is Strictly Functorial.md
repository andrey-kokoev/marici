# 1724 — The Hermitian-Square Rees Packet Is Strictly Functorial

## Naturality gate

For a labelled amplitude map \(f\), define the induced density map

\[
\mathsf H(f)(\rho)=f\rho f^\dagger.
\]

Entry 1723's mixed second-grade coefficient is

\[
H(u,v)=|u\rangle\langle v|+|v\rangle\langle u|.
\]

Exact expansion gives

\[
\boxed{H(fu,fv)=fH(u,v)f^\dagger.}
\]

The diagonal grades obey the same identity, and for composable maps

\[
\mathsf H(g)\mathsf H(f)=\mathsf H(gf)
\]

strictly.

## Narrow result

The complete second-normal quantum packet is the functorial Hermitian square
of the labelled amplitude-normal module.  Its mixed phase coefficient is not
a coordinate-dependent extension, and no additional coherence cell or Cut
carrier stratum is required in the tested finite model.

## Durable artifacts

- `research/benincasa/checkers/hermitian_square_rees_functoriality.rs`
- `research/benincasa/results/hermitian-square-rees-functoriality.json`
- `research/benincasa/hermitian-square-rees-functoriality.md`

## Next falsifier

Test singular amplitude maps.  Determine whether kernel directions disappear
by ordinary Hermitian-square pushforward or survive as supported costalk data
on the rank-drop locus.
