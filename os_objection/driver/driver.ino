// 第三方库，需要安装，按ctrl+shift+i管理第三方库，也可手动安装
#include <AccelStepper.h>
const int X_EN = 2;
const int X_STP = 3;
const int X_DIR = 4;
const int Y_EN = 7;
const int Y_STP = 5;
const int Y_DIR = 8;
// 电机初始化
AccelStepper stepper2(1, X_STP, X_DIR);
AccelStepper stepper1(1, Y_STP, Y_DIR);


int n = 21;
double unit = 1.8 / 8;
int tot = 0;
int mutex = 0;
unsigned long st;


void setup()
{
    // 设置相关引脚
    pinMode(X_EN, OUTPUT);
    pinMode(X_STP, OUTPUT);
    pinMode(X_DIR, OUTPUT);
    pinMode(Y_EN, OUTPUT);
    pinMode(Y_STP, OUTPUT);
    pinMode(Y_DIR, OUTPUT);
    // 电机使能
    digitalWrite(X_EN, 0);
    digitalWrite(Y_EN, 0);
    // 设置电机最大转速（不能大于3000）
    stepper1.setMaxSpeed(100.0);
    stepper2.setMaxSpeed(100.0);
    // 设置电机转速
    stepper1.setSpeed(100);
    stepper2.setSpeed(100);
    Serial.begin(9600);
}

void loop()
{
    // 控制电机转动（需要一直执行）
    stepper1.runSpeed();
    stepper2.runSpeed();
}
