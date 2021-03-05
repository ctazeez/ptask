
#!/bin/bash

docker-compose down

docker volume rm  ptask_dbdata

docker volume rm  ptask_filedata

chmod -R +x db_init/

docker-compose up --no-cache