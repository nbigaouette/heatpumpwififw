NAME = heatpumpwifi


validate:
	uv run esphome config examples/$(NAME).yml

build: compile

compile:
	uv run esphome compile examples/$(NAME).yml

test_native:
	platformio test -e native --project-dir test/native
