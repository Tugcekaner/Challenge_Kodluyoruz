
// ! Easy : Kullanıcıdan aldığın sayının karesini hesaplayarak ekrana yazdıran kod parçacığını yazar mısın?
let say = +prompt("Bir sayı giriniz :");
let sonuc = say**2;
console.log(sonuc);

// ! Medium:  Oluşturduğunuz bir dizinin medyanını hesaplayan bir kod parçacığı yazar mısınız?

function median(nums) {
    let sortedNums = nums.sort((a, b) => a - b);
    let n = sortedNums.length;
  
    if (n % 2 === 0) {
      let middleRight = n / 2;
      let middleLeft = middleRight - 1;
      return (sortedNums[middleLeft] + sortedNums[middleRight]) / 2;
    } else {
      let middle = Math.floor(n / 2);
      return sortedNums[middle];
    }
  }
  
  let array = [1, 3, 5, 7, 9, 2, 4, 6, 8];
  let arrayMedian = median(array);
  console.log("Dizi medyanı:", arrayMedian);


// ! hard :  Kullanıcıdan aldığınız bir sayının Armstrong sayısı olup olmadığını kontrol eden bir kod parçacığı yazar mısınız?

function isArmstrongNumber(num) {
    let numStr = num.toString();
    let numDigits = numStr.length;
    
    let armstrongSum = 0;
    for (let i = 0; i < numDigits; i++) {
      armstrongSum += parseInt(numStr[i]) ** numDigits;
    }
    
    if (armstrongSum === num) {
      return true;
    } else {
      return false;
    }
  }
  
  let num = parseInt(prompt("Bir sayı girin:"));
  if (isArmstrongNumber(num)) {
    console.log(num + " bir Armstrong sayısıdır.");
  } else {
    console.log(num + " bir Armstrong sayısı değildir.");
  }