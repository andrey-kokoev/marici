# Endpoint reproof after row deletion is not transport of the old comparison

Delete the x-lower primitive row from the four-row square manifest. The OLD P=(1,2,0,0) and old signed Q-P=(-1,-1,1,1) have nonzero deleted-row coordinates, so neither literal record survives. Simply dropping the deleted coordinate from the old comparison fails the zero-normal/bound equation. Yet x<=2 remains true and admits a NEW proof using x-upper multiplier 1 with surplus 1; the retained Q proof still works. Their new signed difference on the three-row source is (0,1,1;surplus -1), with zero total normal/bound. Fresh `check_endpoint_reproof_not_path_transport.py` checks these exact equations and differing row-manifest hashes.

Thus a valid reproof on an edited source is not a transport of original execution history. Even matching endpoint meaning and a newly valid signed comparison do not justify a source-owner rebind or equality of histories. All calculations remain LOCAL Farkas math; analytic S,A,R,C,G mapping remains deferred.

Next test minimal disclosure for the NEW reproof: only x-upper row is used, but source-scoped proof publication could still require the complete ordered source manifest if a future grant binds it. Compare proof support with authorization scope, refusing an attempt to replace an exact full-manifest grant with a digest of just the support subset.
