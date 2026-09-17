# qRB microstep 11: varying-width observer closure

The dilation calculation forces one precise adjustment: use the Gaussian family

$$
 g_{\sigma,t}(x)=\exp\!\left(-\frac{(x-t)^2}{2\sigma^2}\right),
 \qquad \sigma>0.
$$

For an affine refinement `x -> ax+b`,

$$
 g_{\sigma,t}(ax+b)
=
 g_{\sigma/|a|,(t-b)/a}(x)
$$

up to the harmless positive normalization factor when normalized Gaussians are used.

Thus the observer family is closed under the elementary affine pullbacks, provided width is treated as an observer parameter rather than frozen.

This is a minimal enlargement: no new positivity assumption is introduced, and fixed-width translation faithfulness remains available as a subfamily.

Status: elementary affine closure established. The actual source refinement maps may be non-affine or may act on the arithmetic labels; their pullback must still be checked separately.
