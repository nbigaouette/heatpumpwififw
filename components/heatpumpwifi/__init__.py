import os

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, output, light
from esphome.components.esp32 import add_idf_sdkconfig_option, final_validate
from esphome.const import CONF_ID
from esphome.core import CORE
from esphome import git


CONF_UART = "uart"

DEPENDENCIES = [
    "esp32",
    "uart",
    # "output",
    # "light",
]
AUTO_LOAD = ["uart"]

CODEOWNERS = ["@nbigaouette"]

COMPONENT_DIR = os.path.dirname(__file__)

# See https://documentation.espressif.com/esp32-c6_technical_reference_manual_en.pdf#iomuxgpio
# | GPIO | Pin   Name | Function 0 | Function 1 | Function 2 | Function 3 | DRV | Reset | Notes |
# | ---- | ---------- | ---------- | ---------- | ---------- | ---------- | --- | ----- | ----- |
# | 16   | U0TXD      | U0TXD      | GPIO16     | FSPICS0    | —          | 2   | 4     | —     |
# | 17   | U0RXD      | U0RXD      | GPIO17     | FSPICS1    | —          | 2   | 3     | —     |
UART_BAUD_RATE = 9600
UART_TX_GPIO = 16
UART_RX_GPIO = 17

heatpumpwifi_ns = cg.esphome_ns.namespace("heatpumpwifi")
HeatPumpWiFi = heatpumpwifi_ns.class_("HeatPumpWiFi", cg.Component, uart.UARTDevice)

# User defined options
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(HeatPumpWiFi),
    cv.Required(CONF_ID): cv.declare_id(HeatPumpWiFi),
    # cv.Optional(CONF_UART, default="heatpumpwifi_uart"): cv.use_id(uart.UARTComponent),
}).extend(uart.UART_DEVICE_SCHEMA).extend(cv.COMPONENT_SCHEMA)

def final_validate(config):
    print("config: ", config)
    # """Auto-configure UART with board defaults if not provided."""
    if CORE.data["esp32"]["board"] != "esp32-c6-devkit-1":
        raise cv.Invalid("This component requires board: 'esp32-c6-devkit-1'")

FINALE_VALIDATE_SCHEMA = cv.Schema(final_validate)


async def to_code(config):
    # FIXME: This seems to be ignored
    # Inject sdkconfig options automatically
    add_idf_sdkconfig_option("CONFIG_ESPTOOLPY_FLASHSIZE_8MB", True)
    add_idf_sdkconfig_option("CONFIG_ESPTOOLPY_FLASHSIZE", "8MB")
    add_idf_sdkconfig_option("CONFIG_ESPTOOLPY_FLASHMODE_QIO", True)
    add_idf_sdkconfig_option("CONFIG_ESPTOOLPY_FLASHMODE", "QIO")
    add_idf_sdkconfig_option("CONFIG_ESPTOOLPY_FLASHFREQ_80M", True)
    add_idf_sdkconfig_option("CONFIG_ESPTOOLPY_FLASHFREQ", "80M")

    # # Point to the partition table bundled with the component
    # # FIXME: This seems to be ignored!
    # partition_file = os.path.join(COMPONENT_DIR, "partitions.csv")
    # add_idf_sdkconfig_option("CONFIG_PARTITION_TABLE_CUSTOM", True)
    # add_idf_sdkconfig_option("CONFIG_PARTITION_TABLE_CUSTOM_FILENAME", partition_file)

    # # Create the UART component with fixed pins
    # uart_var = cg.new_Pvariable(config[uart.CONF_UART_ID])
    # cg.add(uart_var.set_tx_pin(DEFAULT_TX_PIN))
    # cg.add(uart_var.set_rx_pin(DEFAULT_RX_PIN))
    # cg.add(uart_var.set_baud_rate(DEFAULT_BAUD_RATE))
    # await cg.register_component(uart_var, {})

    # Create the HeatPumpWifi component
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
    # var = cg.new_Pvariable(config[cv.GenerateID()], uart_var)
    # await cg.register_component(var, config)

    # var = cg.new_Pvariable(config[CONF_ID])
    # await cg.register_component(var, config)
    # await uart.register_uart_device(var, config)

    # # Create and configure the UART component automatically
    # uart_config = uart.UARTComponent()
    # cg.add(uart_config)
    
    # # Set fixed pins for your custom board
    # cg.add(uart_config.set_tx_pin(DEFAULT_TX_PIN))  # GPIO16
    # cg.add(uart_config.set_rx_pin(DEFAULT_RX_PIN))  # GPIO17
    # cg.add(uart_config.set_baud_rate(DEFAULT_BAUD_RATE))

    # var = cg.new_Pvariable(config[cv.GenerateID()], uart_config)
    # await cg.register_component(var, config)
    # # Create UART component programmatically
    # uart_component = cg.new_Pvariable(cg.esp32_ns.class_("UART"))
    # cg.add(uart_component.set_baud_rate(UART_BAUD_RATE))
    # cg.add(uart_component.set_tx_pin(UART_TX_GPIO))
    # cg.add(uart_component.set_rx_pin(UART_RX_GPIO))
    # await cg.register_component(uart_component, {})

    # cg.add(var.set_uart_parent(uart_component))
