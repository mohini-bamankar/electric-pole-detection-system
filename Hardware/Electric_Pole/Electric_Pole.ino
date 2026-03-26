#define BLYNK_TEMPLATE_ID "TMPL3hBbpAdVP"
#define BLYNK_TEMPLATE_NAME "Smart electric pole"
#define BLYNK_AUTH_TOKEN "vVCkGIbnKLdtTKsB3qM0raXXj1BU-Jnl"

#include <WiFi.h>
#include <BlynkSimpleEsp32.h>
#include <Wire.h>
#include <Adafruit_INA219.h>

/* WiFi details */
char ssid[] = "Realme C35";
char pass[] = "7066294652";

Adafruit_INA219 ina219;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);

  if (!ina219.begin()) {
    Serial.println("INA219 not found");
    while (1);
  }

  ina219.setCalibration_32V_2A();
  Serial.println("Pole Conduction Test with Blynk Started");
}

void loop() {
  Blynk.run();

  float current = ina219.getCurrent_mA();

  Serial.print("Current: ");
  Serial.print(current, 2);
  Serial.println(" mA");

  if (current > 10.0) {
    Serial.println("⚠️ POLE CONDUCTING");
    Blynk.virtualWrite(V1, "POLE CONDUCTING");
    digitalWrite(V2, 1);
  } else {
    Serial.println("✅ POLE SAFE");
    Blynk.virtualWrite(V1, "POLE SAFE");
    digitalWrite(V2, 0);
  }

  delay(1000);
}
