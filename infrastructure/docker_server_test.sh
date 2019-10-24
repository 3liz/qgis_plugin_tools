#!/bin/bash

docker stop qgis-infrastructure-environment &> /dev/null
docker rm qgis-infrastructure-environment &> /dev/null
docker run -d --name qgis-infrastructure-environment -v $(dirname $(pwd)):/"$1" -e QGIS_PLUGINPATH=/ qgis/qgis:"$2"
echo "Waiting 5 seconds"
sleep 5
# docker cp infrastructure/test_runner.py qgis-infrastructure-environment:/usr/bin/qgis_testrunner.py
# docker exec -it qgis-infrastructure-environment sh -c "chmod u+x /usr/bin/qgis_testrunner.py"
docker exec -it qgis-infrastructure-environment sh -c "cd /$1 && python3 -m unittest; exit $?"
# docker exec -it qgis-infrastructure-environment sh -c "cd /$1 && python3 /usr/bin/qgis_testrunner.py; exit $?"

status=$?
# docker stop qgis-infrastructure-environment &> /dev/null
# docker rm qgis-infrastructure-environment &> /dev/null
# echo "Kill and removing the container"
exit ${status}
