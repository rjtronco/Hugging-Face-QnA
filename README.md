# Question Answering Model

Reference: https://towardsdatascience.com/build-a-q-a-app-with-pytorch-cb599480e29

## Highlights

🍭 Building a Question Answering model locally
- Build model using pretrained model from HuggingFace
- Creating API endpoint using FastAPI
- Building and containerizing model using Docker

🍭 [Deploying the QA model in AWS EC2](https://github.com/rjtronco/Hugging-Face-QnA/blob/main/EC2_Deployment.md)
- Setting up EC2 instance
- Deploying the model inside the instance
- Configuring the instance to enable access to the model endpoints


🍭 [Building the QA using BentoML framework](https://github.com/rjtronco/Hugging-Face-QnA/new/main/QnA_BentoML) 
- Make use of a templated BentoMLv1 model service file
- Building and containerizing bento model using bentoml
- Expose bentoml model endpoints to be accesible

🍭 [Load test endpoints using Locust Testing](https://github.com/rjtronco/Hugging-Face-QnA/blob/main/test/Locust%20Testing.md) 
- Create locust testing file
- Use locust testing in a WebUI and/or cli
- Assess model performance during heavy network traffic


## How it works

Create a FastAPI endpoint for `set_context` and `get_answers`. Create a python file for the model class as well. 
See `/app` for the complete files:

```python
import uvicorn
from fastapi import FastAPI, Request
from utils import QASearcher

app = FastAPI()

@app.post("/set_context")
async def set_context(data:Request):
  """
  Fastapi POST method that sets the QA context for search.
  
  Args:
    data(`dict`): Two fields required 'questions' (`list` of `str`)
      and 'answers' (`list` of `str`)
  """
  data = await data.json()
  
  qa_search.set_context_qa(
    data['questions'], 
    data['answers']
  )
  return {"message": "Search context set"}
```


Create a Dockerfile. This downloads pretrained model and install ncessary packages.:

```docker
FROM python:3.8.12-slim-buster

# Install wget and required pip libraries
RUN apt-get update &&\
    apt-get install -y --no-install-recommends wget &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install --no-cache-dir transformers[torch] uvicorn fastapi

# adds the script defining the QA model to docker
COPY download_model.sh .
```

# Build and run your model

```bash
docker build . -t qamodel &&\
  docker run -p 8000:8000 qamodel
```


### TESTING
  - go to the `/test` directory
  - You can run `set_context_test.py` then `get_answer_test.py` to test endpoints
    - on endpoint *init*, it initializes a instance of the Model
    - `set_context` sends set of questions and answers on different context so the model can do embeddings/processing (basically, study the data)
    - `get_answers` sends a new set of questions to the model, and the model returns the best answer to the new questions based on the data processed in `set_context`
    
#### Local test result:

<img src="https://github.com/rjtronco/Hugging-Face-QnA/blob/main/local_testing_result.png" width="800px" margin-left="-5px">
<br>



