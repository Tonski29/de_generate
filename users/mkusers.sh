#!/bin/bash

sleep 5

sudo adduser dave --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
sleep 2
echo "dave:password" | sudo chpasswd

sudo adduser alex --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
sleep 2
echo "alex:trustno1" | sudo chpasswd


sudo adduser paul --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
sleep 2
echo "paul:toor" | sudo chpasswd
