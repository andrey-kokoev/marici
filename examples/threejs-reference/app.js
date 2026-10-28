import { createApp } from 'vue';
import App from './App.vue';
import './style.css';

const app = createApp(App, { host: document.querySelector('#viewport') });
const panel = app.mount('#panel');
// Retain the small diagnostic/test boundary; panel state and rendering are separate.
window.ReferenceViewer = Object.freeze({ dispose: () => panel.dispose(), snapshot: () => panel.snapshot() });
window.addEventListener('pagehide', event => {
  // A persisted page keeps its Vue scope; the renderer suspends for BFCache.
  if (!event.persisted) app.unmount();
});
