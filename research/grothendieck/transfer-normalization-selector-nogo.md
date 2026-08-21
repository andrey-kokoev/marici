# No scalar transfer normalization preserves both norm identity and delta selection

## Normalization no-go theorem

Let `q:G->H` be a finite surjection of degree `d>1`, work over a
characteristic-zero coefficient ring in which `d` is invertible, and consider
a scalar multiple `T=a q_!` of unnormalized fiber-sum transfer.

Because `q_!q^*=d id`, the condition

`T q^*=id`

forces `a=1/d`. But `q_! delta_0,G=delta_0,H`, so the condition

`T delta_0,G=delta_0,H`

forces `a=1`. These requirements are incompatible for `d>1`.

Thus no scalar normalization simultaneously splits pullback and preserves
the frozen identity selector. Unnormalized transfer preserves selection but
retains the degree norm; averaging splits the norm but rescales selection.

## Averaging projector

After inverting `d`,

`P=(1/d)q^*q_!`

is an idempotent projector onto fiber-constant coefficient functions. It sends

`delta_0,G` to `(1/d)1_(ker q)`,

not to `delta_0,G` for a nontrivial kernel.

For `C4->C2`, the image is `(1/2,0,1/2,0)`. Exact rational arithmetic also
checks scalar incompatibility for degrees two, three, and four.

## Scope

This is an algebraic coefficient no-go. A non-scalar geometrically weighted
physical transfer would require new source data and the absent Betti chain
map; it is not ruled in or out here.
