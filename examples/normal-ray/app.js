import { createApp } from 'vue';
import App from './App.vue';
import './style.css';
const app=createApp(App,{host:document.querySelector('#scene')});
const handle=app.mount('#ui');
// Same explicit lifecycle test boundary as the reference; renderer objects never
// enter Vue reactivity. Compatibility diagnostics remain available to checks.
globalThis.NormalRayViewer={inspectView:options=>handle.inspectView(options),snapshot:()=>handle.snapshot(),dispose:()=>handle.dispose(),unmount:()=>app.unmount()};
