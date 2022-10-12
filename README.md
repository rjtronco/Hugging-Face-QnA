# Question Answering Model

Reference: https://towardsdatascience.com/build-a-q-a-app-with-pytorch-cb599480e29

## Highlights

🍭 Building a Question Answering model locally
- Build model using pretrained model from HuggingFace
- Creating API endpoint using FastAPI
- Building and containerizing model using Docker

🍭 Deploying the QA model in AWS EC2
- Setting up EC2 instance
- Deploying the model inside the instance
- Configuring the instance to enable access to the model endpoints


🍭 Building the QA using BentoML framework
- Make use of a templated BentoMLv1 model service file
- Building and containerizing bento model using bentoml
- Expose bentoml model endpoints to be accesible


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

# Build and run your model
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

[<img src="https://github.com/rjtronco/Hugging-Face-QnA/blob/main/local_testing_result.png" width="800px" margin-left="-5px">]
<br>



### EC2 Hosted endpoint
#### Deployment steps
  - Spin up an instance. For this one, we used `ubuntu`
  - Setup **ElasticIP** for your instance. 
  - SSH into your EC2 instance
  - Install **docker** to your instance (docker,docker-compose )
  - Install **nginx** to your instance
  - Copy/Pull your files from your local/Github (FastAPI application files, Dockerfile, docker-compose.yaml)
      - Run `sudo docker-compose up -d` to run the on background
  - Create the nginx config file in `etc/nginx/sites-enabled/` directory
      - ``` server {
            listen 80;
            server_name <Elastic IP Assigned to your Instance>;
            location / {
                proxy_pass http://127.0.0.1:8000;
            }
        }
      - Run `sudo service nginx restart`
  - Try accessing your app via `http://<elastic-ip>/`



URL: `http://18.138.109.43/`

### TESTING
  - go to the `/test` directory
  - You can run `set_context.py` then `get_answer.py` to test endpoints
  - Locust load test
      - run `pip install locust`
      - for testing in *WEB UI*
        - Run `locust` inside the directory where the `locustfile.py` is located
        - Open your browser and go to [http://127.0.0.1:8089](http://127.0.0.1:8089/) to access the GUI
        - Begin load testing
        - Test for N users at X users spawned per second
        - Run the test for 5 minutes
     - for *Headless* testing
        - run `locust -f <locust_file_name>.py --config <config_file_name>.conf`



### Deploying using BentoML
  - install BentoML=>1.0.5, torch, and transformers
  - make sure to have docker/docker-desktop running
  - run `bentoml build -f bentofile.yaml`
  - run `bentoml containerize <svc_name>:<tag>`
  - then to host endpoint, run `docker run -it --rm -p 3000:3000 <svc_name>:<tag>`
      - `docker run -it --rm -p 3000:3000 qna_service:sxmg4ycjdsc6ehua`
   
#### NOTE:
  - You can reach the model using `/predict` endpoint. Flag value differentiate in setting context and getting answers
  - Setting Context: 
  - ``` json_data = {
            'flag':'set_context',
            'data':{
              'questions':questions,
              'answers':answers
            }
          }
  - Getting answers
  - ``` json_data = {
            'flag':'predict',
            'data':{
              'questions':questions,
            }
          }
