import { computed, ref } from 'vue';
export function useViewerModel() {
  const opacity=ref(0.12),phase=ref('loading'),error=ref('');
  const ready=computed(()=>phase.value==='ready');
  const status=computed(()=>ready.value?'ESD7 outer shell ready.':phase.value==='loading'?'Loading local Three.js…':`Static diagram shown. ${error.value}`);
  const renderState=computed(()=>({opacity:Math.max(0,Math.min(0.5,Number(opacity.value)||0))}));
  return {opacity,phase,error,ready,status,renderState};
}
