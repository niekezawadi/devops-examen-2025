#!/bin/bash

curl -X POST \
  -F "name=Nieke" \
  -F "project=DevOps examen" \
  -F "score=100" \
  https://httpbin.org/post
