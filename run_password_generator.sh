#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_password_generator..."
wine "run_password_generator" || ./"run_password_generator" "$@"
