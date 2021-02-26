# cdc-debezium
*CDC example using mysql binlog and debezium*

## Requirements

- docker
- docker-compose

## How to use

1. Execute all containers
    ```
    docker-compose up -d
    ```

2. Run shell
    ```
    bash debezium.sh
    ```

3. execute mysql cli

    ```
    docker exec -ti mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"'
    ```

4. enjoy!

references:

[1] https://debezium.io/documentation/reference/tutorial.html