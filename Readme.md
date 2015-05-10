![Logo](https://raw.githubusercontent.com/jimmytheleaf/astrologly/master/img/Astrologly.png)


Astrologly is the first AAAS (Astrology as a Service) application.

We're changing disrupting the divination industry through offering elegant, REST-like APIs on top of deep occult knowledge graphs.



# Endpoints

## Signs

###Get:

Example Query:

```http
GET /signs/aries/
```

Example Response:

```json
{
  "data": {
      "description": "The Ram", 
      "element": "Fire", 
      "end": "April 19", 
      "name": "Aries", 
      "quality": "Cardinal", 
      "start": "March 21"
    }
}
```

###List:

Example Query:

```http
GET /signs/
```

Example Response:

```json
{
  "data": [
    {
      "description": "The Ram", 
      "element": "Fire", 
      "end": "April 19", 
      "name": "Aries", 
      "quality": "Cardinal", 
      "start": "March 21"
    }, 
    {
      "description": "The Bull", 
      "element": "Earth", 
      "end": "May 20", 
      "name": "Taurus", 
      "quality": "Fixed", 
      "start": "April 20"
    },
...
]
```


## Natal Reading

Format:

```http
/<year>/<month>/<day>/
```

Example Query:

```http
GET /1983/01/31/
```

Example Response:

```json
{
  "data": {
    "signs": {
      "sun": {
        "description": "The Water Bearer", 
        "element": "Air", 
        "end": "February 21", 
        "name": "Aquarius", 
        "quality": "Fixed", 
        "start": "January 21"
      }
    }, 
    "source": {
      "date": {
        "day": 31, 
        "month": 1, 
        "year": 1983
      }, 
      "humanized": "32 years ago", 
      "verbose": "Monday January 31, 1983"
    }
  }
}
```