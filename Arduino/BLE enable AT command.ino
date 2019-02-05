/*
BLE Module– First Run
Hardware 1: MLT-BT05 BLE Bluetooth v4.0
Hardware 2: Arduino Uno R3
Experimental Sketch: By T.K.Hareendran
*/

#include <SoftwareSerial.h>

int bluetoothTx = 2; // D2 to TXD
int bluetoothRx = 3; // D3 to RXD 

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

void setup()
{
    Serial.begin(9600);
    bluetooth.begin(115200);
    delay(100);
    bluetooth.println("U,9600,N");
    bluetooth.begin(9600);
}

void loop()
{
    if (bluetooth.available())
    {
        Serial.print((char)bluetooth.read());
    }
    if (Serial.available())
    {
        bluetooth.print((char)Serial.read());
    }
}