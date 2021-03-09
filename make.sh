
#!/bin/bash

action=$1

if [ "$action" == "up" ]
then
    chmod -R +x db_init/
    docker-compose up

elif [ "$action" == "down" ]

    docker-compose down
    docker volume rm  ptask_dbdata
    docker volume rm  ptask_filedata

else
then    
    echo "Please enter argument as up or down"
    echo "up - To create the application."
    echo "down - To destroy the containers and application."
fi