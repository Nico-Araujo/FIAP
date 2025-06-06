#include <DHT.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <WiFi.h>

// Definição dos pinos
#define LDR_PIN 34
#define DHT_PIN 17
#define DS18B20_PIN 4
#define BUTTON_PIN 16

// Configuração do DHT
#define DHT_TYPE DHT22
DHT dht(DHT_PIN, DHT_TYPE);

// Configuração do DS18B20
OneWire oneWire(DS18B20_PIN);
DallasTemperature sensors(&oneWire);

// Variáveis para debounce do botão
int lastButtonState = HIGH;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  Serial.begin(115200);

//Conectando ao WIFI
  Serial.print("Conectando-se ao Wi-Fi");
  WiFi.begin("Wokwi-GUEST", "", 6);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println(" Conectado!");
  
  // Inicializa os sensores
  dht.begin();
  sensors.begin();
  
  // Configura o pino do botão como entrada com pull-up
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  
  Serial.println("Sistema inicializado. Pressione o botão para realizar leituras.");
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);
  
  // Verifica se o estado do botão mudou (debounce)
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }
  
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // Se o botão foi pressionado (LOW porque está com pull-up)
    if (reading == LOW) {
      Serial.println("Botão pressionado - realizando leituras...");
      
      // Lê o LDR (simulando pH)
      int ldrValue = analogRead(LDR_PIN);
      // Converte para um valor simulado de pH (0-14)
      float simulatedPH = map(ldrValue, 0, 4095, 0, 1400) / 100.0;
      
      // Lê o DHT22 (umidade)
      float humidity = dht.readHumidity();
      
      // Lê o DS18B20 (temperatura)
      sensors.requestTemperatures();
      float temperature = sensors.getTempCByIndex(0);
      
      // Verifica se as leituras são válidas
      if (isnan(humidity)) {
        Serial.println("Falha ao ler o sensor DHT22!");
      } else {
        Serial.print("Umidade: ");
        Serial.print(humidity);
        Serial.println(" %");
      }
      
      if (temperature == DEVICE_DISCONNECTED_C) {
        Serial.println("Falha ao ler o sensor DS18B20!");
      } else {
        Serial.print("Temperatura: ");
        Serial.print(temperature);
        Serial.println(" °C");
      }
      
      Serial.print("Valor do LDR: ");
      Serial.print(ldrValue);
      Serial.print(" - pH simulado: ");
      Serial.println(simulatedPH);
      
      Serial.println("Leituras concluídas.");
      Serial.println("----------------------------------");
      
      // Pequeno delay para evitar múltiplas leituras
      delay(500);
    }
  }
  
  lastButtonState = reading;
}