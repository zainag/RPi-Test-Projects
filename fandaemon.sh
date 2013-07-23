#! /bin/bash
# /etc/init.d/fandaemon
#
### BEGIN INIT INFO
# Provides: fandaemon
# Required-Start:
# Should-Start:
# Required-Stop:
# Should-Stop:
# Default-Start:  3 5
# Default-Stop:   0 1 2 6
# Short-Description: Test daemon process
# Description:    Runs up the test daemon process
### END INIT INFO

# Activate the python virtual environment
    . /path_to_virtualenv/activate

case "$1" in
  start)
    echo "Starting server"
    # Start the daemon
    python /usr/share/fandaemon/fan_control_daemon.py start
    ;;
  stop)
    echo "Stopping server"
    # Stop the daemon
    python /usr/share/fandaemon/fan_control_daemon.py stop
    ;;
  restart)
    echo "Restarting server"
    python /usr/share/fandaemon/fan_control_daemon.py restart
    ;;
  *)
    # Refuse to do other stuff
    echo "Usage: /etc/init.d/fandaemon.sh {start|stop|restart}"
    exit 1
    ;;
esac

exit 0