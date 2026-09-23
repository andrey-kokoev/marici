# Farkas row-evaluation cache cannot cache certificate validity without target and surplus

On the same frozen square rows, x-upper multiplier 1 has raw normal (1,0), raw bound 1. That RAW evaluation can be reused across three local packets. Target x<=1 with surplus 0 passes; target x<=2 with surplus 1 passes; target x<=1 with surplus 1 FAILS. Fresh `check_packet_target_cache_layers.py` shows that caching a Boolean certificate result solely by source/generation/multiplier falsely accepts the third packet after a hit on the first. A separate certificate-result key must bind exact target normal/bound AND surplus, in addition to the raw row-evaluation key.

Even an exact cached certificate result remains mathematical computation only. It does not authenticate a source row issuer, an occurrence ID, a past evaluation event or permission to publish under an exact target. The analytic S,A,R,C,G assignment remains deferred.

Next test a PACKET SERIALIZATION ambiguity where `1`, `1/1` and decimal `1.0` denote the same rational but hash differently unless exact canonical rational normalization is enforced. Refuse non-exact floating input and verify exact numerator/denominator normalization without elevating canonical hashes into source authority.
