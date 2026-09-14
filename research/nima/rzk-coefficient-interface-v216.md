# v216: independent symbolic coordinates are obstructed by source rank

The current physical pullback has integral homology rank one, while the selected packet `Z<s> direct-sum Z<W> direct-sum Z<v>` has rank three. Any linear map from the current source is determined by one three-entry column and has image rank at most one. Therefore it cannot realize independently variable `(a,b,c)`.

The constructed column is `(1,1,1)`, giving the valid normalized five-direction witness and residue `-3 beta`. Integer multiples scale all three entries together.

This is not a failure of the packet trace law `-beta*(a+(b+c))`; that law remains valid on the rank-three packet. It is a source-size obstruction to physically inhabiting every independent triple using the one line from Entry 436. Reopening the symbolic objective requires one of: a rank-three coefficient-enriched physical source, a source-derived nonlinear three-parameter family, or three independent physical Gysin channels.

The exact rank control is `check_rank_one_to_three_packet_no_go.py`; module 238 records the obstruction.
