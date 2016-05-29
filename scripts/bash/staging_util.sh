#!/bin/bash
# Ripped off from:
# https://github.com/wix-private/payment-gateway/blob/master/scripts/pci.sh

if [ $# -ne 2 ]
  then
    echo "[*] Usage: $0 <artifact_name> <port_number>"
    exit 1
fi

clear
echo "[*] Staging Tools"
read -n4 -p $'
[*] Enter app server [5-10]
1)  pizza
2)  glida
3)  munchie
4)  icewine
5)  pita
6)  crispie
7)  sake
->' APP_IN

APP_NAME=$1
APP_PORT=$2
APP=""
IP=""

case $APP_IN in
  1)  APP="pizza.wixpress.com";;
  2)  APP="glida.wixpress.com";;
  3)  APP="munchie.wixpress.com";;
  4)  APP="icewine.wixpress.com";;
  5)  APP="pita.wixpress.com";;
  6)  APP="crispie.wixpress.com";;
  7)  APP="sake.wixpress.com";;
  *) echo $'\n non valid input. run again' && exit 1;;
esac

read -n4 -p $'
[*] Enter command[1-7] (can take few seconds to run)
1) chef-client
2) which version
3) is alive?
4) lock chef
5) remove lock
6) is chef locked
7) sync specs (petri)
8) chef install list
->' CMD_IN

VER_CMD="curl http://$APP:$APP_PORT/$APP_NAME/app-info/app-data"
IS_ALIVE_CMD="curl http://www.$APP/$APP_NAME/health/is_alive"
REMOVE_LOCK_CMD="rm /tmp/chef.lock_com.wixpress.$APP_NAME"
LOCK_CMD="echo \"something\" > /tmp/chef.lock_com.wixpress.$APP_NAME"
IS_LOCKED_CMD="test -f /tmp/chef.lock_com.wixpress.$APP_NAME && echo locked || echo NOT locked"
CHEF_CMD="/opt/wixpress/scripts/run_chef_solo.sh"
SYNC_SPECS_CMD="curl -X POST http://$APP:$APP_PORT/$APP_NAME/sync-specs"
WHAT_IS_INSTALLED="tail -100 /opt/pci-chef/nodes/$APP.json"

CMD_RESULT=""
case $CMD_IN in
  1) `ssh -t root@$APP "sudo -s $CHEF_CMD"` ;;
  2) echo $VER_CMD ;;
  3) $IS_ALIVE_CMD;; 
  4) `ssh root@$APP "$LOCK_CMD"` ;;
  5) `ssh root@$APP "$REMOVE_LOCK_CMD"`;;
  6) CMD_RESULT=`ssh root@$APP "$IS_LOCKED_CMD"`;;
  7) $SYNC_SPECS_CMD ;;
  8) `ssh -t $APP "sudo -s $WHAT_IS_INSTALLED" > /tmp/1.txt` && cat /tmp/1.txt | grep com.wixpress ;;
  *) echo $'\n non valid input. run again' && exit 1;;
esac
echo ""
echo $CMD_RESULT
echo $'\n\n'
