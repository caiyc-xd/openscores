// Service Worker：缓存站点静态资源（alphaTab 引擎、Bravura 字体、音色库 FluidR3_GM.sf3、样式等），
// 使「打开本地谱」在首次在线访问后，断网也能渲染并播放。
// 仅作渐进增强：注册/缓存失败都不影响基本功能。
const CACHE = 'openscores-static-v1';

self.addEventListener('install', () => { self.skipWaiting(); });

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // 仅处理同站资源

  if (req.mode === 'navigate') {
    // 页面：网络优先，离线回退到缓存（保证线上更新可见，且断网仍能打开）
    event.respondWith(
      fetch(req).then((r) => {
        const c = r.clone();
        caches.open(CACHE).then(ca => ca.put(req, c)).catch(() => {});
        return r;
      }).catch(() => caches.match(req).then(m => m || caches.match('./index.html')))
    );
    return;
  }

  // 静态资源：缓存优先（含 14MB 音色库、字体、脚本），离线可用
  event.respondWith(
    caches.match(req).then((m) => {
      if (m) return m;
      return fetch(req).then((r) => {
        if (r && (r.ok || r.type === 'opaque')) {
          const c = r.clone();
          caches.open(CACHE).then(ca => ca.put(req, c)).catch(() => {});
        }
        return r;
      }).catch(() => m);
    })
  );
});
