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
            ESP_LOGE(TAG, "HeatPumpWiFi::HeatPumpWiFi() ERROR");
            ESP_LOGW(TAG, "HeatPumpWiFi::HeatPumpWiFi() WARN");
            ESP_LOGI(TAG, "HeatPumpWiFi::HeatPumpWiFi() INFO");
            ESP_LOGD(TAG, "HeatPumpWiFi::HeatPumpWiFi() DEBUG");
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
        }

        void HeatPumpWiFi::send_command_(uint8_t *data, size_t len)
        {
            write_array(data, len);
            flush();
        }

    } // namespace heatpumpwifi
} // namespace esphome
