import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {studyBottleneckNeutronCoherence} from '../examples/isotope-wiring/core/bottleneck-neutron-coherence.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),model=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true})),results=['direct','neutron-mediated'].map(mode=>studyBottleneckNeutronCoherence(buildStackedFullInterface(model,{mode})));
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify(results.map(r=>({mode:r.mode,status:r.status,counts:r.comparison.counts,accessPairs:r.comparison.localAccessPairsChecked,bridgeChecks:r.bridgeChecks,flatControl:r.flatControl.status,cyclicTwistControl:r.twistedControl.status,bridgeTwistControl:r.bridgeTwistControl.status,interpretation:r.interpretation})),null,2));
