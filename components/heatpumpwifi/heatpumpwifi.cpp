#include "esphome/core/log.h"
#include "heatpumpwifi.hpp"

// gnu++20

namespace esphome
{
    namespace heatpumpwifi
    {
        static const char *const TAG = "HeatPumpWiFi";

        HeatPumpWiFi::HeatPumpWiFi()
        {
            // Do setup here
        }

        void
        HeatPumpWiFi::setup()
        {
            ESP_LOGI(TAG, "HeatPumpWiFi setup");
            // Initialize your device here
        }

        void HeatPumpWiFi::loop()
        {
            // Read data from UART
            while (available())
            {
                uint8_t byte = read();
                // Parse your protocol here
                ESP_LOGD(TAG, "Received: 0x%02X", byte);
            }
        }

        void HeatPumpWiFi::dump_config()
        {
            ESP_LOGCONFIG(TAG, "HeatPumpWiFi:");
            ESP_LOGE(TAG, "HeatPumpWiFi::dump_config() ERROR");
            ESP_LOGW(TAG, "HeatPumpWiFi::dump_config() WARN");
            ESP_LOGI(TAG, "HeatPumpWiFi::dump_config() INFO");
            ESP_LOGD(TAG, "HeatPumpWiFi::dump_config() DEBUG");
        }

        void HeatPumpWiFi::send_command_(uint8_t *data, size_t len)
        {
            write_array(data, len);
            flush();
        }

    } // namespace heatpumpwifi
} // namespace esphome
