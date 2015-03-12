# Wiki

- Instalar RabbitMQ

##

    sudo apt-get install rabbitmq-server

- Intalar dependências

##
    pip install -r requirements.txt

- Criar Base de dados

##
    CREATE SCHEMA `rueda` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;

- Criar tabelas

##
    python manage.py migrate
    
- Configurar o RabbitMQ

##
    sudo rabbitmq-server -detached
    sudo rabbitmqctl add_user rueda rueda
    sudo rabbitmqctl add_vhost celery
    sudo rabbitmqctl set_permissions -p celery rueda ".*" ".*" ".*"
    
- Iniciar Worker

##
    python manage.py celeryd -B --verbosity=2 --loglevel=INFO

