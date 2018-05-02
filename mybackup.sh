backdate=`date +"%Y%m%d"`

echo $backdate


mysqldump -h 127.0.0.1 -u root -p111111 PT_DEMO > ptdemo.sql.$backdate

