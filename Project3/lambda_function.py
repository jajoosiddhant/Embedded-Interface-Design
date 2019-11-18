import json
import boto3

print('Loading function')
temp_alert_flag = True
hum_alert_flag = True
sensor_alert_flag = True

def publish_message(message):
    sns = boto3.client('sns')
    response = sns.publish(
    PhoneNumber ='+17209174941',    
    Message=message)
  
def lambda_handler(event, context):
    global temp_alert_flag,hum_alert_flag,sensor_alert_flag
    #publish_message("Humidity :"+str(event['humidity'])+"\nCurrent Temperature:"+str(event['temperature'])+"Time:"+event['timestamp'])
    print("Received event: " + json.dumps(event, indent=2))
    if(event['Alert']=='false'):
        print("Normal Handler")
        sqs = boto3.resource('sqs')
        queue = sqs.get_queue_by_name(QueueName='test')
        response = queue.send_message(MessageBody=json.dumps(event))
    if(event['Alert']=='Humidity'):
        if(hum_alert_flag == True):
            publish_message("Humidity Alert Set value:"+str(event['humidity_alert_level'])+"\nCurrent Temperature:"+str(event['humidity'])+
            "Time:"+event['timestamp'])
            hum_alert_flag = False
    if(event['Alert']=='Temperature'):
        if(temp_alert_flag == True):
            publish_message("Temperature Alert Set value:"+str(event['temperature_alert_level'])+"\nCurrent Temperature:"+str(event['temperature'])+
            "\nTime:"+event['timestamp'])
            temp_alert_flag = False
    if(event['Alert']=='Sensor_offline'):
        if(sensor_alert_flag == True):
            publish_message("Sensor Disconnected")
            sensor_alert_flag = False
    