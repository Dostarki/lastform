# LastZhood — Project Zomboid esintili katılım uygulaması

## Özgün kullanıcı isteği
https://agnt.trade

Bu siteyi bana birebir kopyala. X katılım formu falan hepsi aynı olsun.
Veritabanı ise mongodb olsun. X follow-rt-COMMENT yazı ve linkleri ise .env den düzednlensin

Tasarım renk konusuna gelirsek eğer daha böyle project zomboid oyun tarzı olsun. Yapmadan önce bana örnekler göster.

## Kullanıcı kararları
- Son kullanıcı isteği: "Proje adı LastZhood olacak. Siteyi ona göre isim yap. x.com/LastZhood". Uygulama markası LastZhood, resmî hesap @LastZhood.
- Kodlamadan önce üç görsel konsept görmek istiyor: kıyamet sonrası terminal, yıpranmış hayatta kalma panosu, retro askerî arayüz.
- Aynı zamanda orijinal sitenin düzenine yakın kalınmasını; renk, tipografi ve doku değişikliklerini seçti.
- X görevleri bağlantı açma ve kullanıcı beyanına dayanacak; gerçek X doğrulaması veya OAuth istenmiyor.
- Kullanıcı 2 · Hayatta Kalma Panosu konseptini seçti; orijinal düzen ve yıpranmış harita dokusuyla uygulama kuruluyor.

## Kullanıcı profili
- X kampanyası katılımı ve erken erişim kaydı yapmak isteyen ziyaretçi.
- Takip, RT ve yorum metinleri/bağlantılarını .env üzerinden düzenlemek isteyen site sahibi.

## Uygulanan mimari
- React arayüz, FastAPI API, MongoDB kalıcılığı.
- Mevcut korumalı MONGO_URL, DB_NAME ve REACT_APP_BACKEND_URL kullanılacak; değiştirilmeyecek.
- Tasarım rehberindeki MONGODB_URI / Mongoose önerileri uygulanmayacak; ortamın mevcut Python/MongoDB yapısı korunacak.
- Herkese açık görev ayarları sunucudan okunacak; gizli ortam değişkenleri istemciye aktarılmayacak.
- X kullanıcı adı girişi kimlik doğrulaması değildir; tamamlanmış görevler doğrulanmış olarak gösterilmeyecek.

## Referans incelemesi — 2026-07-19
- Crawl ve Playwright ile https://agnt.trade herkese açık sayfası incelendi; kaynak siteye kayıt veya form gönderimi yapılmadı.
- İlk ekran: tam ekran hareketli kare ajan ızgarası, sol üst logo, sağ üst sayaç/early access, büyük merkezî agnt logosu, terminal metni, X handle alanı ve CONNECT X, altta yeni katılanlar bandı.
- DOM/crawl içinde: mission console, agent license, cell/class/tier, görev sayacı 0/4, EVM adres alanı/Bind, Claim early access, AGENT LIVE, Post on X, Save card, Copy ref code görüldü.
- Görevlerin kesin içeriği henüz doğrulanmadı; kaynağa kayıt yapılmadan incelenmeli veya kullanıcının istediği follow/RT/comment akışına uyarlanmalı.

## Yapılanlar — 2026-07-19
- Gereksinimler netleştirildi ve üç geçici tasarım yönü /app/design_guidelines.json dosyasında oluşturuldu.
- Üç görsel maket üretildi. Bunlar çalışan uygulama ekranları değil, tasarım örnekleridir; örnek sayaçlar gerçek uygulama verisi değildir.
- Seçilen harita dokusu için bağımsız, metinsiz görsel üretildi; `/frontend/src/assets/survival-map.jpg` dosyasına kaydedildi.
- Kaynağın herkese açık JavaScript dosyaları incelendi: dört görev FOLLOW, LIKE, REPOST, COMMENT; hedef @agntmarkets, gönderi kimliği 2103830135996833932. Kaynak siteye veri gönderilmedi.

## Tamamlanan uygulama — 2026-07-19
- Ana ekran: seçilen harita/pano görünümü, marka, gerçek kayıt sayısı, X kullanıcı adı girişi, son katılanlar, ağ durumu, saat. Yapay katılımcı/sayaç yok.
- Dört adımlı konsol: kullanıcı adı, FOLLOW/LIKE/REPOST/COMMENT linkleri ve açık kullanıcı beyanı kutuları, EVM adresi bağlama/düzenleme, rıza ve kayıt.
- Taslak localStorage'da; kalıcı kayıt MongoDB'de. UUID istek kimliği idempotency için; hesap kimlik doğrulaması değil. X kullanıcı adı case-insensitive benzersiz. Görevler, adres ve rıza API'de doğrulanıyor.
- Kayıt sonucu: numara, hücre, sınıf, tier, referans kodu; yerel canvas ajan kartı PNG indirme/panoya kopyalama; X paylaşımı ve davet bağlantısı. Kart yüklemesi veya dosya saklama entegrasyonu yok.
- `/agent/:refCode` herkese açık kart ve davet akışı. Wallet/request_id/consent gibi özel alanlar public API'de yok.
- Ayarlar: `backend/.env` görev metin/linkleri, yorum mesajı, paylaşım mesajı, X profili. `/api/config` yalnızca izinli açık ayarları döndürür; `.env` güncellemeleri sonraki istekte okunur. Kullanım: `backend/CONFIGURATION.md`.
- API: GET `/api/`, `/api/config`, `/api/agents/stats`, `/api/agents/recent`, `/api/agents/{ref_code}`; POST `/api/participations`.
- Sayfalar: `/`, `/console`, `/agent/:refCode`; bilinmeyen sayfa/kod için hata ekranı.

