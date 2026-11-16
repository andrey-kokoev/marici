import {readFileSync,writeFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {bindChannelTransport,compareDirectAndMediatedTransport} from '../examples/isotope-wiring/core/channel-frame-transport.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),model=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true}));
const direct=buildStackedFullInterface(model),mediated=buildStackedFullInterface(model,{mode:'neutron-mediated'});
const A=[[1,0,0],[0,0,-1],[0,1,0]],B=[[0,-1,0],[1,0,0],[0,0,1]],R=[[0,0,1],[1,0,0],[0,1,0]],H=[[0,0,1],[0,1,0],[-1,0,0]],wrong=[[0,-1,0],[0,0,-1],[1,0,0]];
const result={actual:compareDirectAndMediatedTransport(),parameters:{direct:{edges:direct.interface.forward,rotation:'R in SO(3), unspecified'},mediated:{edges:mediated.interface.forward,rotations:'A, B in SO(3), unspecified',effective:'B A'}},
 matchedControl:compareDirectAndMediatedTransport({direct:R,entry:A,exit:B,intermediateGauge:H}),wrongOrderControl:compareDirectAndMediatedTransport({direct:wrong,entry:A,exit:B}),
 boundControls:{direct:bindChannelTransport(direct,[R]).audit,mediated:bindChannelTransport(mediated,[A,B]).audit},
 conclusion:'Direct and mediated channels have the same endpoint action exactly when R = B A. An intermediate frame change leaves B A unchanged. Neither equality nor a physical R follows from reversibility or the drawing.'};
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({actual:result.actual.status,parameters:result.parameters,matchedControl:result.matchedControl.status,intermediateGaugeControl:result.matchedControl.gauge.status,wrongOrderControl:result.wrongOrderControl.status,conclusion:result.conclusion},null,2));
