# CA-Server

CA Hack-a-thon Server

# DEBUG

## need

* docker / docker-compose
* [wsc](https://github.com/danielstjules/wsc)（WebSocketを利用する場合）
  * これはWebSocketのDEBUG用のツール

## debug-setup

### 1. `Dockerfile` と `docker-compose.yml` の変更

`develop` ブランチのデフォルトの `Dockerfile` と `docker-compose.yml` は開発用のものになっているため、変更する必要がある。
まず `./docker` から `Dockerfile.deploy` と `docker-compose.deploy.yml` をコピーする。

```
> cp ./docker/Dockerfile.deploy ./Dockerfile
> cp ./docker/docker-compose.deploy.yml ./docker-compose.yml
```

### 2. `.env` の用意

`./env.sample` というファイルをコピーして `.env` を用意する必要がある。
コピーしたあと中身の値を変更する。
`DBPASSWORD` のみ空値でも問題ない。

```
> cp env.sample .env
```

### 3. コンテナの実行

コンテナを個別に実行しデバッグ用に立ち上げる。
以下の順で実行する。

```
> docker-compose up -d db
> docker-compose up -d app
> docker-compose up -d web
```

これで `http://127.0.0.1:80/` にアクセスできるようになる

これでアクセスできなかったらhmdに言ってね :love: