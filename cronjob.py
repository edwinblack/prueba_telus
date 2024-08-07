from crontab import CronTab

def init_cron():
    cron = CronTab(user='root')
    job = cron.new(command='cd /usr/src/app/; python get_data.py')
    job.minute.every(1)
    cron.write()