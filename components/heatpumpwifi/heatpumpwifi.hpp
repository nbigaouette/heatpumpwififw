#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"

namespace esphome
{
    namespace heatpumpwifi
    {

        class HeatPumpWiFi : public Component, public uart::UARTDevice
        {
        public:
            HeatPumpWiFi();

            void setup() override;
            void loop() override;
            void dump_config() override;

        private:
            void send_command_(uint8_t *data, size_t len);
            void parse_response_();
        };

    } // namespace heatpumpwifi
} // namespace esphome
