#!/usr/bin/env bash
# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

clear
echo -e "\e[1m"
echo " .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. "
echo "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |"
echo "| | ____    ____ | || |      __      | || | _____  _____ | || |     _____    | || | ____  _____  | || |    ______    | |"
echo "| ||_   \  /   _|| || |     /  \     | || ||_   _||_   _|| || |    |_   _|   | || ||_   \|_   _| | || |  .' ___  |   | |"
echo "| |  |   \/   |  | || |    / /\ \    | || |  | | /\ | |  | || |      | |     | || |  |   \ | |   | || | / .'   \_|   | |"
echo "| |  | |\  /| |  | || |   / ____ \   | || |  | |/  \| |  | || |      | |     | || |  | |\ \| |   | || | | |    ____  | |"
echo "| | _| |_\/_| |_ | || | _/ /    \ \_ | || |  |   /\   |  | || |     _| |_    | || | _| |_\   |_  | || | \ `.___]  _| | |"
echo "| ||_____||_____|| || ||____|  |____|| || |  |__/  \__|  | || |    |_____|   | || ||_____|\____| | || |  `._____.'   | |"
echo "| |              | || |              | || |              | || |              | || |              | || |              | |"
echo "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |"
echo " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' "
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/cacacr4ck/ultroid/main/resources/session/ssgen.py
pip uninstall telethon -y && install telethon
clear
python3 ssgen.py
