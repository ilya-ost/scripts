#! /bin/bash

echo Batt: $(acpi | awk '{printf int($4)}')%
