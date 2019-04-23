# CA-Server

CA Hack-a-thon Server

# DEBUG

## need

* docker / docker-compose
* [wsc](https://github.com/danielstjules/wsc)
  * これはWebSocketのDEBUG用のツール

## how to run-server

**これは最新版じゃないです**

1. docker install
多分、Windowsなら公式サイトから落としてくればできます。（WindowsでやったことないのでQiitaなどで調べていただきたい...）
2. wsc install
`npm` を使ってやるなら上記リンクの通り

```
$ npm install -g wsc
```

3. run `docker-compose up`
割と時間がかかるので注意
`app_1  | INFO: Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)` みたいなのが出れば多分OK
4. test
`http://127.0.0.1:80/` にHTTP通信でアクセスすると `root!!!` って返ってくる
`http://127.0.0.1:80/ws` にwscなどでアクセスして、JSON形式のデータを送ると、全要素が出力される

こんな感じ
```
>> wsc http://127.0.0.1:80/ws
Connected to http://127.0.0.1:80/ws
> {"hoge": "123", "fuga": "456", "json": "yaml"}
< 123
< 456
< yaml
```
