import pyaudio
import boto3
import wave

sampling_rate = 48000
chunk = 2 
device = 2 
audio = pyaudio.PyAudio()
frames = []
wavefile = wave.open("test1.wav",'wb')


def record():
    print("Record")
    print("Starting record")
    stream = audio.open(format = pyaudio.paInt16,rate = sampling_rate ,channels = 1, \
                    input_device_index = device,input = True, \
                    frames_per_buffer=chunk)
  
    for i in range(0,int((sampling_rate/chunk)*3)):
        data = stream.read(chunk,exception_on_overflow=False)
        if i % 3 == 0:
           frames.append(data)
    print("finished recording")
    stream.stop_stream()
    stream.close()
    
def upload_to_s3(filename= None):
    s3 = boto3.client("s3")
    s3.upload_file("/home/pi/Desktop/EID/Final_Project/test1.wav", "my-wand-project", "test1.wav")
   
#Using transcribe   
def speech_to_text():
    link = "https://s3.us-east-1.amazonaws.com/my-wand-project/test1.wav"
    trans = boto3.client("transcribe", region_name="us-east-1")
    try:
        response = trans.delete_transcription_job(TranscriptionJobName="output")
    except:
        pass
    response = trans.start_transcription_job(
        TranscriptionJobName="output",
        LanguageCode='en-US',
        MediaFormat='wav',
        MediaSampleRateHertz = 44100,
        Media={
            'MediaFileUri': link
        },
        #OutputBucketName="my-wand-project-output",
        Settings={
            'ShowSpeakerLabels': True,
            'MaxSpeakerLabels': 8
        }
    )
    print(response)
    
def aws_lex():
    lex = boto3.client('lex-models', region_name = "us-east-1")
    response = lex.get_bot(name = "mybot", versionOrAlias="satya")
    lex_run = boto3.client('lex-runtime', region_name = "us-east-1")
    wavefile = wave.open('test1.wav')
    response = lex_run.post_content(botName = "mybot", botAlias = "satya", contentType = "audio/l16;rate=16000; channels=1", \
                                    accept = "text/plain; charset=utf-8",\
                                    inputStream = wavefile.readframes(96044), userId = "satya")
    print("Speech to text conversion:",response['ResponseMetadata']['HTTPHeaders']['x-amz-lex-message'])

def create_wav_file():
    wavefile.setnchannels(1)
    wavefile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wavefile.setframerate(16000)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

record()
create_wav_file()
#upload_to_s3()
#speech_to_text()
#audio.terminate()
aws_lex()    