from django.db import models


class asset(models.Model):
    asset_name = models.CharField(max_length=25)
    assetid = models.CharField(max_length=25)

    def __str__(self):
        return self.assetid


class worker(models.Model):
    worker_name = models.CharField(max_length=25)
    workerid = models.CharField(max_length=25)

    def __str__(self):
        return self.workerid

class work(models.Model):
    task_act = models.CharField(max_length=25)
    task_freq = models.CharField(max_length=25)
    taskid = models.CharField(max_length=25)

    def __str__(self):
        return self.taskid

class allocatework(models.Model):
    assetId = models.CharField(max_length=25)
    taskId = models.CharField(max_length=25)
    workerId = models.CharField(max_length=25)
    timeOfAllocation = models.CharField(max_length=25)
    taskToBePerformedBy = models.CharField(max_length=25)

    def __str__(self):
        return self.workerId












