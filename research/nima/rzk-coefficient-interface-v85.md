# v85: native cup-to-precomposition variance mate

Independent replay passed 42,503 assertions.

`rzk/111-native-variance-mate.rzk.md` records the normalized algebraic variance
mate between native endpoint bar-cup action and conductor-resolution
precomposition. The right target action is converted to a left action through
the Hopf antipode with the graded-opposite signs retained. The mate is a chain
map on the reconstructed bar and conductor Hom models, sends the primitive to
the retained `v` column with coefficient one, and intertwines the complete
relative-module action.

Full labelled transport and the decomposable reflection correction pass. The
checker also detects the unit defect produced by using the unconverted action
order, confirming that the variance conversion is essential.

The physical line/support adapter into the marked target remains unavailable.
Thus the result supplies the normalized native algebraic mate but not a fully
framed physical mate. The Rzk module passes a fresh check.
