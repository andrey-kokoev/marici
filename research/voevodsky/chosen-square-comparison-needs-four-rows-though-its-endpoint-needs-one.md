# Chosen square comparison needs four rows though its endpoint needs one

The exact local P=(1,2,0,0) and Q=(0,1,1,1) Farkas packets proving x<=2 have support {x-low,x-high} and {x-high,y-low,y-high}. Their CHOSEN comparison union contains all four primitive rows, so deleting any one row invalidates at least one of these two literal packets. Fresh `check_standalone_row_dependency.py` verifies this.

The endpoint x<=2, however, remains provable after deleting x-low, y-low or y-high: x-high alone with multiplier 1 and surplus 1 suffices. Delete x-high and the endpoint itself becomes false; point (3,0) satisfies all other remaining inequalities and violates x<=2. Thus row retention needed to replay THIS comparison is stronger than retention needed merely to check its endpoint inequality. This is not a universal minimum for all proofs or a publication grant.

Next test a semantic endpoint TRUE under source change while a formerly valid signed comparison fails because one deleted row was part of its path. Distinguish a new re-proving witness from a transport of original proof history, with exact row-manifest hashes and no owner/analytic authority inference.
