# Hugging Face Model Deployment
Separated `set_context` and `get_answer` test files

Please see `local_testing_result.png` for a screenshot of local testing 

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
You can run `set_context.py` then `get_answer.py` to test endpoints


# Chatbot

Frontend for chat app: `http://resty-chatbot.com.s3-website-ap-southeast-1.amazonaws.com/`
Webhook flask app url: `https://f411-122-248-241-116.ap.ngrok.io/webhook`
Komunicate app id: `https://widget.kommunicate.io/chat?appId=201b88b52948f69ac0cadb2a8a8b7cbdc`


### DialogFlow Setup
  - Create agent in DialogFlow
  - Create Custom intent for that agent
  - Add keywords to the training
  - Enable webhook for the custom intent
  - Create Flask App for the Fulfillment of the custom intent
  - Install ngrok in your local
  - run your flask app and ngrok
  - Use the test files to check if your endpoints work correctly

# Transcriber
Run `working_rts.py` in cli, then speak to your mic
`CFLAGS="-I/opt/homebrew/include -L/opt/homebrew/lib" python3 -m pip install pyaudio` to install on mac
