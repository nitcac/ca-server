# CA-Server

CA Hack-a-thon Server

# DEBUG

## need

* docker / docker-compose
* [wsc](https://github.com/danielstjules/wsc)（WebSocketを利用する場合）
  * これはWebSocketのDEBUG用のツール

## debug-setup

まず `.env` というファイルを用意する。
以下を実行した後、 `.env` の値を好きなものに変更する。

```
> cp .env.sample .env
```

`DBPASSWORD` のみ空値でも問題ない。

次に以下を実行しコンテナを生成、その後別のターミナルからコンテナにアタッチする。

```
> docker-compose up

# コンテナにアタッチするとき
> docker exec -it ca-server_app_1 bash
```

アタッチした後、以下を実行すると `localhost:80` にサーバが立ち上がってくれるようになる。

```
> python3 app.py   # コンテナで
```

もしこれでサーバが立ち上がらない場合は、 `docker-compose` を停止した後、以下を実行してみる。

```
> docker-compose stop   # composeの停止
> docker-compose down -v
> docker-compose up --build
```

これでも解決しなかったらhmdに言ってね :love: