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
  - Setup the nginx config file in `etc/nginx/sites-enabled/` directory
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
Web app template was downloaded from the internet

# Transcriber
Still WIP, need to upgrade subscription for live transcription. Please see images for local testing result
`CFLAGS="-I/opt/homebrew/include -L/opt/homebrew/lib" python3 -m pip install pyaudio` to install on mac
