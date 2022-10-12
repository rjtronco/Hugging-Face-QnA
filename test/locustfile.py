from locust import HttpUser, task, between

from requests_aws4auth import AWS4Auth

class Testing(HttpUser):
    wait_time = between(1, 3)

    @task
    def login_site_access(self):
        self.client.post("http://18.138.109.43/get_answer",
                         # auth=AWS4Auth('AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_REGION', 'AWS_SERVICE'),
                         json={
                            'questions':[
                                    'How many teams compete in the Premier League ?',
                                    'When does the Premier League starts and finishes ?',
                                    'Who has the highest number of goals in the Premier League ?',
                                ]
                            }
                        )