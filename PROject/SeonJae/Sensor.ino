#include <SoftwareSerial.h> //시리얼통신 라이브러리 호출
#include <DHT.h>
#include <Adafruit_Fingerprint.h>
#include "Timer.h"

SoftwareSerial mySerial(2, 3);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);
DHT mydht(A1, DHT11);
int blueTx=7;   //Tx (보내는핀 설정)at
int blueRx=6;   //Rx (받는핀 설정)
SoftwareSerial MySerial(blueTx, blueRx);  //시리얼 통신을 위한 객체선언
int triggerPin = 9;
int echoPin = 8;
int buzzerPin = 4;
int sensor = 0;
int mode = 0;
uint8_t id;
int ledpin=12;
char k = '3'; //활성화 변수

void setup() 
{
  MySerial.begin(9600); //블루투스 시리얼
  mydht.begin();
  Serial.begin(115200);                     
 
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledpin,OUTPUT); //led
  pinMode(13,INPUT_PULLUP); //진동센서
  digitalWrite(buzzerPin, HIGH);
  Serial.begin(9600);
  finger.begin(57600);
}
void loop()
{
  MySerial.listen();
  /*
  if (MySerial.available()) {

    Serial.write(MySerial.read());

  }

  if (Serial.available()) {

    MySerial.write(Serial.read());
  }
  */
  int temp = mydht.readTemperature();
  int humi = mydht.readHumidity();
    
  delay(500);

  int distance;
  unsigned long duration;
  digitalWrite(triggerPin, HIGH);
  delay(10);
  digitalWrite(triggerPin,LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = ((340*duration)/10000)/2;

  /*Serial.print("온도:");
  Serial.print(temp);
  Serial.print("습도:");
  Serial.print(humi);
Serial.print("거리:"); 
Serial.println(distance); */
  /********활성화 변수 - 초음파*********/
  if (k =='3'){
    if(distance<=10)
    {
      String data = String(temp) + "," + String(humi) + "," + String(distance) + "," + String(sensor) + "," + String(mode) + "," + String(k);
      MySerial.println(data);
      Serial.println(data);
      
      digitalWrite(buzzerPin,LOW);
   
        for (int i=0; i <= 20; i++) 
        {
          digitalWrite(ledpin, HIGH); // 10번핀 부터 13번 핀까지 LED 차례대로 켜기)
          delay(100);
          digitalWrite(ledpin, LOW); //13번 핀부터 10번 핀까지 LED 차례대로 끄기
          delay(100);
        }
        digitalWrite(buzzerPin,HIGH);
    }
    else{
      digitalWrite(buzzerPin,HIGH);
      digitalWrite(ledpin, LOW);
    }
  }

  sensor = digitalRead(13);
  
   if(sensor == HIGH)
  {
    Serial.println("충격이 감지되었습니다!");
    /********활성화 변수 - 충격 감지*********/
    if(k == '3'){
        String data = String(temp) + "," + String(humi) + "," + String(distance) + "," + String(sensor) + "," + String(mode) + "," + String(k);
        Serial.println(data);
        MySerial.println(data);
        digitalWrite(buzzerPin,LOW);
        for (int i=0; i <= 20; i++) 
        {
          digitalWrite(ledpin, HIGH); // 10번핀 부터 13번 핀까지 LED 차례대로 켜기)
          delay(100);
          digitalWrite(ledpin, LOW); //13번 핀부터 10번 핀까지 LED 차례대로 끄기
          delay(100);
        }
        digitalWrite(buzzerPin,HIGH);
    }
    else{
      digitalWrite(buzzerPin,HIGH);
      digitalWrite(ledpin, LOW);
    }
  }
  
  if(Serial.available() > 0){
    //PC에서 아두이노쪽으로 뭔가 전송한값이 존재한다면~
    char recv = Serial.read();

    if(recv == '0') //인식모드
    {
      mode = 0;
    }else if(recv == '1') //등록모드
    {
      mode = 1;
    }else if(recv == '2') //삭제모드
    {
      mode = 2;
    }
    else if(recv =='3' || recv == '4'){
      k = recv;
    }
    
    Serial.println(recv);
    
    
  }
  
if(MySerial.available()){
    //PC에서 아두이노쪽으로 뭔가 전송한값이 존재한다면~
    char recv = MySerial.read();

    if(recv == '0') //인식모드
    {
      mode = 0;
    }else if(recv == '1') //등록모드
    {
      mode = 1;
    }else if(recv == '2') //삭제모드
    {
      mode = 2;
    }
    else if(recv =='3' || recv == '4'){
      k = recv;
    }
    Serial.println(recv);
    //MySerial.println(recv);
    
  }


  String data = String(temp) + "," + String(humi) + "," + String(distance) + "," + String(sensor) + "," + String(mode) + "," + String(k);
  Serial.println(data);
  MySerial.println(data);

/****************************************/
  
  if(mode == 0){
    //인식모드
    mySerial.listen();
    getFingerprintIDez();
  }
    /****************/
  else if(mode == 1){
    //등록모드
    Serial.println("등록절차를 시작합니다..");
    Serial.println("1부터 127까지 원하는 id를 선택하세요");
    MySerial.listen();
    id = readnumber();
    if (id == 0) {// ID #0 not allowed, try again!
       return;
    }
    
    mySerial.listen();
    while (!  getFingerprintEnroll() );
    
    Serial.println("인식모드로 전환합니다!");
    mode = 0;
  }
  
  /***************************/
  else if(mode == 2){
    //삭제모드
    Serial.println("삭제절차를 시작합니다..");
    Serial.println("지우고자 하는 id를 적으세요");
    uint8_t id = readnumber();
    if (id == 0) {// ID #0 not allowed, try again!
       return;
    }

    Serial.println("id를 삭제했습니다!");
   
    mySerial.listen();
    deleteFingerprint(id);
    
    Serial.println("인식모드로 전환합니다!");
    mode = 0;
  }

}



/************************************/
uint8_t readnumber(void) {
  uint8_t num = 0;
  
  while (num == 0) {
    while (! MySerial.available());
    num = MySerial.parseInt();
  }
  return num;
}


/**************************/
int getFingerprintIDez() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)  return -1;

  
  // 잠금해제
  Serial.print("잠금이 해제 되었습니다   ID:"); 
  Serial.println(finger.fingerID); 
  Serial.println("10초 후 보안이 시작됩니다");
 digitalWrite(buzzerPin,HIGH);
 delay(10000);
  return finger.fingerID; 
}

