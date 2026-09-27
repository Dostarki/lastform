# LastZhood kampanya ayarları

`backend/.env` dosyasında takip, beğeni, RT ve yorum görevleri düzenlenir.

| Değişken | Açıklama |
| --- | --- |
| X_PROFILE_LINK | Resmî LastZhood X profil bağlantısı |
| X_FOLLOW_TEXT / X_FOLLOW_LINK | Takip görevinin görünen metni ve X bağlantısı |
| X_LIKE_TEXT / X_LIKE_LINK | Beğeni görevinin metni ve bağlantısı |
| X_REPOST_TEXT / X_REPOST_LINK | RT görevinin metni ve bağlantısı |
| X_COMMENT_TEXT / X_COMMENT_LINK | Yorum görevinin görünen metni ve yanıt bağlantısı |
| X_COMMENT_MESSAGE | X yorum penceresinde önceden yazılan mesaj |
| X_SHARE_TEXT / X_SHARE_LINK | Tamamlanan ajan kaydının paylaşım metni ve X paylaşım adresi |
| PUBLIC_APP_URL | Kart ve referans bağlantılarının uygulama adresi |

Resmî hesap `https://x.com/LastZhood` olarak ayarlanmıştır. Kullanıcı belirli bir gönderi bağlantısı vermediği ve X gönderileri herkese açık taramada okunamadığı için beğeni, RT ve yorum görevleri bu profili açar. Katılımcılar bir LastZhood gönderisi üzerinde işlemlerini tamamlayıp beyan eder. Eski projenin gönderi bağlantıları kaldırılmıştır.

Belirli bir kampanya gönderisini hedeflemek için `X_LIKE_LINK`, `X_REPOST_LINK`, `X_COMMENT_LINK` alanlarını güncelleyin. Bağlantılar HTTPS ve x.com/twitter.com alan adında olmalıdır. Beğeni için `/intent/like?tweet_id=GONDERI_ID`, RT için `/intent/retweet?tweet_id=GONDERI_ID`, yorum için `/intent/post?in_reply_to=GONDERI_ID` biçimleri kullanılabilir. Yorum intent bağlantısında `.env` mesajı otomatik doldurulur. Profil/doğrudan gönderi bağlantısında katılımcı `Copy reply` düğmesiyle aynı mesajı kopyalayabilir.

Kampanya ayarları sonraki API isteğinde dosyadan okunur. Tarayıcıyı yenilemek yeterlidir. MONGO_URL, DB_NAME ve frontend REACT_APP_BACKEND_URL değerlerini değiştirmeyin.

Kullanıcı adı ve görev tamamlama kullanıcı beyanıdır; X hesabı sahipliği, gerçek takip/RT/yorum veya paylaşım doğrulanmaz. Cüzdan yalnızca EVM adresi olarak saklanır; özel anahtar, cüzdan bağlantısı veya işlem imzası istenmez. Cüzdan adresi herkese açık API yanıtlarına dahil edilmez.

Taslak aynı tarayıcının yerel belleğinde tutulur; son talep MongoDB'ye kaydedilir. Hesap girişi bulunmadığından farklı tarayıcıdan mevcut bir kaydın özel alanları görüntülenemez/değiştirilemez. Her X kullanıcı adı için tek kayıt vardır.