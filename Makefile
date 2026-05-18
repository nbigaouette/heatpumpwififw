validate:
	uv run esphome config examples/example.yml

build: compile

compile:
	uv run esphome compile examples/example.yml

test_native:
	platformio test -e native --project-dir test/native