/*************************/
uint8_t getFingerprintEnroll() {
  int p = -1;
  Serial.print("ID 등록중 "); 
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
    case FINGERPRINT_OK:
      Serial.println("");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.print("");
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("에러");
      break;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("이미지 에러");
      break;
    default:
      Serial.println("에러");
      break;
    }
  }

  // OK success!

 /* p = finger.image2Tz(1);
  switch (p) {
    case FINGERPRINT_OK:
      Serial.print("");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("다시 대 주세요");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("에러");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("다시 대 주세요");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("대시 대 주세요");
      return p;
    default:
      Serial.println("에러");
      return p;
  }
  
  Serial.println("손가락을 제거해 주세요");
  delay(2000);
  p = 0;
  while (p != FINGERPRINT_NOFINGER) {
    p = finger.getImage();
  }
  
  p = -1;
  Serial.println("똑같은 손가락을 다시 대 주세요");
  while (p != FINGERPRINT_OK) {
    p = finger.getImage();
    switch (p) {
    case FINGERPRINT_OK:
      Serial.print("");
      break;
    case FINGERPRINT_NOFINGER:
      Serial.print("");
      break;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("에러");
      break;
    case FINGERPRINT_IMAGEFAIL:
      Serial.println("이미지 에러");
      break;
    default:
      Serial.println("에러");
      break;
    }
  }

 

  p = finger.image2Tz(2);
  switch (p) {
    case FINGERPRINT_OK:
      Serial.print("성공");
      break;
    case FINGERPRINT_IMAGEMESS:
      Serial.println("다시 대 주세요");
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      Serial.println("에러");
      return p;
    case FINGERPRINT_FEATUREFAIL:
      Serial.println("다시 대 주세요");
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      Serial.println("다시 대 주세요");
      return p;
    default:
      Serial.println("에러");
      return p;
  }*/
  
  // OK converted!
  
  
  p = finger.createModel();
  if (p == FINGERPRINT_OK) {
    Serial.println("");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("");
    return p;
  } else if (p == FINGERPRINT_ENROLLMISMATCH) {
    Serial.println("");
    return p;
  } else {
    Serial.println("에러");
    return p;
  }   
  
  Serial.print("ID: "); Serial.println(id);
  p = finger.storeModel(id);
  if (p == FINGERPRINT_OK) {
    Serial.print("");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("에러");
    return p;
  } else if (p == FINGERPRINT_BADLOCATION) {
    Serial.println("지문을 저장할 수 없습니다");
    return p;
  } else if (p == FINGERPRINT_FLASHERR) {
    Serial.println("에러");
    return p;
  } else {
    Serial.println("에러");
    return p;
  }   
}

/***************************************/
uint8_t deleteFingerprint(uint8_t id) {
  uint8_t p = -1;
  
  p = finger.deleteModel(id);

  if (p == FINGERPRINT_OK) {
    Serial.println("");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("다시 시도해주세요");
    return p;
  } else if (p == FINGERPRINT_BADLOCATION) {
    Serial.println("다시 시도해주세요");
    return p;
  } else if (p == FINGERPRINT_FLASHERR) {
    Serial.println("다시 시도해주세요");
    return p;
  } else {
    Serial.print("에러"); Serial.println(p, HEX);
    return p;
  }   
}