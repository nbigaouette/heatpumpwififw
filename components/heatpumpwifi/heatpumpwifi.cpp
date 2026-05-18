#include "heatpumpwifi.hpp"

namespace esphome
{
    namespace heatpumpwifi
    {
        static const char *const TAG = "HeatPumpWiFi";

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
