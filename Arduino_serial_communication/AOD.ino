const int analogPin0 = A0;
int analogValue0;
unsigned long lastTime,sampleTime;

void setup() {
  Serial.begin(9600);
  analogValue0 = 0;
  sampleTime = 40;
  lastTime = millis();
}

void loop() {
  if (millis() - lastTime >= sampleTime)
  {
    lastTime=millis();
    analogValue0 = analogRead(analogPin0);
    Serial.println(scaling(analogValue0,0,1023,0,100));
  }
}

float scaling(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
