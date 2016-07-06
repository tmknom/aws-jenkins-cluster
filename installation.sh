#!/bin/bash

echo 'start installation...'

# 最初にプロジェクトルートに移動
cd $(git rev-parse --show-toplevel)
echo "Project root : $(pwd)"

# Ruby : Itamae, Serverspec, unix-crypt, etc
bundle install --path vendor/bundle

echo 'end installation!'
