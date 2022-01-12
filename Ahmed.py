import user_agent,requests
from user_agent import generate_user_agent
Token=input('Token : ')
ID =input('ID : ')
ahmed=(generate_user_agent())
print(ahmed)
requests.post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text= ⌯ USER_AGENT
• - - - - - - - - - - - - - - - - - - - - - - - •
⌯	{ahmed}
• - - - - - - - - - - - - - - - - - - - - - - - •
<\> PY : @O99_5_O </> ''' )
