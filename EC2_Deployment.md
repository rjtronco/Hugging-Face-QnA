## EC2 Hosted endpoint

Reference: https://dev.to/theinfosecguy/how-to-deploy-a-fastapi-application-using-docker-on-aws-4m61

### Deployment steps
  - Spin up an instance. For this one, we used `ubuntu`
  - Setup **ElasticIP** for your instance. 
  - Configure your instance's security group to accept  all `http` and `https` request (this is not the best practice, but for the sake of demo, this will do)
  - SSH into your EC2 instance
  - Install **docker** to your instance (docker,docker-compose )
  - Install **nginx** to your instance
  - Copy/Pull your files from your local/Github (FastAPI application files, Dockerfile, docker-compose.yaml)
      - Run `sudo docker-compose up -d`. The `-d` flag will run the docker compose on the background
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
