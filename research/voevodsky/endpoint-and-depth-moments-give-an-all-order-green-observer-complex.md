# Endpoint and depth moments give an all-order Green observer complex

## Result

Adding all polynomial moments of endpoint length and total seam depth gives an explicit complete observer space on which the prescribed Green mate is continuous. It is stable under the observer differential and maps continuously into the representable-mate graph complex. This strengthens the fixed two-seam sufficient domain without declaring the whole receiver Green-self-dual.

Input:
`../nima/two-seam-green-mates-require-endpoint-incidence-control.md`.
The local insertion/mate estimate and its actual vacuum obstruction are inherited from that note. The present calculation supplies the all-depth norm control.

## 1. Keep the four different counts

A homogeneous typed record has:

- outer endpoint event length n;
- total seam-complex factor count r;
- active edge count k, with 0<=k<=r;
- total retained feature count m.

The remaining r-k separators are vertices. Keep the existing graph multiplier b_s(k)=(2 lambda s)^k k!, feature multiplier b^m, and positive slot norms. The signed Green form is unchanged; these graph multipliers are control norms, not coefficients in that form.

Define observer seminorms

    O_(s,b,p,q)(y)
      = sum_shapes (1+n)^p (1+r)^q b_s(k)b^m ||y_shape||,

for integers s,b>=1 and p,q>=0. Let O_mom be the compatible intersection of these weighted l1 spaces. It is complete. Finite endpoint/depth/degree support with algebraic feature approximations is dense in every finite set of its seminorms.

Do not replace r by n or k. Arbitrary observer terms can have inactive vertex factors, and the source's minimum-event relation bound is not a bound on every ambient observer.

## 2. All-depth mate estimate

For a fixed vertex separator in an n-event Boolean interval there are at most n incident elementary edges. Each supplies at most two channels: reversed vacuum insertion, or extraction of the unique adjacent end feature. Thus there are at most 2n channels per vertex. The prescribed local Green mate has Hilbert norm at most lambda because the normalized ambient signatures have norm one.

The mate increases k to k+1, so its graph-weight ratio is 2 lambda s(k+1). Total feature count, outer endpoint length, and r are preserved. With r-k vertices, the bound is

    4 lambda^2 s n (r-k)(k+1).

The elementary inequality

    4(r-k)(k+1)<=(r+1)^2

therefore gives

    O_(s,b,p,q)(d^sharp y)
      <= lambda^2 s O_(s,b,p+1,q+2)(y).

When k=r the mate in this direction is zero. For r=2 the sharper count recovers the supplied 8 lambda^2 s endpoint-moment estimate. Triangle inequalities handle coincident outputs; no sign cancellation is needed for the bound.

Hence d^sharp extends continuously to O_mom. The endpoint and depth moments—not a fixed change of feature or active-depth radius alone—supply the missing incidence control.

## 3. Observer differential and graph inclusion

Apply the prescribed cochain-dual sign in each degree and write delta_O for the resulting signed mate. On finite records its transpose satisfies delta_O^2=0. The estimate above makes its continuous extension map O_mom into itself. Density and injectivity of the ambient beta imply the same square-zero identity on the completion.

More explicitly,

    beta(delta_O y)=d_(T^h) beta(y).

Both sides are continuous into the strong scalar dual. A second application gives beta(delta_O^2 y)=0, hence delta_O^2 y=0. This uses the nondegenerate ambient signed carrier, not a nondegenerate source-image Gram.

The map

    y -> (y,delta_O y)

is continuous into Nima's representable-mate graph domain, with its existing graph seminorms. Thus O_mom is an explicit stable subcomplex of that maximal graph complex. Equality with the maximal domain is not claimed: cancellations may permit observers without all absolute moments.

## 4. Paired attachment squares

Restrict the already constructed Green beta and attachment transposes to O_mom. The source connecting projection and its dual inclusion do not change. The observer square still commutes because it is the restriction of the same continuous transposed identity.

The same construction may be used sectorwise at every seam depth, with the established attachment shift and tensor-of-shifts signs. Opposite-history reversal remains a different operation. No statement that all source dual functionals lift is implied; the approximate-null source families continue to obstruct that surjectivity.

Source actions on these observers require their own moment bounds if one wants an action-stable module assertion. The result here is the observer differential complex and its paired attachment maps, not an unrestricted representation of every completed dual source action.

## 5. Why the strengthening is necessary but not characterized as minimal

The supplied two-seam family y=sum_(n>=2) y_n/n^2 belongs to every old depth/feature scale but has no Green mate in that receiver. It is excluded by the endpoint moment p=1, as intended. Adding only s or b could not exclude it.

The added depth moments handle the possible number of inactive vertex factors for all r. The estimate is sufficient, not an optimal domain characterization. No finite Green form, theta forcing, memory weight, or source attachment has been altered.

## Verification

Fresh `uv run python research/nima/checkers/check_two_seam_green_mate_incidence.py` passes 3098 actual vacuum boundary tests and 152 graph/moment checks.

`uv run python research/voevodsky/checkers/check_all_depth_observer_moment_bounds.py` passes 30240 exact general channel/weight comparisons. The completion and square-zero extensions are proved above; the checker does not infer them from a sampled spectral matrix.
