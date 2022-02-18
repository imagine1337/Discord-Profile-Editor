#!/bin/bash

token="" #Discord token
username="" #Username string
password="" #Password string

for i in {0..9999}
do
   sleep 43200
   curl --data "discriminator=${i}&password=${password}&username=${username}" --header "Authorization: $token"
done
