START_DATE=$( date '+%Y-%m-%d %H:%M:%S' )
echo "START ETL: $START_DATE"

echo "Clean processed and final data"
file="./data/final/Employees.sqlite3"
rm -f $file

(
    set -e
    source ./etl.sh
)

statusCode=$?
if [ $statusCode = 0 ]; then
    echo "ETL STATUS: Success"
else
    echo "ETL STATUS: Failure"
fi

END_DATE=$( date '+%Y-%m-%d %H:%M:%S' )
echo "END ETL: $END_DATE"

START_DATE_EPOCH=$( date -d "$START_DATE" +%s )
END_DATE_EPOCH=$( date -d "$END_DATE" +%s )
RUNTIME=$(( END_DATE_EPOCH - START_DATE_EPOCH ))
echo "ETL TOOK: $RUNTIME seconds"