## LastZhood isim güncellemesi — 2026-07-19
- Kullanıcının son isteğiyle logo, büyük başlık, footer, sekme başlığı, açıklama, LZ favicon, kart görseli/indirme dosya adı, paylaşım metinleri LastZhood olarak değiştirildi.
- Resmî X hesabı `https://x.com/LastZhood`; follow intent `screen_name=LastZhood`.
- Kullanıcı belirli bir gönderi URL'si vermedi; X profil taraması da gönderi döndürmedi. Bu nedenle LIKE/REPOST/COMMENT açıkça "a @LastZhood post" metniyle LastZhood profilini açıyor. Eski agntmarkets hedefleri tamamen kaldırıldı. Belirli tweet hedefi istenirse `.env` linkleri güncellenebilir.
- Yorum mesajı konsolda görünür ve `Copy reply` ile kopyalanabilir; intent URL ayarlanırsa aynı mesaj URL'ye eklenir.
- LocalStorage yeni anahtarı `lastzhood-survivor-v1`; önceki `agnt-survivor-v1` taslakları için okuma geçişi korundu.

## Doğrulama ve düzeltmeler — 2026-07-19
- İlk test raporu `/app/test_reports/iteration_1.json`: 13/13 backend geçti; cüzdan düzenleme düğmesinde tık sonrası formun tekrar submit olması hatası bulundu.
- Düzeltme: düzenle/bağla düğmelerine ayrı React key, düzenleme olayında preventDefault, adres düzenlenince rıza sıfırlama.
- Son rapor `/app/test_reports/iteration_2.json`: backend ve frontend kapsamı %100 geçti; açık hata yok.
- LastZhood adı ve taşma testleri: 1920×800 masaüstü, 390/381/375/320 genişlik mobil; kullanıcı adı, görev açma/beyan ayrımı, adres hataları, düzenle/tekrar bağla, rıza, kayıt ve yeni wallet değerinin MongoDB'de kalıcılığı doğrulandı.
- PNG indirme, panoya kopyalama/fallback, public kart, referans kaydı, hata durumları, duplicate/idempotency ve private alanların dışarı sızmaması test edildi.
- `yarn build` başarılı. Test kayıtları temizlendi. X üzerinde gerçek sosyal işlem yapılmadı; X API entegrasyonu kullanıcı tercihi gereği yok.
- Son görseller `/app/test_reports/artifacts/iteration_2/` altında.
- Runtime wallet kontrol dosyası, geçici test kaydı temizlendikten sonra tekrar koşulduğunda yanlış alarm vermemesi için pytest dizininden kaldırıldı; sonuç raporda kayıtlıdır.

### Görsel örnekler
1. CRT terminal: https://static.prod-images.emergentagent.com/jobs/a2dcf251-5c25-48b6-bb5b-fcddb74891ae/images/64ae54abfdee76899a9fef1c0eedd7e08001e3ae5533b3a803062e0455cc8eb0.jpeg
2. Hayatta kalma panosu: https://static.prod-images.emergentagent.com/jobs/a2dcf251-5c25-48b6-bb5b-fcddb74891ae/images/c968eb18e6ddacedef4d108b5c04e6e2eb5777a650340d10682954693c715f56.jpeg
3. Askerî radar: https://static.prod-images.emergentagent.com/jobs/a2dcf251-5c25-48b6-bb5b-fcddb74891ae/images/c9cae18d6079489b15507949c8af294fb5a9048846f31441f8c714d0df2fbf71.jpeg

## Önceliklendirilmiş kalan işler
- P0: Yok; istenen çekirdek akış ve LastZhood isim güncellemesi tamamlandı.
- P1 (isteğe bağlı kampanya girdisi): Kullanıcı belirli gönderi bağlantısı paylaşırsa beğeni/RT/yorum görevlerini o gönderiye yönlendirmek. Şimdiki profil akışı kullanılabilir durumdadır.
- P2 önerileri (henüz kullanıcı istemedi): Referans davet sıralaması; hayatta kalma temalı farklı ajan portreleri; Türkçe/İngilizce dil seçimi.