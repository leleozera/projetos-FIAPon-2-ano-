
#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22

#define MQ2_PIN 34

// LEDs
#define LED_VERDE 26
#define LED_VERMELHO 27

// Quantidade máxima de registros offline
#define MAX_REGISTROS 100

DHT dht(DHTPIN, DHTTYPE);

// Simulação de Wi-Fi
bool wifiConectado = false;

// Estrutura dos dados
struct Registro {
  float temperatura;
  float umidade;
  int qualidadeAr;
};

// Memória local
Registro memoria[MAX_REGISTROS];

int totalRegistros = 0;

unsigned long ultimoToggleWifi = 0;
unsigned long ultimaLeitura = 0;

void setup() {

  Serial.begin(115200);

  dht.begin();

  // Configuração LEDs
  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_VERMELHO, OUTPUT);

  Serial.println("================================");
  Serial.println("Sistema Hospitalar Inteligente");
  Serial.println("Monitoramento via Edge Computing");
  Serial.println("================================");
}

void loop() {

  // Alterna estado do Wi-Fi a cada 15 segundos
  if (millis() - ultimoToggleWifi > 15000) {

    wifiConectado = !wifiConectado;

    Serial.println("--------------------------------");

    if (wifiConectado) {

      Serial.println("Wi-Fi CONECTADO");

      digitalWrite(LED_VERDE, HIGH);
      digitalWrite(LED_VERMELHO, LOW);

    } else {

      Serial.println("Wi-Fi DESCONECTADO");

      digitalWrite(LED_VERDE, LOW);
      digitalWrite(LED_VERMELHO, HIGH);
    }

    ultimoToggleWifi = millis();
  }

  // Faz leitura dos sensores a cada 5 segundos
  if (millis() - ultimaLeitura > 5000) {

    float temperatura = dht.readTemperature();
    float umidade = dht.readHumidity();

    int qualidadeAr = analogRead(MQ2_PIN);

    Serial.println("Nova leitura dos sensores:");

    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" C");

    Serial.print("Umidade: ");
    Serial.print(umidade);
    Serial.println(" %");

    Serial.print("Qualidade do ar: ");
    Serial.println(qualidadeAr);

    // =========================
    // MODO ONLINE
    // =========================
    if (wifiConectado) {

      Serial.println("Enviando dados para nuvem...");

      Serial.print("TEMP=");
      Serial.print(temperatura);

      Serial.print(" | UMIDADE=");
      Serial.print(umidade);

      Serial.print(" | GAS=");
      Serial.println(qualidadeAr);

      // Sincroniza dados offline
      if (totalRegistros > 0) {

        Serial.println("Sincronizando registros offline...");

        for (int i = 0; i < totalRegistros; i++) {

          Serial.print("Registro ");
          Serial.print(i + 1);

          Serial.print(" -> ");

          Serial.print(memoria[i].temperatura);
          Serial.print(" C | ");

          Serial.print(memoria[i].umidade);
          Serial.print(" % | ");

          Serial.print("Gas: ");
          Serial.println(memoria[i].qualidadeAr);
        }

        // Limpa memória local
        totalRegistros = 0;

        Serial.println("Memória local limpa.");
      }

    }

    // =========================
    // MODO OFFLINE
    // =========================
    else {

      if (totalRegistros < MAX_REGISTROS) {

        memoria[totalRegistros].temperatura = temperatura;
        memoria[totalRegistros].umidade = umidade;
        memoria[totalRegistros].qualidadeAr = qualidadeAr;

        totalRegistros++;

        Serial.println("Sem conexão com internet.");
        Serial.println("Dados armazenados localmente.");

      } else {

        Serial.println("Limite de armazenamento atingido!");
      }
    }

    Serial.print("Total de registros armazenados: ");
    Serial.println(totalRegistros);

    Serial.println("--------------------------------");

    ultimaLeitura = millis();
  }
}

