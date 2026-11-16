# Parabolic quarter-turn sources for the two-bite Ramsey construction

Date: 2026-11-09.  Status: exact infinite-family source theorem and finite checks. No new bound on `R(3,k)`.

## Aim

Find a source-generated *deterministic* replacement for the two random coordinate graphs and the local neighborhood controls in Harris–Hefty–Horn–King–Pfender, *A short proof that R(3,k)=Theta(k²/log k)*, arXiv:2609.01782v1, Lemma 3.1. Retain a literal quarter-turn interchanging the two incidence layers. Determine separately whether its global pair-loss bound (Lemma 3.2) follows.

## Source graph theorem

Let `q >= 5` be an odd prime with `q ≡ 2 (mod 3)`. Work in `W=F_q²`, and choose any `H subset F_q^×` of cardinality `h`. Put

    D_H = { (t,t²), (-t,-t²) : t in H }.

Make a Cayley graph `R` on `W`, joining `a,b` if `b-a in D_H`. The set `D_H` is inverse closed and avoids zero, so `R` is a simple undirected `d=2h` regular graph.

**Theorem A.** `R` is triangle-free, and all distinct vertices `a,b` obey `|N_R(a) cap N_R(b)| <= 6`.

Proof of triangle-freeness: a triangle requires `d1+d2+d3=0` with nonzero `di` from the signed parabola. In the mixed-sign case, after changing the signs of all terms if necessary, write `x+y=z` and `x²+y²=z²`, forcing `2xy=0`, impossible. In the all-equal-sign case, `x+y+z=0` and `x²+y²+z²=0` imply `x²+xy+y²=0`. For nonzero `x,y`, this gives a root of `r²+r+1`, i.e. a primitive third root of unity in `F_q`. Such a root cannot exist when `q≡2 (mod 3)`.

Proof of codegree bound: for a nonzero difference `(a,b)`, a pair of points on the same signed parabola realizes that difference in at most one way. There are two same-sign choices. Across opposite signs, the equations reduce to a quadratic in one parameter and have at most two solutions for each of the two sign orders. In total at most `1+1+2+2=6` ordered representations, which equals the common-neighbor count.

Let `rho(x,y)=(-y,x)`. It has order four on `W`, with `rho²=-I`. Define the second source graph `B` by the difference set `rho(D_H)`. It is also triangle-free, `d`-regular and codegree bounded by six. Rotation by `rho` maps the first layer to the second.

## Quarter-turn pair carrier

Choose a finite `T subset W` invariant under `-rho`. Set

    V_T = { (a,b) in W×W : b-a in T },
    s=|T|,  n=|V_T|=q²s.

Each coordinate fiber has exactly `s` elements. The quarter-turn on the final vertices is

    tau(a,b) = (rho(b),rho(a)).

It satisfies `tau²(a,b)=(-a,-b)`, `tau^4=id`, and `tau(V_T)=V_T`. It exchanges the red and blue lifted edge layers.

Let `X_x^R` be the lifted red source neighborhood at source coordinate `x`, and `X_y^B` its blue analogue.

**Theorem B.** For all different source coordinates in one layer,

    |X_x^R cap X_y^R| <= 6s,
    |X_x^B cap X_y^B| <= 6s,

and for all red source coordinates `x` and blue coordinates `y`,

    |X_x^R cap X_y^B| <= 16s.

For one color, each common source neighbor has exactly `s` representatives. For the mixed bound, fix `t=b-a in T`. The lifted overlap corresponds to the intersection of one translated signed parabola with a translated quarter-rotated signed parabola. For a fixed choice of two signs, substitute `y=c+eps(x-a)^2` into `x=d-eta(y-b)^2`. The resulting polynomial has degree four with nonzero leading coefficient, so at most four intersections. Four sign combinations and `s` available differences give `16s`.

The overlay may contain mixed triangles. Removing red edges that close blue length-two paths, and blue edges that close red length-two paths, produces a triangle-free graph. The operation commutes with `tau` because it uses permutation-equivariant Boolean matrix multiplication.

