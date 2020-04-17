#!/bin/sh
docker build ./party-a/. -t party-a
docker build ./party-b/. -t party-b
docker build ./party-c/. -t party-c
