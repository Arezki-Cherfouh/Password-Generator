#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_password_generator_gui..."
wine "run_password_generator_gui" || ./"run_password_generator_gui" "$@"
