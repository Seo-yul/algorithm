# import tempfile
#
#
# def print_tmp():
#     """
#     Support
#
#         $ cd `tmp`
#
#     """
#     print(tmp())
#
#
# def tmp():
#     """
#     Create temp dir
#     """
#     return tempfile.mkdtemp()
#
#
# if __name__ == '__main__':
#     print_tmp()


'''
from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is:', ip)
'''

"""
import boto3
import json

sns = boto3.client('sns')
codepipeline = boto3.client('codepipeline')

def lambda_handler(event, context):

    def userParams(event):
        value = ''
        try:
            value = event['CodePipeline.job'].data.actionConfiguration.configuration.UserParameters
        except Exception:
            value = ''

        return value
    print('EVENT--------')
    print(event)

    jobId = event['CodePipeline.job'].id
    try:
        sns.publish(
            Message= '{} 배포 완료!'.format(userParams(event)),
            TopicArn='arn:aws:sns:region:0123456789:my-topic-arn',
        )

        pipelineParams = {
            'jobId': jobId
        }

        try:
            return codepipeline.putJobSuccessResult(pipelineParams)
        except Exception as pipelineErr:
            print(pipelineErr)
            print('SNS: success, CodePipeline: fail')
            return pipelineErr

    except Exception as snsErr:
        print(snsErr)
        pipelineParams = {
            'jobId': jobId,
            'failureDetails': {
                'message': json.dumps(snsErr),
                'type': 'JobFailed',
                'externalExecutionId': context.invokeid
            }
        }

        try :
            return codepipeline.putJobFailureResult(pipelineParams)
        except Exception as pipelineErr:
            print(pipelineErr)
            print('SNS: fail, CodePipeline: fail')
            return pipelineErr
        return snsErr
"""

