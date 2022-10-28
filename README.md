
![Logo](https://raw.githubusercontent.com/Ozookevin/Sentiment_Reader/main/logo.png)


# Ozoo_Sentiment_Reader

Sentiment reader API ia a free to use Sentiment tool. Providing the API with a url will then generate a Sentiment score. sentiment scores are created using textblob and vadar. Because of the low cost of processing request this APi is free and does not require Auth.





## Authors
- [Github](https://github.com/Ozookevin)
- [Dev.to @Ozookevin](https://dev.to/ozookevin)
## API Reference

#### Get all items

```http
  GET /
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `sentimentURL` | `string` | **Required**.  |


`Example`: http://73.116.143.197/sentimentAPI?sentimentURL= + url


## Run Locally

Clone the project

```bash
  git clone https://github.com/Ozookevin/Ozoo_Sentiment_API
```

Go to the project directory

```bash
  cd Ozoo_Sentiment_API
```

Install dependencies

```bash
  pip install requirements.txt 
```

Start the server

```bash
  pyton3 run app.py
```




### Using Local

This API and be installed to your local server and used to run sentiment on urls. You can also mod the code to taking in a raw string to get sentiment scores as well. 


## Related

This API was created for the use of the sentiment reader chrome extension. The source code can be found below. 



[Sentiment Chrome Extension](https://github.com/Ozookevin/Sentiment_Reader)

