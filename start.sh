#!/usr/bin/env bash
# 启动第一个服务
nohup rasa run --cors "*" 2>&1 &
ps aux |grep cors |grep -q -v grep
PROCESS_1_STATUS=$?
echo "rasa runs status..."
echo $PROCESS_1_STATUS
if [ $PROCESS_1_STATUS -ne 0 ]; then
echo "Failed to start rasa run: $PROCESS_2_STATUS"
exit $PROCESS_1_STATUS
fi
sleep 5

# 启动第二个服务
nohup rasa run actions 2>&1 &
ps aux |grep actions |grep -q -v grep
PROCESS_2_STATUS=$?
echo "rasa actions status..."
echo $PROCESS_2_STATUS
if [ $PROCESS_2_STATUS -ne 0 ]; then
echo "Failed to start rasa actions: $PROCESS_2_STATUS"
exit $PROCESS_2_STATUS
fi

# 每隔60秒检查进程是否运行
while sleep 60; do
  ps aux |grep cors |grep -q -v grep
  PROCESS_1_STATUS=$?
  ps aux |grep actions |grep -q -v grep
  PROCESS_2_STATUS=$?
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
  echo "One of the processes exited."
  exit 1
  fi
done