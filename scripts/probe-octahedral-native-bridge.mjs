import {probeOctahedralNativeBridge} from '../research/strominger/octahedral-native-bridge.mjs';
console.log(JSON.stringify([0,1,2].map(radius=>({radius,...probeOctahedralNativeBridge(radius).audit})),null,2));
