alias cn-dev="docker-compose build app && docker-compose up app"
alias cn-bash="docker exec -it custom_news bash"
alias cn-bash-unable="docker-compose run --rm app bash"

alias cn-front-dev="docker-compose build front && docker-compose up front"
alias cn-front-bash="docker exec -it custom_news_front bash"