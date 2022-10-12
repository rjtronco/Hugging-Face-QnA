# Deploying using BentoML
  - install BentoML=>1.0.5, torch, and transformers
  - create the `model_service.py` file 
  - create the bentofile.yaml

## Testing
  - make sure to have docker/docker-desktop running
  - run `bentoml build -f bentofile.yaml`
  - run `bentoml containerize <svc_name>:<tag>`
  - then to host endpoint, run `docker run -it --rm -p 3000:3000 <svc_name>:<tag>`
      - `docker run -it --rm -p 3000:3000 qna_service:sxmg4ycjdsc6ehua`
   
#### NOTE:
  - You can reach the model using `/predict` endpoint. Flag value differentiate in setting context and getting answers
  - Setting Context json payload: 
  - ``` json_data = {
            'flag':'set_context',
            'data':{
              'questions':questions,
              'answers':answers
            }
          }
  - Getting answers json payload:
  - ``` json_data = {
            'flag':'predict',
            'data':{
              'questions':questions,
            }
          }