## Matching the paper's local hypotheses

Take `r=floor((log q)^2)` and `T` consisting of zero plus `r` distinct four-cycles under `-rho`, so `s=1+4r ~ (log n)^2`. Set

    h = floor[ sqrt(n log n)/(2s) ]

(truncated to `[1,q-1]` for small q). Then `ds=2hs <= sqrt(n log n)` and `s <= (log n)^2` for all sufficiently large q. Since the cross-layer overlap is at most `16s=O(log²n)`, it is at most `log³n` for sufficiently large n.

Hence this deterministic family satisfies the three numerical conclusions of **Lemma 3.1** of Harris et al. (fiber size, lifted neighborhood size, and pairwise source-neighborhood overlap), with no random coordinate graph or random projection. This does **not** establish the simultaneous pair-loss conclusion of their Lemma 3.2, the projection-size lemma, or the independent-set theorem.

## Exact finite results

The companion checker constructs the source graphs and a definite carrier `T` (first `r` four-cycles in lexicographic order) and computes maximum cross-layer source-neighborhood intersections by exact integer enumeration.

| q | final vertices n | fiber s | source degree d | lifted degree ds | maximal same-layer overlap | maximal cross-layer overlap |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 225 | 9 | 2 | 18 | 9 | 4 |
| 11 | 2541 | 21 | 6 | 126 | 42 | 8 |
| 17 | 9537 | 33 | 8 | 264 | 66 | 12 |
| 23 | 19573 | 37 | 10 | 370 | 74 | 12 |
| 29 | 37845 | 45 | 14 | 630 | 90 | 16 |

The universal estimates `<=6s` and `<=16s` are not claimed sharp.

## Exact finite obstruction to Lemma 3.2

The paper's key *global* bound is, for **every** relevant `K`-subset `I`, the loss

    L(I) = sum_x binom(|X_x^R cap I|,2)
         + sum_y binom(|X_y^B cap I|,2)

being at most `(1/20+5 eps)K²` for sufficiently large n in its random model.

At `q=29`, with `H={1,...,7}`, `s=45`, `n=37845`, and `K=floor(10 sqrt(n log n))=6316`, take the first 6316 vertices in lexicographic source-first order `(a,b)`, with every selected red fiber filled before advancing to the next. Their **exact** pair-loss is

    L_R = 8,006,820,
    L_B = 4,696,880,
    L   = 12,703,700,
    L/K² = 0.31845347080366476.

This exceeds `1/20+5/1000=0.055`. All the local bounds above still hold. Therefore local overlap bounds and exact quarter-turn symmetry alone **do not imply** the paper's global pair-loss bound. This is a finite counterexample to the proposed implication, not an asymptotic impossibility theorem for the entire parabolic family. In particular, `H={1,...,h}` is an intentionally structured source choice, and the paper's asymptotic proof requires additional pseudorandom incidence properties.

## Consequence for the Ramsey generator

The first probabilistic ingredient (good fiber and local-neighborhood overlaps) now has an exact, scalable, geometric replacement, compatible with the original four-phase symmetry operation. The missing next operation is **global dispersion of source incidences and transverse projections**, ensuring no large subset packs too heavily into shared source neighborhoods.

Next discriminating tests:

- Replace the interval `H` with a dispersed, source-defined selector without altering the triangle-free or codegree theorems.
- Prove or falsify a global uniform bound on the overlap loss `L(I)` for `K ~ 10 sqrt(n log n)` across all `K`-subsets, not just sampled sets.
- Independently establish that every large `K`-subset has a projection of size at least `(1/2-eps)K`, so the paper's Section 4 argument can be transported.

The present construction does not prove a new lower bound, an exact Ramsey-number formula, or any universality of the rotation-generated family.

## Reproduction

    python /mnt/data/check_ramsey_parabolic_quarter_turn.py

Source: Harris, Hefty, Horn, King, Pfender, arXiv:2609.01782v1, especially §§2–4; prior note `ramsey_quarter_turn_pair_loss_transversality_2026-11-09.md`.
