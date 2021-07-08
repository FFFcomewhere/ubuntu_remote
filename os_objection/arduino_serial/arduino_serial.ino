/*
   Serial
   串口通讯实验
*/
int incomedate = 0;
void setup() {
  Serial.begin(9600); //设置串口波特率9600

}

void loop() {
  Serial.println(02, HEX);// "1001110"

  if (Serial.available())//串口接收到数据
  {
    incomedate = Serial.read();//获取串口接收到的数据
    if (incomedate == '1')
    {
      Serial.println(01, HEX);// "1001110"
      //Serial.println(78, BIN);// "1001110"

    }
  }

  delay(100);

}
