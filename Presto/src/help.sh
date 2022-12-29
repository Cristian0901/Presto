#!/bin/bash

for i in $(ls -I 'help')
do
	touch "./$i/docs/index.md"
	touch "./$i/readme.md"
done
