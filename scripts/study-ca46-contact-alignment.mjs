import {writeFileSync} from 'node:fs';
import {solveContactFrameAlignment} from '../examples/isotope-wiring/core/contact-frame-alignment.mjs';
const axis=[0,0,1],reference=[1,0,0];
const result={contact:{from:'space:s1-00:B',to:'space:s2-01:T'},actual:solveContactFrameAlignment(),
 axisOnlyControl:solveContactFrameAlignment({source:{axis},target:{axis}}),
 alignedReferenceControl:solveContactFrameAlignment({source:{axis,reference},target:{axis,reference}}),
 quarterTurnReferenceControl:solveContactFrameAlignment({source:{axis,reference},target:{axis,reference:[0,1,0]}}),
 conclusion:'Both identity and quarter-turn transport fit the same aligned contact axes when different transverse references are supplied. A physical port reference, not point contact or projected stacking alone, is required to select the frame rotation.'};
if(process.argv[2])writeFileSync(process.argv[2],JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({actual:result.actual.status,axisOnly:result.axisOnlyControl.status,remainingFreedom:result.axisOnlyControl.freedom,alignedReferenceRotation:result.alignedReferenceControl.rotation,quarterTurnReferenceRotation:result.quarterTurnReferenceControl.rotation,conclusion:result.conclusion},null,2));
