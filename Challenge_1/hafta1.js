
// !Easy: 
// *Kullanıcının doğum tarihini alarak kaç yaşında olduğunu bulan bir algoritma yazmanızı istiyorum.


dateYear = Number(prompt("Doğum tarihinizi giriniz : "));

const year = new Date();
let yearNow = year.getFullYear();

let age = yearNow - dateYear
console.log(`yaşınız : ${age}`);


// !Medium: 
// *Kullanıcıdan bir metin almanızı istiyorum. Bu metnin içindeki en çok tekrar eden harfi bulmalı ve 
// *kaç kere tekrar ettiğini göstermeli.


function enCokTekrarEdenHarf(metin) {
    const harfSayilari = {};
    const metinDuzgun = metin.replace(/[^a-zA-Z]/g, '').toLowerCase();

    for (let harf of metinDuzgun) {
      if (harfSayilari[harf]) {
        harfSayilari[harf]++;
      } else {
        harfSayilari[harf] = 1;
      }
    }

    let enCokTekrarEdenHarf = '';
    let enCokTekrar = 0;

    for (let harf in harfSayilari) {
      if (harfSayilari[harf] > enCokTekrar) {
        enCokTekrar = harfSayilari[harf];
        enCokTekrarEdenHarf = harf;
      }
    }

    return { harf: enCokTekrarEdenHarf, tekrarSayisi: enCokTekrar };
  }

  const text = prompt("Bir metin giriniz : ");
  const sonuc = enCokTekrarEdenHarf(text);

  console.log(`Metinde en çok tekrar eden harf: ${sonuc.harf}`);
  console.log(`Tekrar sayısı: ${sonuc.tekrarSayisi}`);


// !Hard: 
// *Bir tam sayı dizisi oluşturmanı istiyorum. Kullanıcıdan aldığın hedef sayı doğrultusunda sayı dizisinin 
// *içinden sayılar seçip toplayarak hedef sayıya ulaşmasını sağlamalısın. Farklı farklı kombinasyonlar ile 
// *hedef sayıya ulaşıyor olman burada çok önemli!


const sayilar = [];

for (let i = 1; i <= 100; i++) {
    sayilar.push(i);
}

let hedefSayi = Number(prompt("Hedef sayı giriniz : "))

if (hedefSayi <= 0) {
    console.log(`Girilen sayı 0'dan büyük olmalı.`);
}
else {
    function hedefSayiyaUlas(sayilar, index, hedef, secilmis) {
        if (hedef === 0) {
            console.log(`Hedef sayıya ulaşan kombinasyon: ${secilmis.join(" + ")}`);
            return;
        }

        if (index >= sayilar.length || hedef < 0) {
            return;
        }

        hedefSayiyaUlas(sayilar, index + 1, hedef, secilmis);

        secilmis.push(sayilar[index]);
        hedefSayiyaUlas(sayilar, index + 1, hedef - sayilar[index], secilmis);
        secilmis.pop();
    }

    hedefSayiyaUlas(sayilar, 0, hedefSayi, []);
}
