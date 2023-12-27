import json
from flask      import request, Flask

import config
from core.chatgpt_web.chatgpt import ChatGpt
# from .internet  import get_search_message


class Backend_Api:
    def __init__(self, app: Flask) -> None:
        self.app: Flask = app
        self.routes = {
            '/backend-api/v2/models': {
                'function': self.models,
                'methods' : ['GET']
            },
            '/backend-api/v2/providers': {
                'function': self.providers,
                'methods' : ['GET']
            },
            '/backend-api/v2/version': {
                'function': self.version,
                'methods' : ['GET']
            },
            '/backend-api/v2/conversation': {
                'function': self._conversation,
                'methods': ['POST']
            },
            '/backend-api/v2/gen.set.summarize:title': {
                'function': self._gen_title,
                'methods': ['POST']
            },
            '/backend-api/v2/error': {
                'function': self.error,
                'methods': ['POST']
            }
        }
    
    def error(self):
        print(request.json)
        
        return 'ok', 200
    
    def models(self):
        return list()
    
    def providers(self):
        return [
            ""
        ]
        
    def version(self):
        return {
            "version": config.VERSION,
        }
    
    def _gen_title(self):
        return {
            'title': ''
        }
    
    def _conversation(self):
        messages = request.json['meta']['content']['parts']
        # if request.json['internet_access']:
        #     messages[-1]["content"] = get_search_message(messages[-1]["content"])
        # model = request.json.get('model')
        conversation_id = request.json.get('conversation_id')

            
        def try_response():
            try:
                yield from ChatGpt.create(
                    conversation_id=conversation_id,
                    messages=messages,
                    stream=True
                )
            except Exception as e:
                print(e)
                yield json.dumps({
                    'code'   : 'G4F_ERROR',
                    '_action': '_ask',
                    'success': False,
                    'error'  : f'{e.__class__.__name__}: {e}'
                })

        return self.app.response_class(try_response(), mimetype='text/event-stream')