import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {auditDefinitionPathReversal} from '../examples/isotope-wiring/core/path-reversal.mjs';
import {auditFrameReturn} from '../examples/isotope-wiring/core/frame-return.mjs';
// A JSON file supplies an absolute definition with an explicit pathTopology.
// With no argument, audit the current built-in Ca46 without inventing topology.
const args=process.argv.slice(2),frame=args[0]==='--frame';if(frame)args.shift();
let definition;
if(args[0])definition=JSON.parse(readFileSync(args[0],'utf8'));
else{
 const html=readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8'),context=vm.createContext({});
 vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],context);
 definition=context.IsotopeWiring.fixtures().Ca46;
}
const result=frame?{definitionId:definition.id,...auditFrameReturn(definition.frameTopology)}:auditDefinitionPathReversal(definition);
console.log(JSON.stringify(result,null,2));
// Distinguish a counterexample from missing evidence for automation.
process.exitCode=result.status==='verified'?0:result.status==='refuted'?1:2;
