import requests

__author__ = 'asafliv'

from rtmbot.core import Plugin, Job


class GetUsersAvgJob(Job):
    def run(self, slack_client):
        return [["general", requests.get("localhost:5000/average")]]


class myPlugin(Plugin):
    def register_jobs(self):
        job = GetUsersAvgJob(60)
        self.jobs.append(job)
