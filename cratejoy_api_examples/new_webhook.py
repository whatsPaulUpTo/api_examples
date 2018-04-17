"""
This command-line utility demonstrates how to create
a webhook using the Cratejoy API.

Documentation at:   http://docs.cratejoy.com/docs/hook
                    http://docs.cratejoy.com/docs/web-hook-methods

Example Usage: 
python newHook.py --user user-id --pw password --event subscription_new --target https://yourwebhooktarget.com/id/ --request_type POST --name postNewSubToTarget

"""

import json
import requests


def new_webhook(auth, event, target, request_type, name,
                base_url='https://api.cratejoy.com/v1/'):
    """
        Create a new webhook for your Cratejoy store.
    """

    payload = json.dumps({
        u'event': event,
        u'target': target,
        u'name': name,
        u'request_type': request_type
    })

    base_url = 'https://api.cratejoy.com/v1/'

    webhooks_endpoint = '{}hooks/'.format(base_url)

    resp = requests.post(
        webhooks_endpoint,
        data=payload,
        auth=auth
    )

    print('POST request to {} responded with status '
          'code: {}'.format(webhooks_endpoint,
                            resp.status_code))


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument(u'--user',
                        type=unicode,
                        required=True, help=u'Basic auth user')
    parser.add_argument(u'--pw',
                        type=unicode,
                        required=True, help=u'Basic auth password')
    parser.add_argument(u'--event',
                        type=unicode,
                        required=True,
                        help=u'(string): name of a cratejoy event that will trigger this hook')
    parser.add_argument(u'--target',
                        type=unicode,
                        help=u'(string): the target URI of your endpoint')
    parser.add_argument(u'--request_type',
                        type=unicode,
                        help=u'(string): either POST or GET', default='POST')
    parser.add_argument(u'--name',
                        type=unicode,
                        help=u'name of the new webhook')

    args = parser.parse_args()
    auth = (args.user, args.pw)

    fn_args = {
        'auth': auth,
        'event': args.event,
        'target': args.target,
        'request_type': args.request_type,
        'name': args.name
    }

    new_webhook(**fn_args)