#include <SoftwareSerial.h>
#include<Wire.h>
const int MPU=0x68; 
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;


int bluetoothTx = 2; // D2 to TXD
int bluetoothRx = 3; // D3 to RXD 

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

void setup()
{
    //MPU 5060
    Wire.begin();
    Wire.beginTransmission(MPU);
    Wire.write(0x6B); 
    Wire.write(0);    
    Wire.endTransmission(true);
    Serial.begin(9600);
    //Bluetooth
    bluetooth.begin(115200);
    delay(100);
    bluetooth.println("U,9600,N");
    bluetooth.begin(9600);
}

void loop()
{
    if (bluetooth.available())
    {
        //Serial.print((char)bluetooth.read());
    }
    if (Serial.available())
    {
        bluetooth.print((char)Serial.read());
        //Serial.print(get_accel());
    }
    bluetooth.print(get_accel());
    delay(1000);
}

String get_accel(){
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);  
  Wire.endTransmission(false);
  Wire.requestFrom(MPU,12,true);  

  AcX=Wire.read()<<8|Wire.read();    
  AcY=Wire.read()<<8|Wire.read();  
  AcZ=Wire.read()<<8|Wire.read();  
  
  String accelorometer = (String)AcX + (String)AcY + (String)AcZ + "\n";
  //Serial.println(accelorometer);
  //String tes = "ok bro \n";
  return (accelorometer);
}