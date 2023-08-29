
// !Easy: 
// *Kullanıcıdan bir sayı almanızı ve bu sayının asal olup olmadığını kullanıcıya söylemenizi istiyorum. 


let sayi = Number(prompt("Bir sayı giriniz : "));
let bolenSayisi = 0;

for (let i = 1; i < sayi; i++) {
    if (sayi%i==0){
        bolenSayisi += 1;
    }
}

if (bolenSayisi==1){
    console.log(`Girilen ${sayi} sayısı asaldır.`);
}
else{
    console.log(`Girilen ${sayi} sayısı asal değildir.`);
}


// !Medium: 
// *Kullanıcıdan bir kelime almanız gerekiyor. Bu kelimenin harflerini büyük harflere 
// *dönüştüren bir program yazmanızı istiyorum. 


function upper(a) {
    let b = a.toUpperCase();
    console.log(b);
}
let metin = prompt("Bir metin giriniz : ");
upper(metin)


// !Hard: 
// *Bir şirket, bir ürünü üretmek ve satmak için belirli bir maliyet ve satış fiyatı hesaplamaktadır. 
// *Şirketin bir ürün için birim maliyeti ve birim satış fiyatı verildiğinde, kaç adet ürünün satılması durumunda 
// *şirketin kar edeceğini bulmanı istiyorum.


let urunMaliyet = 0;
let asgari = 11000;
let secim1 = Number(prompt("Ürün maliyetini hesaplamak için 1, maliyeti kendiniz belirlemek için 2 yazınız : "));

if (secim1 === 1) {
    let a = Number(prompt("Günde kaç adet ürün üretildiğini giriniz: "));
    let b = Number(prompt("Çalışan işçi sayısını giriniz: "));
    let c = Number(prompt("Günlük çalışma saatini giriniz: "));
    let d = Number(prompt("Ürün aylık hammadde alış fiyatını giriniz: "));
    let e = Number(prompt("Ayda çalışılan gün sayısını giriniz: "));

    let aylikMaliyet = ((b * asgari) / (c * e)) + (d / (a * e));
    let gunlukMaliyet = aylikMaliyet / e;
    urunMaliyet = Math.round((gunlukMaliyet / a));
    console.log(`Ürün maliyeti: ${urunMaliyet}`);
} else if (secim1 === 2) {
    urunMaliyet = Number(prompt("Ürün maliyetini giriniz: "));
} else {
    console.log("Hatalı giriş yaptınız!");
}

if (urunMaliyet !== 0) {
    let secim2 = Number(prompt("Ürün satış fiyatını hesaplamak için 1, fiyatı kendiniz belirlemek için 2 yazınız: "));
    if (secim2 === 1) {
        let karOran = Number(prompt("Elde etmek istediğiniz kar oranını giriniz: "));
        let fiyat = urunMaliyet + ((urunMaliyet / 100) * karOran);
        console.log(`Ürün satış fiyatı: ${fiyat}`);
        let fark = fiyat - urunMaliyet;
        let adet = (urunMaliyet / fark) + 1;
            console.log(`Kar elde edebilmek için en az ${Math.floor(adet)} ürün satışı yapmalısınız.`);
    } else if (secim2 === 2) {
        let fiyat = Number(prompt("Ürün fiyatını giriniz: "));
        let fark = fiyat - urunMaliyet;
        let adet = (urunMaliyet / fark) + 1;
        if (adet > 0) {
            console.log(`Kar elde edebilmek için en az ${Math.floor(adet)} ürün satışı yapmalısınız.`);
        } else {
            console.log("Bu şekilde kar elde edemezsiniz.");
        }    
        if (fiyat < urunMaliyet) {
            console.log("Fiyat ürün maliyetinden düşük olamaz!");
        }
    } else {
        console.log("Hatalı giriş yaptınız!");
    }
}
