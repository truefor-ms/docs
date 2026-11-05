TRUEFORMS MASTER SPEC + HANDOFF / v2.0 / 5 Kasım 2026

BAŞLANGIÇ
1. trueforms-logo-master-spec.pdf veya aynı adlı HTML dokümanı açın.
2. examples/index.html ile B/A, tema, renk modu ve genişliği inceleyin.
3. Uygulamada ana logo assets/svg/trueforms-logo.svg (B/color).
4. A alternatifi assets/svg/trueforms-logo-alt-a.svg.

MODLAR
color: #16765C ikon / #183C32 yazı / #AFBDB0 nokta.
dark: #E8EFE5 ikon / #F8F7F2 yazı / #657B70 nokta. Yeni öneri.
mono: bütün parçalar #183C32. black: #000000. white: #FFFFFF.
currentcolor: yalnızca inline SVG için CSS color mirası.
Tüm modlar A ve B olarak hazır. Sabit renk PNG'ler 1200 ve 2400 px.

ÖRNEKLER
examples/index.html: sistem temasıyla başlar.
examples/light.html: açık.
examples/dark.html: koyu.
examples/monochrome.html: tek renk.
HTML örneklerini ZIP'i çıkardıktan sonra yerelde açabilirsiniz. Relative klasör yapısını koruyun.
Master HTML görseller ve arayüz fontları dahil tek dosyadır, internet gerektirmez.

GELİŞTİRİCİ
examples/TrueformsBrand.tsx: layout B/A, mode ve assetBase.
tokens/trueforms.css + trueforms.tokens.json: renkler ve tema.
specs/trueforms-logo-spec.json: kesin ölçüler ve A/B deltaları.
HANDOFF-INSTRUCTIONS.txt: doğrudan devredilecek talimat.
source-reference: mevcut B/A/ikon/avatarın değişmemiş kaynakları.

DOĞRULAMA
Python 3: python3 scripts/validate-assets.py (standart kütüphane).
Node.js + sharp: node scripts/render-pngs.cjs [paket-dizini].
Üretim PNG'leri hazırdır; tüketmek için Node/sharp kurulumu gerekmez.
PDF/HTML bu sürümün kaynak spec'ini birlikte taşır. PDF'nin Attachments bölümünde B/A SVG, JSON, master HTML ve üretim ZIP'i bulunur.

SINIRLAR
Yeni koyu tema/spacing/UI değerleri [Öneri]; mevcut logo geometrisi kesin referanstır.
HTML tarayıcı görsel/etkileşim ve hedef React proje build testi alıcı ortamında tamamlanmalı.
Font bildirimlerini licenses/ altında koruyun. Logo Nimbus outline'dır; UI display fontu Linux Libertine ile karıştırmayın.
