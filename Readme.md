# 题库系统

# question => 题库



# API

1. GET /question
```
{
  "_items": [
    {
      "_updated": "Fri, 21 Apr 2017 12:25:25 GMT",
      "_created": "Fri, 21 Apr 2017 12:25:25 GMT",
      "_id": "58f9fa351e9ed67e7556c082",
      "_links": {
        "self": {
          "href": "question/58f9fa351e9ed67e7556c082",
          "title": "qt"
        }
      },
      "_etag": "386ba47e213de932480a3ced5bee393fe7e7000b"
    },
    {
      "_updated": "Fri, 21 Apr 2017 12:35:31 GMT",
      "topic": "请问北京有几家烤鸭店？",
      "_links": {
        "self": {
          "href": "question/58f9fc931e9ed6805516fde9",
          "title": "qt"
        }
      },
      "_created": "Fri, 21 Apr 2017 12:35:31 GMT",
      "_id": "58f9fc931e9ed6805516fde9",
      "_etag": "38bf9ba92a16dee47ea8cd4b3a524f209d1d29ff"
    }
  ],
  "_links": {
    "self": {
      "href": "question",
      "title": "question"
    },
    "parent": {
      "href": "/",
      "title": "home"
    }
  },
  "_meta": {
    "max_results": 25,
    "total": 2,
    "page": 1
  }
}
```

2. POST /question

in Content-Type: application/json
```
{
	"topic": "两对父子去买帽子，为什么只买了三顶？",
	"options": [1,2,3],
	"type": "select"
}

response
{
  "_updated": "Mon, 24 Apr 2017 13:16:31 GMT",
  "_links": {
    "self": {
      "href": "question/58fdfaaf1e9ed6baa97da1ad",
      "title": "qt"
    }
  },
  "_created": "Mon, 24 Apr 2017 13:16:31 GMT",
  "_status": "OK",
  "_id": "58fdfaaf1e9ed6baa97da1ad",
  "_etag": "d8b794a3a32cfcb847b4eaaa1e65b5737112e6e7"
}

```
