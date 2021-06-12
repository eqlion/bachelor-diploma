#!/bin/sh

./utils/latexmkmod -r .latexmkmodrc "$@" -- main.tex
./utils/latexmkmod -r .latexmkmodrc "$@" -- practice.tex
