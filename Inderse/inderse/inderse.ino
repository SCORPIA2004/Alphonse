#include <ArduinoHttpClient.h>
#include <ESP8266WiFi.h>
#include <HTTPClient.h>


#define ssid "MetroBandAP"
#define password "SyQGaMq6ahrE"

void setup()
{
  // setup
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid,password);
  
  Serial.begin(11520);

  while(WiFi.status() != WL_CONNECTED)
  {
    
  }
}
void loop()
{
  // 
}