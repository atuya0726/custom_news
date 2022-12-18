alias cn-back-dev="docker-compose build back && docker-compose up back"
alias cn-back-bash="docker exec -it custom_news_back bash"
alias cn-bash-unable="docker-compose run --rm back bash"

alias cn-front-dev="docker-compose build front && docker-compose up front"
alias cn-front-bash="docker exec -it custom_news_front bash"

alias cn-db-bash="docker exec -it custom_news_db bash"